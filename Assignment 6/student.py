#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''

class student:
    def __init__(self, name, student_id, year, major, gpa):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
        self.gpa = gpa

    def honorsProgram(self):
        if self.gpa > 3.5:
            return("True")
        else:
            return ("False")

    def studentID(self):
        import random
        for x in range(1):
            value = random.randint(10000,19999)
            print(value)
        if value == self.student_id:
            print("Winner!", self.name, "gets free lunch!")
        else:
            print("Loser!")
    
def main():
    #create three students and check if they get free lunch and if they qualify for honors
    student1 = student("Rachel", 12903, "s", "Music", 3.7)
    print(student1.honorsProgram())
    student1.studentID()
    student2 = student("Finn", 17382, "j", "History", 2.6)
    print(student2.honorsProgram())
    student2.studentID()
    student3 = student("Quinn", 13789, "s", "Communications", 3.9)
    print(student3.honorsProgram())
    student3.studentID()
    
main()
