#break
x = int(input("How many candy: "))
av = 10
i = 1
while i <= x:
    if i > av: #if this condition is true the loop will stop
        print()
        break
    print("Candy")
    i+=1

#continue
for i in range(100):
	if i%3 == 0 or i%5 == 0:#if this condition is true the loop will hop to next value
		continue
	print(i)

#pass
for i in range(100):
	if i%2==0:
		pass
	else:
		print(i)
#pass is same as continue

