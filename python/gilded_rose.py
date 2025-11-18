# -*- coding: utf-8 -*-
from items.item_names_enum import ItemNames
from items.aged_brie import update_quality_aged_brie
from items.backstage import update_quality_backstage
from items.conjured import update_quality_conjured
    
class GildedRose(object):
    """
    Quality-related class variables
    """
    __MAX_ITEM_QUALITY = 50 
    __MIN_ITEM_QUALITY = 0 
    
    def __init__(self, items):
        self.items = items
        
    def update_quality(self):
        for item in self.items:
            if item.name==ItemNames.SULFURAS.value: 
                continue            
            
            self.__update_sell_in(item)
            
            if item.name==ItemNames.AGED_BRIE.value:
                update_quality_aged_brie(item, GildedRose.__MAX_ITEM_QUALITY) 
                           
            elif item.name==ItemNames.BACKSTAGE.value:
                update_quality_backstage(item, GildedRose.__MAX_ITEM_QUALITY)            

            elif item.name==ItemNames.CONJURED.value:
                update_quality_conjured(item, GildedRose.__MIN_ITEM_QUALITY)  
                              
            else:                
                if item.sell_in<0:
                    item.quality=max(item.quality-2, GildedRose.__MIN_ITEM_QUALITY)
                else:
                    item.quality=max(item.quality-1, GildedRose.__MIN_ITEM_QUALITY)
    
    def __update_sell_in(self, item):
        item.sell_in-=1
        return
    
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
