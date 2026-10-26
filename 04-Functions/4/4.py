###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    absolute_number = abs(any_number)
    string_number = str(absolute_number)
    sum_digits = sum(int(digit) for digit in string_number)
    return sum_digits

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print('The sum of the digits in the number', any_number, 'is', result)