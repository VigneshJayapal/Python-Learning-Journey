name = input("Please enter your name: ")
id = int(input("Please enter your id: "))
Total_budget = float(input("Please enter your total budget: "))
Salary = float(input("Please enter your salary: "))
Remaining_budget = Total_budget - Salary

print("========== QA EXECUTION REPORT ==========")
print("Name:", name)
print("ID:", id)
print("Total Budget:", Total_budget)
print("Salary:", Salary)
print("Remaining Budget:", Remaining_budget)
print("Money left after salary deduction in percentage:", (Remaining_budget / Total_budget) * 100)
print("========== END OF REPORT ==========")