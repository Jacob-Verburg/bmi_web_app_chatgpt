from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    weight = float(request.form['weight'])
    height_feet = float(request.form['height_feet'])
    height_inches = float(request.form['height_inches'])
    height = (height_feet * 12 + height_inches) * 0.0254
    weight = weight * 0.453592  # convert pounds to kg
    bmi = weight / (height ** 2)
    return render_template('result.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)
