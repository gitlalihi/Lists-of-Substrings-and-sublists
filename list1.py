#Python – Count Strings with substring String List
userinput1= input("Enter your list of string seperated by a comma:")
str1input=userinput1.split(',')
print("Your list of strings is :",str1input)

userinput2= input("Enter your substring:")
print("Your substring is :",userinput2)

newlist=[]
newlist=len([i for i in str1input if userinput2 in i])
print("The count for the given substring entered by you in your list is:",newlist)