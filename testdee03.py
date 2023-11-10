# File Handling
# ไฟล์ การจัดการ
# การทำงานกับไฟล์
# การเปิดไฟล์ write (w)/ extend (x)/ read (r)/append (a)

try :
    
    f_iot = open("iot2.txt","x", encoding="utf-8") 

    f_iot.write("โย่ว")
    f_iot.write("ว่างาย\n")
    f_iot.write("อ้ายสราดดดด\n")
                
    f_iot.close()

except FileExistsError :
    
    print("เปลี่ยนชื่อใหม่อ้ายสราดดดมันซํ้า")