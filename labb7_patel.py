"""
Nihar patel
Feb 19 , 2026
lab 7 working with data in python
"""

print("\n ------ Examole 1 : readd file")
with open("phrasess.txt","r") as file1:
    filecontent = file1.read(30)
    print (filecontent)
    filecontent = file1.read(5)
    print (filecontent)

#check if the file is closed.
print(f"Is the file closed? {file1.closed}")

print("\n ------ Examole 2 : readline file")
with open("phrasess.txt","r") as file1:
    filecontent = file1.readline(30)
    print (filecontent)
    filecontent = file1.readline(5)
    print (filecontent)

print("\n ------ Examole 3 : readlines file")
#readlines make a list of all the lines in the text file. each line is hte item in the list
with open("phrasess.txt","r") as file1:
    filecontent = file1.readlines()
    print (filecontent)
    filecontent = file1.readlines(5)
    print (filecontent)

print("\n ------ Examole 4 : look each line in file")
with open("phrasess.txt","r") as file1:
    filecontent = file1.readlines()
    for eachline in filecontent:
        print(eachline.strip()) # strip() mehtod removes \n in each line

print("\n ------ Examole 5 : create file")
# w mode create a file if the file doesn't exist. on the other hand if the file exists, w mode will overwrite the data in the file
with open("Patel.txt", "w") as file: 
    file.write("python basics for data science\n")
    file.write("Nihar patel")

print("\n ------ Examole 6 : appeadn data into an existing file")
#append the date and item into "Patel.txt" file

from datetime import datetime

with open ("Patel.txt", "a") as file:
    file.write(f"\n last update: {datetime.now()}")

print("\n ------ Examole 7 : copy file")
#copy file "lastname.txt" into a new file
with open ("Patel.txt", "r") as readfile:
    with open("newfile.txt","w") as writefile:
        for eachline in readfile: 
            writefile.write(eachline)
        
print("\n---- Example 8: pandas file")
import pandas as pd

data ={
    'Name' : ['Alice', 'Bob', 'charlie'],
    'Age' : [25,30,35]
}
df = pd.DataFrame(data)
print(df)

print("\n---- Example 9: creating df with pandas from an excel file")
df = pd.read_excel("classdata.xlsx")
print(df)
print(df.head())

print ("\n ------- EXERCISE")


def email_read():
    gmail = 0
    yahoo = 0
    hotmail = 0

    try:
        # Read the email file
        with open("user_email.txt", "r") as file:
            for line in file:
                line = line.lower()  # make case-insensitive
                if "@gmail.com" in line:
                    gmail += 1
                elif "@yahoo.com" in line:
                    yahoo += 1
                elif "@hotmail.com" in line:
                    hotmail += 1

        with open("reportemail.txt", "w") as report:
            report.write(f"gmail = {gmail}\n")
            report.write(f"yahoo = {yahoo}\n")
            report.write(f"hotmail = {hotmail}\n")

        return gmail, yahoo, hotmail

    except FileNotFoundError:
        print("Error: user_email.txt file not found.")
    except Exception as e:
        print("An error occurred:", e)


email_read()
