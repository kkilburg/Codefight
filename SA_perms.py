from itertools import permutations

def stringsRearrangement(inputArray):
  for perm in list(permutations(inputArray)):
    p = list(perm)
    if check(p) == 1:
      return True
  return False

def check(p):
  # print (p)
  for e in range(len(p)-1):
    count = sum(1 for a, b in zip(p[e], p[e+1]) if a != b)
    # print (p[e], p[e+1], count)
    if count != 1:
      return 0
    else:
      continue
  return 1

test2 = ["arc", "abc", "bbc", "bcc", "bdc", "bec", "bef", "ber", "bar", "arc", "abc", "bbc", "bcc", "bdc", "bec", "bef", "ber", "bar"]
test1 = ["abc", "abc", "acc", "acc", "azc"]

stringsRearrangement(test1)
stringsRearrangement(test2)

