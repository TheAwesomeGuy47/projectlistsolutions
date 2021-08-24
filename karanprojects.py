# find pi to the nth digit

def calcPi(limit):
  
  q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
  decimal = limit
  counter = 0
  
  while counter != decimal + 1:
    if 4 * q + r - t < n * t:
      yield n
      if counter == 0:
        yield '.'
