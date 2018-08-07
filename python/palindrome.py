def palindrome(word):
    reversed_letters = word[::-1]

    return word == reversed_letters

if __name__ == '__main__':
    word = str(input('Escribe una palabra: '))

    if(palindrome(word)):
        print( '{} es un palindrome'.format(word))
    else:
        print('{} NO es palindrome'.format(word))
