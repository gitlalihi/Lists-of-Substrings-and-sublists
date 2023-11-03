#Python – Test if Substring occurs in specific position
userinput1= input(" Enter your string in the list seperated by a comma:")
strlist1=userinput1.split(',')
print("List of strings is:",strlist1)

userinput2= input(" Enter your substring")
print (userinput2)

flag = False

for substring in userinput2:
    for string in strlist1:
        if substring in string:
            flag = True

print("Does any substring occur in your list?", flag)

            
