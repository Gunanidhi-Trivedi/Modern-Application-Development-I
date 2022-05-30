
from flask import Flask, request, url_for
from flask import render_template
from jinja2 import Template
import matplotlib.pyplot as plt
import pandas as pd
import csv
template1="""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Student Data</title>
</head>
<body>
    <h1> Student Details </h1>
    <table border="2" id = "student-details-table">

            <tr>
                <th>Student Id</th>
                <th>Course Id</th>
                <th>Marks</th>
            </tr>
            {% for each in student_data %}
            <tr>
                <td>{{each[0]}}</td>
                <td>{{each[1]}}</td>
                <td>{{each[2]}}</td>
            </tr>
            {% endfor %} 
            <tr>
                <td colspan = "2" style="text-align:center"> Total Marks </td>
                <td>{{total_marks}}</td>
            </tr>
    </table>
    <br>
    <br> 
    <a href="/">Go Back</a>

</body>

</html>
"""

template2="""
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Course Data</title>
</head>

<body>
    <h1> Course Details </h1>
    <table border="2" id="course-details-table">
        <tr>
            <td> Average Marks </td>
            <td> Maximum Marks </td>
        </tr>
        <tr>    
            <td> {{average_marks}} </td>
            <td> {{maximum_marks}} </td>
        </tr>
    </table>  
    <br>
    <img src="static/image.png">
    <br>
    <a href="/"> Go Back </a>
</body>

</html>"""
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def main():
    if request.method=="GET":
        return render_template("index.html")

    elif request.method=="POST":

        # import the data file
        data=pd.read_csv("data.csv")
        data_list=data.values.tolist()

        # taking value from index.html
        id=request.form["ID"]
        id_value=int(request.form["id_value"])

        try:
            if id =="student_id" and id_value in list(data['Student id']):
                student_data=[]
                for i in data_list:
                    if i[0]==id_value:
                        student_data.append(i)
                total_marks=data[data["Student id"]==1001][" Marks"].sum()

                result = Template(template1)
                content=result.render(student_data=student_data,total_marks=total_marks)
                file=open("templates/student.html","w")
                file.write(content)
                file.close()
                return render_template("student.html")

            elif id=="course_id" and id_value in list(data[' Course id']):

                cource_mark_data=[]
                for i in data_list:
                    if i[1]==id_value:
                        cource_mark_data.append(i[2])
                average_marks=sum(cource_mark_data)/len(cource_mark_data)
                maximum_marks=max(cource_mark_data)
                plt.hist(cource_mark_data)
                plt.xlabel('Marks')
                plt.ylabel('Frequency')
                plt.savefig('static/image.png')
                result = Template(template2)
                content=result.render(average_marks=average_marks,maximum_marks=maximum_marks)
                file=open("templates/cource.html","w")
                file.write(content)
                file.close()

                return render_template("cource.html")  

            else:
                return render_template("wrong.html")

        except:
            return render_template("wrong.html")

if __name__ == '__main__':
    debug=True
    app.run()


    
