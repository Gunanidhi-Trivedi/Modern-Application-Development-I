
from jinja2 import Template
import sys
from numpy import average
import pandas as pd
import matplotlib as plt

TEMPLATE_1 = """
<!DOCTYPE html>
<html>
    <head>
        <title> Students Data </title>
        <style>
            th{border:1px solid black;}
            td{border:1px solid black;}
        </style>
    </head>  
    <body>
        <h1> Student Details </h1> 
        <table style="border:1px solid black;">
            <tr>
                <th> Student id </th>
                <th> Course id </th>
                <th> Marks </th>
            </tr>
            {% for s in t1_data["student_data"] %}
                <tr>
                    <td>s['Student id']</td>
                    <td>s['Course id']</td>
                    <td>s['Marks']</td>
                </tr>
            {% end for %}    
            <tr>
                <td colspan="2"> Total Marks </td>
                <td> {{t1_data["total_marks"]}} </td>
            </tr>
        </table>
    </body>
 </html> 
"""
TEMPLATE_2 = """
<!DOCTYPE html>
<html>
    <head>
        <title> Course Data </title>
        <style>
            td{border:1px solid black;}
        </style>
    </head>  
    <body>
        <h1> Course Details </h1> 
        <table style="border:1px solid black;">
            <tr>
                <td> Average Marks </th>
                <td> Maximum Marks </th>
            </tr>
            <tr>
                <td>{{t2_data["average_mark"]}}</td>
                <td>{{t2_data["max_mark"]}}</td>
            </tr>
        </table>
        <img src="image.jpg">
    </body>
 </html> 
"""
TEMPLATE_3 = """
<!DOCTYPE html>
<html>
    <head>
        <title> Something Went Wrong </title>
    </head>  
    <body>
        <h1> Wrong Inputs </h1> 
        <h4> Something went wrong </h4>
    </body>
 </html> 
"""

if __name__=="__main__":
    
    first_parameter=sys.argv[1]
    second_parameter=sys.argv[2]
    data=pd.read_csv("data.csv")

    if first_parameter == "-s" and second_parameter in list(data["Student id"]):
        student_data=data[data["Student id"]==second_parameter]
        total_marks=data[data["Student id"]==second_parameter][" Marks"].sum()
        t1_data={"student_data":student_data,"total_marks":total_marks}
        template = Template(TEMPLATE_1)
        content=template.render(t1_data=t1_data)
        html_file=open('output.html','w')
        html_file.write(content)
        html_file.close()

    elif first_parameter == "-c" and second_parameter in list(data[" Course id"]):
        data=data[data[' Course id']==2001][" Marks"]
        average_mark=average(data)
        max_mark=max(data)
        t2_data={"average_mark":average_mark,"max_mark":max_mark}
        marks=list(data[data[" Course id"]==second_parameter][" Marks"])
        plt.hist(marks)
        plt.xlabel('Marks')
        plt.ylabel('Frequency')
        plt.savefig('image.jpg')
        template=Template(TEMPLATE_2)
        content=template.render(t2_data=t2_data)
        html_file=open('output.html','w')
        html_file.write(content)
        html_file.close()
    else:
        template = Template(TEMPLATE_3)
        content=template.render()
        my_html_document_file= open('output.html','w')
        my_html_document_file.write(content)
        my_html_document_file.close()







