#Filter 
print(list(filter(lambda x:x<6,[0,1,2,3,4,5,6,7,8,9])))

#Map
print(list(map(lambda x:x<6,[0,1,2,3,4,5,6,7,8,9])))

#filter within map function
print(set(map(lambda x:x+2,list(filter(lambda x:x>=3,[0,1,2,3,4,5,6,7])))))

#map within filter
print(set(filter(lambda x:x+2,list(map(lambda x:x>=3,[0,1,2,3,4,5,6,7])))))


#map within a filter function
print(list(filter(lambda x:x%2==0,
            list(map(lambda x:x+3,[1,2,3,4])))))

#filter within map function
print(list(filter(lambda x:x<4,
            list(map(lambda x:x+1,
                     [1,2,3,4,5,6,7,8,9])))))