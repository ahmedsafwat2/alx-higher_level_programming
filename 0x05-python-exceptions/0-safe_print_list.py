def safe_print_list(my_list=[], x=0):
    '''print x elements from list
    Args:
    my_list: is the list of elements
    x: number will be printed
    Returns
    number of element printed
    '''
    ret = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end = "")
            ret +=1
    except:
        IndexError
    print()
    return (ret)
