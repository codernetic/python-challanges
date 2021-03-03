def capital_indexes(txt):

    result = []
    txt_list = list(txt)

    for i in range(len(txt_list)):
        if txt_list[i].isupper():
            result.append(i)

    return result

capital_indexes('HelLo, WoRlD')
