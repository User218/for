#Git verkefni FOR
#Alexander Örn
#25/01/17

#Dæmi 1
t1=int(input("Sláðu inn tölu: "))
t2=int(input("Sláðu inn aðra tölu: "))
print("Tölurnar lagðar saman eru",t1+t2,"og tölurnar margfaldaðar saman eru",t1*t2)

#Dæmi 2
fn=input("Fornafn:")
en=input("Eftirnaft: ")
print("Halló",fn,en)

#Dæmi 3
texti=input("Sláðu inn texta: ")
c = 0
b = 0
for i in texti:
    if i.isupper():
        c += 1
for i in texti:
    if i.islower():
        b += 1
print()
print("Í þessum texta eru:")
print(c,"hástafir og",b,"lágstafir.")