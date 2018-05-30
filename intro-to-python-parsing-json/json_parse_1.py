# Part 1
var={"car":"volvo", "fruit":"apple"}
print(var["fruit"])
for f in var:	
	print("key: " + f + " value: " + var[f])

# Printing blank lines
print()
print()

# Part 2	
var1={"donut":["chocolate","glazed","sprinkled"]}
print(var1["donut"][0])
print("My favorite donut flavors are:", end= " ")
for f in var1["donut"]:
	print(f)

# Printing blank lines
print()
print()

#Using the examples above write code to print one value of each JSON structure and a loop to print all values.	
var={"vegetable":"carrot", "fruit":"apple","animal":"cat","day":"Friday"}
print(var["vegetable"])
for i in var:
	print("key: " + i + " Value: " + var[i])

var1={"animal":["dog","cat","fish","tiger","camel"]}
print(var1["animal"][0])
for y in var1["animal"]:
	print(y)

myvar={"dessert":"ice cream", "exercise":"push ups","eyes":"blue","gender":"male"}
print(myvar["dessert"])
for z in myvar:
		print(myvar[z])

myvar1={"dessert":["cake","candy","ice cream","pudding","cookies"]}
print(myvar1["dessert"][0])
for a in myvar1["dessert"]:
	print(a)