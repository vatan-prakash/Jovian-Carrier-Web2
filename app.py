from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS =[
  {
    'id':1,
    'title':'Data Scientist',
    'location': 'Benagaluru, India',
    'salary': 'Rs 10,00,000'
  },
  {
    'id':2,
    'title':'Full Stack Develoepr',
    'location': 'Benagaluru, India',
    'salary': 'Rs 19,00,000'
  },
  {
    'id':3,
    'title':'Frontend Developer',
    'location': 'Benagaluru, India',
    'salary': 'Rs 15,00,000'
  },
  {
    'id':4,
    'title':'UI & UX Designer',
    'location': 'Benagaluru, India',
   
  },
]

@app.route("/")
def hello_world():  
    return render_template('home.html', jobs=JOBS, company_name='Jovian')

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

# print(__name__)
if __name__ == '__main__':
    # print("yes")
  app.run(host='0.0.0.0', debug= True)