from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def homepage():
    global wordlist
    if request.method == "POST":
        wordlist = request.form['wordlist']

        with open("uzbekwordlists.txt", "r") as f:
            existing_words = [line.strip() for line in f]

        if wordlist not in existing_words:
            with open("uzbekwordlists.txt", "a") as f:
                f.write(wordlist + "\n")
            return render_template("index.html", message="Wordlist qo'shildi")
        else:
            return render_template("index.html", message="Bu wordlist mavjud")

    return render_template("index.html", message="")

@app.route("/uzwordlists")
def uzwordlists():
    return send_file("uzbekwordlists.txt")

@app.route("/uzwordlistsdownload")
def uzwordlistsdownload():
    return send_file("uzbekwordlists.txt", as_attachment=True)

app.run(debug=True)