### 
equation_string = ""
numberss = [5, 4, 3, 2, 1]
operatorss = ["+", "-", "*", "/", ""]
for num in numberss:
    equation_string += str(num) + str(operatorss[numberss.index(num)])
print(equation_string)
