from items.modify_item_quality import decrease_quality
def update_quality_conjured(item, min_conjured_quality):           
    if item.sell_in<0:
        decrease_quality(item, 4, min_conjured_quality)
    else:
        decrease_quality(item, 2, min_conjured_quality)
    return