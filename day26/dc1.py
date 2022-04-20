# Day 26 - dictionary comprehension 1
# split + count

import re

# split into each word and count chars
sentence = "The quick brown fox jumped over the lazy dog."
result = {word: len(word) for word in re.split('\s+', sentence)}
print(result)
