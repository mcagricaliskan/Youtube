



"""
range(100) o sayıya kadar git
range(50,100) 50 den o sayıya git
range(50,100,2) 50 den o sayıya kadar 2 2 atlayarak

"""

"""


for sayi in range(1,100,2):     # range(100) 0 dan 100 e kadar olan sayılar (50,100) dersek 50 den 100 e kadar olan sayıları yazdırır.
    print(sayi)
    
"""



"""
Liste = ["Mehmet","Alper","Cemil","Fatih","Meral","Buse","Ceren"]

for i in Liste:
    print(i)
    
"""
"""

Liste = []

for i in range(100):
    Liste.append(i)
    
"""

"""
Liste = ["Mehmet","Alper","Cemil","Fatih","Meral","Buse","Ceren","Mehmet"]
ListeMehmet = []

for i in Liste:
    if i == "Mehmet":
        ListeMehmet.append(i)
        
"""
"""
for i in range(100,0,-1):
    print(i)"""
 
"""
    
for i in range(100):
    if i == 50:
        break
    
    print(i)
    
"""




Liste = ["Mehmet","Alper","Cemil","Fatih","Meral","Buse","Ceren","Mehmet"]

for i in Liste:  
    
    if i == "Meral":
        continue
    print(i)


