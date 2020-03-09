# 5. Напишите функцию которая находит самою длинную
# слово в строке.

def stroka(word):
    count = 0
    long_word = word.split()
    for i in range(0,len(long_word)):
        if len(long_word[i]) > len(long_word[count]):
            count = i

    return long_word[count]
print(stroka("asd rtyugikb sf qwertyuirhd sdf"))


