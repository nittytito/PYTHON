frontend = {"Nitty","Miya","Niya"}
backend = {"Siya","Asiya","Liya"}

backend.add("Biya")
print("New name: ",backend)

frontend.remove("Miya")
print("Remove name: ",frontend)

both_courses = frontend | backend
print("List students: ",both_courses)

only_backend = frontend - backend
print("\nOnly one in backend: \n",backend)

total_number = frontend.union(backend)
print("\nTotal number: \n",total_number)

course_counts = {
    "Frontend": len(frontend),
    "Backend": len(backend)
}

for course, count in course_counts.items():
    print(f"{course} has {count} students")

new_dict = {course: count * 2 for course,count in course_counts.items()}
print("\nExpected growth: \n",new_dict)