#Python – Replace Substrings from String List to your list
userinput1= input(" Enter your string in the list seperated by a comma:")
strlist1=userinput1.split(',')
print("List of strings is:",strlist1)

userinput2= input(" Enter your substring  in the second list seperated by a comma:")
strlist2=userinput2.split(',')
print("List of substrings is:",strlist2)

newlist=[]
newlist=[i.replace(x[0],x[1]) for i in strlist1 for x in strlist2 if x[0] in i]
print("Your relaced list with substring  is :",str(newlist))

