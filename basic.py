from base import Tokenizer
from base import get_stats, merge
import tqdm

class BasicTokenizer(Tokenizer):
    def __init__(self):
        super().__init__()


    def train(self, text, vocab_size):
        num_merges = vocab_size - 256
        
        ids = list(text.encode("utf-8"))
        merges = {}
        vocab = {idx : bytes(idx) for idx in range(256)}
        for i in tqdm.tqdm(range(num_merges)):

            stats = get_stats(ids)
            #print(ids)
            #print(stats)
            pair = max(stats, key=stats.get)

            idx = 256 + i

            ids = merge(ids, pair, idx)

            merges[pair] = idx
            vocab[idx] = vocab[pair[0]] + vocab[pair[1]] 

            print(f"merge {i + 1}/{num_merges} : {pair} -> {idx}")
        self.merges = merges
        self.vocab = vocab
    
    def encode(self,text):
        encoded_bytes = text.encode("utf-8")
        ids = list(encoded_bytes)

        while len(ids) >= 2:
            stats = get_stats(ids)
            #print(stats)
            pair = min(stats, key=lambda p : self.merges.get(p, float("inf")))

            if pair not in self.merges:
                break

            ids = merge(ids, pair, self.merges[pair])
        return ids
    

    def decode(self,ids):
        text_bytes = b"".join(self.vocab[idx] for idx in ids)
        text = text_bytes.decode("utf-8",errors="replace")
        return text