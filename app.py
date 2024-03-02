from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "ssAY54^!"
app.config["MYSQL_DB"] = "sehat_db"

app.secret_key = 'your secret key'


mysql = MySQL(app)


@app.route('/')
def user_page():
    return render_template('index.html')

    
@app.route('/')
def home():
    if 'email' in session:
        return render_template('index.html')
    else:
        return redirect('/login')
    
@app.route("/signup")
def signup_page():
    return render_template('signup.html')
    
@app.route('/signup', methods=['Post'])
def signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    conn = mysql.connection
    cur = conn.cursor()
    cur.execute('SELECT * FROM patients WHERE email = %s', (email,))
    result = cur.fetchone()
    if result:
        conn.close()
        return redirect('/?message=Email already exists!')
    
    cur.execute('INSERT INTO patients (name, email, password) VALUES (%s, %s, %s)', (name, email, password))
    conn.commit()
    
    session['email'] = email
    conn.close()
    
    return redirect('/')

@app.route("/details")
def bdetails():
    if 'email' not in session:
        return redirect('/login')
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT name, blood_group, phone FROM patients WHERE email=%s", (session['email'],))
    patient = cur.fetchone()
    cur.close()
    
    if patient:
        return render_template('details.html', name=patient[0], blood_group=patient[1], phone_number=patient[2])
    else:
        return "Patient not found"
        
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('signup.html')
    
    email = request.form['email']
    password = request.form['password']
    
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute('SELECT * FROM patients WHERE email = %s AND password = %s', (email, password))
    user = cur.fetchone()
    
    if user:
        session['email'] = email
        conn.close()
        return redirect('/')
    else:
        conn.close()
        return redirect('/login?message=Incorrect email/password!')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'email' not in session:
        return redirect('/login')
    
    if request.method == 'POST':
        age = request.form['age']
        blood_group = request.form['blood_group']
        phone_number = request.form['phone']
        marital_status = request.form['marital_status']
        gender = request.form['gender']
        medical_history = request.form['health_history']
        test_name = request.form['test_name']
        test_result = request.form['test_result']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO patients (age, blood_group, phone, m_status, gender, health_history, test_name, test_result) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (age, blood_group, phone_number, marital_status, gender, medical_history, test_name, test_result)) 
        mysql.connection.commit()
        cur.close()
        return redirect('/')
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/login')


def subscribe():
    email = request.form['email']
    cur = mysql.connection.cursor()
    sql = "INSERT INTO subscribers (email) VALUES (%s)", [email]
    val = (email)
    cur.execute(sql, val)
    mysql.connection.commit()
    cur.close()
    return "Subscribed Successfully!"

if __name__ == '__main__':
    app.run(debug=True)