def romanToInt(s: str) -> int:
    dictRomano = {"M": 1000, "D": 500, "C": 100,"L": 50,"X": 10, "V": 5, "I": 1}
    somaTotal = 0
    for i in range(len(s)):
        if i < len(s) - 1 and dictRomano[s[i]] < dictRomano[s[i+1]]:
            somaTotal -= dictRomano[s[i]]
        else:
            somaTotal += dictRomano[s[i]]
    return somaTotal

print(romanToInt('III'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))