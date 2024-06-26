def make_distinct():
  """
  Finds the minimum number of operations to make all elements in the array distinct.
  """
  
  n = int(input())
  a = list(map(int, input().split()))
  
  operations = 0
  freq = {}
  for x in a:
    freq[x] = freq.get(x, 0) + 1
  
  for x in sorted(freq):
    if freq[x] > 1:
      operations += freq[x] - 1
      for i in range(1, freq[x]):
        operations += i
  
  print(operations)

make_distinct()