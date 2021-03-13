import numpy as np

corruptedImgs = np.load("/content/gdrive/MyDrive/VinBigData/corruptedImgs.npy")

cmdStr = ""
for name in corruptedImgs:
  cmdStr += name + " "

print(cmdStr)

