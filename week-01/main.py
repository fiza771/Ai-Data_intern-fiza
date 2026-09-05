#student perfomance manager
def calculate_grade(marks):
   if marks>= 90:
     return "A+"
   elif marks>= 80:
      return "A"
   elif marks>= 70:
      return "B"
   elif marks>=60:
      return "C"
   elif marks>=50:
      return "D"
   else:
      return"F"
def add_student(students):
   name=input("Enter student name: ")
   try:
      marks=float(input("Enter student marks(0-100): "))
      if marks < 0 or marks > 100:
         print("Error: Marks must be between 0 and 100.")
         return
      grade= calculate_grade(marks)
      student = {"name":name,
                 "marks":marks,
                 "grade":grade}
      students.append(student)
      print("student added successfully!")
      print("Name:",name)
      print("Marks:",marks)
      print("Grade:",grade)
   except ValueError:
    print("Error:please enter numbers for marks.")
def show_student(students):
   if not students:
      print("no students found.")
      return
   print("\n---students record---")
   for student in students:
       print("Name:", student["name"],
         "|marks:",student["marks"],
         "| Grade",student["grade"])
def main():
      students=[]
      while True:
         print("\n=== student performance manager ===")
         print("1. Add student")
         print("2. Show student")
         print("3.Exit")
         choice= input("Enter your choice : ")
         if choice =="1":
            add_student(students)
         elif choice=="2":
          show_student(students)
         elif choice=="3":
          print("program ended bye")
          break
      else:
       print("invalid choice. Please select 1,2 or 3.")

if __name__=="__main__":
     main()
