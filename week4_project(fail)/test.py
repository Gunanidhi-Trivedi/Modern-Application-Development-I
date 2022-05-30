import pandas as pd
from jinja2 import Template


data=pd.read_csv("data.csv")
datas=list(data['Student id'])
id_value=1001
print(type(id_value))
print(datas)
print(id_value in list(data['Student id']))
student_data=data[data['Student id']== id_value]
total_marks=data[data['Student id']== id_value][' Marks'].sum()
template = '''
			    <!DOCTYPE html>
			    <html>
			    <head>
			        <style>
                        table, th, td { border: 1px solid black; }
			    	</style>
			    	<title> Student Details </title>
			    </head>
			    <body>
			        <h1>Enter the Details</h1>
			        <div id="main">
			        <table>                             
                   	    <tr>
                            <th>Student Id</th>
                            <th>Course Id</th>
                            <th>Marks</th>
                        </tr>
                        {% for each in {{student_data}} %}
                            <tr>
                                <td>each['Student id']</td>
                                <td>each['Course id']</td>
                                <td>each['Marks']</td>
                            </tr>
                        {% end for %} 
                        <tr>
                            <td colspan = "2" style="text-align:center"> Total Marks </td>
                            <td>{{total_marks_data}}</td>
                        </tr>
			    	</table>
                    <a href="index.html">Go Back</a>
	            </body>
			    </html> '''

result = Template(template)
File = open("student.html","w")
output = File.write(result.render(student_data=student_data,total_marks=total_marks))
File.close()


# data=pd.read_csv("data.csv")
# student=list(data['Student id'])
# cource=list(data[" Course id"])
# print(student)
# print(cource)
