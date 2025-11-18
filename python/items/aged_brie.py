def update_quality_aged_brie(item, max_aged_brie_quality):
    item.sell_in-=1  
    if item.sell_in<0:     
        item.quality=min(item.quality+2, max_aged_brie_quality)   
    else:
        item.quality=min(item.quality+1, max_aged_brie_quality) 
    return