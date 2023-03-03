a=input("podaj liczbe: ")
b=input("podaj druga liczbe: ")
c=input("podaj trzecia liczbe: ")
a=int(a)
b=int(b)
c=int(c)
if (a>0&a<=10)&(a>b|b>c):
    print("a zawiera sie w przedziale (0,10> i a>b lub b>c) ")
else:
    print("nie spelnia zadnego z warunkow")