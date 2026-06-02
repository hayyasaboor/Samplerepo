astring = "buttercup ftw"
doggo = list (astring)
slice = doggo[2:6]
print (slice)
>>>['t', 't', 'e', 'r']
astring = "buttercup ftw"
doggo = list (astring)
slice = doggo[:6]
print (slice)
>>>['b', 'u', 't', 't', 'e', 'r']
astring = "buttercup ftw"
doggo = list (astring)
slice = doggo[4:]
print (slice)
>>>['e', 'r', 'c', 'u', 'p', ' ', 'f', 't', 'w']
astring = "buttercup ftw"
doggo = list (astring)
slice = doggo[:]
print (slice)
>>>['b', 'u', 't', 't', 'e', 'r', 'c', 'u', 'p', ' ', 'f', 't', 'w']
astring = "buttercup ftw"
doggo = list (astring)
slice = doggo[2:10:2]
print (slice)
>>>['t', 'e', 'c', 'p]
astring = "buttercup ftw"
doggo = list (astring)
slice = doggo[::-1]
print (slice)
>>>['w', 't', 'f', ' ', 'p', 'u', 'c', 'r', 'e', 't', 't', 'u', 'b']
astring = "buttercup ftw"
doggo = list (astring)
slice = doggo[:-4:-1]
print (slice)
>>>['w', 't', 'f']
Or do this
astring = "buttercup ftw"
slice = list (astring)
print (slice[2:6])
print (slice[:6])
print (slice[4:])
print (slice[:])
print (slice[2:10:2])
print (slice[::-1])
print (slice[:-4:-1])

