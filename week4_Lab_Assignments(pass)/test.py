from re import template
from numpy import average, maximum
import pandas as pd
from jinja2 import Template
from sklearn.utils import compute_class_weight
import matplotlib.pyplot as plt
# template="""
# <!DOCTYPE html>
# <html>

# <head>
#     <meta charset="UTF-8">
#     <title>Course Data</title>
# </head>

# <body>
#     <h1> Course Details </h1>
#     <table border="2" id="course-details-table">
#         <tr>
#             <td> Average Marks </td>
#             <td> Maximum Marks </td>
#         </tr>
#         <tr>    
#             <td> {{average_marks}} </td>
#             <td> {{maximum_marks}} </td>
#         </tr>
#     </table>  
#     <img src="static/image.png">
#     <a href="index.html"> Go Back </a>
# </body>

# </html>
# """

data=pd.read_csv("data.csv")
id_value=2001
data_list=data.values.tolist()
cource_mark_data=[]
for i in data_list:
    if i[1]==id_value:
        cource_mark_data.append(i[2])

print(cource_mark_data)
# total_marks=data[data["Student id"]==1001][" Marks"].sum()
average_marks=sum(cource_mark_data)/len(cource_mark_data)
maximum_marks=max(cource_mark_data)
print(maximum_marks,average_marks)
# result = Template(template)
# content=result.render(average_marks=average_marks,maximum_marks=maximum_marks)
# file=open("templates/cource.html","w")
# file.write(content)
# file.close()

plt.hist(cource_mark_data)
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.savefig('static/image.png')