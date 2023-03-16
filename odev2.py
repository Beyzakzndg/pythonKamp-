students=["Beyza Kozandağı","Hamza Enes Yolcu","Büşra Kevser Yolcu","Zeynep Özer"]

def addStudent():
    addStudent=input("Ad-Soyad:")
    students.append(addStudent)
    print(students)

addStudent()

def removeStudent():
    removeStudent=input("Ad-Soyad:")
    students.remove(removeStudent)
    print(students)

removeStudent()

def AddStudents():
    sayi=int(input("Kayıt yapılacak öğrenci sayısı:"))
    for i in range(sayi):
        addStudent=input("Ad-Soyad:")
        students.append(AddStudents)
        print(students)

AddStudents

for students in students:
    print(students)

def studentsIndex():
    print(students)
    for i in range(len(students)):
        print(f"Numara: {i} isim: {students[i]}")
print(students)
studentsIndex()

