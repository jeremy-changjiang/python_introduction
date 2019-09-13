n = 0
#方法1
for n in range(0,100):
	n += 1
	if n % 7 == 0 or n % 10 == 7 or n // 10 == 7:
		continue
	else:
		print(n)
#a = 0
#while a < 100:
#	a += 1
#	if a % 7 == 0 or a % 10 == 7 or a // 10 ==7:
#		continue 
#	print(a)


