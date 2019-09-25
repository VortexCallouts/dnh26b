#Function One
def Login(username,password):
    if username and password == "user":
        return True
#Function Two
def Grade(points,totalPoints):
    return points/totalPoints

#Function Three
def Submit(filename):
    if filename == "homework.txt":
        return True
#Function Four
def Comment(message):
    if message != "":
     return False

#Function Five
def Search(student):
    studentlist = ["Davin"]
    if student not in studentlist:
        return False
