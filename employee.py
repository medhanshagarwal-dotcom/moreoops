class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor called")
def create_obj():
    print("Creating object")
    obj=Employee()
    print("Funtion end")
    return obj
print("Calling create object funtion")
obj=create_obj()
print("Program finished")
