from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def homePage():
    return redirect(url_for('startPage'))
@app.route("/profile")
def startPage():
    return render_template('startPage.html')

if __name__ == "__main__":
    app.run()