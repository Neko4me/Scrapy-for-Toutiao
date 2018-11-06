from scrapy import Item, Field
class ImageItem(Item):
    collection=table='images'
    title=Field()
    url=Field()