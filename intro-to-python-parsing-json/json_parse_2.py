var={"donut":{"flavors":["chocolate","jelly","maple","plain"]}}
print(var["donut"]["flavors"][0])
print("My favorite donut flavors are:", end=" ")
for f in var["donut"]["flavors"]:
	print(f, end=" ")
print()
print()

var1={"type":"donut","flavors":{"flavor":[{"type":"chocolate","id":1001}, {"type":"glazed","id":1002},{"type":"sprinkled","id":1003}]}}
print("Id: " + str(var1["flavors"]["flavor"][0]["id"]) + " type: " + var1["flavors"]["flavor"][0]["type"])
for f in var1["flavors"]["flavor"]:
	print("Id: " + str(f["id"]) + " type: " + f["type"])
print()
print()
	
	
#Using the examples above write code to print one value of each JSON structure and a loop to print all values.	
myvar={"exercise":{"high impact":["running","jumping","jump rope","running down stairs","skiing"]}}
print(myvar["exercise"]["high impact"][0])
for i in myvar["exercise"]["high impact"]:
	print(i)

print()
print()
myvar={"foods":{"healthy":["yogurt","nuts","vegetables","fruits","beans"]}}
print(myvar["foods"]["healthy"][0])
for i in myvar["foods"]["healthy"]:
	print(i)
	
myvar1={"author":"Stephen King","famous works":{"novels":[{"title":"The Shining","id":1001}, {"title":"Carrie","id":1002},{"title":"It","id":1003},{"title":"Misery","id":1004},{"title":"Night Shift","id":1005}]}}

print("author: " + myvar1["author"] + ". One of Famous work is " + myvar1["famous works"]["novels"][0]["title"])

for y in myvar1["famous works"]["novels"]:
	print("Id: " + str(y["id"]) + " novel: " + y["title"])
	
myvar1={"type":"car","cars":{"sports":[{"make":"Chevrolet", "model":"Corvette", "id":1001},{"make":"Chevrolet", "model":"Camaro", "id":1002},{"make":"Ford", "model":"Mustang", "id":1003},{"make":"Dodge", "model":"Viper", "id":1004},{"make":"Porsche", "model":"911", "id":1005}]}}
print("type " + myvar1["type"] + ". One of Fav car is " + myvar1["cars"]["sports"][0]["model"])
for y in myvar1["cars"]["sports"]:
	print("Id: " + str(y["id"]) + " make: " + y["make"] + " model: " + y["model"])