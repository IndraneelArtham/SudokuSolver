from flask import Flask, render_template, send_from_directory, url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from solvesudoku import Sudoku
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'asdf'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'uploads')

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)


class UploadForm(FlaskForm):
    photo = FileField(
        validators=[
            FileAllowed(photos, 'Only images are allowed'),
            FileRequired('File should not be empty')
        ]
    )
    submit = SubmitField('Upload')

@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = os.path.join("uploads", filename)
        print(file_url)
        solver = Sudoku(file_url)
        initial = solver.sudoku.tolist()
        # solver.solve_sudoku()
        # solution = solver.sudoku

        if initial is not None:
            return render_template('puzzle.html', file_url= f'uploads/{filename}', solution =initial)
        else:
            return "Failed to solve Sudoku puzzle"

    return render_template('index.html', form=form, file_url=None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
