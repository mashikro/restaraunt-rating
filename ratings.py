"""Restaurant rating lister."""
def add_rating():

    restaraunt_name = input("Name of restaraunt: > ")
    restaraunt_rating = input("Rating: >")

    restaraunt_name = restaraunt_name.title()

    return (restaraunt_name, restaraunt_rating)



def read_ratings(text_file):

    text_file = open(text_file)
    rating_dict = {}

    for line in text_file:
        line = line.rstrip()
        restaraunt_rating = line.split(":")
        rating_dict[restaraunt_rating[0]] = restaraunt_rating[1]

    def sort_print_resto():
        restaraunts = sorted((rating_dict.keys()))
    # print(restaraunts)

        for restaraunt in restaraunts:
            print(f'{restaraunt} is rated at {rating_dict[restaraunt]}')

    sort_print_resto()

    want_to_add = input("Want to add a restaraunt rating? (Y/N) > ")

    if want_to_add == 'Y':
        restaraunt_name, restaraunt_rating = add_rating()
        rating_dict[restaraunt_name] = restaraunt_rating
    elif want_to_add != 'N':
        print("That's not a valid answer")


    sort_print_resto()


    text_file.close()



read_ratings("scores.txt")
# put your code here
