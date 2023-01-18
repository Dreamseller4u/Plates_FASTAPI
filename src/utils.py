import random
import re


def generate_plate_number(amount: str = 1):
    sym = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']
    plates = []
    for j in range(int(amount)):
        plate = ''
        for i in range(6):
            if i == 0 or i > 3:
                plate += random.choice(sym)
            elif 0 < i < 4:
                if plate[1:] == '00':
                    plate += str(random.randint(1, 9))
                else:
                    plate += str(random.randint(0, 9))
        plates.append(plate)
    return plates


def check_plate(plate: str):
    plate_re = r'^[АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{2}$'
    if re.fullmatch(plate_re, plate):
        return plate
    else:
        return None
