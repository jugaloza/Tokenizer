from base import get_stats, merge, Tokenizer
import re
import tqdm
#import regex

#GPT2_SPLIT_PATTERN = r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
GPT2_SPLIT_PATTERN = r"""'(?:[sdmt]|ll|ve|re)| ?[a-zA-Z]+| ?\d+| ?[^\s\w]+|\s+(?!\S)|\s+"""

class RegexTokenizer(Tokenizer):
    def __init__(self):
        super().__init__()
        self.compiled_regex = re.compile(GPT2_SPLIT_PATTERN)
        
        #self.special_tokens = {}

        self.merges = {}

        self.vocab = self._build_vocab()


    def train(self,text, vocab_size):
        num_merges = vocab_size - 256

        text_chunks = re.findall(self.compiled_regex, text)
        print(text_chunks)
        ids = list(map(int, text_chunks))
        print(ids)
        exit()
        ids = [list(ch.encode("utf-8") for ch in text_chunks)]
        print(ids)
        vocab = {idx : bytes(idx) for idx in range(256)}
        merges = {}

        for i in tqdm.tqdm(range(num_merges)):

            stats = {}
            #print(ids)
            for chunk_ids in ids:
                get_stats(chunk_ids, stats)
            print(stats)
            pair = max(stats, key=stats.get)
            idx = 256 + i
            
            ids = merge(ids, pair, idx)

            merges[pair] = idx
            
            vocab[idx] = vocab[pair[0]] + vocab[pair[1]]

        self.merges = merges
        self.vocab = vocab
    
    def encode(self,text):
        text_chunks = re.findall(self.compiled_regex, text)

        ids = [list(ch.encode("utf-8", errors = "replace")) for ch in text_chunks]

        while len(ids) >= 2:

            stats = get_stats(ids)

            pair = min(stats, lambda p: stats.get(p, float("inf")))

            if pair not in self.merges:
                break

            ids = merge(ids, pair, self.merges[pair])
        return ids
    

    def decode(self,ids):
        decoded_bytes = b"".join([self.vocab[idx] for idx in ids])
        return decoded_bytes.decode("utf-8",errors="replace")



    def _build_vocab(self):
        vocab = {idx : bytes(idx) for idx in range(256)}
        for (p0,p1), idx in self.merges.items():
            vocab[idx] = vocab[p0] + vocab[p1]

        #for special_token, idx in self.special_tokens.items():
        #    vocab[idx] = vocab[special_token.encode("utf-8",errors="replace")]

        return vocab