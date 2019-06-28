from collections import OrderedDict

def solution(n):

#     roman = OrderedDict()
#     roman[1000] = "M"
#     roman[900] = "CM"
#     roman[500] = "D"
#     roman[400] = "CD"
#     roman[100] = "C"
#     roman[90] = "XC"
#     roman[50] = "L"
#     roman[40] = "XL"
#     roman[10] = "X"
#     roman[9] = "IX"
#     roman[5] = "V"
#     roman[4] = "IV"
#     roman[1] = "I"

    roman = { 1 : 'I',
              4 : 'IV',
              5 : 'V',
              10 : 'X',
              50 : 'L',
              40: 'XL',
              100 : 'C' ,
              500 : 'D' ,
              400 : 'CD',
              900 : 'CM',
              1000 :'M'
             }
    print(roman)

    def roman_num(n):
        for r in roman.keys():
            x, y = divmod(n, r)
            yield roman[r] * x
            n -= (r * x)
            if n <= 0:
                break

    return "".join([a for a in roman_num(n)])
