def index(a,y):
   x = len(a)
   i = 0
   while i < x:
        if a[i]==y:
          return i
        i=i+1
   return -1
        
a=[1,2,3,4,5]
y=12
h=index(a,y)
print(h)