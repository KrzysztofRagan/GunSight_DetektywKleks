import os

path = '/Users/krzysztofragan/Desktop/vscode/DetektywKleks_gra/images/ghul_move'
num = 1
for root, dirs, files in os.walk(path):
  for i in files:
    if i != '.DS_Store':
      os.rename(i, (i[:15]+str(num)+'.png'))
      num += 1
    else:
      pass