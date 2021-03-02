unit = float(input("ป้อนคะแนนหน่าย(80): "))
final = float(input("ป้อนคะแนนสอบปลายภาค(20): "))
score = unit + final

if score >= 80 :
  print('%d'%score, "คุณได้เกรด 4")
elif  score >= 75 :
  print('%d'%score, "คุณได้เกรด 3.5")
elif  score >= 70 :
  print('%d'%score, "คุณได้เกรด 3")
elif  score >= 65 :
  print('%d'%score, "คุณได้เกรด 2.5")
elif  score >= 60 :
  print('%d'%score, "คุณได้เกรด 2")
elif  score >= 55 :
  print('%d'%score, "คุณได้เกรด 1.5")
elif  score >= 50 :
  print('%d'%score, "คุณได้เกรด 1.0")
else :
  print('%d'%score, "คุณได้เกรด 0")
