from flask import Flask, render_template, redirect, url_for, request
import face_recognition
import pandas as pd

app = Flask(__name__)

app.config['SECRET_KEY'] = "abc123hij456lmn789"


@app.route("/")
@app.route("/main")
def hello():
    return render_template('HomePage.html', title='Main')


@app.route("/markAttendance")
def MarkAtt():
    att =[]
    data = pd.read_csv("filename.csv")
    encodings = pd.read_csv("filename.csv")
    pict = request.form['Picture']
    image = face_recognition.load_image_file(pict)
    face = face_recognition.face_locations(image)
    for i in face:
        biden_encoding = face_recognition.face_encodings(i)
        for j in range(len(encodings['biden'])):
            if(face_recognition.compare_faces([biden_encoding], encodings[j])):
                att.append("Present")
            else:
                att.append("Absent")
    att2 = data + att
    att2.to_csv('filename.csv')


if __name__ == '__main__':
    app.run(debug=True)


