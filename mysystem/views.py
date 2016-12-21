from django.shortcuts import render
import os, time, re
from stat import  *

# Create your views here.
def show(request):
    # provide information last modified time
    root_dir = "/usr/local/class/1052sp/assignment1/"
    status_list = []
    for dirpath, dir_list, file_list in os.walk(root_dir):
        print "Walking into directory: " + str(dirpath)
        if len(file_list) > 0:
            student_id = re.search(r"(u[0-9]+)", dirpath).group(1)
            "Found student:", student_id

            for f in file_list:
                if str(f) == "score.txt":
                    st = os.stat(dirpath + "/" + f)
                    t = time.asctime(time.localtime(st[ST_MTIME]))
                    student = Student(student_id, True, t)

                    status_list.append(student)
        else:
            print "No file is found."

                    #  with open(dirpath +"/"+ f) as file:
                    #      corpus.append(file.read())

    #print info_dicts
    return render(request, 'show.html', {'status_list': status_list})

class Student(object):

    # The class "constructor" - It's actually an initializer
    def __init__(self, student_id, submission_status, submission_time):
        self.student_id = student_id
        self.submission_status = submission_status
        self.submission_time = submission_time

