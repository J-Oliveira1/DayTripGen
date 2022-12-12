destinations = "Charolotte, NC" , "Austin, TX", "Las Vegas, NV", "Boston, Ma"
resturants = "Southern BBQ", "Tacos", "Steak House", "Burgers"
entertainments = "Music Concert", "Sports Game", "Sight Seeing Tours", "Amusement Park"
transportations = "Ferry", "Train", "Taxi", "Tandem Bike"


import random
randomdesination = random.choice(destinations)
randomresturant = random.choice(resturants)
randomentertainment = random.choice(entertainments)
randomtransportation = random.choice(transportations)
print(f'Destination: {randomdesination}')
print(f'Resturant : {randomresturant}')
print(f'Entertainment: {randomentertainment}')
print(f'Transportation: {randomtransportation}')

full_trip = randomdesination + randomresturant + randomentertainment + randomtransportation
n = len(full_trip)

while True:
    determine_satisfaction = input("Are you satisfied with your trip? Y or N ")
    if determine_satisfaction == "Y":
        print(f"Here is your final trip! {full_trip}")
        break
    
    
    
