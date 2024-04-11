f=open('image.JPG','wb')
f1=open('download.JPG','rb')
for i in f1:
    f.write(i)
