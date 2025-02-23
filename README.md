# Tokenizer

# Implementation of LLM  basic tokenizer from scratch using python 

## 🧑‍💻 Custom Tokenizer
## Problem:

## The tokenization process is critical for breaking down raw text into smaller units (tokens) that can be processed by a machine learning model. Most LLMs rely on pre-built tokenizers, but I wanted to create one tailored to my specific needs.

## Approach:

### I built a custom tokenizer that converts text into subword tokens using a combination of Byte-Pair Encoding (BPE) and WordPiece algorithms. Here's how it works:

###    Preprocessing:
###        Clean and normalize text data.
###        Split text into words and characters for token creation.

###    Byte-Pair Encoding (BPE):
###        This algorithm merges the most frequent pair of bytes in the corpus iteratively until we reach a predefined vocabulary size.
###        It allows for efficient compression of text into manageable tokens, especially for rare or out-of-vocabulary words.

###    Vocabulary Creation:
###        The final tokenizer uses the learned vocabulary to map raw text into token ids, which can be processed by the LLM.
