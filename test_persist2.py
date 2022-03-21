# Python Code for factory method
import psycopg2
import  datetime

import  time
from time import  time




try:


    conn = psycopg2.connect(
     database="student", user='postgres', password='root', host='localhost', port='5432'
    )
    conn.autocommit = True
  # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
except psycopg2.DatabaseError as ec:
    print("CONNECTION ERROR : {} ".format(ec))

def test_timer_func(func):
        # This function shows the execution time of
        # the function object passed
        def wrap_func(*args, **kwargs):
            t1 = time()
            result = func(*args, **kwargs)
            t2 = time()
            print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
            return result

        return wrap_func





class create():


    def __init__(self):
        try:
            student_id = int(input("Enter the student ID"))
            first_name = input("Enter the firts name")
            last_name = input("Enter the last name")
            email_id = input("Enter the email ID")

            self.signup(student_id, first_name, last_name, email_id)
        except ValueError:

            print(" value should be integer {}".format(ValueError))


    @test_timer_func
    def signup(self, student_id, first_name, last_name, email_id):
        # time_stamp=str(datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))
        time_stamp = datetime.datetime.now().strftime('@ %Y-%m-%d %H:%M:%S')
        cursor.execute(
            "INSERT INTO register(student_id, first_name, last_name,email_id,time_stamp)VALUES (%s, %s, %s,%s,%s)",
            (student_id, first_name, last_name, email_id, time_stamp))

        print("DATA INSERTED IN DB STUDENT : ")

        conn.close()





class info():
    def __init__(self):
        try:

            emp_id=int(input("EMPLOYEES ID FOR INFO __ "))
            self.getinformation(emp_id)
        except ValueError:
            print("value should be integer {}".format(ValueError))
    @test_timer_func
    def getinformation(self, emp_id):
        print("GETTING INFORMAION  RECORD ")
        try:
            sql_select_query = """select * from register where student_id = %s"""
            cursor.execute(sql_select_query, (emp_id,))
            record = cursor.fetchone()


            if (record==None):
                print( "STUDENT DOESNOT EXIT ........ ")
            else:
                print(record)


        except psycopg2.DatabaseError as queryerror:
            print("FETCHING INFORMATION ERROR  : {}".format(queryerror))

            conn.close()


class update(info):
    def __init__(self):
        studentID=int(input("Enter the employee id which You want to Update "))

        self.updateStudent(studentID)

    @test_timer_func
    def updateStudent(self,studentID):

        info.getinformation(self,studentID)
        id = input("confirm the id ")
        print("First Name PRESS : 1" )
        print("LAST Name PRESS : 2")
        print("email id PRESS : 3")

        ch = input("Which Field U Want to Edit?")

        pat = ""
        if (ch == "1"):
            nn = input("Enter New first_namr:")
            pat = "first_name='{}'".format(nn)
        elif (ch == "2"):
            nd = input("Enter New last name:")
            pat = "last_name='{}'".format(nd)
        elif (ch == "3"):
            nd = input("Enter New email:")
            pat = "email_id='{}'".format(nd)

        elif (ch == '5'):
            print("Exit")
        else:
            print("Invalid Option")
            time_stamp = 435


        # time_stamp = str(time.strftime("""%a %d %b %Y %I:%M:%S %p %Z""", time.gmtime()))
        # time_stamp = str(datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))
        time_stamp = datetime.datetime.now().strftime('@ %Y-%m-%d %H:%M:%S')
        time="time_stamp='{}'".format(time_stamp)
        q = "update register set {},{} where student_id={}".format(pat,time,studentID)

        print(q)
        cursor.execute(q)
        conn.commit()


def Factory(language ="english"):

    """Factory Method"""
    localizers = {
        "create": create,
        "info" : info,
        "update" : update,


    }

    return localizers[language]()



if __name__ == "__main__":

    while True:
        try:
            x=str(input("ENTER WHICH PROCCESS YOU LIKE :create:info:update  "))
            f = Factory(x)
        except TypeError:
            print("TYPE ERROR {}".format(TypeError))

