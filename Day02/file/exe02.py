with open("data/exercice.txt","r") as file:
    reader=file.readlines()
    # print(reader.value())

keys=[]
val=[]
all=[]
for i in reader:
    print(i)

for i in reader:
    k=i.split(" ",1)
    print(k)
    keys.append(k[0])

# print(f"{keys}\n")
    