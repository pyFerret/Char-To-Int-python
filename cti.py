data = [["A", 65],["B", 66],["C", 67],["D", 68],["E", 69],["F", 70],["G", 71],["H", 72],["I", 73],["J", 74],["K", 75],["L", 76],["M", 77],["N", 78],["O", 79],["P", 80],["Q", 81],["R", 82],["S", 83],["T", 84],["U", 85],["V", 86],["W", 87],["X", 88],["Y", 89],["Z", 90],["a", 97],["b", 98],["c", 99],["d", 100],["e", 101],["f", 102],["g", 103],["h", 104],["i", 105],["j", 106],["k", 107],["l", 108],["m", 109],["n", 110],["o", 111],["p", 112],["q", 113],["r", 114],["s", 115],["t", 116],["u", 117],["v", 118],["w", 119],["x", 120],["y", 121],["z", 122],[" ", 32],[",", 44],[".", 46],["!", 33],["?", 63]]

def single(_conv):
    result = 0
    for i in range(len(data)):
        if (str(_conv) == data[i][0]):
            result = data[i][1]
    return result

def multi(_conv, _pretty = False):
    result = []
    for a in range(len(_conv)):
        for i in range(len(data)):
            if (str(_conv[a]) == data[i][0]):
              result.append(data[i][1])

    if(bool(_pretty) == True):
      newResult = ""
      for i in range(len(result)):
        newResult += str(result[i])
        if(i != len(result) - 1):
          newResult += ", "
      
      return newResult 
    else:
      return result 

def prtMulti(_conv):
  result = []
  for a in range(len(_conv)):
    for i in range(len(data)):
      if (str(_conv[a]) == data[i][0]):
        result.append(data[i][1])


  strResult = ""
  for i in range(len(result)):
    strResult += str(result[i])
    if(i != len(result) - 1):
      strResult += ", "
  
  print(strResult)

  return result

def example():
  print('print(cti.single("T")) \n', 
  single("T"), '\n')
  print('print(cti.multi("This must be printed!", True)) \n',
  multi("This must be printed!", True), '\n')
  print('print(cti.multi("This must be printed!", False)) \n',
  multi("This must be printed!", False), '\n')
  print('cti.prtMulti("This does not need to be printed!")')
  prtMulti("This does not need to be printed!")
  print('\n cti.bin("Print This!") \n', bin("Print This!"))

def bin(_conv):
  valInt = []; valBin = []
  for a in range(len(_conv)):
    for i in range(len(data)):
      if(str(_conv[a]) == data[i][0]):
        valInt.append(data[i][1])
  for i in range(len(valInt)):
    valBin.append("")
    if(valInt[i] < 128): valBin[i] += "0"
    else: valBin[i] += "1"; valInt[i] -= 128
    if(valInt[i] < 64): valBin[i] += "0"
    else: valBin[i] += "1"; valInt[i] -= 64
    if(valInt[i] < 32): valBin[i] += "0"
    else: valBin[i] += "1"; valInt[i] -= 32
    if(valInt[i] < 16): valBin[i] += "0"
    else: valBin[i] += "1"; valInt[i] -= 16
    if(valInt[i] < 8): valBin[i] += "0"
    else: valBin[i] += "1"; valInt[i] -= 8
    if(valInt[i] < 4): valBin[i] += "0"
    else: valBin[i] += "1"; valInt[i] -= 4
    if(valInt[i] < 2): valBin[i] += "0"
    else: valBin[i] += "1"; valInt[i] -= 2
    if(valInt[i] < 1): valBin[i] += "0"
    else: valBin[i] += "1"; valInt[i] -= 1
  return valBin
