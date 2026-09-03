import exe07 as re
L=[12,33,42,55,12,12,45,42,12]


tab = []
for i in L:
    if i in tab:
        continue
    else:
        tab.append(i)
        print(f"{i} -> {re.compterOccurrences(i,L)} | ")

"""
Re=[]
Num=[]

for x in L:
    count=0

    for i in range(len(L)-1):
        
        if x == L[i]:
            count+=1
            number=L[i]     
                   
    Re.append(count)
    Num.append(number) 

    


print(Re)
print(Num)
"""
