import flask
from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def Img_tag():
   return render_template('Img.html')





if __name__=='__main__':
   app.run(debug=True)
   
