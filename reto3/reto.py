# -*- coding:utf-8 -*-

def reto():
    primos = [1, 2, 3, 5, 7]
    count = 2
    while count <= 100:
        two = count / 2
        three = count / 3
        five = count / 5
        seven = count / 7
        if str(seven).find(".0") != -1 or str(five).find(".0") != -1 or str(three).find(".0") != -1 or str(two).find(".0") != -1:
            print("divisible")
        else:
            print(count)
            primos.append(count)
        count += 1
    #print(str(count).find(".0"))
    print(primos)

reto()