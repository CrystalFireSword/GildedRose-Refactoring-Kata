# -*- coding: utf-8 -*-
from enum import Enum
from items.aged_brie import update_quality_Aged_Brie
from items.backstage import update_quality_backstage

class ItemNames(Enum):
    AGED_BRIE = "Aged Brie"
    CONJURED = "Conjured Mana Cake"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
    
class GildedRose(object):
    """
    Quality-related class variables
    """
    __MAX_ITEM_QUALITY = 50 
    __MIN_ITEM_QUALITY = 0 
    
    def __init__(self, items):
        self.items = items
        self.update_quality_special_products = {
            ItemNames.CONJURED.value:self.__update_quality_conjured,
            }
        
    def update_quality(self):
        for item in self.items:
            if item.name==ItemNames.SULFURAS.value:
                continue
            
            if item.name==ItemNames.AGED_BRIE.value:
                update_quality_Aged_Brie(item, GildedRose.__MAX_ITEM_QUALITY)
                continue
            
            if item.name==ItemNames.BACKSTAGE.value:
                update_quality_backstage(item, GildedRose.__MAX_ITEM_QUALITY)
                continue
                
            update_quality_special_product = self.update_quality_special_products.get(item.name)

            if update_quality_special_product is not None:
                update_quality_special_product(item)
                continue
            
            item.sell_in-=1
             
            item.quality=max(item.quality-1, GildedRose.__MIN_ITEM_QUALITY)
            if item.sell_in<0:
                item.quality=max(item.quality-1, GildedRose.__MIN_ITEM_QUALITY)
    
    def __update_quality_conjured(self, item):
        item.sell_in-=1                  
        item.quality=max(item.quality-2, GildedRose.__MIN_ITEM_QUALITY)
        if item.sell_in<0:
            item.quality=max(item.quality-2, GildedRose.__MIN_ITEM_QUALITY)
        return
    
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
