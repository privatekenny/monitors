class Product:
    def __init__(self, name, size, price, link, image):
        self.name = name
        self.size = size
        self.price = price
        self.link = link
        self.image = image

    def get_product(self):
        product_dict = {
            "name": self.name,
            "size": self.size,
            "price": self.price,
            "link": self.link,
            "image": self.image
        }

        return product_dict
