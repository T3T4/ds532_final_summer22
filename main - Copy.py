from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL, MySQLdb
import mysql.connector


app = Flask(__name__)
#db = yaml.load(open('db.yaml'))
mysql = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port='3307',
    database='finalproject'
)


@app.route('/')
def index():
    #return render_template('index.html')
    mycursor = mysql.cursor()
    mycursor.execute('select * from Total_Number order by Tiktok_Rank LIMIT 25')
    data1 = mycursor.fetchall()
    mycursor.close()
    return render_template('index.html', tiktok_influencer=data1)


@app.route("/ajaxlivesearch", methods=["GET", "POST"])
def ajaxlivesearch():
    mycursor = mysql.cursor()
    if request.method == "POST":
        search_word = request.form['query']
        print(search_word)
        if search_word == '':
            query = "select * from total_number  WHERE Accounts=%s"
            mycursor.execute(query)
            tiktok = mycursor.fetchall()
        else:
            query = "select * from total_number  WHERE Accounts LIKE '%{}%'".format(search_word )
            mycursor.execute(query)
            numrows = int(mycursor.rowcount)
            tiktok = mycursor.fetchall()
            print(numrows)
    return jsonify({'htmlresponse': render_template('response.html', tiktok=tiktok, numrows=numrows)})


#search records
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        cursor = mysql.cursor()
        cursor.executemany('''select * from total_number where name = Accounts=%s''', request.form['search'])
        return render_template("results.html", records=cursor.fetchall())
        mysql.commit()
    return render_template('search.html')


# update records in index.html
@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        Accounts = request.form['Accounts']
        #Tiktok_Rank= request.form['Tiktok_Rank']
        Comments_avg = request.form['Comments_avg']
        Likes_avg = request.form['Likes_avg']
        Shares_avg = request.form['Shares_avg']
        Subscribers_count = request.form['Subscribers_count']
        Views_avg = request.form['Views_avg']
        cursor = mysql.cursor()
        cursor.execute(
            "UPDATE Total_Number SET Comments_avg=%s, Likes_avg=%s, Shares_avg=%s, Subscribers_count=%s, Views_avg=%s WHERE Accounts=%s",
            (Comments_avg, Likes_avg, Shares_avg, Subscribers_count, Views_avg, Accounts))

        flash("Data Updated Successfully")
        mysql.commit()
        return redirect(url_for('index'))

#New Page 1 on Subscribers


@app.route('/Subscribers')
def subscribers():
    mycursor = mysql.cursor()
    mycursor.execute('select * from Subscribers order by Subscribers_rank LIMIT 25')
    data2 = mycursor.fetchall()
    mycursor.close()
    return render_template('Subscribers.html', subscribers=data2)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':
        Accounts = request.form['Accounts']
        Subscribers_count = request.form['Subscribers_count']
        cursor = mysql.cursor()
        cursor.execute('''INSERT INTO New_Tiktok_Subscribers VALUES(%s,%s)''', (Accounts, Subscribers_count))
        mysql.commit()
        cursor.close()
        return f"Thank you!!"

#New Page 2 on Shares
@app.route('/shares')
def shares():
    mycursor = mysql.cursor()
    mycursor.execute('select * from Shares order by Shares_rank LIMIT 25')
    data3 = mycursor.fetchall()
    mycursor.close()
    return render_template('shares.html', shares=data3)

@app.route('/form2')
def form2():
    return render_template('form2.html')

@app.route('/login2', methods=['POST', 'GET'])
def login2():
    if request.method == 'GET':
        return "Please Enter the Information"

    if request.method == 'POST':
        Accounts = request.form['Accounts']
        Shares_avg = request.form['Shares_avg']
        cursor = mysql.cursor()
        cursor.execute('''INSERT INTO New_Tiktok_Shares VALUES(%s,%s)''', (Accounts, Shares_avg))
        mysql.commit()
        cursor.close()
        return f"Thank you!!"

#New Page 3 on Comments
@app.route('/comments')
def comments():
    mycursor = mysql.cursor()
    mycursor.execute('select * from Comments order by Comments_rank LIMIT 25')
    data4 = mycursor.fetchall()
    mycursor.close()
    return render_template('comments.html', comments=data4)

@app.route('/form3')
def form3():
    return render_template('form3.html')

@app.route('/login3', methods=['POST', 'GET'])
def login3():
    if request.method == 'GET':
        return "Please Enter the Information"

    if request.method == 'POST':
        Accounts = request.form['Accounts']
        Comments_avg = request.form['Comments_avg']
        cursor = mysql.cursor()
        cursor.execute('''INSERT INTO New_Tiktok_Comments VALUES(%s,%s)''', (Accounts, Comments_avg))
        mysql.commit()
        cursor.close()
        return f"Thank you!!"

#New Page 4 on Likes
@app.route('/likes')
def likes():
    mycursor = mysql.cursor()
    mycursor.execute('select * from Likes order by Likes_rank LIMIT 25')
    data5 = mycursor.fetchall()
    mycursor.close()
    return render_template('likes.html', likes=data5)

@app.route('/form4')
def form4():
    return render_template('form4.html')

@app.route('/login4', methods=['POST', 'GET'])
def login4():
    if request.method == 'GET':
        return "Please Enter the Information"

    if request.method == 'POST':
        Accounts = request.form['Accounts']
        Likes_avg = request.form['Likes_avg']
        cursor = mysql.cursor()
        cursor.execute('''INSERT INTO New_Tiktok_Likes VALUES(%s,%s)''', (Accounts, Likes_avg))
        mysql.commit()
        cursor.close()
        return f"Thank you!!"


#New Page 5 on Views
@app.route('/views')
def views():
    mycursor = mysql.cursor()
    mycursor.execute('select * from Views order by Views_rank LIMIT 25')
    data6 = mycursor.fetchall()
    mycursor.close()
    return render_template('views.html', views=data6)

@app.route('/form5')
def form5():
    return render_template('form5.html')

@app.route('/login5', methods=['POST', 'GET'])
def login5():
    if request.method == 'GET':
        return "Please Enter the Information"

    if request.method == 'POST':
        Accounts = request.form['Accounts']
        Views_avg = request.form['Views_avg']
        cursor = mysql.cursor()
        cursor.execute('''INSERT INTO New_Tiktok_Views VALUES(%s,%s)''', (Accounts, Views_avg))
        mysql.commit()
        cursor.close()
        return f"Thank you!!"

#end of adding routes

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
