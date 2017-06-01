from flask import Response
from flask import request, Flask, render_template, redirect
import shelve
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/home/yulia/PycharmProjects/untitled/json_repository-master/media'
app.config['UPLOAD_FOLDER'] = 'media'

DBNAME='shelve_lib'

def get_project_info():
    greeting_text = 'Hi, User! It\'s simple json repository based on Flask. Enjoy it'
    return render_template("index.html", text_block=greeting_text)

def get_storage_stat():
    if request.method == 'GET':
        with shelve.open(DBNAME) as db:
            return render_template('storage_stat.html', db=db)

def download_file(tag):
    #get file_content from request_obj
    if request.method == 'GET':
        filename = request.files['download.html']
        return filename
    if request.method=='POST':
        file=request.files['download_file']
        real_file=file.filename
        upload_data = {'filename': file.filename,
                      'real_file': real_file}

    filepath = os.path.join('media', real_file)
    file.save(filepath)


    filetag=request.form['tag']

    with shelve.open(DBNAME) as db:
        if filetag in db:
            db[tag] += upload_data
        else:
            db[tag] = upload_data

    return redirect('/storage/files/')


def upload_files(tag):
         with shelve.open(DBNAME) as db:
             tag_files = db.get('tag', [])
         return render_template('tag_list.html', filetag=tag_files, tag=tag)


def update_file(tag, filename):
    if request.method == 'GET':
        with shelve.open(DBNAME) as db:
            if tag in db:
                tag = False
            else:
                tag = tag
            file_name = False
            real_file = False

            for file in db[tag]:
                if file['filename'] == filename:

                    file_name = filename
                    real_file = file['real_file']
                    break

        return render_template('update_tag_list.html',
                               tag=tag, filename=file_name, realfile=real_file)
    elif request.method == 'POST':

        return redirect('/storage/stat/')

