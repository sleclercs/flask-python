import os
from flask import Flask, render_template, flash, request, redirect, url_for
from forms import LoginForm

#create the object of Flask
app  = Flask(__name__)

app.config['SECRET_KEY'] = 'hardsecretkey'

#creating our routes
@app.route('/')
def index():

    return render_template('index.html')



#login route
@app.route('/login' , methods = ['GET', 'POST'])
def Login():
    form = LoginForm()

    if form.validate_on_submit():
        if request.form['username'] != 'codeloop' or request.form['password'] != '12345':
            flash("Invalid Credentials, Please Try Again")


        else:
            return redirect(url_for('index'))



    return render_template('login.html', form = form)





#run flask app
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)