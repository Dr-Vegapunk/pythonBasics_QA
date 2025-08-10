# file = open("test_data.txt", "w")
# file.write("TC001: Login Test\n")
# file.write("TC002: Search Feature\n")
# file.write("TC003: Cart Functionality\n")
# file.close()
# print("File created and data written.")


# file = open("test_data.txt", "r")
# print(file.read())
# file.close()

# file = open("test_data.txt", "a")
# file.write("TC003: Payment Gateway\n")
# file.close()

# file= open("test_cases.txt", "w")
# file.write("TC001: Login Test\n")
# file.write("TC002: Search Feature\n")
# file.write("TC003: Cart Functionality\n")
# file.close()
# print("File created and data written.")

# file= open("test_cases.txt", "r")
# print(file.read())
# file.close()
try:
    file = open("test_cases1.txt", "a")
   
except Exception as e:
    print("Error occurred:", e)

finally:
    file.write("TC003: Payment Gateway\n")
    file.close()
