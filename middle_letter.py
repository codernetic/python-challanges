def mid(txt):
    txt_list = list(txt)
    list_len = len(txt_list)

    if (list_len % 2) != 0 :
        result = int((list_len - 1) / 2)

        return txt_list[result]
    else:
        return ''

print(mid('Hello    '))
