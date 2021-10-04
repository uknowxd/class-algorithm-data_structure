car_size = int(input('รถขนาด (CC) : '))
if car_size < 1300:
    print('ภาษี 800 บาท')
elif car_size >= 1300 and car_size < 1800 :
    print('ภาษี 1200 บาท')
elif car_size >= 1800 and car_size < 2500 :
    print('ภาษี 1500 บาท')
else :
    print('ภาษี 2000 บาท')