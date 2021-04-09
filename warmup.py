truck = "toyota tacoma"
sedan = "hyundai sonata"
sports_car = "lamborghini diablo"

def car_to_dict(str):
    return dict(make=str.split()[0], model=str.split()[1])

def capitalized_car_to_dict(str):
    return dict(make=(str.split()[0]).capitalize(), model=(str.split()[1]).capitalize())

def yell_car_to_dict(str):
    return dict(make=(str.split()[0]).upper(), model=(str.split()[1]).upper())

print(car_to_dict(truck))
print(capitalized_car_to_dict(truck))
print(yell_car_to_dict(truck))