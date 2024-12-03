import json
import mysql.connector as sql
import Query
mydb = sql.connect(
    host="localhost",
    user="root",
    password="root1234",
    use_pure=True,
    database="mini_project_1"
)

mycursor = mydb.cursor()

def addNewDataChannelTable(data):
    mycursor.execute(Query.channel_insert,tuple(data.values()))
    mydb.commit()

def addNewDataCommentTable(data):
    mycursor.execute(Query.comment_insert,tuple(data.values()))
    mydb.commit()

def addNewDataVideoTable(data):
    mycursor.execute(Query.video_insert,tuple(data.values()))
    mydb.commit()

def getQueryBasedOnQuestion(index):
    sql_query = ""
    match index:
        case 0:
            sql_query = Query.question_one
        case 1:
            sql_query = Query.question_two
        case 2:
            sql_query = Query.question_three
        case 3:
            sql_query = Query.question_four
        case 4:
            sql_query = Query.question_five
        case 5:
            sql_query=Query.question_six
        case 6:
            sql_query = Query.question_seven
        case 7:
            sql_query = Query.question_eight
        case 8:
            sql_query = Query.question_nine
        case 9:
            sql_query = Query.question_ten


    if len(sql_query) > 0:
        mycursor.execute(sql_query)
        row_headers=[x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        return {
            "rows": myresult,
            "columns":row_headers
        }


