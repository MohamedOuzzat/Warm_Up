keys=[]
info=[]
all=[]
with open("data/exercice.txt","r") as file:
    reader = file.readlines()
    for i in reader:
        k=i.split(" ",1)
        # print(k,type(k))
        # print(k[0])
        info.append(k[1])
        keys.append(k[0])

for i in range(len(info)):
    obj={
        keys[i]:info[i]
    }
    all.append(obj)
# print(all)
# print(obj)
# print(keys)
# print(info)
# print(reader)
# print(all)
with open("data/exercice.txt","w")as file:
    for i in all:
        file.write(f"{i}\n")

