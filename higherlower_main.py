import art
import game_data as gd
import random as rand
import os

def highlow():

    random_int_1= rand.randint(0,len(gd.data)-1)
    random_int_2= rand.randint(0,len(gd.data)-1)

    if random_int_2 == random_int_1:
        while random_int_2 == random_int_1:
            random_int_2= rand.randint(0,len(gd.data)-1)
    game_on = True
    score = 0
    msg = ""
    while game_on:

        os.system('cls')
        print(art.logo)
        print(f"{msg}\nCurrent score: {score}.")
        first_pick = gd.data[random_int_1]
        second_pick = gd.data[random_int_2]

        #first pick
        name_first_pick = first_pick["name"]
        description_first_pick = first_pick["description"]
        country_first_pick = first_pick["country"]
        followers_first_pick = first_pick["follower_count"]
        #second pick
        name_second_pick = second_pick["name"]
        description_second_pick = second_pick["description"]
        country_second_pick = second_pick["country"]
        followers_second_pick = second_pick["follower_count"]

        print(f"Compare A: {name_first_pick}, a {description_first_pick}, from {country_first_pick}.")
        print(art.vs)
        print(f"Compare B: {name_second_pick}, a {description_second_pick}, from {country_second_pick}.")
        user_choice = input("Who has more followers? Type 'A' or 'B': ")
        winner = max(followers_first_pick,followers_second_pick)
        user_follower_count = None

        if user_choice.lower() == 'a':
            user_follower_count = followers_first_pick
        else:
            user_follower_count = followers_second_pick



        if user_follower_count == winner:
            score +=1
            msg = "You are right!"
            random_int_1 = random_int_2
            random_int_2= rand.randint(0,len(gd.data)-1)


            if random_int_2 == random_int_1:
                while random_int_2 == random_int_1:
                    random_int_2= rand.randint(0,len(gd.data)-1)


        else:
    ##        game_continue = False
            game_on = False
            print(f"You lost! Your final score is {score}")
            if (input("Play again? Type 'y' to play and 'n' to exit: ")) == 'y':
                highlow()
            else:
                print("Goodbye!")
highlow()


#IF WIN:
#You're right! current score: 1.
#Compare loser of last game with new one from list
