class Stack:
    def __init__(self):
        self.stack = []
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
    def push(self,val):
        return self.stack.append(val)
    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return self.size() == 0

def main():

    while True:
        print("Please choose number from the following:")
        print("1 : Insert new URL")
        print("2 : View Browser History")
        print("3 : Exit the application")

        user_input = int(input())

        if user_input == 1:
            newURL = input("Please insert new URL")

        if user_input == 2:
                print("All browser history:")
                while True:
                    print("Please choose number from the following:")
                    print("1 : Go back in browser history")
                    print("2 : Go forward in browser history")

