from html.parser import HTMLParser
import codecs
from bs4 import BeautifulSoup
import os
import csv
rel_csv_path = input("Podaj nazwe pliku csv z kontaktami: \n")
script_dir = os.path.dirname(__file__)
rel_path = input("Podaj nazwe pliku html (template): \n")
abs_file_path = os.path.join(script_dir, rel_path)
abs_csv_file_path = os.path.join(script_dir, rel_csv_path)
f=codecs.open(abs_file_path, 'r',"utf-8")

document= BeautifulSoup(f.read(), "html.parser")
mydivs_name = document.find(class_="name")
mydivs_number = document.find(class_="number")
mydivs_mail = document.find(class_="mail")
mydivs_position = document.find(class_="position")

with open(abs_csv_file_path, newline='', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        mydivs_name.string = row[0] + " " + row[1]
        mydivs_mail.find('a')['href'] ="mailto:"+row[3]
        mydivs_number.find('a')['href'] ="tel:+48"+row[2]
        name = row[0] + " " + row[1]
        mydivs_number.find('a').string.replace_with(row[2])
        mydivs_mail.find('a').string.replace_with(row[3])
        mydivs_position.string = row[4]
        html = document.prettify("utf-8")
        filename = row[0] + "_" + row[1] + ".html"
        with open(filename, "wb") as file:
            file.write(html)
