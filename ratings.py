"""Restaurant rating lister."""
def read_ratings(text_file):

    text_file = open(text_file)
    rating_dict = {}

    for line in text_file:
        line = line.rstrip()
        restaraunt_rating = line.split(":")
        rating_dict[restaraunt_rating[0]] = restaraunt_rating[1]

    # print(rating_dict)

    restaraunts = sorted((rating_dict.keys()))
    print(restaraunts)

    for restaraunt in restaraunts:
        print(f'{restaraunt} is rated at {rating_dict[restaraunt]}')


    text_file.close()

read_ratings("scores.txt")
# put your code here
