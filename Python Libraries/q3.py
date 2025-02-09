import re

text = "This is a sample sentence. Here are some random numbers - 100, 650."
#Finding a match for a pattern within a string
pattern = r'\d+'  #Matching any number 
match = re.search(pattern, text)
print("a. First match:", match.group() if match else "No match found")

compiled_pattern = re.compile(r'\d+') #Compiling a regular expression for repeated use
print("b. Compiled regex results:", compiled_pattern.findall(text))

print("c. Starts with 'This':", bool(re.match(r'^This', text)))#Checking if the string starts or ends with the pattern
print("   Ends with a period:", bool(re.search(r'\.$', text)))

print("d. All numbers:", re.findall(pattern, text)) #Finding all occurrences of the pattern in a string

print("e. Replace numbers with 'XXX':", re.sub(pattern, 'XXX', text)) #Searching the pattern and replace it with another string

print("f. Split text by spaces:", re.split(r'\s+', text))#Splitting the string based on the pattern

word = 'sentence' #Matching pattern but match special characters using word boundary escape sequence
print("g. Word boundary match:", re.findall(rf'\b{word}\b', text))

match = re.search(r'(\d+), (\d+)', text) #Finding the pattern using grouping technique
print("h. Grouped match:", match.groups() if match else "No match found")

print("i. Non-capturing group:", re.findall(r'(?:\d+)', text))#Defining groups without defining them 

match = re.search(r'(.*)numbers - (\d+), (\d+)(.*)', text) #Matching pattern but capture the strings before and after the pattern
print("j. Capture before & after numbers:", match.groups() if match else "No match found")

print("k. Case insensitive match for 'this':", re.findall(r'this', text, re.IGNORECASE)) #Using IGNORECASE

match = re.search(r'numbers - (?P<first>\d+), (?P<second>\d+)', text) #Assigning names to groups and call them using the reference
print("l. Named groups:", match.groupdict() if match else "No match found")

#Matching pattern in a multi-line text
multi_line_text = """This is a sample sentence. 
Here are some random numbers - 100, 650.
More numbers: 200, 350.
"""
print("m. Multi-line match for 'Here':", re.findall(r'^Here', multi_line_text, re.MULTILINE))
