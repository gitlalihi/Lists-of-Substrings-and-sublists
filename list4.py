#Python - Remove Redundant Substrings from Strings List
userinput1= input(" Enter your string in the list seperated by a comma:")
strlist1=userinput1.split(',')
print("List of strings is:",strlist1)
newlist=[]

strlist1.sort(key=len,reverse=True)

for i ,val in enumerate (strlist1):
    isredundant=False
    for j in range (i+1,len(strlist1)):
        if val in strlist1[j]:
            isredundant=True
            break
    if not isredundant:
        newlist.append(val)    
    
print("The filtered list : " ,newlist)
   