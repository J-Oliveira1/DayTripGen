destinations = "Charolotte, NC" , "Austin, TX", "Las Vegas, NV", "Boston, Ma"
resturants = "Southern BBQ", "Tacos", "Steak House", "Burgers"
entertainments = "Music Concert", "Sports Game", "Sight Seeing Tours", "Amusement Park"
transportations = "Ferry", "Train", "Taxi", "Tandem Bike"



import random


while True:
    randomdesination = random.choice(destinations)
    randomresturant = random.choice(resturants)
    randomentertainment = random.choice(entertainments)
    randomtransportation = random.choice(transportations)


    full_trips = f'{randomdesination}\n{randomresturant}\n{randomentertainment}\n{randomtransportation}'
    print(f'Destination: {randomdesination}')
    print(f'Resturant: {randomresturant}')
    print(f'Entertainment: {randomentertainment}')
    print(f'Transportation: {randomtransportation}')
    determine_satisfaction = input("Are you satisfied with your trip? Y or N ")
    if determine_satisfaction == "Y":
        print(" ")
        print(f"Here is your final trip!\n{full_trips}")
        print(" ")
        break

    else:
        pass

        
        
        