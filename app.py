from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify
import json
import os.path
# from werkzeug.utils import secure_filename
import datetime
import os

app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=30)
# Set up this secret_key to be generated
app.secret_key = os.urandom(24)

print(__name__)


@app.route("/")
def home():
    if 'user1' in session:
        res = session['user1']
        return render_template('home.html', photos=res)
    else:
        return render_template('home.html')


@app.route("/uploaded-photo", methods=['GET', 'POST'])
def uploaded_photo():
    if request.method == 'POST':
        ct = datetime.datetime.now()
        print("current time:-", ct)
        # ts = ct.timestamp()

        photos = {}

        if os.path.exists('photos.json'):
            with open('photos.json') as photo_file:
                    photos = json.load(photo_file)

        # Secure the uploaded file
        f = request.files['photo']
        f_name = "user1_" + f.filename
        # f_name = secure_filename(f.filename) + ct
        f.save('C:/Users/Stella/PycharmProjects/dl-image-recognition/static/user_files/' + f_name)

        if 'user1' in photos.keys():

            # Add new photo under the user1
            photos['user1'].append({'photo': f_name, 'letter': request.form['letter'],
                                    'letterColor': request.form['letterColor']})
        else:
            # Create user1
            photos['user1'] = [{'photo': f_name, 'letter': request.form['letter'],
                                'letterColor': request.form['letterColor']}]

        with open('photos.json', 'w') as photo_file:
            json.dump(photos, photo_file)
            # Change this to timestamp later
            session['user1'] = photos['user1']
        return render_template('uploaded_photo.html', formData=request.form)

    else:
        return redirect(url_for('home'))


@app.route('/<string:photo>')
def redirect_to_url(photo):
    if os.path.exists('photos.json'):
        with open('photos.json') as photo_file:
            photos = json.load(photo_file)['user1']
            return render_template('home.html', photos=photos)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/api/user1/photos')
def fetch_all():
    res = session['user1']
    return jsonify(res)