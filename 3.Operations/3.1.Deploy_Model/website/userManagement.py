import sqlite3 as sql
import bcrypt


# this was an example i'm just leaving it in here in case i need to use it
def getdata():
    connection = sql.connect("databaseFiles/database.db", check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM developer_logs")
    devlogs = cursor.fetchall()
    connection.close()
    return devlogs


# OLD code for creating the devlog table
# connection = sql.connect("databaseFiles/database.db", check_same_thread=False)
# cursor = connection.cursor()
# cursor.execute("CREATE TABLE developer_logs(dev_id TEXT NOT NULL, developer_name TEXT NOT NULL, project_name TEXT NOT NULL, start_time TEXT NOT NULL, end_time TEXT NOT NULL, diary_time_spent TEXT NOT NULL, working_time_spent TEXT NOT NULL, repo_info TEXT NOT NULL, project_notes TEXT NOT NULL)")
# connection.close()


# authenticates login
def loginput(user, pwd):
    connection = sql.connect("databaseFiles/database.db", check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("SELECT password FROM user_data WHERE username = ?", (user,))
    details = cursor.fetchone()
    connection.close()
    if details == None:
        print("login failed!")
        return False
    else:
        hashedinput = pwd.encode("utf-8")
        passwordoutput = details[0]
        print("login success!")
        return bcrypt.checkpw(hashedinput, passwordoutput)


# login failed and login success print messages are used for debugging and have no actual effect on the website


# adds user
def signupinput(user, pwd):
    try:
        if user == "":
            user = None
            return False
        if pwd == "":
            pwd = None
            return False
        connection = sql.connect("databaseFiles/database.db", check_same_thread=False)
        cursor = connection.cursor()
        bytes = pwd.encode("utf-8")
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes, salt)
        cursor.execute(
            "INSERT INTO user_data (username,password) VALUES (?,?)", (user, hash)
        )
        connection.commit()
        connection.close()
        return True
    except sql.IntegrityError:
        return False


def devlogadd(user, developer, project, start, end, diarytime, worktime, repo, notes):
    try:
        if user == "":
            user = None
        if developer == "":
            print("removed empty strings")
            developer = None
        if project == "":
            project = None
        if start == "":
            start = None
        if end == "":
            end = None
        if diarytime == "":
            diarytime = None
        if worktime == "":
            worktime = None
        if repo == "":
            repo = None
        if notes == "":
            notes = None
        connection = sql.connect("databaseFiles/database.db", check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO developer_logs (dev_id, developer_name, project_name,start_time, end_time, diary_time_spent, working_time_spent, repo_info, project_notes) VALUES (?,?,?,?,?,?,?,?,?)",
            (user, developer, project, start, end, diarytime, worktime, repo, notes),
        )
        connection.commit()
        connection.close()
        return True
    except sql.IntegrityError:
        print("uhhhhhhhh")
        return False


def devlogsearch(searchdata):
    try:
        print(searchdata)
        connection = sql.connect("databaseFiles/database.db", check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM developer_logs WHERE developer_name = ?", (searchdata,)
        )
        logs = cursor.fetchall()
        connection.close()
        return logs
    except sql.IntegrityError:
        return False


# TEST CODE FOR THE INPUT SYSTEM - NO HASHING NO INPUT VALIDATION WE DIE LIKE
# usertest = input("no ")
# passtest = input("yes ")

# cursor.execute(f"INSERT INTO user_data (username, password) VALUES ('{usertest}','{passtest}')")

# cursor.execute("SELECT * FROM user_data")
# SensitiveInformation = cursor.fetchall()
# print(SensitiveInformation)

# if username and password combination brings results from sql database, log user in
# if not, say incorrect username or password

# youtube tutorials
# https://www.youtube.com/watch?v=biU3SvIctWI - html form output to python variable
# https://www.youtube.com/watch?v=lK-P5kOiQ6Y - how to use sql in python
