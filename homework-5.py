name = str(input('กรุณาใส่ชื่อ : '))
last_name = str(input('กรุณาใส่นามสกุล : '))
print('==========================')
print('แม่สูตรคูณ - พิมพ์ "0" ')
print('หารัศมีของวงกลม - พิมพ์ "1" ')
print('==========================')
func_chosen = input("คุณ "+  name  +" "+last_name +" ต้องการรู้สิ่งใด : ")
if func_chosen == "0" :
        x = int(input('ใส่หมายเลขแม่สูตรคูณ : '))
        n = 0
        if x> 1 and x <= 25 :
                while n < 12:
                        n += 1
                        print(x ,'x', n , '=' ,x*n)
        else :
                print('ไม่พบแม่สูตรคูณ')
elif func_chosen == "1" :
        side=int(input('รัศมีของวงกลม : ')) 
        area=(3.14*side**2)
        print('พื้นที่ของวงกลม :',area)
else :
        print ('ไม่พบสิ่งที่ท่านต้องการรู้')