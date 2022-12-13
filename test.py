destinations = "Charolotte, NC" , "Austin, TX", "Las Vegas, NV", "Boston, Ma"
resturants = "Southern BBQ", "Tacos", "Steak House", "Burgers"
entertainments = "Music Concert", "Sports Game", "Sight Seeing Tours", "Amusement Park"
transportations = "Ferry", "Train", "Taxi", "Tandem Bike"

import random

def generate_trip():
    randomdesination = random.choice(destinations)
    randomresturant = random.choice(resturants)
    randomentertainment = random.choice(entertainments)
    randomtransportation = random.choice(transportations)
  
    print(f'Destination: {randomdesination}')
    print(f'Resturant: {randomresturant}')
    print(f'Entertainment: {randomentertainment}')
    print(f'Transportation: {randomtransportation}')
    full_trips = f'Destination: {randomdesination}\nRestaurant: {randomresturant}\nEntertainment: {randomentertainment}\nTransportation: {randomtransportation}'
    return full_trips

def determine_satisfaction(day_trip):
    determine_satisfaction = input("Are you satisfied with your trip? Y or N ")
    if determine_satisfaction == "Y":
        print(f"Here is your final trip!\n{day_trip}")
    
   
        

        
    
def run_whole_day():
    result = generate_trip()
    determine_satisfaction(result)





run_whole_day()