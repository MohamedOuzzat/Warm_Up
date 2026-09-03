text="Hello my name is Mohamed"
text_2="spain is the word Cup champion"

t=text.split()
t2=text_2.split()
print(t)
print(t2)

for w in t:
    if len(w)<=3:
        t.remove(w)
        continue

for w in t2:
    if len(w)<=3:
        t2.remove(w)
        continue

print(t)
print(t2)