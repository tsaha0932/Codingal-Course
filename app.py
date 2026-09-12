from flask import Flask, render_template, request, redirect
import mysql.connector
import re

app = Flask(__name__)


# =========================
# LOGIN
# =========================
@app.route('/login', methods=['GET', 'POST'])
def login():

    msg = ''

    if request.method == 'POST' and \
            'username' in request.form and \
            'password' in request.form:

        username = request.form['username']
        password = request.form['password']

        # Connect to MySQL
        mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="Rz8hqnldk4",
            password="nd0wK03xe0",
            database="Rz8hqnldk4"
        )

        mycursor = mydb.cursor()

        # Check login details
        mycursor.execute(
            "SELECT * FROM LoginDetails WHERE Name = %s AND Password = %s",
            (username, password)
        )

        account = mycursor.fetchone()

        if account:

            print("Login successful!")

            id = account[0]
            name = account[1]

            msg = "Logged in Successfully"

            return render_template(
                'index.html',
                msg=msg,
                name=name,
                id=id
            )

        else:

            msg = "Incorrect Credentials. Kindly check"

            return render_template(
                'login.html',
                msg=msg
            )

    return render_template('login.html')


# =========================
# REGISTER
# =========================
@app.route('/register', methods=['GET', 'POST'])
def register():

    msg = ''

    if request.method == 'POST' and \
            'username' in request.form and \
            'password' in request.form and \
            'email' in request.form:

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Connect to MySQL
        mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="Rz8hqnldk4",
            password="nd0wK03xe",
            database="Rz8hqnldk4"
        )

        mycursor = mydb.cursor()

        # Check if account already exists
        mycursor.execute(
            "SELECT * FROM LoginDetails WHERE Name = %s AND Email_id = %s",
            (username, email)
        )

        account = mycursor.fetchone()

        if account:

            msg = "Account already exists!"

        elif not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):

            msg = "Invalid email address!"

        elif not re.match(r'^[A-Za-z0-9]+$', username):

            msg = "Username must contain only characters and numbers!"

        elif not username or not password or not email:

            msg = "Kindly fill the details!"

        else:

            # Insert new account
            mycursor.execute(
                "INSERT INTO LoginDetails VALUES (NULL, %s, %s, %s)",
                (username, password, email)
            )

            mydb.commit()

            msg = "Your Registration is Successful"

            name = username

            return render_template(
                'index.html',
                msg=msg,
                name=name
            )

        return render_template(
            'registration.html',
            msg=msg
        )

    return render_template('registration.html')


# =========================
# LOGOUT
# =========================
@app.route('/logout')
def logout():

    name = ''
    id = ''

    msg = "Logged out Successfully"

    return render_template(
        'login.html',
        msg=msg,
        name=name,
        id=id
    )


# =========================
# RUN APPLICATION
# =========================
if __name__ == '__main__':
    app.run(debug=True)