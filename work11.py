customer = input("ชื่อลูกค้า: ")
total_price = int(input("ราคาทั้งหมด: "))

if (total_price >= 100) :
  discount = total_price * 5 / 100
  print("ส่วนลด:", discount, "บาท")
  print("จำนวนเงินที่ต้องจ่าย:", discount + total_price, "บาท")
elif (total_price >= 500) :
  discount = total_price * 10 / 100
  print("ส่วนลด:", discount, "บาท")
  print("จำนวนเงินที่ต้องจ่าย:", discount + total_price, "บาท")
elif (total_price >= 1000) :
  discount = total_price * 20 / 100
  print("ส่วนลด:", discount, "บาท")
  print("จำนวนเงินที่ต้องจ่าย:", discount + total_price, "บาท")
