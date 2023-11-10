# File Handling
# ไฟล์ การจัดการ
# การทำงานกับไฟล์
# การเปิดไฟล์ write (w)/ extend (x)/ read (r)/append (a)

f_iot = open("iot3.txt","w", encoding="utf-8") 

f_iot.write("โย่ว")
f_iot.write("ว่างาย\n")
f_iot.write("อ้ายสราดดดด\n")
            
f_iot.close()