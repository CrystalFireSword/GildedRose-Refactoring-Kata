# -*- coding: utf-8 -*-

class GildedRose(object):
    """
    Quality-related class variables
    """
    __MAX_ITEM_QUALITY = 50 
    __MIN_ITEM_QUALITY = 0
    __MAX_AGED_BRIE_QUALITY = __MAX_ITEM_QUALITY
    __MIN_AGED_BRIE_QUALITY = __MIN_ITEM_QUALITY
    __MAX_CONJURED_QUALITY = __MAX_ITEM_QUALITY
    __MIN_CONJURED_QUALITY = __MIN_ITEM_QUALITY
    __MAX_SULFURAS_QUANTITY = 80    
    
    def __init__(self, items):
        self.items = items
        self.update_quality_special_products = {
            "Aged Brie":self.__update_quality_Aged_Brie, 
            "Conjured Mana Cake":self.__update_quality_conjured,
            "Sulfuras, Hand of Ragnaros": self.__update_quality_Sulfuras, 
            "Backstage passes to a TAFKAL80ETC concert": self.__update_quality_backstage, 
            }
        
    def update_quality(self):
        for item in self.items:
            update_quality_special_product = self.update_quality_special_products.get(item.name)

            if update_quality_special_product is not None:
                update_quality_special_product(item)
                continue
            
            item.sell_in-=1
             
            item.quality=max(item.quality-1, GildedRose.__MIN_ITEM_QUALITY)
            if item.sell_in<0:
                item.quality=max(item.quality-1, GildedRose.__MIN_ITEM_QUALITY)
    
    def __update_quality_Aged_Brie(self, item):
        item.sell_in-=1
        item.quality=min(item.quality+1, GildedRose.__MAX_AGED_BRIE_QUALITY)   
        if item.sell_in<0:     
            item.quality=min(item.quality+1, GildedRose.__MAX_AGED_BRIE_QUALITY)   
        return
        
    def __update_quality_backstage(self, item):

        """
        bounds on the number of days remaining to sell concert tickets, 
        based on which quality is modified differently
        """
        
        CONCERT_DAYS_UB_1 = 10   
        CONCERT_DAYS_UB_2 = 5  
        
        # decrement number of days left to sell
        item.sell_in-=1
        
        if item.sell_in<0:
            item.quality=0
            return
        
        item.quality=min(item.quality+1, GildedRose.__MAX_ITEM_QUALITY) 

        if item.sell_in<CONCERT_DAYS_UB_1:
            item.quality=min(item.quality+1, GildedRose.__MAX_ITEM_QUALITY) 

        if item.sell_in<CONCERT_DAYS_UB_2:
            item.quality=min(item.quality+1, GildedRose.__MAX_ITEM_QUALITY)
        
        return 
       
    def __update_quality_Sulfuras(self, item):
        item.quality=GildedRose.__MAX_SULFURAS_QUANTITY
        return
    
    def __update_quality_conjured(self, item):
        item.sell_in-=1                  
        item.quality=max(item.quality-2, GildedRose.__MIN_CONJURED_QUALITY)
        if item.sell_in<0:
            item.quality=max(item.quality-2, GildedRose.__MIN_CONJURED_QUALITY)
        return
    
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
