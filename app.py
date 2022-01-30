from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = 'TIGER'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'trevor@0409'
app.config['MYSQL_DB'] = 'travel'

mysql = MySQL(app)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/uslogin/', methods=['GET', 'POST'])
def login():
    msg = 'Please enter your usename and passwod'
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM account1 WHERE username = %s AND passw = %s', (username, password,))
        acc = cursor.fetchone()
        if acc:
            session['loggedin'] = True
            session['id'] = acc['id']
            session['username'] = acc['username']
            session['dloc']=acc['dloc']
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username or password!'
    return render_template('login.html', msg=msg)

@app.route('/uslogin/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = 'Sign up!'
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'phone' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        dloc = request.form['dloc']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM account1 WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not re.match(r'[0-9]+', phone):
            msg = 'phone no must contain only  numbers!'
        elif not username or not password or not email or not phone:
            msg = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO account1 VALUES (NULL, %s, %s, %s,%s,%s)', (username, password, email,phone,dloc,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)

@app.route("/htol",methods=['GET', 'POST'])
def htol():
    if 'loggedin' in session:
        locat=session.get("locat")
        print(locat)
        username = session['username']
        # if request.method == 'POST' and 'New_loc' in request.form:
        #locat = request.form['New_loc']
        cursor = mysql.connection.cursor()
        cursor.execute("select l_name from locat where not l_name=%s",(locat,))
        oloc = cursor.fetchall()
        cursor = mysql.connection.cursor()
        cursor.execute("select Distinct(e_name),l_id,l_name,e_id,photoname,price,address,le_id from locat left outer join loc_event on l_id=le_id  where l_name=%s and e_name not in (select e_name from planner where username=%s) order by price DESC",(locat,username,))
        dts = cursor.fetchall()
        print(dts)
        locatid=dts[0][1]
        #print(eventid)
        cursor.execute("select e_id,e_name,st1,st2,st3,st4 from loc_event inner join timing on e_id=te_id where le_id=%s",(locatid,))
        mt = cursor.fetchall()
        print(mt)
        return render_template("Location.html",value=dts,value2=mt,value3=oloc,loc=locat)
    else:
        return redirect(url_for('login'))

@app.route("/historyins",methods=['GET','POST'])
def historyins():
    if 'loggedin' in session:
        username=session['username']
        print(request.form)
        if request.method == 'POST' and 'e_name' in request.form and 'loc' in request.form and 'price' in request.form and 'date' in request.form:
            e_name=request.form['e_name']
            loc=request.form['loc']
            price=request.form['price']
            date=request.form['date']
            #time=request.form['time']
            print(e_name)
            cursor = mysql.connection.cursor()
            cursor.execute("insert into hist(username,location,e_name,price,e_date) values(%s,%s,%s,%s,%s)",(username,loc,e_name,price,date,))
            mysql.connection.commit()
            cursor = mysql.connection.cursor()
            return redirect(url_for('history'))
    return redirect(url_for('login'))

@app.route("/history",methods=['GET','POST'])
def history():
    if 'loggedin' in session:
        username=session['username']
        cursor = mysql.connection.cursor()
        cursor.execute("select e_name,location,price,e_date from hist where username=%s",(username,))
        bodet=cursor.fetchall()
        print(bodet)
        return render_template("history.html",value=bodet)
    return redirect(url_for('login'))

@app.route("/ltoh",methods=['GET', 'POST'])
def ltoh():
    if 'loggedin' in session:
        locat=session.get("locat")
        print(locat)
        username = session['username']
        # if request.method == 'POST' and 'New_loc' in request.form:
        #locat = request.form['New_loc']
        cursor = mysql.connection.cursor()
        cursor.execute("select l_name from locat where not l_name=%s",(locat,))
        oloc = cursor.fetchall()
        cursor = mysql.connection.cursor()
        cursor.execute("select Distinct(e_name),l_id,l_name,e_id,photoname,price,address,le_id from locat left outer join loc_event on l_id=le_id  where l_name=%s and e_name not in (select e_name from planner where username=%s) order by price ASc",(locat,username,))
        dts = cursor.fetchall()
        print(dts)
        locatid=dts[0][1]
        #print(eventid)
        cursor.execute("select e_id,e_name,st1,st2,st3,st4 from loc_event inner join timing on e_id=te_id where le_id=%s",(locatid,))
        mt = cursor.fetchall()
        print(mt)
        return render_template("Location.html",value=dts,value2=mt,value3=oloc,loc=locat)
    else:
        return redirect(url_for('login'))

@app.route("/home")
def home():
    if 'loggedin' in session:
        username = session['username']
        dloc = session['dloc']
        cursor = mysql.connection.cursor()
        cursor.execute("select l_name from locat where not l_name=%s",(dloc,))
        oloc = cursor.fetchall()
        cursor = mysql.connection.cursor()
        cursor.execute("select Distinct(e_name),l_id,l_name,e_id,photoname,price,address,le_id from locat left outer join loc_event on l_id=le_id  where l_name=%s and e_name not in (select e_name from planner where username=%s)",(dloc,username,))
        dts = cursor.fetchall()
        print(dts)
        locatid=dts[0][1]
        #print(eventid)
        cursor.execute("select e_id,e_name,st1,st2,st3,st4 from loc_event inner join timing on e_id=te_id where le_id=%s",(locatid,))
        mt = cursor.fetchall()
        print(mt)

        return render_template("Profile.html",value=dts,value2=mt,value3=oloc,value4=dloc)
    return redirect(url_for('login'))


@app.route("/loc",methods=['GET', 'POST'])
def loc():
    if 'loggedin' in session:
        username = session['username']
        if request.method == 'POST' and 'New_loc' in request.form:
            locat = request.form['New_loc']
            session['locat']=locat
            cursor = mysql.connection.cursor()
            cursor.execute("select l_name from locat where not l_name=%s",(locat,))
            oloc = cursor.fetchall()
            cursor = mysql.connection.cursor()
            cursor.execute("select Distinct(e_name),l_id,l_name,e_id,photoname,price,address,le_id from locat left outer join loc_event on l_id=le_id  where l_name=%s and e_name not in (select e_name from planner where username=%s)",(locat,username,))
            dts = cursor.fetchall()
            print(dts)
            locatid=dts[0][1]
            #print(eventid)
            cursor.execute("select e_id,e_name,st1,st2,st3,st4 from loc_event inner join timing on e_id=te_id where le_id=%s",(locatid,))
            mt = cursor.fetchall()
            print(mt)
            return render_template("Location.html",value=dts,value2=mt,value3=oloc,loc=locat)
    return redirect(url_for('login'))

@app.route("/addtoplan",methods=['GET','POST'])
def addtoplan():
    if 'loggedin' in session:
        username = session['username']
        u_id = str(session['id'])
        print(request.form)
        if request.method == 'POST' and 'c_loc' in request.form and 'e_name' in request.form and 'time' in request.form and 'e_date' in request.form and 'e_add' in request.form and 'e_price' in request.form:
            locat=request.form['c_loc']
            event=request.form['e_name']
            price=request.form['e_price']
            date=request.form['e_date']
            time=request.form['time']
            add=request.form['e_add']
            cursor = mysql.connection.cursor()
            cursor.execute("insert into planner(u_id,username,location,e_name,price,e_date,e_time,address) values(%s,%s,%s,%s,%s,%s,%s,%s)",(u_id,username,locat,event,price,date,time,add,))
            mysql.connection.commit()
            cursor = mysql.connection.cursor()
            cursor.execute("select location,e_name,price,e_date,e_time,address from planner where u_id=%s",(u_id))
            bodet=cursor.fetchall()
            print(bodet)
            cursor = mysql.connection.cursor()
            cursor.execute("select sum(price) as pr from planner where u_id=%s",(u_id))
            exp=cursor.fetchall()
            print(exp)
            return render_template("planner.html",value=bodet,exp=exp)
    return redirect(url_for('login'))

@app.route("/plans",methods=['GET','POST'])
def plans():
    if 'loggedin' in session:
        username=session['username']
        u_id = str(session['id'])
        cursor = mysql.connection.cursor()
        cursor.execute("select location,e_name,price,e_date,e_time,address from planner where u_id=%s",(u_id))
        bodet=cursor.fetchall()
        cursor = mysql.connection.cursor()
        cursor.execute("select sum(price) as pr from planner where u_id=%s",(u_id))
        exp=cursor.fetchall()
        return render_template("planner.html",value=bodet,exp=exp)
    return redirect(url_for('login'))

@app.route("/rem",methods=['GET','POST'])
def rem():
    if 'loggedin' in session:
        username=session['username']
        u_id = str(session['id'])
        print(request.form)
        if request.method == 'POST' and 'e_name' in request.form:
            e_name=request.form['e_name']
            print(e_name)
            cursor = mysql.connection.cursor()
            cursor.execute("delete from planner where e_name=%s and username=%s",(e_name,username,))
            mysql.connection.commit()
            cursor = mysql.connection.cursor()
            # cursor.execute("select sum(price) as pr from planner where id=%s",(u_id))
            # exp=cursor.fetchall()
            # return render_template("planner.html",exp=exp)
            return redirect(url_for('plans'))
    return redirect(url_for('login'))


if __name__=="__main__":
    app.run(debug=True);