from flask import Flask, render_template, request, current_app
import requests
import random
import os


app = Flask(__name__)


def save_photo(photo, userid):
    _, file_extention = os.path.splitext(photo.filename)
    photo_name = str(userid)+file_extention
    file_path = os.path.join(current_app.root_path,
                             'static/uploads/photo', photo_name)
    photo.save(file_path)
    return photo_name


def save_college_id(photo, userid):
    _, file_extention = os.path.splitext(photo.filename)
    photo_name = str(userid)+file_extention
    file_path = os.path.join(current_app.root_path,
                             'static/uploads/college_id', photo_name)
    photo.save(file_path)
    return photo_name


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template("register.html")

    if request.method == 'POST':
        o_event = ""
        name = request.form['name']
        userid = random.randint(10000, 90000)
        mobile = request.form['mobile']
        email = request.form['email']
        gender = request.form['gender']
        dtype = request.form['dtype']
        dob = request.form['dob']
        stream = request.form['stream']
        course = request.form['course']
        institute = request.form['institute']
        c_event = request.form['c_event']
        o_event = request.form['o_event']
        photo = request.files['photo']
        college_id = request.files['college_id']

        url = 'http://alupdduc.in/api/registerapi.php'

        data = {
            "name": name,
            "userid": userid,
            "mobile": mobile,
            "email": email,
            "dob": dob,
            "gender": gender,
            "stream": stream,
            "course": course,
            "dtype": dtype,
            "institute": institute,
            "c_event": c_event,
            "o_event": o_event,
            "photo": photo.filename,
            "college_id": college_id.filename
        }
        # print(data)
        # print(o_event)
        if len(mobile) == 10:
            res = requests.post(url, data=data)
            response = res.json()
            print(response)

            if response['status']:
                print(save_photo(photo, userid))
                print(save_college_id(college_id, userid))
                return "<script>alert('You have successfully registered !');window.location = '/';</script>"
            else:
                return "<script>alert('This mobile number already registered !');window.location = '/';</script>"
            return render_template("register.html")
        else:
            return "<script>alert('Enter 10 digit mobile number !');window.location = '/';</script>"


@app.route('/file_list', methods=['POST', 'GET'])
def file_list():
    photo = os.path.join('static/uploads', 'photo')
    college_id = os.path.join('static/uploads', 'college_id')
    photos = os.listdir(photo)
    college_ids = os.listdir(college_id)
    return render_template('files.html', photos=photos, college_ids=college_ids)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
