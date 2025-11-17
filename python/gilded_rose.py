# -*- coding: utf-8 -*-

class GildedRose(object):
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def __init__(self, items):
        self.items = items
        self.update_quality_special_products = {
            "Aged Brie":self._update_quality_Aged_Brie, 
            "Backstage passes to a TAFKAL80ETC concert": self._update_quality_backstage, 
            "Sulfuras, Hand of Ragnaros": self._update_quality_Sulfuras, 
            "Conjured Mana Cake":self._update_quality_conjured
            }
        
    def update_quality(self):
        for item in self.items:
            update_quality_special_product = self.update_quality_special_products.get(item.name)

            if update_quality_special_product is not None:
                update_quality_special_product(item)
                continue
            
            item.sell_in-=1
             
            item.quality=max(item.quality-1, GildedRose.MIN_QUALITY)
            if item.sell_in<0:
                item.quality=max(item.quality-1, GildedRose.MIN_QUALITY)

    def check_quality_limit(self, item, upper_limit=MAX_QUALITY):
        if item.quality>upper_limit or item.quality<0:
            return False
        return True
    
    def _update_quality_Aged_Brie(self, item): 
        item.sell_in-=1
        item.quality=min(item.quality+1, GildedRose.MAX_QUALITY)   
        if item.sell_in<0:     
            item.quality=min(item.quality+1, GildedRose.MAX_QUALITY)   
        return
        
    def _update_quality_backstage(self, item):
        # decrement number of days left to sell
        item.sell_in-=1

        CONCERT_DAYS_UB_1 = 10
        CONCERT_DAYS_UB_2 = 5
        if item.sell_in<0:
            item.quality=0
            return
        item.quality=max(item.quality-1, GildedRose.MIN_QUALITY)
        if item.sell_in<CONCERT_DAYS_UB_1:
            item.quality=min(item.quality+1, GildedRose.MAX_QUALITY)        
        if item.sell_in<CONCERT_DAYS_UB_2:
            item.quality=min(item.quality+1, GildedRose.MAX_QUALITY)
        
        return 
       
    def _update_quality_Sulfuras(self, item):
        SULFURAS_MAX_QUALITY = 80
        item.quality=SULFURAS_MAX_QUALITY
        return
    
    def _update_quality_conjured(self, item):
        item.sell_in-=1                  
        item.quality=max(item.quality-2, GildedRose.MIN_QUALITY)
        if item.sell_in<0:
            item.quality=max(item.quality-2, GildedRose.MIN_QUALITY)
        return
    
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

'''
            Conditions:
            1. quality always >0 and <=50
            2. sell_in can be negative
            3. assume when sell_in>0 and default, lower both of them by 1
            4. if sell_in<0: degrade quality twice;
            5. Anomaly:
                i. Aged Brie - increase quality, but always <=50
                ii. Sulfuras - do nothing, set maximum quality 80
                iii. Backstage pass - increase Q by 2 if 5<sellIn<10, and by 3 if 0<sellIn<5, 0 otherwise
                iv. Conjured - degrade twice as fast in quality
            Steps:
            1. Have a dictionary that has a dict for special products, and each product have its own update function
            2. Otherwise, do a normal decrement
            3. Define class variables for magic numbers
            '''