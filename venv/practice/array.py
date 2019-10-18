import array as arr

vals = arr.array('i', [5,8,-7,6,4])

#for i in range(len(vals)):
 #   print (vals[i])
#for e in vals:
 #   print (e)

newArr = arr.array(vals.typecode, (a*a for a in vals))
for e in newArr:
    print (e)
