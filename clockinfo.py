import time

Mapper = {

0:'twelve',
1:'one',
2:'two',
3:'three',
4:'four',
5: 'five',
6: 'six',
7: 'seven',
8: 'eight',
9: 'nine',
10: 'ten',
11: 'eleven',
12: 'twelve',
13: 'thirteen',
14: 'fourteen',
15: 'fifthteen',
16: 'sixteen',
17: 'seventeen',
18: 'eighteen',
19: 'nineteen',
20: 'twenty',
30: 'thirty',
40: 'forty',
50: 'fifty' }

def readMinutes(value):
  if value < 21: return Mapper[value] + ' ' +'past '
  if value == 30: return 'half past'
  x, y = divmod(value,10)
  if value > 20 and value < 30: return Mapper[10*x] + ' ' + Mapper[y] + ' ' +'past '
  if value > 30 and value < 40:
   x = 60 - value
   x, y = divmod(x,10)
   return Mapper[10*x] + ' ' + Mapper[y] + ' ' +'to '
  if value > 39:
   x = 60 - value
   return Mapper[x] + ' ' +'to '

def speech(time):
  if (':' not in time): return 'Not a valid time input; required format is [hh]:[mm]'
  hour, minute = map(int, time.split(':'))
  if minute == 0 : return Mapper[hour%12]  +' '  +' o\'clock'
  if minute > 30 :
    hour = hour + 1
    return readMinutes(minute) +' '+ Mapper[hour%12]
  return readMinutes(minute) +' '+ Mapper[hour%12]

def translate(Input):
 if(type(Input) is str):
    try:
       time.strptime(Input, '%H:%M')
       return speech(Input)
    except ValueError:
       return ' Invalid Input; must be time string in hh:mm format '
 else:
    return 'Invalid Input; must be time string (":" included)'
  
