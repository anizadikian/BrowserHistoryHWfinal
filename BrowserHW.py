class BrowserHistory:

    def __init__(self, url=None):
        self.url = url
        self.next = None

class Stack:

    def __init__(self):
        self.__head = None

    def push(self, newurl):
        if self.__head == None:
            self.__head = BrowserHistory(newurl)

        else:
            newData = BrowserHistory(newurl)
            newData.next = self.__head
            self.__head = newData

    def back(self):
        if self.isEmpty():
            return None
        else:
            poppedData = self.__head
            self.__head = self.__head.next
            global frw
            frw = poppedData
            poppedData.next = None
            return poppedData.url

    def open(self):
        if self.isEmpty():
            return None
        else:
            return self.__head.url

    def display(self):
        printval = self.__head
        if self.isEmpty():
            print("Stack is empty")
        else:
            while printval is not None:
                print(printval.url)
                printval = printval.next


    def forward(self):
        temp = self.__head
        if temp.next is not None:
            print(frw.url)
        else:
            print("No Data")

    def isEmpty(self):
        if self.__head == None:
            return True
        else:
            return False


def main():

    browserhistory = Stack()

    while True:

        print("Please choose number from the following:")
        print("1 : Insert new URL")
        print("2 : View Browser History")
        print("3 : Edit Browser History")
        print("4 : Exit the application")

        user_input = int(input())

        if user_input == 1:
            while True:
                url = input("Insert the url, such as www.hotmail.com:  ")
                browserhistory.push(url)
                break

        elif user_input == 2:
            print("All browser history:")
            browserhistory.display()


        elif user_input == 3:

            browserhistory.display()

            while True:
                print("Please choose number from the following:")
                print("1 : Go back in browser history")
                print("2 : Go forward in browser history")

                user_input2 = int(input())
                if user_input2 == 1:
                    browserhistory.back()
                    browserhistory.display()
                    break
                elif user_input2 == 2:
                    browserhistory.forward()
                    browserhistory.display()
                    break
                else:
                    print("Please type as required, inserting the number 1 or 2")


        elif user_input == 4:
            exit()

        else:

            print("Please type as required, inserting the number 1, 2, 3 or 4")

main()