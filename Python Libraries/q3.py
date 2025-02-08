import re

text = "This is a sample sentence. Here are some random numbers - 100, 650."
#Find a match for a pattern within a string
pattern = r'\d+'  #Match any number 
match = re.search(pattern, text)
print("a. First match:", match.group() if match else "No match found")

compiled_pattern = re.compile(r'\d+') #Compile a regular expression for repeated use
print("b. Compiled regex results:", compiled_pattern.findall(text))

print("c. Starts with 'This':", bool(re.match(r'^This', text)))#Check if the string starts or ends with the pattern
print("   Ends with a period:", bool(re.search(r'\.$', text)))

print("d. All numbers:", re.findall(pattern, text)) #Find all occurrences of the pattern in a string

print("e. Replace numbers with 'XXX':", re.sub(pattern, 'XXX', text)) #Search the pattern and replace it with another string

print("f. Split text by spaces:", re.split(r'\s+', text))#Split the string based on the pattern

word = 'sentence' #Match pattern but match special characters using word boundary escape sequence
print("g. Word boundary match:", re.findall(rf'\b{word}\b', text))

match = re.search(r'(\d+), (\d+)', text) #Find the pattern using grouping technique
print("h. Grouped match:", match.groups() if match else "No match found")

print("i. Non-capturing group:", re.findall(r'(?:\d+)', text))#Define groups without defining them 

match = re.search(r'(.*)numbers - (\d+), (\d+)(.*)', text) #Match pattern but capture the strings before and after the pattern
print("j. Capture before & after numbers:", match.groups() if match else "No match found")

print("k. Case insensitive match for 'this':", re.findall(r'this', text, re.IGNORECASE)) #Use IGNORECASE

match = re.search(r'numbers - (?P<first>\d+), (?P<second>\d+)', text) #Assign names to groups and call them using the reference
print("l. Named groups:", match.groupdict() if match else "No match found")

#Match pattern in a multi-line text
multi_line_text = """This is a sample sentence. 
Here are some random numbers - 100, 650.
More numbers: 200, 350.
"""
print("m. Multi-line match for 'Here':", re.findall(r'^Here', multi_line_text, re.MULTILINE))
