st="core@426"
count1=0
count2=0
count3=0
for i in st:
    if i>='a' and i<='z' or i>='A' and i<='Z':
        count1+=1
    elif i>='0' and i<='9':
        count2+=1
    else:
        count3+=1
        print('count of alphabets',count1)
        print('count of digits',count2)
        print('count of specialchar',count3)