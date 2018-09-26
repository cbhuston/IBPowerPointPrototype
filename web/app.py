import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/tombstone/api/v1.0/upload', methods=['POST'])
def upload_data():
    # check if the post request has the file part
  if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      print(f.filename)
      return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)