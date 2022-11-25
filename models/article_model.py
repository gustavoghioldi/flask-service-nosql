class ArticleModel:
    def __init__(self, sku:str,name:str, description:str, price:float, tags:tuple) -> None:
        self.__sku =sku
        self.__name = name
        self.__description = description
        self.__price = price
        self.__tags = tags
        self._validate_sku()
        
    def _validate_sku(self):
        if len(self.__sku) >25:
            raise Exception("sku in too long (max: 24 chars)")

    def json(self):
        return {
            "sku" : self.__sku,
            "name" : self.__name,
            "description": self.__description,
            "price": self.__price,
            "tags": self.__tags
        }
