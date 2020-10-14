# Char To Int

#### This python module can convert a single character or a string into the ASCII value of that character. This currently only works with the alphabet in caps and lowercase.

To use it, download the `cti.py` file, make sure it is in the same folder as the project you are working on and write `import cti`

Now you can use `cti.single()` or `cti.multi()` to convert each

`cti.single()` takes a string of one character; if given more it will give 0, and if given less it will give you an error. It will return an integer

`cti.multi()` takes a string of any amount and a boolean. It will return a list (array) if the boolean is `False`, and a more readable string if ` True`

Neither function takes more than one argument, so any mutilation of the string will have to be done manually.

Note that any characters given for either function that isn't part of the alphabet (or space) will return for 0 (for single) or a blank list (for multi).
For multi, if one such character is mixed in with other characters that do work, these characters will simply not appear, whilst the others (that do work) will.

##### Source Code

``` py
letters = [
  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O","P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s","t", "u", "v", "w", "x", "y", "z", " "
  ]


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
        return newResult # returns string; easier to read. will not print result
      else:
        return result # returns list. will not print result
```
