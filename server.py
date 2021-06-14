from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    fname_from_form = request.form['fname']
    lname_from_form = request.form['lname']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    return render_template("show.html", fname_on_template=fname_from_form, lname_on_template=lname_from_form, location_on_template=location_from_form, language_on_template=language_from_form)

if __name__ == "__main__":
    app.run(debug=True)