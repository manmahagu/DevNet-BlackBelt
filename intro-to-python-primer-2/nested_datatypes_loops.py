food={"vegetables":["carrots","kale","cucumber","tomato"],"desserts":["cake","ice cream", "donut"]}
for hungry in food["desserts"]:
	print("My favorite dessert is " + hungry)

cars={"sports":{"Volkswagen":"Porsche","Dodge":"Viper","Chevy":"Corvette"},"classic":{"Mercedes-Benz":"300SL","Toyota":"2000GT","Lincoln":"Continental"}}
for classicc in cars["classic"]:
	print("My favorite classics " + classicc + " car is a " + cars["classic"][classicc])
	
dessert={"iceCream":["Rocky Road","strawberry","Pistachio Cashew","Pecan Praline"]}
for taste in dessert["iceCream"]:
	print("My favorite ice cream taste is " + taste)

soup={"soup":{"tomato":"healthy","onion":"bleh!","vegetable":"good for you"}}
for souptype in soup["soup"]:
	print("This " + souptype +" soup is " + soup["soup"][souptype])