food={"vegetables":["carrots","kale","cucumber","tomato"],"desserts":["cake","ice cream", "donut"]}
fav_veg = "My favorite vegetables is "
fav_des = "My favorite desserts is "
print(fav_veg + food["vegetables"][0])
print(fav_veg +  food["vegetables"][1])
print(fav_veg +  food["vegetables"][2])
print(fav_veg +  food["vegetables"][3])
print(fav_des + food["desserts"][0])
print(fav_des + food["desserts"][1])
print(fav_des + food["desserts"][2])


cars={"sports":{"Volkswagen":"Porsche","Dodge":"Viper","Chevy":"Corvette"},"classic":{"Mercedes-Benz":"300SL","Toyota":"2000GT","Lincoln":"Continental"}}
fav_sport = "My favorite sports car is "
fav_classic = "My favorite classic car is "
print(fav_sport + "a Dodge " + cars["sports"]["Dodge"])
print(fav_classic + "a Lincoln " + cars["classic"]["Lincoln"])
print(fav_classic + "a Mercedes-Benz " + cars["classic"]["Mercedes-Benz"])
print(fav_classic + "a Toyota " + cars["classic"]["Toyota"])

dessert={"iceCream":["Rocky Road","strawberry","Pistachio Cashew","Pecan Praline"]}
print(fav_des + dessert["iceCream"][0])
print(fav_des + dessert["iceCream"][1])
print(fav_des + dessert["iceCream"][2])
print(fav_des + dessert["iceCream"][3])

soup={"soup":{"tomato":"healthy","onion":"bleh!","vegetable":"good for you"}}
this_soup = "This soup is "
print(this_soup + soup["soup"]["tomato"])
print(this_soup + soup["soup"]["onion"])
print(this_soup + soup["soup"]["vegetable"])