from flask import Flask,request ,render_template , jsonify

app= Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])
def math_ops():

    #print(str(request.form))

    if(request.method=='POST'):
        ops=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])

        if ops == 'add':
            r=num1+num2
            result="Addition of the "+str(num1)+" and "+str(num2)+" is "+str(r)

        if ops =='subtract':
            r=num1-num2
            result="Substraction of  "+str(num1)+"  and  "+str(num2)+"  is  "+str(r)

        if ops == 'multiply':
            r=num1*num2
            result="Multiplication of the  "+str(num1)+ " and " +str(num2)+" is "+str(r)

        if ops == 'divide':
            r=int(num1/num2)
            result=f"Division of the  {num1} and {num2} is {r}"
            

        return render_template('results.html', result_in_html=result)
    



if __name__=="__main__":
    app.run(host="0.0.0.0")
