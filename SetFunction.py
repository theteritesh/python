s={10,20,30,40,50,60,70,80}

l=[90,100,110,120]
# update
s.update(l)
print(s)

#set()
l=set(l)
print(l,type(l))

#add()

s.add(90)
print(s)

#POP
p=s.pop()
print(p)

#remove
    
s.remove(50)
print(s)

# discard
s.discard(60)
print(s)

# clear

s.clear()
print(s)