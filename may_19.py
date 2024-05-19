# # # try- except
# # # file handling

# exception handling
# print("1"+2)

# class SalaryNotInRangeError(Exception):
#     """Exception raised for errors in the input salary.

#     Attributes:
#         salary -- input salary which caused the error
#         message -- explanation of the error
#     """

#     def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
#         self.salary = salary
#         self.message = message
#         super().__init__(self.message)


# salary = int(input("Enter salary amount: "))
# if not 5000 < salary < 15000:
#     raise SalaryNotInRangeError(salary,"wrong")


# try:
#     print("1"+2)
# except SalaryNotInRangeError as e:
#     print( f"not possible becuase of error {e}")
# finally:
#     print("finally")
# except 
# finally 


# define Python user-defined exceptions
# class InvalidAgeException(Exception):
#     "Raised when the input value is less than 18"
#     pass

# # you need to guess this number
# number = 18

# try:
#     input_num = int(input("Enter a number: "))
#     if input_num < number:
#         raise InvalidAgeException
#         print("")
#     else:
#         print("Eligible to Vote")
        
# except InvalidAgeException:
#     print("Exception occurred: Invalid Age")
 

# File handling

# with open('1.txt', '') as f:
#     f.write()

# "x" - use to create a file (create mode) --- if file already exists
# "a" - use to append the data ina file (append mode) --- if file downt oresent then create new file
# "w" - use to write the data in teh file (write mode) --- if file downt oresent then create new file
# "r" - use to read the data from the file -- if file doent exists then error

# with open('1.txt',"x") as f:
#     pass

# with open('12.txt',"w") as f:
#     f.write("i am a royal student")

# with open('12.txt',"w") as f:
#     f.write("\n hello everyone")

# with open('12.txt',"r") as f:
#     print(f.read())