import pickle,Student

f = open("student.dat", "wb")
s = Student.Student(123,"Henil",39)
pickle.dump(s,f)
f.close()