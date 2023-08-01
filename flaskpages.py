from flask import Flask,request ,render_template , jsonify

app= Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home_page():
    return render_template('index.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")
