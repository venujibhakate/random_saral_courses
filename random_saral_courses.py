import requests
import json
import random

# Here we are writing a file.
def writingFile(fileName,fileData):
      file=open(fileName,"w")  
      file.write(fileData)
      file.close()

# Here we are reading a file.
def readingFile(fileName):
      file=open(fileName ,"r")
      data_file = file.read()
      loded_file = json.loads(data_file)
      return loded_file


#Api calling
def apiCalling(url):
    getData = requests.get(url)
    json_data = getData.json()
    json_string = json.dumps(json_data)

    fileName="courses.json"
    fileData=json_string
    writingFile(fileName,fileData)
    data=readingFile(fileName)
    return data

url = 'http://saral.navgurukul.org/api/courses'

#Function Calling
saralData=apiCalling(url)

#List of Saral courses
courseName_list = []
courseId_list = []
def courseList(saralData):
    for index in range(0,len(saralData['availableCourses'])):
        courseName= saralData["availableCourses"][index]["name"]
        courseId = saralData["availableCourses"][index]["id"]
        courseName_list.append(courseName)
        courseId_list.append(courseId)
        print (index+1 , ":",courseName,"=",courseId)
    user_input= input("Enter courseName:")
    if user_input == "r" or user_input == "R" or user_input == "random" or user_input == "Random":
        a = random.choice(courseName_list)
        print (a)
    else:
        user = courseName_list[int(user_input)-1]
        print (user)
courseList(saralData)