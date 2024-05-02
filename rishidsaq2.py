k=0
a="abcd"
b="dcab"
if len(a)!=len(b):
     print('no permutation')
else:
     for i in a:
          if i in b:
               k+=1
     if k==len(a)==len(b):
          print("permuatation") 
     else:
          print("no permutation")