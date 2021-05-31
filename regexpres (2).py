import re

k = 0
while k < 100:
	k += 1
	s = str(k)
	g = re.match(r'([2-7][02468])$',s)
	if g:
		print (g.group(1))
#четные от 20 до 79

a = "0000.123210142"
g = re.match(r'^0*([1-9]*[0-9][.][0-9]*)$',a)
if g:
	print (g.group(1))
else:
	print ("fail 0")
#число без ведущих 0 (исправлено)

b = "123214.124214"
g = re.match(r'([0-9]+)([.][0-9]+)$' ,b)
if g:
	print (g.group(1))
	print (g.group(2))
else:
	print ("fail")
#дробное число (?)

c = "123.213000213000"
g = re.match(r'([0-9]+)([.][0-9]*[1-9]+)([0]*)$' ,c)
if g:
		print (g.group(1),g.group(2))
else:
	print ("fail")
#число без незначащих 0

d = "234.213"
g = re.match(r'(^0*([1-9]*[0-9]))?([.][0-9]*?)$',d)
if g:
	print (g.group(2), g.group(3))
else:
	print ("fail")
#число с возможностью быть без части. как убрать none не знаю
