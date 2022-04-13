from flask import Flask, render_template, request, redirect, url_for
from BMI_calc import web_BMI_calc

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        weight_lb = request.form["weight_lb"]
        height_ft = request.form["height_ft"]
        height_in = request.form["height_in"]

        bmi, bmi_category = web_BMI_calc(weight_lb, height_ft, height_in)
        # return render_template("base.html")
        return redirect(url_for("bmi_result", BMI=bmi, BMI_Category=bmi_category))
    else:
        return render_template("base.html")

@app.route("/BMI_result/<BMI>/<BMI_Category>", methods=["POST", "GET"])
def bmi_result(BMI, BMI_Category):
    # BMI = request.args.get('BMI', None)
    # BMI_Category = request.args.get('BMI_Category', None)

    #if request.method == "GET":
    #    return render_template("base.html")
    #else:
    return render_template("BMI_result.html", BMI=BMI, BMI_Category=BMI_Category)

if __name__ == "__main__":
    app.run()
