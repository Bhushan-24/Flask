import flask
from flask import Flask,url_for,request,render_template
app=Flask(__name__)
@app.route('/')
def link_tag():
    return render_template('link.html')


if __name__=='__main__':
   app.run(debug=True)
    
