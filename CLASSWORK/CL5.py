python_std = {"Nitty","Soorya","Arunnya"}
datascience_std = {"Anjana","Anjanna","Miya"}

python_std.add("Asiya")
print("New name: \n",python_std)

datascience_std .remove("Miya")
print("\nRemove name: \n",datascience_std)

both_courses = python_std | datascience_std
print("\nList students: \n",both_courses)

only_std = python_std - datascience_std
print("\nOnly one in python: \n",only_std)

all_students = python_std.union(datascience_std)
print("\nAll students: \n",all_students)

course_dict = {
    "Python" : len(python_std),
    "Data science" : len(datascience_std)
    }
print("\nDictionary: \n",course_dict)

for course, count in course_dict.items():
    print(f"\nCourse:{course}, Students:{count}")

new_dict = {course: count * 2 for course, count in course_dict.items()}
print("\nExpected growth: \n",new_dict)