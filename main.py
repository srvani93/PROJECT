
from flask import Flask,render_template,url_for,request
from link import *
app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template("home.html")

@app.route('/data',methods=["POST"])
def form_data():
    if request.method == "POST":
       c_name=request.form.get("company_name")
       date_time=request.form.get("company_time")
       result=get_details(c_name,date_time)
       return date_time




if __name__ == '__main__':
    app.run(debug=True)