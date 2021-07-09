class Country:
    def __init__(self, name, continent):
        self.name = name
        self.continent = continent

    def present(self):
        return f"The country is {self.name} which is in {self.continent}"

class Brand:
    def __init__(self, b_name, s_date):
        self.b_name = b_name
        self.s_date = s_date

    def present(self):
        return f"The {self.b_name} was established at {self.s_date}"

class Season:
    def __init__(self, s_name, temp):
        self.s_name = s_name
        self.temp = temp

    def present(self):
        return f"In {self.s_name} the average temperature is {self.temp}"

class Product(Country, Brand, Season):
    def __init__(self, p_name, type, price, quantity, promo):
         Country.__init__(self, name, continent)
         Brand.__init__(self, b_name,s_date)
         Season.__init__(self, s_name, temp)
         self.p_name = p_name
         self.type = type
         self.price = price
         self.quantity = quantity
         self.promo = promo

    def present(self):
        #return f"name: {self.p_name}, type: {self.type}, price: {self.price}, quantity: {self.quantity}"
        return f"The {self.p_name} is ideal for {self.s_name} and average temperature {self.temp}.This {self.type} is very comfortable and is from company {self.b_name}, which was estab;ished at {self.s_date}." \
               f"The company makes its products in {self.name} which is in {self.continent}"

    def discount(self):
        if self.promo == "ARM":
            return f"{self.price - (self.price * 0.2)} is your new price"
        else:
            return f"Invalid promocode: {self.promo}"
            #return self.price - (self.price * 0.2)

    def increase(self):
        self.quantity += 1
        return f"You added one new {self.p_name},that means that currently there are {self.quantity} of them"

    def decrease(self):
        self.quantity -= 1
        return f"You cleared one {self.p_name},that means that currently there are {self.quantity} of them"


country_1 = Country("Armenia", "Eurasia")
brand_1 = Brand("Nike", "12/12/1980")
# #winter = Season("winter", -10)
# spring = Season("spring", 15)
summer = Season("summer", 35)
# autumn = Season("autumn", 20)
pr_1 = Product("shoes", "sneakers", 1500, 5, "ARM")
# print(pr_1.discount())
# print(pr_1.increase())
# print(pr_1.decrease())
print(pr_1.present())
