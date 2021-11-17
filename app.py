from flask import Flask, request, render_template
from os import listdir
import json
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True

STUDENTS_DIRECTORY = open("config.txt", 'r').read()


@app.route("/")
def main() -> str:
    return render_template("index.html")


@app.route("/search_result", methods=['POST'])
def search_result() -> str:
    indices = find_indices(str(request.form.get('search_word', '')))
    return render_template('index.html', students=[df.loc[index]['name'] for index in indices])


@app.route('/details/<name>')
def details(name) -> str:
    """
    :param name: name of student
    :return: html string displaying the details of the student
    """
    student = df[df['name'] == name].iloc[0].to_dict()
    student = {k: v for k, v in student.items() if v.__class__ == str}
    return render_template("details.html", student=student)


def find_indices(search_word: str) -> list:
    """
    :param search_word: string, which to look for in entire DataFrame
    """
    s = df.apply(lambda row: row.astype(str).str.contains(search_word).any(), axis=1)
    return s[s].index


def create_df(dir) -> pd.DataFrame:
    """
    :param dir: path where the student jsons can be found
    :return: pandas Dataframe with all the students information
    """
    students_jsons = listdir(dir)
    dicts = [json.load(open(dir + students_json)) for students_json in students_jsons]
    return pd.DataFrame(dicts)


df = create_df(STUDENTS_DIRECTORY)
