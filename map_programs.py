# insert update iterate

# Map Programs

d=dict()

d[1]="Suraj Sahani"
d[2]="Sayali Virkar"
d[3]="Komal"
d[4]="Kirti"
d[5]="Rubi"

print(d)

d[4]="Kajal"
print(d)

if 1 in d:
    print("Kajal is present in the map")
    
print(d.keys())
print(d.values())
print(d.items())

for index,key in enumerate(d):
    print(index," : ",key," : ",d[key])
