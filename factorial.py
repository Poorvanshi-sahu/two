def fact(no):
    if no==1:
        return 1
    return no*fact(no-1)

def fact2(no,facto):
    if no==1:
        return facto
    facto[0]*=no
    fact2(no-1,facto)
    
facto=[1]
fact2(5,facto)
print(facto[0])
