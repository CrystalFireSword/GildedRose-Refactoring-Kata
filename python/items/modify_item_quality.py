# will be wayyyy better if these can be implemented inside the item class itself
# if allowed, but for now, assuming the class cannot be modified, writing
# an extra file here

def increase_quality(item, increase_by, upper_bound):
    item.quality=min(item.quality+(increase_by), upper_bound)

def decrease_quality(item, decrease_by, lower_bound):
    item.quality=max(item.quality-decrease_by, lower_bound)

def set_quality(item, value):
    item.quality = value