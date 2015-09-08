def hotel_cost(nights):
    return nights*140
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city== "Pittsburgh":
        return 222
    elif city=="Los Angeles":
        return 475
        
def rental_car_cost(days):
        if days>=7:
            return 40*days-50
        elif days>=3:
                return days*40-20
        else:
            return days*40
            
def trip_cost(city,days,spending_money):
            return plane_ride_cost(city)+hotel_cost(days)+rental_car_cost(days)+spending_money
print trip_cost("Los Angeles",5,600)
        
        
