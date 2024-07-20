def calculate_shipping_cost(weight, destination):
    
    if weight <= 0 or weight > 20:
        return "Invalid weight"
    
    if destination == "domestic":
        rate = 1.5
    elif destination == "international":
        rate = 2
    else:
        return "Invalid destination"
    
    if weight <= 10:
        return weight * 0.5 * rate
    else:
        return weight * 0.3 * rate