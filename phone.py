def letterCombinations(digits: str) -> list[str]:    
    a = list(digits)   
    num = {
        '2':  ['a','b','c'],
        '3' : ['d','e','f'],
        '4' : ['g','h','i'],
        '5' : ['j','k','l'],
        '6' : ['m','n','o'],
        '8' : ['t','u','v'],
        '7' : ['p','q','r','s'],
        '9' : ['w','x','y','z'],
        }

    if digits == "":
        return []

    if len(digits) == 1:
        return num[digits]

    for char in a:
        l = num[char]
        return [(x + y) for x in l for y in letterCombinations(digits[1:len(digits)])]
        
        
if __name__ == '__main__':
    a = '23'
    print(letterCombinations(a))

