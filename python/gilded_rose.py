# -*- coding: utf-8 -*-
from items.item_names_enum import ItemNames
from items.aged_brie import update_quality_aged_brie
from items.backstage import update_quality_backstage
from items.conjured import update_quality_conjured
from items.modify_item_attributes import decrease_quality, decrease_sell_in

class GildedRose(object):
    """
    Quality-related class variables
    """
    __MAX_ITEM_QUALITY = 50 
    __MIN_ITEM_QUALITY = 0 
    # items that do not have specific conditions for quality/sell_in modifications are regular
    __QUALITY_DECREMENT_REGULAR = 1
    __SELL_IN_DECREMENT = 1
    
    def __init__(self, items):
        self.items = items
        
    def update_quality(self):
        for item in self.items:
            if item.name==ItemNames.SULFURAS.value: 
                continue            
            
            decrease_sell_in(item, GildedRose.__SELL_IN_DECREMENT)
            
            if item.name==ItemNames.AGED_BRIE.value:
                update_quality_aged_brie(item, GildedRose.__MAX_ITEM_QUALITY) 
                           
            elif item.name==ItemNames.BACKSTAGE.value:
                update_quality_backstage(item, GildedRose.__MAX_ITEM_QUALITY)            

            elif item.name==ItemNames.CONJURED.value:
                update_quality_conjured(item, GildedRose.__MIN_ITEM_QUALITY)  
                              
            else:                
                if item.sell_in<0:
                    decrease_quality(item, GildedRose.__QUALITY_DECREMENT_REGULAR*2, GildedRose.__MIN_ITEM_QUALITY)
                else:
                    decrease_quality(item, GildedRose.__QUALITY_DECREMENT_REGULAR, GildedRose.__MIN_ITEM_QUALITY)
    
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
