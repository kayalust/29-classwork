# เขียนโปรแกรมคำนวณค่าเฉลี่ย
print("----------------------------------------------")
print(" ")
print("คำนวนค่าเฉลี่ยของนักเรียน")
print(" ")
# คะแนน
subject_thai = 78
subject_eng = 84
subject_social = 64
subject_science = 96
subject_math = 100

midterm_score = 49
final_score = 45


# ชื่อ
name = "Nathakorn"
surname = "Jumderm"
print("----------------------------------------------")
print("จัดทำโดย", name, surname)

# สูตร
avg = (subject_thai + subject_eng + subject_social + subject_science + subject_math)/5

# Print
print("----------------------------------------------")
print(" ")
print(name, surname, "มีคะแนนทั้งหมด", ' %.2f ' % avg, "คะแนน")
print(name, surname, "มีคะแนนทั้งหมด", ' %.3f ' % avg, "คะแนน")
print(" ")
print("----------------------------------------------")
