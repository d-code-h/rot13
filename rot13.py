import sys
up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

rot = ''
for e in sys.argv[1]:
  if e.isupper():
    i = up.index(e)
    i += 13
    while i >= len(up):
      i = i - len(up)
    rot += up[i]
  elif e.islower():
    i = low.index(e)
    i += 13
    while i >= len(low):
      i = i - len(low)
    rot += low[i]
  else:
    rot += e
print(rot)