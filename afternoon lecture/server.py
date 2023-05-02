from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "any string you want"

languages = ["python", "java", "c", "javascript", "ruby"]


@app.route('/')
def index():
    return render_template('index.html',
                           languages=languages)


@app.route('/handle_form', methods=['POST'])
def create():
    print(request.form)
    session['name'] = request.form['name']
    session['language'] = request.form['language']
    return redirect('/show')


@app.route('/show')
def another():
    return render_template('show.html')


# MORE ROUTES HERE


if __name__ == "__main__":
    app.run(debug=True)
