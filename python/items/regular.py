from items.modify_item_attributes import decrease_quality
def update_quality_regular(item, quality_decrement_regular, min_regular_quality):      
    if item.sell_in<0:
        decrease_quality(item, quality_decrement_regular*2, min_regular_quality)
    else:
        decrease_quality(item, quality_decrement_regular, min_regular_quality)
    return