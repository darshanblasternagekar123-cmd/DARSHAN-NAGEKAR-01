# Create a string
s="Hello Python Programming"

# indexing and slicing
print("First Character:",s[0])
print("Last Character:",s[-1])
print("slicing",s[0:5])

# b.uppercase to lowercase and vice versa
print("Uppercase:",s.upper())
print("Lowercase:",s.lower())

# c.count occurance of a character or substring
print("Count of 'o':",s.count('o'))
print("Count of 'Python':",s.count('Python'))

# d.replace a word in the string
print("Replace",s.replace("Python","Java"))

# e.split and join a string
words=s.split()
print("Split:",words)

new_string="=".join(words)
print("Join:",new_string)

# f.check startswith and endswith
print("Starts with 'Hello':",s.startswith("Hello"))
print("Ends with 'Programming':",s.endswith("Programming"))
