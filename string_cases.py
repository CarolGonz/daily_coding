# # Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order.
# # Essentially, rearrange the digits to create the highest possible number.
# #
# # Examples:
# # Input: 21445 Output: 54421
# #
# # Input: 145263 Output: 654321
# #
# # Input: 1254859723 Output: 9875543221


def Descending_Order(num):

    sorted_num = sorted(str(num), reverse = True)

    return int("".join(sorted_num))


# Check to see if a string has the same amount of 'x's and 'o's.
#  The method must return a boolean and be case insensitive.
#  The string can contain any char.

def xo(s):
    o = ['o','O']
    x = ['x','X']

    soma_o = 0

    for i in o:
        count_o = s.count(i)
        soma_o += count_o

    soma_x = 0

    for i in x:
        count_x = s.count(i)
        soma_x += count_x

    if soma_x == soma_o:
        return True
    else:
        return False

# # In a factory a printer prints labels for boxes. For one kind of boxes
# the printer has to use colors which, for the sake of simplicity, are named
#  with letters from a to m.
# #
# # The colors used by the printer are recorded in a control string.
# For example a "good" control string would be aaabbbbhaijjjm meaning that
#  the printer used three times color a,four times color b, one time color h
#  then one time color a...
# #
# # Sometimes there are problems: lack of colors, technical malfunction and
# a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters
# not from a to m.
# #
# # You have to write a function printer_error which given a string will
# output the error rate of the printer as a string representing a rational
# whose numerator is the number of errors and the denominator the length of
# the control string. Don't reduce this fraction to a simpler expression.
# #
# # The string has a length greater or equal to one and contains only letters
# from ato z.

def printer_error(s):
    # your code

    wronglet = list(map(chr, range(ord('n'), ord('z')+1)))
    countwl = 0

    len_s = len(s)

    for i in wronglet:
        countwl_ = s.count(i)
        countwl += countwl_

    return str(countwl)+'/'+str(len_s)
