from flask import Flask, render_template, request, redirect, url_for
import cdcss_top_five_finder as cdcss
import json
import cohere
co= cohere.Client('AnhwcBAs6bP9NTeUYvAfsI0eMNYTiykmbSVg8HKg')
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

@app.route('/diseases')
def diseasePage():
    return render_template("diseases.html")

@app.route("/", methods=["POST"])
def diseases():
    output = request.get_json()
    result = json.loads(output)
    getResponse(result)
    txt1 = "{response}".format(response=result)
    return render_template("diseases.html")

@app.route("/test", methods=["POST", "GET"])
def getResponse():
  # response = ''
  input_json = ''
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
      input_json = request.json
      # return json
  else:
      return 'Content-Type not supported!'
  inputText = json.loads(json.dumps(input_json))["userInput"]

  if request.method == "GET":
    return "hello"
  if request.method == "POST":
    response = co.generate(
      model='command-xlarge-nightly',
      prompt= inputText,
      max_tokens=900,
      temperature=0.5,
      k=0,
      stop_sequences=[],
      return_likelihoods='GENERATION')
  return response.generations[0].text
        
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