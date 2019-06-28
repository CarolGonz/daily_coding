# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only
# if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

import re

def to_camel_case(text):
    #cria uma lista de strings seprando pelos delimitadores [' ','-', '_']
    list_strings = re.split('-| |_|\n',text)

    ''' checa se a primeira string é lower case, se verdadeiro
        cria nova lista excluindo a primeira string e capitaliza cada elemeto
        depois junta todas as strings da lista com a primeira string da lista sem capitalizar
   '''
    if list_strings[0].islower():
        new_list = list_strings[1:]
        list_capit = [x.capitalize() for x in new_list]
        join_strings = ''.join(list_capit)

        return list_strings[0]+join_strings

    else:
        list_capit = [x.capitalize() for x in list_strings]
        join_strings = ''.join(list_capit)

        return join_strings
