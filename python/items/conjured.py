def update_quality_conjured(item, min_conjured_quality):
    item.sell_in-=1                  
    item.quality=max(item.quality-2, min_conjured_quality)
    if item.sell_in<0:
        item.quality=max(item.quality-2, min_conjured_quality)
    return