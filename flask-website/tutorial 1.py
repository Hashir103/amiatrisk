from flask import Flask, redirect, url_for, render_template, request
import cohere
import json
co = cohere.Client('AnhwcBAs6bP9NTeUYvAfsI0eMNYTiykmbSVg8HKg')

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/", methods=["POST"])
def login():
    output = request.get_json()
    result = json.loads(output)
    getResponse(result)
    txt1 = "{response}".format(response=result)
    return render_template("index.html")

#@app.route("/<name>")
#def user(name):
#  txt="Hello {userName}!".format(userName=name)
#  return txt\
@app.route("/test", methods=["GET","POST"])
def getResponse():
  # response = ''
  input_json = ''
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
      input_json = request.json
      # return json
  else:
      return 'Content-Type not supported!'
  print(input_json)
  inputText = json.loads(json.dumps(input_json))["userInput"]

  if request.method == "GET":
    return "hello"
  if request.method == "POST":
    print("user_input", inputText)
    
    response = co.generate(
      model='command-xlarge-nightly',
      prompt= inputText,
      max_tokens=900,
      temperature=0.5,
      k=0,
      stop_sequences=[],
      return_likelihoods='GENERATION')
  print(response.generations[0].text)
  return response.generations[0].text

if __name__ == "__main__":
  app.run()