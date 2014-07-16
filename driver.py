import os
import sys
from lexicon import *

wordList = lexicon()
wordList.load_files("example.txt")
wordList.find_sentiment()
