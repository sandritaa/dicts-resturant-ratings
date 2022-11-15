"""Restaurant rating lister."""


# put your code here
def restaurant_rating(filename):

    score_list = open(filename)

    dic = {}

    for line in score_list:

        # Here line = ["Florean Fortescue's Ice Cream Parlour:4"]

        line = line.split(":")

        # Here line = ["Florean Fortescue's Ice Cream Parlour", "4"]

        # dictionary of restaurants and ratings NON sorted
        dic[line[0]] = int(line[1])

        # Here dic = {'Florean Fortescue's Ice Cream Parlour' : 4}

    print(dic)

    # Now we need to sort it

    # Step 1 is use the dictionary method called .items() which returns a dict_items type with an array of tuples
    new_dic_items = dic.items()
    print(new_dic_items)

    # Step 2 is to use built in function sorted() to sort the dict_items which returns an array of tuples
    sorted_new_dic_items = sorted(new_dic_items)
    print(sorted_new_dic_items)

    # Step 3 is to convert the array of tuples into a dictionary using built in function dict
    new_dict = dict(sorted_new_dic_items)
    print(new_dict)

    # result = dic[words[0]]  # dic[words[1]]
    # return result
    # print(dic)
    # return dic

    # for restaurant, rating in dic.items():
    #     print(restaurant, rating)

    #ratings = dic.items()
    # return ratings


restaurant_rating('scores.txt')
