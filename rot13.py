import sys
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

rot13 = ''
rot = sys.argv[1]
for each in rot:
  if each.isupper():
    i = upper.index(each)
    i += 13
    while i >= len(upper):
      i = i - len(upper)
    rot13 += upper[i]
  elif each.islower():
    i = lower.index(each)
    i += 13
    while i >= len(lower):
      i = i - len(lower)
    rot13 += lower[i]
  else:
    rot13 += each
print(rot13)