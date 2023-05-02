from flask_app import app, render_template

@app.route("/dashboard")
def dashbaord():
    return render_template('dashboard.html')