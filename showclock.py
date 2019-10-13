import sys
import re
from clockinfo import translate
from datetime import datetime

if len(sys.argv) == 1:
  timetoshow = datetime.now()
  print (translate(timetoshow.strftime("%H:%M")))
elif len(sys.argv) == 2:
  print (translate(sys.argv[1]))
