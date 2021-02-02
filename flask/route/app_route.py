from flask import Blueprint, render_template, request, redirect
import pymysql
from flask_sqlalchemy import SQLAlchemy

app_route = Blueprint('first_route',__name__)


db = pymysql.connect(host='aws_public_ip', port=3306, user='root', passwd='password',db='W2A', charset='utf8')

cursor = db.cursor()


@app_route.route('/', methods=['GET'])
def index():
    return render_template('login.html')


@app_route.route('/test')
def test():
    print("HI")
    result_="wpgur"
    return render_template('index.html',result=result_)


@app_route.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        login_info = request.form

        username = login_info['username']
        password = login_info['password']

        sql = "SELECT * FROM UserInfo WHERE username=%s"
        rows_count = cursor.execute(sql, username)

        if rows_count >0:
            user_info =cursor.fetchone()
            print("user info: ", user_info)

            is_pw_correct = user_info[2]
            print("password check: ", is_pw_correct)

            return render_template('login.html',info=user_info)

        else:
            print('user does not exist')
            return render_template('login.html',info='user does not exist')

        #return redirect(request.url)

    return render_template('login.html')


@app_route.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        register_info = request.form

        username = register_info['username']
        password = register_info['password']
        email = register_info['email']
        sql = """
            INSERT INTO UserInfo (username, hashed_password, email)
            VALUES (%s, %s, %s);
        """
        cursor.execute(sql,(username, password, email))
        db.commit()
        

        print(username, password, email)

        #return redirect(request.url)
        return render_template('login.html')

    return render_template('login.html')
    
