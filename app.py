from flask import *
from flask_mail import *
import random
import requests,json

app=Flask(__name__)
app.config['MAIL_SERVER']='Your Server'  
app.config['MAIL_PORT']=465  
app.config['MAIL_USERNAME'] = 'Your Username'  
app.config['MAIL_PASSWORD'] = 'Your Password'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/")
def home():
    return render_template("design.html")

@app.route("/mydata",methods=['POST'])
def mydata():
    r=requests.get("https://open.kickbox.com/v1/disposable/"+request.form['email']+"")
    b=r.json()
    if b['disposable']==True:
        a={'status':'False'}
    else:
        m=Message(request.form['sub'], sender = 'angel@rohitchouhan.com', recipients=[request.form['email']])
        m.body=request.form['content']
        mail.send(m)
        a={'status':'True'}
    return render_template("print.html",x=a)
    

if __name__=='__main__':
    app.run(debug = True)
