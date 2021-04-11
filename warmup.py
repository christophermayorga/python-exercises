truck = "toyota tacoma"
sedan = "hyundai sonata"
sports_car = "lamborghini diablo"

def car_to_dict(str):
    return dict(make=str.split()[0], model=str.split()[1])
print(car_to_dict(truck))
def capitalized_car_to_dict(str):
    return dict(make=(str.split()[0]).capitalize(), model=(str.split()[1]).capitalize())
print(capitalized_car_to_dict(truck))

trucks = [
    {'make': 'honda',
    'model': 'ridgeline'},
    {'make': 'ford',
    'model': 'ranger'},
    {'make': 'chevrolet',
    'model': 'colorado'}
]

for truck in trucks:
    truck['make'] = truck['make'].upper()
    truck['model'] = truck['model'].upper()
print(trucks)