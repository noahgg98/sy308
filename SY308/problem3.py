
def el_string_combiner(theList):
    #get/set needed vals
    llen = len(theList)
    listOfStrs = list()

    #parse list and combine strings
    for i in range(0, llen-1):
        if theList[i][-1] == '-' and \
          theList[i+1][0] == '-':

          listOfStrs.append(theList[i][:-1] + theList[i+1][1:])

    return listOfStrs



if __name__ == '__main__':

    test_list = ["hyper-", "-sonic", "filler", "bat-", "-man"]

    print(el_string_combiner(test_list))
           

