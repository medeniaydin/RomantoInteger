rom_val = {'I': 1, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'D': 500, 'M': 1000,
           'CD': 400, 'CM': 900}

def is_valid_roman(romenNumbers):
    invalid_patterns = ['IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD']
    # Yan yana "IIII" gibi geçersiz durumu kontrol et
    for pattern in invalid_patterns:
        if pattern in romenNumbers:
            return False
    return True


def roman_to_int(romenNumbers):
    try:
        if not is_valid_roman(romenNumbers):
            return "Geçersiz giriş: Geçersiz kombinasyonları kullanamazsınız."

        num = 0

        for i in range(len(romenNumbers)-1):

            sol = romenNumbers[i]

            sağ = romenNumbers[i + 1]

            # Ardışık olarak aynı romen rakamını tekrar kontrolü
            if i + 1 < len(romenNumbers) and romenNumbers[i:i + 2:] == sağ * 2:
                return "HATA: Ardışık olarak aynı romen rakamını tekrar kullanamazsınız."

            if rom_val[sol] < rom_val[sağ]:
                num -= rom_val[sol]

            else :
                num += rom_val[sol]

        #print(romenNumbers[1])

        num += rom_val[romenNumbers[-1]]
        return num

    except KeyError and IndexError:
        return ("HATA: Böyle Bir Romen Rakamı Yok")


print(roman_to_int("CXM"))
