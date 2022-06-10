def double_char(s):
    out = []
    for i in s:
        out.append(i+""+i)
    return "".join(out)   
s=input()
item=double_char(s) 
print(item)    