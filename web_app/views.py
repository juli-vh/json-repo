from flask import Response
from flask import request, Flask, render_template, redirect
import shelve
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/home/yulia/PycharmProjects/untitled/json_repository-master/media'
app.config['UPLOAD_FOLDER'] = 'media'

DBNAME='shelve_lib'

def get_project_info():
    response_text = "<b>Hi. It's simple json repository based on Flask. Enjoy it.</b>"
    return Response(response=response_text,
                    status=200)


def get_storage_stat():
    return Response(response=[{'<path_to_file>:<tag>'}],
                    status=200,
                    mimetype="application/json")


def download_file(tag):
    #get file_content from request_obj
    if request.method == 'GET':
        filename = request.files['file_1.html']
        return filename
    if request.method=='POST':
        file=request.files['download_file']
        real_file=file.filename
        upload_data = {'filename': file.filename,
                      'real_file': real_file}

    filepath = os.path.join('media', real_file)
    file.save(filepath)

    filetag=request.form['filetag']
    with shelve.open(DBNAME) as db:
        if filetag in db:
            db[filetag] += upload_data
        else:
            db[filetag] = upload_data

    return redirect('/storage/files/')


def upload_files(tag):
         with shelve.open(DBNAME) as db:
             tag_files = db.get('filetag', [])
         return render_template('tag_list.html', filetag=tag_files)


def update_file(tag):
    #get file_content from request_obj
    return Response(response="should update file by specific tag")
