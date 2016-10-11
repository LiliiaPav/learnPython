# Print a single line of  space-separated integers denoting the final state of the array after performing d left rotations.
temp=raw_input()
temp= map (int, temp.strip().split())

val=raw_input()
val= map (int, val.strip().split())
d=temp[1]
for i in xrange(d):
    shift=val[0]
    del val[0]
    val.append(shift)
print ' '.join(map(str, val))