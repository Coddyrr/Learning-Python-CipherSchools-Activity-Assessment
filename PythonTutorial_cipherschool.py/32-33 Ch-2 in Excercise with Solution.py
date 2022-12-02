#take two comma seperated inputs from user
#1.)user's name , example - "Surjeet"
#2.)a single character , "Surjeet"

#output - 2 print lines
#1.)user's name length
#2.)count the character that user inputed(bonus : case insensitive coount)

name, chr = input("enter comma seperated name and character : ").split(",")
print(f"length of your name is {len(name)}")
print(f"character count : {name.lower().count(chr.lower())}") # case sensitive
#Surjeet - surjeet
#S - s