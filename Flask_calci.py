from flask import Flask,render_template,redirect,request
import os
import numpy as np

app=Flask(__name__)
@app.route("/",methods=["GET"])
def home_page():
    return render_template("index.html")

@app.route("/maths",methods=["POST"])
def maths_operations():
    if request.method=="POST":
        operations=request.form["operation"]
        num1=int(request.form["num1"])
        num2=int(request.form["num2"])
        
        if (operations=="add"):
            add=num1+num2
            result= f"The sum of {num1} and {num2} is {add}"
        if (operations=="multiply"):
            mul=num1*num2
            result= f"The multiple of {num1} and {num2} is {mul}"
        if (operations=="subtract"):
            sub=num1-num2
            result= f"The substraction of {num1} and {num2} is {sub}"
        if (operations=="divide"):
            div=num1/num2
            result= f"The division of {num1} and {num2} is {div}"
        if (operations=="log"):
            log1=np.log(num1)
            log2=np.log(num2)
            logg=log1+log2
            result=f"The log of {num1} and {num2} is {logg}"
        if (operations=="sqrt"):
            sqrt1=np.sqrt(num1)
            sqrt2=np.sqrt(num2)
            sqr=sqrt1+sqrt2
            result=f"The Square root of {num1} and {num2} is {sqr}"
        if (operations=="cbrt"):
            cbrt1=np.cbrt(num1)
            cbrt2=np.cbrt(num2)
            cbr=cbrt1+cbrt2
            result=f"The Square root of {num1} and {num2} is {cbr}"
        return render_template("result.html",result=result)

port=os.getenv("PORT",5000)
        
if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0",port=port)
