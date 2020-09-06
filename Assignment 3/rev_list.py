def rev(l):
    rev_l=[]
    for i in range(len(l)-1,0,-1):
        rev_l.append(l[i])
    print("Reversed List :",rev_l)

org_l=[9,56,826,784,529,351]
print("Original List :",org_l)
rev(org_l)
