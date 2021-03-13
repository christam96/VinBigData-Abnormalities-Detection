import numpy as np

destinationPath = "./drive/MyDrive/VinBigData/train/"
srcPath = "train/"

totalSize = 118000000000
count = 0
splitRate = 99999999 + 1
cmdStr = ''
while(True):
  beg = count * splitRate
  end = (count+1) * splitRate - 1
  if end < totalSize:
    cmdLine = "curl --range " + str(beg) + "-" + str(end) + " -o dataset.part" + str(count) +str(" \"")+"https://storage.googleapis.com/kaggle-data-sets/1042002/1794153/compressed/train.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1615524282&Signature=Bi9bfnT5Lh%2BRcrivDkr8RsbslpajTlhLiCxtoSuzgJGq9Lt2S7dmo8HHyc%2BDJ6ULruiKs%2BjzsU8A18hOzhONp6Oj23H3vUoDGBuvAEKFg9BJ35sA3NB5T6W9W%2FXl%2B1Ol6nDY6nVoqprYylva%2FTbdLHNNzhVU1rWYHAFIjzVPkbmB5EkE69JOzt7zqjm3pbZgGZphjwTttNx8M9gODl8Gc4D%2BWM9nsOClBrUe9iyMyQV3xFsIgk%2FWr%2BeXiFfSOoPzBSZwuQvzPJYJM6yYo9p9gf7%2FPzui2vxZluqaSLO1ZHmqzvZTCEfHcravKjGaXgYWzzfSsdj9KtEH6oOJ7h213A%3D%3D&response-content-disposition=attachment%3B+filename%3Dtrain.zip" + str("\" *")
    #print(cmdLine)
    cmdStr += cmdLine
  else:
    cmdLine = "curl --range " + str(beg) + "-" + " -o dataset.part" +str(count) +str(" \"")+"https://storage.googleapis.com/kaggle-data-sets/1042002/1794153/compressed/train.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1615524282&Signature=Bi9bfnT5Lh%2BRcrivDkr8RsbslpajTlhLiCxtoSuzgJGq9Lt2S7dmo8HHyc%2BDJ6ULruiKs%2BjzsU8A18hOzhONp6Oj23H3vUoDGBuvAEKFg9BJ35sA3NB5T6W9W%2FXl%2B1Ol6nDY6nVoqprYylva%2FTbdLHNNzhVU1rWYHAFIjzVPkbmB5EkE69JOzt7zqjm3pbZgGZphjwTttNx8M9gODl8Gc4D%2BWM9nsOClBrUe9iyMyQV3xFsIgk%2FWr%2BeXiFfSOoPzBSZwuQvzPJYJM6yYo9p9gf7%2FPzui2vxZluqaSLO1ZHmqzvZTCEfHcravKjGaXgYWzzfSsdj9KtEH6oOJ7h213A%3D%3D&response-content-disposition=attachment%3B+filename%3Dtrain.zip" + str("\" *")
    #print(cmdLine)
    cmdStr += cmdLine
    break;
  count += 1
print(cmdStr)
