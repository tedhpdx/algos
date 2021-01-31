
st = "algorithm"
len_list = []
def check_string(i,j):
    global ss_len
    ss_len = 0
    while (st[i] == st[j]):
        i+=1
        j-=1
        if (i==j or i>len(st)-1 or j<1):
            return ss_len
        ss_len += 1
    return ss_len

for i in range(len(st)):
    for j in range(i+1,len(st)):
        if st[i] == st[j]:
            len_list.append(check_string(i,j))
if len_list:
    print (max(len_list))
else:
    print ('0')