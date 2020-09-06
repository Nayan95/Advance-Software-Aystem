def largest(l):
    max=-999
    for i in l: 
        if max<i:
            max=i
    print("Maximum is :",max)

ll=[15,82,75,3,66]
print("List :",ll)
largest(ll)
