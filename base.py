def encode_text(text):
    print(type(text))
    encoded_text = text.encode("utf-8")
    print(encoded_text)
    encoded_text = list(map(int, encoded_text))
    return encoded_text

def decode_text(ids):
    decoded_text = b"".join([bytes(idx) for idx in ids])
    #print(type(decoded_text))
    decoded_text = decoded_text.decode("utf-8", errors="replace")
    return decoded_text
def get_stats(ids, stats=None):
    stats = {} if stats is None else stats
    for id1, id2 in zip(ids, ids[1:]):
        pair = (id1, id2)
        stats[pair] = stats.get(pair, 0) + 1

    return stats


def merge(ids, pair, idx):
    new_ids = []
    i = 0

    while i < len(ids):

        if ids[i] == pair[0] and i < len(ids) - 1 and ids[i + 1] == pair[1]:
            new_ids.append(idx)
            i += 2
        else:
            new_ids.append(ids[i])
            i += 1
    return new_ids



class Tokenizer:
    def __init__(self,):
        self.merges = {}
        self.vocab = self._build_vocab()
        self.merges = {}
        #self.special_tokens = {}



    def _build_vocab(self):
        vocab = {idx : bytes(idx) for idx in range(256)}
        for (p0,p1), idx in self.merges.items():
            vocab[idx] = vocab[p0] + vocab[p1]
        #for special, idx in self.special_tokens.items():
        #    vocab[idx] = special.encode("utf-8")
        return vocab
    

    def train(self, text, vocab_size):
        return NotImplementedError

    def encode(self,text):
        return NotImplementedError

    def decode(self,ids):
        return NotImplementedError
    


