#Python – Sort String by Custom Integer Substrings
userinput1= input(" Enter your string in the list seperated by a comma:")
strlist1=userinput1.split(',')
print("List of strings is:",strlist1)

result = sorted(strlist1,key=str,reverse=True)
print("Your sorted list based on integers Substring :",result)
    
