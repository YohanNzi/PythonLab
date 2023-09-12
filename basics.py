
print("Hello Yorld !")

def sum_or_product():
    num1 = int(input("Entrez un nombre : "))
    num2 = int(input("Entrez un autre nombre : "))

    if num1 * num2 > 1000:
        print("La somme de ces deux nombres est : ", num1 + num2)
    else:
        print("Le produit de ces deux nombres est : ", num1 * num2)


def sum_of_digits():
    previous = 0
    for i in range(0, 10):
        print("Current Number : ", i, "Previous Number : ", previous, "Sum : ", i + previous)
        previous = i


def even_letters():
    word = input("Original string is : ")
    print("Printing only even index chars")

    for i in range(0, len(word), 2):
        print("index[", i, "] = ", word[i])

def delete_chars(originalString, n):

    if n < len(originalString):
        x = originalString[n:]
        return x
    else:
        return "n is greater than the length of the string"
#        Also works :
#        for i in range(n, len(originalString)):
#            print("index[", i, "] = ", originalString[i])


def check_if_palindrome():
    word = input("Enter a word : ")
    if word == word[::-1]:
        print("This word is a palindrome")
    else:
        print("This word is not a palindrome")

def check_first_last_numbers(givenlist):
    print("Given list is ", givenlist)
    if givenlist[0] == givenlist[-1]:
        print("result is " + str(True))
    else:
        print("result is " + str(False))
    
print(check_first_last_numbers([10, 20, 30, 40, 10]))
print(check_first_last_numbers([75, 65, 35, 75, 65]))