"""Restaurant rating lister."""
def add_rating():

    restaraunt_name = input("Name of restaraunt: > ")
    restaraunt_rating = input("Rating: >")

    restaraunt_name = restaraunt_name.title()

    return (restaraunt_name, restaraunt_rating)


def sort_print_resto(rating_dict):
    restaraunts = sorted((rating_dict.keys()))
    # print(restaraunts)

    for restaraunt in restaraunts:
        print(f'{restaraunt} is rated at {rating_dict[restaraunt]}')

import random 
def user_choice():
    print("What do you want to do? ")
    print("""You can A. See the restaraunt list. B. Add your own rating. 
        C. Update a random restarount's rathing D. Quit""")
    decision = input("Your choice: > ")

    return decision.upper()

def read_ratings(text_file):

    text_file = open(text_file)
    rating_dict = {}

    for line in text_file:
        line = line.rstrip()
        restaraunt_rating = line.split(":")
        rating_dict[restaraunt_rating[0]] = restaraunt_rating[1]

    decision = user_choice()
 
    while decision != 'D':

        if decision == 'A':
            sort_print_resto(rating_dict)
            decision = user_choice()
        elif decision == 'B':
            restaraunt_name, restaraunt_rating = add_rating()
            rating_dict[restaraunt_name] = restaraunt_rating
            decision = user_choice()
        elif decision == 'C':
            random_resto = random.choice(list(rating_dict.keys()))
            print('How would you rate this restaraunt: {}'. format(random_resto))
            rating = input('Your rating: > ')
            rating_dict[random_resto] = rating
            decision = user_choice()
        else:
            print('That was not a valid answer')
            decision = user_choice()


    text_file.close()


read_ratings("scores.txt")
