alpha=raw_input("enter the input:")
if(isinstance(alpha,str)):
    x=alpha.lower()
    if(x in ('a','e','i','o','u')):
        print("vowel")
    else:
        print("consonants")
