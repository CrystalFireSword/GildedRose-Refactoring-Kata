def update_quality_backstage(item, max_backstage_quality):
    """
    bounds on the number of days remaining to sell concert tickets, 
    based on which quality is modified 
    """        
    CONCERT_DAYS_UB_1 = 10   
    CONCERT_DAYS_UB_2 = 5  
    CONCERT_DAYS_LB = 0
    
    # decrement number of days left to sell
    item.sell_in-=1
    
    if item.sell_in>=CONCERT_DAYS_UB_1:
        item.quality=min(item.quality+1, max_backstage_quality) 
    elif item.sell_in>=CONCERT_DAYS_UB_2:
        item.quality=min(item.quality+2, max_backstage_quality) 
    elif item.sell_in>=CONCERT_DAYS_LB:
        item.quality=min(item.quality+3, max_backstage_quality)
    else:
        item.quality=0       
    
    return 