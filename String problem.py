## 1)Output== my name is adesh 
# sample = "my name is adesh"
#print(sample.split())
#l = []
#for i in sample.split():
 #   print(i.capitalize())
  #  l.append(i.capitalize())
#print(l)
#print(" ".join(l))



#### 2)abs@gmail.com   output : abs
#sample = "abs@gmail.com"
#print(sample[:sample.find('@')])



###3)input : [1,1,2,3,4,3,4,2,5,6,7,6,5,7]
#output :[1,2,3,4,5,6,7]
L1 = [1,1,2,3,4,3,4,2,5,6,7,6,5,7]
l = []
for i in L1:
    if i not in l:
        l.append(i)
print(l)
    