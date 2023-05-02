from flask import Flask, render_template
from players import players
app = Flask(__name__)    

@app.route('/')         
def hello_world():
    print(players)
    return render_template('index.html', players_for_jinja = players)  

## MORE ROUTES HERE 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__=="__main__": 
    app.run(debug=True)