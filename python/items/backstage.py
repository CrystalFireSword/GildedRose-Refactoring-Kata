from items.modify_item_attributes import increase_quality, set_quality
def update_quality_backstage(item, max_backstage_quality):
    """
    bounds on the number of days remaining to sell concert tickets, 
    based on which quality is modified 
    """        
    CONCERT_DAYS_UB_1 = 10   
    CONCERT_DAYS_UB_2 = 5  
    CONCERT_DAYS_LB = 0
    QUALITY_INCREMENT_BACKSTAGE_1 = 1
    QUALITY_INCREMENT_BACKSTAGE_2 = 2
    QUALITY_INCREMENT_BACKSTAGE_3 = 3
    
    if item.sell_in>=CONCERT_DAYS_UB_1:
        increase_quality(item, QUALITY_INCREMENT_BACKSTAGE_1, max_backstage_quality)
    elif item.sell_in>=CONCERT_DAYS_UB_2:
        increase_quality(item, QUALITY_INCREMENT_BACKSTAGE_2, max_backstage_quality)
    elif item.sell_in>=CONCERT_DAYS_LB:
        increase_quality(item, QUALITY_INCREMENT_BACKSTAGE_3, max_backstage_quality)
    else:
        set_quality(item, 0)     
    
    return 