
bak=open('kelimeler.txt','r').readlines()
dosya=open('kelimeler1.txt','w')
dosya.close()
ds=[]

for i in bak:
    b=i.replace("\n", "")
    ds.append(b)


for i in bak:
    i.replace('\n', '')
    if  ds.count(i) ==0 :
        bak2 =open('kelimeler1.txt','a')
        bak2.write(i)
        print (i)
bak2.close()