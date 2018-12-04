from flask import Flask, render_template, redirect


app = Flask(__name__)

number = 0

@app.route('/')
@app.route('/request-counter')
def route_index():
    global number
    number += 1
    return render_template("main.html", number=number)

def route_counter():
    return redirect("main.html")


if __name__ == "__main__":
    app.run()
