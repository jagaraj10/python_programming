a=input("enter the no:")
if(isinstance(a,(int,float))):
    if(a%2==0):
        print("even")
    else:
        print("odd")
else:
     print("invalid")
