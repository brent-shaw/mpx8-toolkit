import json
from bs4 import BeautifulSoup

filename = "kit.xml"

obj = open(filename)

kit = BeautifulSoup(obj, features="xml")

print kit.findAll("pad")
