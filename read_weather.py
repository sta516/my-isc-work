#Exercise 1:

#1:
def read_header(name):
	with open(name) as f:
		head = {}
		i = 0
		while i < 3:
			line = f.readline()
			line - line.strip()
			key, value = line.split(":")
			header[key] = value
			i += 1
	return header

print(header)
