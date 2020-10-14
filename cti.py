letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O","P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s","t", "u", "v", "w", "x", "y", "z", " "]


def single(_conv): # takes single character. will return 0 if given more
  result = 0
  for i in range(len(letters)):
    if (str(_conv) == letters[i]):
      if (i >= 27):
        result = i + 76
      else:
        result = i + 65
    if (result == 128):
      result = 32
  return result # returns int. will not print result

def multi(_conv, _pretty = False): # takes any amount of characters
  result = []
  for a in range(len(_conv)):
    for i in range(len(letters)):
      if (str(_conv[a]) == letters[i]):
        if (i >= 26):
          if (i < 52):
            result.append(i + 71)
          else:
            result.append(32)
          else:
            result.append(i + 65)
  if(bool(_pretty) == True):
    newResult = ""
    for i in range(len(result)):
      newResult += str(result[i])
      if(i != len(result) - 1):
        newResult += ", "
    return newResult # returns string. will not print result
  else:
    return result # returns list. will not print result

def prtMulti(_conv):
  result = []
  for a in range(len(_conv)):
    for i in range(len(letters)):
      if (str(_conv[a]) == letters[i]):
        if (i >= 26):
          if (i < 52):
            result.append(i + 71)
          else:
            result.append(32)
        else:
          result.append(i + 65)

  strResult = ""
  for i in range(len(result)):
    strResult += str(result[i])
    if(i != len(result) - 1):
      strResult += ", "
  
  print(strResult)

  return result
