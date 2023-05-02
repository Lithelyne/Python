from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    # This checks if counter exist in the session, if it doesn't it sets to 0
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    # counter is my variable that I'm setting to session['counter'']
    return render_template('index.html', visits=session['counter'])


@app.route('/add_2', methods=['POST'])
def add_2():
    session['counter'] += 1
    return redirect('/')


@app.route('/destroy_session', methods=['POST'])
def destroy():
    session.clear()
    return redirect('/')

# MORE ROUTES HERE


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug pmode.
