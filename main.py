from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def receive_data():
    names = request.form['username']
    password = request.form.get('password')
    message = request.form['message']
    return f"<h1>{names} {password} {message}</h1>"






if __name__ == "__main__":
    app.run(debug=True)

