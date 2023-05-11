def txt_to_dict(file_name):
    with open(file_name, 'r') as file:
        listy = []
        while True:
            string = file.readline()
            if len(string) > 0:
                listy.append(string.strip().strip(',').rstrip(')').lstrip('('))
            else:
                break


    tuple_list = []

    for i in range(len(listy)):
        count = 0
        for x in range(len(listy[i])): 
            if listy[i][x] == ',' and count == 0:
                count += 1
                sub_tuple = (listy[i][:x],listy[i][x+1:])
                tuple_list.append(sub_tuple)
                
                
    return tuple_list



