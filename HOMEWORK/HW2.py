para="""Python is  powerfull language. Python is object-oriented programming language."""

print("\nLength of paragraph:",len(para))

print("\nFirst Character:",para[0])
print("Last Character:",para[-1])

print("\nPreview:",para[:50])

paragraph = "Python"
print(paragraph.replace("Python", "\nPYTHON"))


print("\nLowercase: ",para.lower())

print(para.strip())

print("\nList of word:",para.split())

a="\nCourse" in para
print(a)

message="The course descripition is {} character long and has {} word."
print("\nLength of message:",len(message))
