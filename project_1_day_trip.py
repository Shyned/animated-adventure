import random , time
from unicodedata import name



#function that starts the game
def random_trip_planner_start():
      
   
    print("Welcome to day trip planner !! \n My name is Johnny 5")
    #just for some time delay between response
    time.sleep(.5)

    users_name = input("What is your name : ")
    time.sleep(.5)
    print(f"{users_name},hahahahaha what a weird name. Sorry")

    
     #ask user if they would like to use trip planner
    user_start_game_choice =  input("Would you like to have plan a trip for you (y or n): ")
  
    #funuction to pick random item
    def random_finder(list_of_types):
        return random.choice(list_of_types)
    
   
   

    #condition to keep looping over location selection repeats if user/users doesn't like the selection
    while True:
            #start of selections phase 
            if user_start_game_choice == 'y':
                
                #loop will restart if user gets to the end and doesn't like the final result
                while True:

                    
                    locations_list = ["Hogwarts ","Willy Wonka's Factory","Gotham City","Asgard","South Park","middle earth","Silent Hill"]
                    
                    print("Lets start by finding you a location.")

                    #users random selection
                    users_randm_place =random_finder(locations_list)

                    locations_list.remove(users_randm_place)
                    print(locations_list)
                    time.sleep(.5)
                    print(f"Your location is {users_randm_place}")
                    
                    time.sleep(.5)
                    location_happiness = input("Are you happy with your selection(y or n): ")
                    
                    #re-select location and remove previous pick
                    if location_happiness == "n":
                        print("c'mon that was a good one but ok.")
                        continue
                    else:
                        #will break out of a while loop and move to next loop
                        break
                
                
                while True:
                    
                    time.sleep(.5)
                    mode_list = ["broom","jetpack","walking","flying","gaint hamster","teleportation","magic schhol bus",]


                    #users random selection
                    users_randm_mode =random_finder(mode_list)
                    
                    time.sleep(.5)
                    print(f"Your mode of transportation is {users_randm_mode}.")
                    
                    time.sleep(.5)
                    mode_happiness = input("Are you happy with your selection(y or n): ")
                    
                  
                    
                    if mode_happiness == "n":
                        print("Don't be difficult.")
                        continue
                        

                    else:
                        break
                        
                
                
                while True:
                    
                    #start of selections phase
                    restaurant_list = ["Bob's Burgers","The Krusty Krab","Monk's Café","Jack Rabbit Slims","The Three Broomsticks","Pizza Planet"]


                    #users random selection
                    users_randm_restaurant =random_finder(restaurant_list)
                    
                    time.sleep(.5)
                    print(f"Your restaurant is {users_randm_restaurant}.")

                    time.sleep(.5)
                    restaurant_happiness = input("Are you happy with your selection(y or n): ")
                   
                    if restaurant_happiness == "n":
                        print(f"{name} your killing me!")
                        continue
                        

                    else:
                        break
                
                
                while True:
                    
                    #start of selections phase
                    entertainment_list = ["Labyrinth tour","lava rafting trip", "mars excavation","Graboid hunt", "legolas archery class","gladiator school",]


                    #users random selection
                    users_randm_entertainment =random_finder(entertainment_list)
                    
                    time.sleep(.5)
                    print(f"Your entertainment is a {users_randm_entertainment}.")
                   
                    time.sleep(.5)
                    entertainment_happiness = input("Are you happy with your selection(y or n): ")
                    
                    if entertainment_happiness == "n":
                        print("why me!?!")
                        continue

                    else:
                        break
                
                while True:
                    time.sleep(.5)
                    print(f"You are headed to {users_randm_place} by {users_randm_mode}. While there you will eat at {users_randm_restaurant} and participate in {users_randm_entertainment}.")
                    over_all_happiness = input("Are you happy with your trip (y or n)" )

                    if over_all_happiness == "n":
                        time.sleep(.5)
                        print("OMG back to the start ")
                        time.sleep(.5)
                        break


                    else:
                        time.sleep(.5)
                        print(f"Alright Goodbye {users_name}")
                        quit()

      
            else:
                time.sleep(.5)
                print("Thanks for wasting my time.")
                break
        

    



random_trip_planner_start()
