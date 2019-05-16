

import sys
import re

"""
getCourse returns the course name in the specified line of given data

:return: l_name, c_name
:param: line
"""
def getCourse(line):
    lname, c_name = line.rstrip().split("/")    ##EE1 Used wrong character for split, uses "/" in test csv
    return lname, c_name   ##EE2 Should return lname first


"""
getCoursesForLects returns the Courses with the specified Lecturers

:return: courses
:param: lectfn
"""
def getCoursesForLects(lectsfn):
    courses = {}  # dictionary: for each lect returns list of courses
    lf = open(lectsfn)
    for line in lf:
        lect, course = getCourse(line)
        if lect in courses: # is the lecturer in the dictionary
            courses[lect].append(course)  # add course to the list ##EE3 Needs to add the course to the list not the lecturer
        else:
            courses[lect] = [course]  
    lf.close()
    return courses


"""
getExams returns the list of exams for the specified examfname

:return: exams
:param: examfname
"""
def getExams(examfname):
    exams = {}
    for line in open(examfname):
        data = line.rstrip().split(",")
        exams[data[0]]=(data[1],data[2])
    return exams


"""
getTimeTable returns a nested list of ttable for the specified courses and exams

:return: ttable
:param: courses, exams
"""
def getTimeTable(courses,exams):
    ttable = []  # nested list -- for each lect a list of exams
    for lect in sorted(courses.keys()):
        l_exams   = [] # build list of lecturer's exams
        l_courses = courses[lect] # get their courses
        for c in l_courses:
            if c not in exams:
                the_exam=("TBD","TBD")
            else:
                the_exam = exams[c]
            l_exams.append((c,the_exam))
        ttable.append((lect,l_exams)) # now we know the exams add it list
    return ttable


"""
showTimeTable prints the specified timetable to the terminal

:return: returns nothing
:param: ttable
"""
def showTimeTable(ttable):
    for (lect, l_exams) in ttable:
        print(lect)
        for c,ex in l_exams:
            print("   ",c,ex[0],ex[1])
        

if __name__ == "__main__":
    examfn    = sys.argv[1]
    lectsfn     = sys.argv[2]
    courses    = getCoursesForLects(lectsfn)
    exams     = getExams(examfn)
    tt = getTimeTable(courses,exams)
    showTimeTable(tt)
