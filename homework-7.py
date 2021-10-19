import random
import replit
player_name = str(input('กรุณาใส่ชื่อของท่าน : '))
item = ['Iphone' , 'Macbook' , 'IPad' , 'R37']
inventory_player = []
gacha_result = 0
player_point = 0
while True:
  print('ชื่อของท่าน : ' , player_name)
  print('คุณมี Point จำนวณ : ' , player_point , 'Point')
  print('ไอเท็มในกระเป๋า : ' , len(inventory_player) , ' ชิ้น ')
  print('คุณสุ่มกาชาไปทั้งหมด : ',gacha_result , ' ครั้ง')
  print ('===== เลือก =====')
  print ('เคลียร์ Console - 0')
  print ('สุ่มกาชา - 1')
  print ('เติม Point - 2')
  print ('กระเป๋าของคุณ - 3')
  print ('ออกจากโปรแกรม - 4')
  print ('================')
  select_function = str(input('เลือก :'))
  if select_function == '0' :
    replit.clear()
  elif select_function == '1' :
    if player_point >= 10 :
      gacha_result += 1
      player_point -= 10
      print('#########  ทำการสุ่มกาชา  #########')
      random_item = random.choice(item)
      inventory_player.append(random_item)
      print('ยินดีด้วยคุณได้รับ :' , random_item)
      print('#################################')
    else:
      print('#################################')
      print('Point ของท่านไม่พอ')
      print('#################################')
  elif select_function == '2' :
      print('########## เพิ่ม Point ############')
      add_point = int(input('กรุณาใส่จำนวณ Point : '))
      player_point += add_point
      print ('คุณเพิ่ม : ' , add_point , ' Point')
      print('#################################')
  elif select_function == '3' :
      print('########## กระเป๋า ############')
      print(inventory_player)
      print('#############################')
  elif select_function == '4' :
      break
  else :
    print('#############################')
    print('ไม่พบสิ่งที่ท่านเลือก')
    print('#############################')