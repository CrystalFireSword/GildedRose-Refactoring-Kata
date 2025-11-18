from items.modify_item_attributes import decrease_quality
def update_quality_conjured(item, min_conjured_quality):      
    QUALITY_DECREMENT_CONJURED = 2
    if item.sell_in<0:
        decrease_quality(item, QUALITY_DECREMENT_CONJURED*2, min_conjured_quality)
    else:
        decrease_quality(item, QUALITY_DECREMENT_CONJURED, min_conjured_quality)
    return