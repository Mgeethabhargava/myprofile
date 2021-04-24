from flask import Flask,session,flash,render_template,redirect,session,url_for,request,send_from_directory,send_file
from uuid import uuid1

app = Flask(__name__)
app.secret_key = 'Alexas'



@app.route('/')
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)