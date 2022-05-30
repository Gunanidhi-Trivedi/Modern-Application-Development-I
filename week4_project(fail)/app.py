from distutils.log import debug
from flask import Flask, request, url_for
from flask import render_template
from jinja2 import Template
from matplotlib import pyplot as plt
from numpy import true_divide
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method=="GET":
        return render_template("index.html")
    elif request.method=="POST":
        data=pd.read_csv('data.csv')
        id=request.form["ID"]
        id_value=request.form["id_value"]

        try:
            if id =="student_id" and id_value in list(data['Student id']):
                student_data=data[data['Student id']== id_value]
                total_marks=data[data['Student id']== id_value]['Marks'].sum()
                return render_template("student.html",student_data=student_data,total_marks_data=total_marks)
            elif id=="course_id" and id_value in list(data['Course id']):
                mark=list(data[data['Course id']==id_value]['Marks'])
                highest_marks=data[data['Course id']== id_value]['Marks'].max()
                sum_marks=sum(list(data[data['Course id']== id_value][' Marks']))
                count=data[data['Course id']== id_value]['Marks'].count()
                average_marks=sum_marks/count
                plt.clf() 
                plt.hist(mark)
                plt.xlabel('Marks')
                plt.ylabel('Frequency')
                plt.savefig('static/image.png')
                return render_template("courses.html",maximum_marks=highest_marks,average_marks=average_marks)  

            else:
                return render_template("wrong.html")

        except:
            return render_template("wrong.html")

if __name__ == '__main__':
    debug=True
    app.run()


    
