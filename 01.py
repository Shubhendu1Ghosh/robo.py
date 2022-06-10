def func1():
    print('''Enter no.s giving space btw 
    consequtive nos to make a list''')
    l1=input()
    a=l1.split()
    print('''Enter asc or desc or none''')
    l2=input() 
    if l2=="asc":
      a.sort()
    elif l2=="desc":
      a.sort(reverse=True)
    elif l2=="none":
      a
    return a  
c=func1()
print(c)  