from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r


def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n >= 4000:
        return 'Error!'

    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value

    return result
#수정부분
def RomanTodec(numStr):

    try:
        s = str(numStr)
    except:
        return "Error!"

    #소문자로 입력해도 자동으로 변환할 수 있게 만들기
    s = s.upper()

    #오류 처리 (로마자가 아닌 문자를 입력했을 경우)
    rom_list = ['I','V','X','L','C','D','M']
    for i in range(len(s)):
        if s[i] not in rom_list:
            return "3000↓의 로마자를 입력해"

    romans = {
        'M' : 1000 , 'CM' : 900 , 'D' : 500 , 'CD' : 400 ,
        'C' : 100 , 'XC' : 9  , 'L' : 50 , 'XL' : 40,
        'X' : 10 ,'IX' : 9 , 'V' : 5 , 'IV' : 4,
        'I' : 1
    }
    current = ''
    previous = ''
    result = 0
    
    while s != "":
        if previous == "" :
            previous = s[len(s) - 1]
            s = s[0:len(s) - 1]
            result += romans[previous]
        else:
            for key in romans.keys():
                if (len(s) > 0):
                    if (key == s[len(s) - 1]):
                        current = key
                        if (romans[current] < romans[previous]):
                            result -= romans[current]
                            previous = ""
                            s = s[0:len(s) - 1]
                        elif (romans[current] >= romans[previous]):
                            result += romans[current]
                            previous = current
                            s = s[0:len(s) - 1]
                else:
                    return result
