"""
Programer: Saurav Pokharel
Date: 11/07/2024
Description: Webpage. 
"""

import webbrowser #importing the webbrowser module 
 
filename = input("Enter the file name you would like to use (add .html at end of file name): ") #get the filename from the user

topic = input("Enter your topic name: ") #get the topic of the page from the user 
paragraph = input("Enter a paragraph about the topic: ") #get the paragraph text from the user 
list_items = input("Enter three ways to use the topic (separate by a comma): ").split(',') #get the list items from the user and split them by comma 

#creating html content
html_template = f""" 
<!DOCTYPE html> 
<html>
    <head> <title>{topic}</title> </head>
    <body> 
        <h1>{topic}</h1> 
        <p>{paragraph}</p> 
        <ul> """ 
#adding each item to list to html content
for item in list_items: 
    html_template += f" <li>{item.strip()}</li>" 
html_template += """            
        </ul> 
    </body> 
</html> """     #closing list and body tags

file = open(filename, 'w') 
file.write(html_template) #writing the content to file
file.close() #closing the file