from flask import *

app = Flask(__name__)
JOBS=[

  {
    'id': 1,
    'title':'Data Analyst',
    'location':'Dhaka',
    'salary':'BDT.15,000',
  },
  {
    'id': 2,
    'title':'CTO',
    'location':'Dhaka',
    'salary':'BDT.70,000',
  }
]
@app.route('/')
def hello_world():
  return render_template('home.html', jobs= JOBS)
@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)
if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)