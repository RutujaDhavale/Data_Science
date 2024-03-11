from flask import Flask, redirect, render_template, request, jsonify, url_for
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/match', methods=['POST'])
def match():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = [match.group(0) for match in re.finditer(regex_pattern, test_string)]
    count = len(matches)
    return redirect(url_for('result', count=count, matches=matches, test_string=test_string, regex_pattern=regex_pattern))


@app.route('/result')
def result():
    count = request.args.get('count')
    matches = request.args.getlist('matches')
    test_string = request.args.get('test_string')
    regex_pattern = request.args.get('regex_pattern')
    return render_template('result.html', count=count, matches=matches, test_string=test_string, regex_pattern=regex_pattern)



@app.route('/validate-email', methods=['POST'])
def validate_email():
    email = request.form['email']
    is_valid = bool(re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email))
    return jsonify({'valid': is_valid})




if __name__ == '__main__':
     app.run(debug=True,host='0.0.0.0',port=5000)
