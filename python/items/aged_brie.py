from items.modify_item_quality import increase_quality

def update_quality_aged_brie(item, max_aged_brie_quality): 
    QUALITY_INCREMENT_AGED_BRIE = 1
    if item.sell_in<0:   
        increase_quality(item, QUALITY_INCREMENT_AGED_BRIE*2, max_aged_brie_quality)   
    else:
        increase_quality(item, QUALITY_INCREMENT_AGED_BRIE, max_aged_brie_quality) 
    return