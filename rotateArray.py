
//Python program for left rotation
import os
import re
import sys
import math
import random

if '__name__'=='__main__' :
  nd=input().split()
  n = int(nd[0])
  d = int(nd[1])
  a = list(map(int,input().split()))
  a = [d:] + [:d]
  print(*a)
