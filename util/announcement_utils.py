########### reconditon .txt file list to raw text
#in list is the list returned by .readlines() containing lists of strings with \n as break
def parse_announcement(in_list):
    string_annc = ''
    for str in in_list:
        if (str == '\n'):
            string_annc = string_annc + ' <br> '
        elif (str[-2:-1] == '\n'):
            string_annc = string_annc + str[0:-2] + ' <br> '
        else:
            string_annc = string_annc + str
    return string_annc
#does not currently space lines correctly.
