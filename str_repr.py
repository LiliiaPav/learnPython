# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"Person {self.name}"
#     def __repr__(self):
#         return f"<Person ({self.name}, {self.age})>"

# bob= Person("Bob", 35)

# print(bob)

class Store:
    def __init__(self, name):
        self.name=name
        self.items=[]
    
    def add_item(self, name, price):
        self.name=name
        self.price=price
        self.items.append({"name": self.name, "price": self.price})

    # def stock_price(self):
    #     result=0
    #     for x in self.items:
    #         result+=x["price"]
    #     return(result)
    def stock_price(self):
        return sum([item['price'] for item in self.items])


vons = Store("Vons")
vons.add_item("Bread")