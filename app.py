from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    if request.method == 'POST':
        weight = request.form.get('weight')
        height = request.form.get('height')

        # Problem 1: No input validation
        # Problem 2: Division by zero risk
        # Problem 3: BMI formula error (height should be in meters squared)
        bmi = float(weight) / float(height)

    return render_template('index.html', bmi=bmi)

if __name__ == '__main__':
    # Problem 4: Debug mode should not be used in production
    app.run(debug=True)
