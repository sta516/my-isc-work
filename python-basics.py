#Python basics course

#Exercise 1: The basics
#1:
course = 'python'
rating = 5
print(course)
print(rating)
print(course * rating)

#2:
#using pythagoras
b = 6
c = 3
a = ((b ** 2) + (c ** 2)) * 0.5
print(a)

#3:
#Investigating what data type each variable in 2 are.
print(type(a))
print(type(b))
print(type(c))

#4:
a = int(a)
print(type(a))


#Exercise 2: Control flow
#1:
#The following is a never ending loop
#while 1:
    #x = 1
#The following loop never gets called
while 0:
	pass
    
#2:
gases = ['He', 'Ne', 'Ar', 'Kr']
count = 0
while count < 4:
	item = gases[count]
	print(item, count)
	count += 1

#3:
name = 'Lisa'
if name == 'Lisa':
    print(name, "plays saxophone")
elif name == Bart:
    print(name, "rides skateboard")
else:
    print(name, "lives in Springfield")

#4:
x = 0
if x:
	print(x, "is True")
	
	
#Exercise 3: Lists and Slicing
#1:
x = [1,2,3,4,5]
print(x[1])
print(x[-2])
print(x[:])
print(x[1:4])

#2:
#We make a list from 1 to 10
y = list(range(1, 11))
#We change the first value in the list to 10
y[0] = 10
#We add 11 to the list
y.append(11)
#We extend the list with 12, 13 and 14
y.extend([12, 13, 14])
print(y)

#3
forward = []
backward = []
values = ["a", "b", "c"]
