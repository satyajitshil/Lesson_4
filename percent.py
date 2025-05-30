print("Enter your grades of four supjects: ")
history = int(input("History: "))
math = int(input("Math: "))
science = int(input("Science: "))
algebra = int(input("Algebra: "))
sum = history + math + algebra + science
print("Your grades are: ", sum)
print("Your average grades are: ", (sum/400)*100)