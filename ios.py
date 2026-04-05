class IOString:
    def __init__(self):
        self.str1=''
    def get_string(self):
        self.str1=input("Enter a string: ")

    def print_String(self):
        print("The string in all caps is: ", self.str1.upper())

hello=IOString()
hello.get_string()
hello.print_String()