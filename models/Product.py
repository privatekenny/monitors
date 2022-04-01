class Product:
    def __init__(self, name, size, price, link, image):
        self.name = name
        self.size = size
        self.price = price
        self.link = link
        self.image = image

    def get_product(self):
        return self.__dict__
