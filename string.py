s=raw_input("Please enter a word: ")
upper_s = s.upper()
print (upper_s)
lower_s = s.lower()
print (lower_s)

combined = (upper_s + lower_s)
print (combined)

num_s = len(s)
print (num_s)

num_combined = len(combined)
print (num_combined)

print ("HELLO")
halfway = len(s)/2
print (s[halfway])
print (s[0])
print (s[4])

last = len(s)-1
print (s[last])
print (s[-1])

firsthalf = s[:halfway]
lasthalf = s[halfway:len(s)]
print (lasthalf)
print (firsthalf)

copy = s[:]
print (copy)

skip = s[::2]
print (skip)
skip2 = s[1::2]
print (skip2)

value = s[::-1]
print (value)

print (s.count("l"))
print (s.find("o"))
print (s[:s.find("o")])

replaced = s.replace("great","awsome")
print (replaced)

words = s.split()
print (words)

numberofwords = len(words)
print (words[0:2])
print (words[0:2:-1])
print (words[::-1])

sentence = "\n".join(words)
print (sentence)

newsentence = sentence.replace("\n",":-)")
print (newsentence)
