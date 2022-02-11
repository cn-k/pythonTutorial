class Car:
    def __init__(self, id, brand, model, package, year, km, color, price, href, img):
        self.id = id
        self.brand = brand
        self.model = model
        self.package = package
        self.year = year
        self.km = km
        self.color = color
        self.price = price
        self.href = href
        self.img = img

    def __str__(self):
        return self.id + "|" + self.brand + "|" + self.model + "|" + self.package + "|" + str(self.year) + "|" + self.km + "|" + self.color + "|" + self.price + "|" + self.href + "|" + self.img