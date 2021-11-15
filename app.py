from flask import Flask
from os import listdir, getcwd
import json
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True

STUDENTS_DIRECTORY = getcwd() + '\\students\\students\\'


@app.route("/")
def main():
    return list_students()


def list_students():
    """
    Assignment1: list of students
    :return: str with list of students
    """
    students_jsons = listdir(STUDENTS_DIRECTORY)
    dicts = [json.load(open(STUDENTS_DIRECTORY + students_json)) for students_json in students_jsons]
    df = pd.DataFrame(dicts)
    return str(df['name'])

list_students()