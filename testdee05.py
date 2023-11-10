# File Handling
# ไฟล์ การจัดการ
# การทำงานกับไฟล์
# การเปิดไฟล์ write (w)/ extend (x)/ read (r)/append (a)

f_iot = open("iot2.txt","r", encoding="utf-8") 

data = f_iot.read()

f_iot.close

print(data)