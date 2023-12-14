#This is my data validation
class DataValidation():
    def __init__(self):
        self.myList = []


    def checkData(self, list):
        for i in list:
            try:
                if int(i) > 0:
                    self.myList.append(i)
            except ValueError:
                pass

        print(self.myList)


#Here is a list
a_list = ["hello", "6", "me", "you", "2", "11", "ohno", "-1", "yup", "0"]

#This is an example
myclass = DataValidation()
myclass.checkData(a_list)

#Merry Christmas