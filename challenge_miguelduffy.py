"""
---Ejercicio 1---
"""
string_of_numbers = "45,2500,10,31,100,1500"

def sum_of_numbers(string_of_numbers):
    sum_numbers = 0

    for number in string_of_numbers.split(','):
            sum_numbers += int(number)

    print("Resultado: {}".format(sum_numbers))

sum_of_numbers(string_of_numbers)

"""
---Ejercicio 2---
"""

list_of_lists = [[300,12,55], 
                 [15,3000,400], 
                 [88,75,60]]

def substaction_of_diagonals(list_of_lists):
    sum_first_diagonal = 0
    sum_second_diagonal = 0
    start_index_first_diagonal = 0
    start_index_second_diagonal = -1

    for number in list_of_lists:
        sum_first_diagonal += number[start_index_first_diagonal]
        sum_second_diagonal += number[start_index_second_diagonal]
        start_index_first_diagonal += 1
        start_index_second_diagonal -= 1
        
    print("La resta de las diagonales es: {}".format(sum_first_diagonal - 
    sum_second_diagonal))

substaction_of_diagonals(list_of_lists)

"""
---Ejercicio 3---
"""
while True:
    try:
        number = int(input("Por favor ingresá un número mayor a 1: "))
        while number < 2:
            number = int(input("El número que ingresaste no es mayor a 1."
        " Por favor ingresá un número mayor a 1: "))
        break
    except ValueError:
        print("No ingresaste un número. Por favor ingresá uno.")

def hashtag_pyramid(number):
    for i in range(number):
        for j in range(number - 1, i, -1):
            print(end = " ")
        for k in range(i + 1):  
            print(end = "# ")
        print("")

hashtag_pyramid(number)
