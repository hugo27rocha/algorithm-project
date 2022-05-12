"""
implement an appropriate randomized input generator

m data centers(excluding the super data center)
m ≥ 4 
m1 ≥ 2
m − m1 ≥ 2 (tier 1 and tier 2 have at least two data centers each)

super data center indexed by j = 0

𝑠1 + 𝑠2 = s
s1= number of servers in tier1

𝑎𝑐𝑠𝑗 = 
The cost to access a different server in the same data center j

𝑎𝑐𝑓𝑗, 𝑗 = 1,...,𝑚  
cost between a data center j and its “father” 

r𝑖𝑗,𝑖=1,...,𝑠, 𝑗=1,...,𝑚
The cost to deploy a replica of the data block in server 𝑖 of data center j 


"""

import random

"""
m data centers(excluding the super data center)
m ≥ 4 
m1 ≥ 2
m − m1 ≥ 2 (tier 1 and tier 2 have at least two data centers each)
"""
m = random.randint(4, 10)
m1 = random.randint(2, m-2)

#test with low numbers
m=4
m1=2
m2=m-m1

#s >1
#s1= number of servers in tier1
#s2= number of servers in tier2
s1 = random.randint(1, 10)
s2 = random.randint(2, 10)

#test with low numbers
s1=2
s2=2
s=s1+s2

#LINE 2

#access costs to servers in tier 1
#how many datacenter in that tier + number of servers
acsS=[]
for x in range(0,m1):
    for y in range(0,s1):
        acsS.append(random.randint(1, 50))

#access costs to servers in tier 2
for x in range(0,m2):
    for y in range(0,s2):
        acsS.append(random.randint(1, 50))



#LINE 3
acf=[]
#access costs to data centers “fathers”
for x in range(0,m1):
    acf.append(random.randint(1, 50))



#LINE 5
r=[]
#deploy costs data center 1
for x in range(0,m1):
    r.append(random.randint(1, 50))

#deploy costs data center 2
for x in range(0,m2):
    r.append(random.randint(1, 50))



f = open("inputfile.txt", "w")

#1st line
f.write(str(m) + " " +str(m1)+ " " +str(s1)+ " " +str(s2) + '\n')

#2nd line
for i in acsS:
    f.write(str(i) + " ")
f.write('\n')

#3rd line
for i in acf:
    f.write(str(i) + " ")
f.write('\n')

#4rd line
f.write("4rd line -> did not understand (?) "+ '\n')

#5th line
for i in r:
    f.write(str(i) + " ")
f.write('\n')


f.close()




