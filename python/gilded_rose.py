# -*- coding: utf-8 -*-

class GildedRose(object):
    """
    Quality-related class variables
    """
    _MAX_ITEM_QUALITY = 50 
    _MIN_ITEM_QUALITY = 0
    _MAX_AGED_BRIE_QUALITY = _MAX_ITEM_QUALITY
    _MIN_AGED_BRIE_QUALITY = _MIN_ITEM_QUALITY
    _MAX_CONJURED_QUALITY = _MAX_ITEM_QUALITY
    _MIN_CONJURED_QUALITY = _MIN_ITEM_QUALITY
    _SULFURAS_MAX_ITEM_QUALITY = 80    
    
    def __init__(self, items):
        self.items = items
        self.update_quality_special_products = {
            "Aged Brie":self._update_quality_Aged_Brie, 
            "Conjured Mana Cake":self._update_quality_conjured,
            "Sulfuras, Hand of Ragnaros": self._update_quality_Sulfuras, 
            "Backstage passes to a TAFKAL80ETC concert": self._update_quality_backstage, 
            }
        
    def update_quality(self):
        for item in self.items:
            update_quality_special_product = self.update_quality_special_products.get(item.name)

            if update_quality_special_product is not None:
                update_quality_special_product(item)
                continue
            
            item.sell_in-=1
             
            item.quality=max(item.quality-1, GildedRose._MIN_ITEM_QUALITY)
            if item.sell_in<0:
                item.quality=max(item.quality-1, GildedRose._MIN_ITEM_QUALITY)
    
    def _update_quality_Aged_Brie(self, item):
        item.sell_in-=1
        item.quality=min(item.quality+1, GildedRose._MAX_AGED_BRIE_QUALITY)   
        if item.sell_in<0:     
            item.quality=min(item.quality+1, GildedRose._MAX_AGED_BRIE_QUALITY)   
        return
        
    def _update_quality_backstage(self, item):

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
        
        item.quality=min(item.quality+1, GildedRose._MAX_ITEM_QUALITY) 

        if item.sell_in<CONCERT_DAYS_UB_1:
            item.quality=min(item.quality+1, GildedRose._MAX_ITEM_QUALITY) 

        if item.sell_in<CONCERT_DAYS_UB_2:
            item.quality=min(item.quality+1, GildedRose._MAX_ITEM_QUALITY)
        
        return 
       
    def _update_quality_Sulfuras(self, item):
        item.quality=GildedRose._SULFURAS_MAX_ITEM_QUALITY
        return
    
    def _update_quality_conjured(self, item):
        item.sell_in-=1                  
        item.quality=max(item.quality-2, GildedRose._MIN_CONJURED_QUALITY)
        if item.sell_in<0:
            item.quality=max(item.quality-2, GildedRose._MIN_CONJURED_QUALITY)
        return
    
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
