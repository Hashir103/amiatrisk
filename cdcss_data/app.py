from flask import Flask, render_template, request, redirect, url_for
import cdcss_top_five_finder as cdcss

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/questionnaire", methods=["POST","GET"])
def question():
    if request.method == "POST":
        sex = request.form['sex']
        age = request.form['age']
        province = request.form['province']
        
        data = cdcss.getTopDiseases(str(province),str(sex),age)

        return render_template("result.html", data=data)

    else:
        return render_template("questionnaire.html")
    
# @app.route("/result", methods=["POST","GET"])
# def result():
#     if request.method == "POST":
#         race = request.form['race']
#         fam = request.form['fam']

@app.route("/diseases")
def diseases():
    return render_template("diseases.html")
        
@app.route("/applynow")
def applynow():
    return render_template("apply.html")

@app.route("/screening", methods=["POST","GET"])
def screening():
    if request.method == "POST":
        sex = request.form['sex']
        age = request.form['age']
        province = request.form['province']
        
        data = cdcss.getTopDiseases(province, sex, age)
        return render_template("screening_part2.html", data=data)
    else:
        return render_template("screening.html")

if __name__ == "__main__":
    app.run(debug=True)