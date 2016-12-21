import sys, re, os, shutil, pwd, grp, time

class Submit:
    """ This program aims to submit assignment directory into /usr/local/class/sp1052/ """

    def __init__(self):
        """ Input Format Check and Basic Initialization """

        print "Submitting System Programming Assignment..."
        try:
            if int(sys.argv[1]) > 0:
                self.assign_num = sys.argv[1]
                print "\nAssignment number:", self.assign_num
            else:
                raise
        except:
            print "Format Error"
            print "Usage: submit # ( # being the number of your assignment)"
            exit()

        self.src_dir = os.path.dirname(os.path.abspath(__file__)) + "/assignment" + self.assign_num + "/"
        self.tmp_dir = "/usr/local/class/1052sp/.tmp/"
        self.dst_dir = "/usr/local/class/1052sp/assignment" + self.assign_num + "/"
	self.owner = ""

    def check_source(self):
        print "\nStep1: Checking if you have the directory assignment", self.assign_num
        if os.path.isdir(self.src_dir):
            return True
        else:
            print "Abort: No assignment" + self.assign_num + " is found"
            exit()

    def get_owner(self):
        """ Get the owner name of the directory """

        print "Step2: Checking the owner of the directory ..."
        # Check the status of the directory
        if os.stat(self.src_dir):
            file_status = os.stat(self.src_dir)
            # Get owner name
            self.owner = pwd.getpwuid(file_status.st_uid).pw_name

    def check_dirs(self):
        """ Delete directory if it exists | This is for repeated submission """

        """ remove the existing /assignment1/u1001xxxx """
        dir1 = self.dst_dir + self.owner + "/"
        if os.path.exists(dir1):
            #print "Removeing existing directory: " + dir1
            shutil.rmtree(dir1)

    def submit(self):
        """ Copy codes from source to destination """

        print "Step3: Submitting your assignment ..."
        try:
            """ /assignment1/everything -> /assignment1/u1001xxxx/everything """
            shutil.copytree(self.src_dir, self.dst_dir + self.owner)

            uid = pwd.getpwnam("utaipei").pw_uid
            gid = grp.getgrnam("utaipei").gr_gid
            shutil.chown(self.dst_dir + self.owner, user=uid, group=gid)

            # print now => 2016-12-21 21:54:51
            now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        except:
            print "Error occurred while copying your code"
            raise

    def workflow(self):
        if self.check_source():
            self.get_owner()
            self.check_dirs()
            self.submit()

        print "\nSubmission Successful!"

if __name__ == '__main__':
    submit = Submit()
    submit.workflow()
