from flask import *
import os
import pyrebase

app = Flask(__name__)

firebaseConfig = {
  "apiKey": "AIzaSyDe8avmHiNkm4oOH9Ng3aNmjrU1_TAv4ts",
  "authDomain": "pearlhacks2021-envizion.firebaseapp.com",
  "databaseURL": "https://pearlhacks2021-envizion-default-rtdb.firebaseio.com",
  "projectId": "pearlhacks2021-envizion",
  "storageBucket": "pearlhacks2021-envizion.appspot.com",
  "messagingSenderId": "1060421957904",
  "appId": "1:1060421957904:web:13e79ec795b159a0dd0d95",
  "measurementId": "G-6TKLZLLKL6"
};

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

@app.route('/',methods=['GET','POST'])
def login():
    successful = "Login successful!"
    unsuccessful = "Login failed!"
    if request.method == 'POST':
        print("reached post method")
        email = request.form['email']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email,password)
            return render_template('login.html',s=successful)
        except:
            return render_template('login.html',us=unsuccessful)

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))