def list_binary_search(my_list, the_value):
    print(my_list)
    # indicates whether the_value is in my_list
    if len(my_list) == 0:
        return False
    elif len(my_list) == 1:
        return my_list[0] == the_value
    else:
        mid_index = len(my_list) // 2
        if the_value < my_list[mid_index]:
            new_list = my_list[:mid_index]
        else:
            new_list = my_list[mid_index:]
        return list_binary_search(new_list, the_value)

def list_binary_search_depth(my_list, the_value):
    print(my_list)
    # indicates whether the_value is in my_list and how deep we search for it
    if len(my_list) == 0:
        return [False, 0]
    elif len(my_list) == 1:
        return [my_list[0] == the_value, 0]
    else:
        mid_index = len(my_list) // 2
        if the_value < my_list[mid_index]:
            new_list = my_list[:mid_index]
        else:
            new_list = my_list[mid_index:]
        result, depth = list_binary_search_depth(new_list, the_value)
        return ( [result, depth+1] )

def list_binary_search_where(my_list, the_value, list_first_index = 0):
    print(my_list, list_first_index)
    # indicates whether the_value is in my_list and where it is
    if len(my_list) == 0:
        return [False, None]
    elif len(my_list) == 1:
        if my_list[0] != the_value:
            return [False, None]
        else:
            return [True, list_first_index]
    else:
        mid_index = len(my_list) // 2
        if the_value < my_list[mid_index]:
            new_list = my_list[:mid_index]
            list_first_index += 0
        else:
            new_list = my_list[mid_index:]
            list_first_index += mid_index
        return list_binary_search_where(new_list, the_value, list_first_index)

def list_binary_search_depth_2(my_list, the_value):
    print(my_list)
    # indicates whether the_value is in my_list and how deep we searched for it
    if len(my_list) == 0:
        return [False, 0]
    elif len(my_list) == 1:
        return [my_list[0] == the_value, 0]
    else:
        mid_index = len(my_list) // 2
        if the_value == my_list[mid_index]:
            return [True, 0]

        if the_value < my_list[mid_index]:
            new_list = my_list[:mid_index]
        else:
            new_list = my_list[mid_index+1:]  # we start at mid_index+1 now
        result, depth = list_binary_search_depth_2(new_list, the_value)
        return ( [result, depth+1] )
                            
                                                         