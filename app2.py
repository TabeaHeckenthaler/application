from flask import Flask, request, render_template
from os import listdir
import json
import pandas as pd
import markdown

app = Flask(__name__)
app.config["DEBUG"] = True

STUDENTS_DIRECTORY = open("config.txt", 'r').read()


@app.route("/")
def main():
    # df = create_df(STUDENTS_DIRECTORY)
    # index = find_indices()
    # mark_string = single_student(df.loc[index])
    return render_template("index.html")


@app.route("/echo", methods=['POST'])
def echo():
    return render_template('index.html', text=request.form.get('text', ''))


def find_indices():
    return 17


def single_student(serie):
    """
    :return: markdown string for a series of a student.
    """
    return '[' + serie['name'] + "](" + serie['exercism_profile'] + ")"


def create_df(dir):
    students_jsons = listdir(dir)
    dicts = [json.load(open(dir + students_json)) for students_json in students_jsons]
    return pd.DataFrame(dicts)


if __name__ == '__main__':
    print(main())
