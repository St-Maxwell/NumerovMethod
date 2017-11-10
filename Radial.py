R={"r0":1e-15}
F={"f0":0.0}
G={"g0":0.0}
nn=0

l=float(input("Enter angular quantum number(l<0):"))
s=float(input("Enter the increment sr:"))
m=int(input("Enter the number of intervals m:"))
E=float(input("Enter the reduced energy Er:"))

F["f1"]=0.0001
R["r1"]=R["r0"]+s
G["g0"]=l*(l+1)/(R["r0"]**2)-2/R["r0"]-2*E
G["g1"]=l*(l+1)/(R["r1"]**2)-2/R["r1"]-2*E
ss=s*s/12

for i in range(1,m+1):
    R["r%s" % (i+1)]=R["r%s" % i]+s
    G["g%s" % (i+1)]=l*(l+1)/(R["r%s" % (i+1)]**2)-2/R["r%s" % (i+1)]-2*E
    F["f%s" % (i+1)]=(-F["f%s" % (i-1)]+2*F["f%s" % i]+10*G["g%s" % i]*F["f%s" % i]*ss+G  ["g%s" % (i-1)]*F["f%s" % (i-1)]*ss)/(1-G["g%s" % (i+1)]*ss)
    if (F["f%s" % i]*F["f%s" % (i+1)]<0):
        nn=nn+1

print("Er="+str(E))
print("Nodes="+str(nn))
for i in range(m+1):
    print("%f %f" % (R["r%s" % i],(F["f%s" % i]/R["r%s" % i])))
