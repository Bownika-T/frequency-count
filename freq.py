a="baddc"
dic={}
for char in a:
    if char in  dic:
        dic[char]=dic[char]+1
    else:
        dic[char]=1
sort=sorted(dic.keys())
output=""
for char in sort:
    output=output+char+str(dic[char])
    
print(output)