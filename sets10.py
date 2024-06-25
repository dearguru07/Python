# s={}
# print(type(s)) ========> defaultly it gives type was dict


'''

s={1,55,75,65,9835,49}

# add()
# update({})
# pop()
# remove()


s.add(648)
print(s)

s.update({68,37,97,64})
print(s)

# s.pop()
# print(s)  ===> randomly remove one value

s.remove(65)
print(s)
'''


'''
union()
intersection()
difference()
issubset()  ===> true and false
issuperset()  ===> true and false

'''


set1={1,2,3}
set2={65,32,9,4,48,7,1}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2)) #=====> common value will be remove and only set1 is o/p
print(set1.symmetric_difference(set2))

