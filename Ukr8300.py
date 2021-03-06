# -*- coding: utf-8 -*-

def bouquets(narcissus_price, tulip_price, rose_price, summ):
    def amount_of_single_type(cash, flowers_price):
        check_summ = 0
        flowers_amount = 0

        while check_summ < cash:
            check_summ = check_summ + flowers_price
            flowers_amount += 1

        if check_summ > cash:
            check_summ = check_summ - flowers_price
            flowers_amount = flowers_amount - 1

        return flowers_amount

    narcissus_amount = amount_of_single_type(summ, narcissus_price)
    tulip_amount = amount_of_single_type(summ, tulip_price)
    rose_amount = amount_of_single_type(summ, rose_price)

    total_amount = 0
    for i in range(narcissus_amount + 1):
        for j in range(tulip_amount + 1):
            for k in range(rose_amount + 1):
                if (narcissus_price * i + tulip_price * j + rose_price * k) <= summ and (i + j + k) != 0 and (
                        i + j + k) % 2 != 0:
                    # print ('n'*i + 't'*j + 'r'*k), (str(i) + ' n ' + str(j) + ' t ' + str(k) + ' r '), (narcissus_price*i + tulip_price*j + rose_price*k), summ
                    total_amount += 1

    return total_amount


print bouquets(200, 300, 400, 100000)
