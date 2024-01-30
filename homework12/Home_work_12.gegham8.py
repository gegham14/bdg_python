#Write a function that takes a dictionary with information about students. Return info
#about the youngest student


def youngest_student(student):
	return min(student, key=student.get) 
k = 3
students_info = {
'student1': {
'name': 'John Doe',
'age': 20,
'subjects': ['Math', 'Physics', 'English'],
'scores': [7, 9, 9, 6],
},
'student2': {
'name': 'Jane Smith',
'age': 19,
'subjects': ['Chemistry', 'Biology', 'History'],
'scores': [5, 6, 8, 10],
},
'student3': {
'name': 'Bob Johnson',
'age': 21,
'subjects': ['Computer Science', 'Statistics', 'Psychology'],
'scores': [8, 8, 9, 9, 9],
},
}   

print(youngest_student({"john doe": 20, "Jane Smith": 19, 
                      "Bob Johnson": 21,}))