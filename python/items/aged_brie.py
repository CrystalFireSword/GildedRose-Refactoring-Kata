from items.modify_item_quality import increase_quality

def update_quality_aged_brie(item, max_aged_brie_quality): 
    if item.sell_in<0:   
        increase_quality(item, 2, max_aged_brie_quality)   
    else:
        increase_quality(item, 1, max_aged_brie_quality) 
    return