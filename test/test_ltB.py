import unittest

import find_exams.find_exams


class TestExclude(unittest.TestCase):

    def test_getCourse(self):
        courseAndLect = find_exams.getCourse("Hazelhurst/ELEN7039")
        self.assertEqual(courseAndLect, ("Hazelhurst","ELEN7039") )

    def test_getCoursesForLects(self):
        courses = find_exams.getCoursesForLects("lectlist.csv")
        self.assertEqual(courses, {'Cronje':['ELEN4014'],'Dinger': ['SCMD1003'],'Hazelhurst': ['ELEN7039', 'ELEN3020', 'COMS7059'],'Hofsajer': ['ELEN3003', 'ELEN3002'],'Levitt':['ELEN4010','ELEN3008']})

    def test_getExams(self):
        exams = find_exams.getExams("examlist.csv")
        self.assertEqual(exams, {'ELEN4013': ('2020-06-01', 'SHWWB'),'SCMD1003': ('2020-05-28', 'CM2'),'ELEN7039': ('2020-06-15', 'CM2'),'COMS7059': ('2020-05-23', 'FNB64'),'ELEN3002': ('2020-05-24', 'CM3'),'ELEN3003': ('2020-05-24', 'CM3'),'ELEN3008': ('2020-06-03', 'EH'),'ELEN4010': ('2020-05-29', 'TND')})

    ##def test_getTimeTable(self):
    ##   courses = find_exams.getCoursesForLects("lectlist.csv")
    ##    exams = find_exams.getExams("examlist.csv")
    ##    timetable = find_exams.getTimeTable(courses, exams)
    ##    self.assertEqual(timetable, "NotSure")

    ##def test_showTimeTable(self):
    ## Not Sure





if __name__ == '__main__':


    unittest.main()
