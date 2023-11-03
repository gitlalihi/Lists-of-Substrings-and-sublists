#Python- Group sublists in your list
userinput1= input(" Enter your string in the list seperated by a comma:")
strlist1=userinput1.split(',')
print("List of strings is:",strlist1)

userinput2= input(" Enter your substring  in the second list seperated by a comma:")
strlist2=userinput2.split(',')
print("List of substrings is:",strlist2)

def grouping_list(strlist1,strlist2):
    return [[[i for i in strlist1 if i[0] == x ] for x in strlist2]]

print("Your modified list after grouping your sublist is:",grouping_list(strlist1,strlist2))