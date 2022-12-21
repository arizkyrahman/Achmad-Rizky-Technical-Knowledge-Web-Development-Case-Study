def display_results(studentName, studentScore):  # pass studentName and studentScore as arguments
  studentScore = int(studentScore)  # convert studentScore to an integer
  if studentScore < 0 or studentScore > 100:
    return "Invalid Score"
  grades = ["E", "D", "C", "B", "A"]
  return "Nilai " + studentName + " mendapatkan nilai " + grades[min(int(studentScore / 20), 4)]

def display_group(studentName):  # pass studentName as an argument
  groups = ["In a first group", "In a second group", "In a last group"]
  return groups[min(ord(studentName[0]) // 8, 2)]

studentName = input("Input the student name! ")
studentScore = input("Input the student score! ")

print(display_results(studentName, studentScore))  # pass studentName and studentScore as arguments
print(display_group(studentName))  # pass studentName as an argument