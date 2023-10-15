import sys
import os

def CountBytesInTheFile(filePath):
    numberofBytes = os.stat(filePath).st_size
    print(f"{numberofBytes}\t{os.path.basename(filePath)}")

def CountLinesInTheFile(filePath):
    return

def CountWordsInTheFile(filePath):
    return

def CountCharectersInTheFile(filePath):
    return

if sys.argv[1] == '-c':
    filePath = sys.argv[2]
    CountBytesInTheFile(filePath)

if sys.arv[1] == '-l':
    filePath = sys.argv[2]
    CountLinesInTheFile(filePath)

if sys.argv[1] == '-w':
    filePath = sys.argv[2]
    CountWordsInTheFile(filePath)










