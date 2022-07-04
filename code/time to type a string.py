keyboard=input()
text=input()
m=0
previous=0
for i in text:
    present=keyboard.index(i)
    m+=abs((present-previous))
    previous=present
print(m)