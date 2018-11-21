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

#3:
forward = []
backward = []
values = ["a", "b", "c"]
for item in values:
	forward.append(item)
	backward.insert(0, item)
print("forward is:", forward)
print("backward is:", backward)
forward.reverse()
print(forward == backward)

#4:
Countries = ["uk", "usa", "uk", "uae"]
print(dir(Countries))
#help(Countries.count)
#To be able to see the answer you need to use "print"
print(Countries.count("uk"))


#Exercise 4: Tuples
#1:
t = (1,)
print(t[-1])
myrange = range(100,200)
mytuple = tuple(myrange)
print(mytuple[0], mytuple[-1])


#2:
mylist = [23, "hi", 2.4e-10]
for index,item in enumerate(mylist):
	print(index,item)
	
#3:
(first, middle, last) = mylist
print(first, middle, last)
(first, middle, last) = (middle, last, first)
print(first, middle, last)


#Exercise 5: Input and Output
#1:
with open("weather.csv", "r") as reader:
	data = reader.read()
print(data)


#2:
with open("weather.csv", "r") as reader:
	#readline gives the header
	line = reader.readline()
	while line:
		print(line)
		line = reader.readline()
print("It's over")


#3:
with open("weather.csv", "r") as reader:
	header = reader.readline()
	rain = []
	for line in reader.readlines():
		#strip removes any spaces in the csv file
		#Split shows that the string should be split by comma into variables
		r = line.strip().split(",")[-1]
		#float is making it into decimal numbers
		r = float(r)
		rain.append(r)
print(rain)
with open("rain.txt", "w") as writer:
	for r in rain:
		writer.write(str(r) + "\n")


#4:
import struct
bin_data = struct.pack("bbbb", 123,12,45,34)
with open("mybinary.dat", "wb") as b_writer:
	b_writer.write(bin_data)
	
with open("mybinary.dat", "rb") as b_reader:
	bin_data2 = b_reader.read()
	data = struct.unpack("bbbb", bin_data2)
print(data)


#Exercise 6:Strings
#1:
s = "I love to write python"
for c in s:
	print(c)

print(s[4])
print(s[-1])
print(len(s))
print(s[0])
print(s[0][0])
print(s[0][0][0])

#2:
s = "I love to write python"
split_s = s.split(" ")
for word in split_s:
	if word.lower().find("i") > -1:
	    print(f"I found 'i' in: {word}")
	
#3:
something = "Completely Different"
print(dir(something))
print(something.count("t"))
print(something.find("plete"))
print(something.split("e"))
thing2 = something.replace("Different", "Silly")
print(thing2)
#Strings cannot be changed, so the following will create an error
#something[0] = "B"


