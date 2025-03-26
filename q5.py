#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

class string:
    def __init__(self):
        self.s = " "

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

    def test_string(self):
        self.getString()
        self.printString()

st = string()
st.getString()
st.printString()
#st.test_string()