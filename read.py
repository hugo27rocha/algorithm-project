with open('inputfile.txt') as f:
    lines = f.readlines()

line1= lines[0].split()
line2= lines[1].split()
line3= lines[2].split()
line4= lines[3].split()
line5= lines[4].split()

#m data centers(excluding the super data center)
m = int(line1[0])

#number of datacenters in tier 1
m1= int(line1[1])

#number of datacenters in tier 2
m2=m-m1

#number of servers in tier 1
s1 = int(line1[2])

#number of servers in tier 2
s2 = int(line1[3])




datacenterList=[]
FatherCost={}
i=1
z=0
for x in range(1,m1+1):
    datacenterList.append("datacenter_"+str(i)+"_tier_1")
    FatherCost["datacenter_"+str(i)+"_tier_1"] = line3[z]
    i=i+1    
    z=z+1


for x in range(1,m2+1):
    datacenterList.append("datacenter_"+str(i)+"_tier_2")
    i=i+1

#print(datacenterList)

i=1
z=1
serverList=[]
for x in range(0,m1):
    for y in range(0,s1):
        serverList.append("datacenter_"+str(i)+"_tier_1" +
            "_server_"+str(z))
        z=z+1
    i=i+1

for x in range(0,m2):
    for y in range(0,s2):
        serverList.append("datacenter_"+str(i)+"_tier_2" +
            "_server_"+str(z))
        z=z+1
    i=i+1



serverCost={}
x=0
for i in serverList:
    serverCost[serverList[x]] = line2[x]
    x=x+1


deployCost={}
x=0
for i in datacenterList:
    deployCost[datacenterList[x]] = line5[x]
    x=x+1


print("Datacenter List")
print(datacenterList , '\n')
print("serverList")
print(serverList, '\n')
print("serverCost")
print(serverCost, '\n')
print("FatherCost")
print(FatherCost, '\n')
print("deployCost")
print(deployCost, '\n')
