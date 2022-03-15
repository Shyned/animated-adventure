import random


#function that starts the game
def random_trip_planner_start():
      
   
    print("Welcome to day trip planner !!")
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

                    
                    locations_list = ["Hogwarts ","Willy Wonka's Factory","Gotham City","Asgard","South Park","middle earth"]
                    
                    print("Lets start by finding you a location.")

                    #users random selection
                    users_randm_place =random_finder(locations_list)
                    
                    
                    print(f"Your location is {users_randm_place}")

                    location_happiness = input("Are you happy with your selection(y or n): ")
                    
                    #re-select location and remove previous pick
                    if location_happiness == "n":
                        continue
                    else:
                        #will break out of a while loop and move to next loop
                        break
                
                
                while True:
                    
                    
                    mode_list = ["broom","jetpack","walking","flying","gaint hamster","teleportation"]


                    #users random selection
                    users_randm_mode =random_finder(mode_list)
                    

                    print(f"Your mode of transportation is {users_randm_mode}.")
                    

                    mode_happiness = input("Are you happy with your selection(y or n): ")
                    
                  
                    
                    if mode_happiness == "n":
                        continue
                        

                    else:
                        break
                        
                
                
                while True:
                    
                    #start of selections phase
                    restaurant_list = ["Bob's Burgers","The Krusty Krab","Monk's Café","Jack Rabbit Slims","The Three Broomsticks","Pizza Planet"]


                    #users random selection
                    users_randm_restaurant =random_finder(restaurant_list)
                    
                    
                    print(f"Your restaurant is {users_randm_restaurant}.")

                    restaurant_happiness = input("Are you happy with your selection(y or n): ")
                   
                    if restaurant_happiness == "n":
                        continue
                        

                    else:
                        break
                
                
                while True:
                    
                    #start of selections phase
                    entertainment_list = ["Labyrinth tour","lava rafting trip", "mars excavation","Graboid hunt", "legolas archery class"]


                    #users random selection
                    users_randm_entertainment =random_finder(entertainment_list)
                    
                    
                    print(f"Your entertainment is a {users_randm_entertainment}.")

                    entertainment_happiness = input("Are you happy with your selection(y or n): ")
                    
                    if entertainment_happiness == "n":
                        continue

                    else:
                        break
                
                while True:
                    print(f"You are headed to {users_randm_place} by {users_randm_mode}. While there you will eat at {users_randm_restaurant} and participate in {users_randm_entertainment}.")
                    over_all_happiness = input("Are you happy with your trip (y or n)" )

                    if over_all_happiness == "n":
                        print("Sorry to hear that let's try again.")
                        break


                    else:
                        print("Enjoy")
                        quit()

      
            else:
                print("Ok, see you next time.")
                break
        

    



random_trip_planner_start()