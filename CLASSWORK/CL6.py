attendence = [18,20,19,15,21]
full = 0
total_attendence = 0
not_full = 0
for std in attendence:
    if std >= 20:
        print("Attendence full")
        full += 1
    else:
        print("Attendecne not full")
    total_attendence += std
print("Total days: ",full)
print("Total attendence: ",total_attendence)