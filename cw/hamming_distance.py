def hamming(a,b):
  return sum(ch1 != ch2 for ch1, ch2 in zip(a, b))
