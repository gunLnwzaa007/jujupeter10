# File Handling
# ไฟล์ การจัดการ
# การทำงานกับไฟล์
# การเปิดไฟล์ write (w)/ extend (x)/ read (r)/append (a)

f_iot = open("iot2.txt","r", encoding="utf-8") 

data = f_iot.readline()
print(data, end="")
data = f_iot.readline()
print(data, end="")
data = f_iot.readline()
print(data, end="")
data = f_iot.readline()
print(data, end="")

f_iot.close()