from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)


JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bulawayo, Zimbabwe',
        'salary': '$1500',
    },
    {
        'id': 2,
        'title': 'Front End Developer',
        'location': 'Harare, Zimbabwe',
        'salary': '$1000',
    },
    {
        'id': 3,
        'title': 'Back End Developer',
        'location': 'Bulawayo, Zimbabwe',
        'salary': '$1300',
    },
    {
        'id': 4,
        'title': 'Data Scientist',
        'location': 'Mutare, Zimbabwe',
        'salary': '$2000',
    }
]

@app.route('/')
def index():
    return render_template('home.html', jobs=JOBS, company_name='Nando')

@app.route('/jobs', strict_slashes=False)
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(debug=True)