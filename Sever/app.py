import flask
import werkzeug
import time
from flask import Flask, request, Response
import numpy as np
import cv2


app = flask.Flask(__name__)

# route http posts to this method
@app.route('/', methods=['GET','POST'])
def handle_request():         
    files_ids = list(flask.request.files)
    print("\nNumber of Received Images : ", len(files_ids))
    image_num = 1
    for file_id in files_ids:
        print("\nSaving Image ", str(image_num), "/", len(files_ids))
        imagefile = flask.request.files[file_id]
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        print("Image Filename : " + imagefile.filename)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        imagefile.save(timestr+'_'+filename)
        image_num = image_num + 1
    print("\n")
    return "Image(s) Uploaded Successfully. Come Back Soon."

# Use your ip address host = 'ipv4 address' or host = '0.0.0.0'
app.run(port=5000, host='192.168.43.124', debug=True)
