total_days = int(input("Enter total number of working days: "))
absent_days = int(input("Enter total number of days absent: "))

present_days = total_days - absent_days

attendance_percentage = (present_days / total_days) * 100

print(f"\nAttendance Percentage: {attendance_percentage:.2f}%")

if attendance_percentage >= 75:
    print("Status: Eligible to sit in the exam.")
else:
    print("Status: Not eligible to sit in the exam due to low attendance.")
