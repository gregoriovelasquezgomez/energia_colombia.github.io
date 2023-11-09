from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,4),
        (7,3),
        (8,2),
        (9,5),
        
    ]
    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("home.html", labels=labels, values=values)


if __name__ == "__main__":
    app.run(debug=True)