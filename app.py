from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['GET',  'POST'])
def upload():
    if request.method == 'POST':
        name = request.form['name']
    
    return render_template('img.html', name= name)
    
    
if __name__ == '__main__':
    app.run(debug=True)