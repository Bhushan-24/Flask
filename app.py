import flask
from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def Sample():
    return render_template('index1.html')




if __name__=='__main__':
   app.run(debug=True)
