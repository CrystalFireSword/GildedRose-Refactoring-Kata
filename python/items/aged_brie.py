def update_quality_Aged_Brie(item, max_aged_brie_quality):
    item.sell_in-=1
    item.quality=min(item.quality+1, max_aged_brie_quality)   
    if item.sell_in<0:     
        item.quality=min(item.quality+1, max_aged_brie_quality)   
    return