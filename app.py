from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bloglist')
def contact():
    return render_template('bloglist.html')

@app.route('/introduction')
def explore():
    return render_template('blogs/introduction.html')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
