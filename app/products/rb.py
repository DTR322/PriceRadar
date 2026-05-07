

class RBProduct:
    def __init__(self, name: str | None = None,
                 sku: str | None = None,
                 shop_domain: str | None = None,
                 category: str | None = None,
                 url: str | None = None,
                 brand: str | None = None):
        self.name = name
        self.sku = sku
        self.shop_domain = shop_domain
        self.category = category
        self.url = url
        self.brand = brand


    def to_dict(self) -> dict:
        data = {
            'name': self.name,
            'sku': self.sku,
            'shop_domain': self.shop_domain,
            'category': self.category,
            'url': self.url,
            'brand': self.brand
        }
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data