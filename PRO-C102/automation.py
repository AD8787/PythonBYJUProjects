import time

class automate():
    def __init__(self, doHW):
        self.doHW = doHW

    def mathhw(self):
        print("Finishing up your math homework... ")
        print("Finished! Check tommorrow to see it done again!")

    def englishhw(self):
        print("Finishing up your english homework... ")
        print("Finished! Check tommorrow to see it done again!")

    def sciencehw(self):
        print("Finishing up your science homework... ")
        print("Finished! Check tommorrow to see it done again!")

    def historyhw(self):
        print("Finishing up your history homework... ")
        print("Finished! Check tommorrow to see it done again!")

def main():
    doHW = input("Enter your grade level: ")

    student = automate(doHW)

    print("Select Which Homework to choose and I will do! Write your answer as the given number for each subject.")
    selecthw = int(input("1. Math, 2. English, 3. History, 4. Science "))

    if(selecthw == 1):
        student.mathhw()
    elif(selecthw == 2):
        student.englishhw()
    elif(selecthw == 3):
        student.historyhw()
    elif(selecthw == 4):
        student.sciencehw()
    else:
        print("Please Enter a valid number. ")

    if(time == 86400):
        student.mathhw()
        student.englishhw()
        student.historyhw()
        student.sciencehw()

main()