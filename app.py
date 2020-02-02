from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/chat_room')
def chat_room():
    return render_template("chat_room.html")

if __name__ == "__main__":
    app.run(debug=True)
