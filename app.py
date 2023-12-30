from flask import Flask, render_template
from problemtwo import display_combinations
from problemthree import calculate_probability
from problemone import Total_Outcomes
app = Flask(__name__)

@app.route('/total_outcomes')
def Total_outcomes():
    ans=Total_Outcomes()
    return render_template('displayone.html',ans=ans)
@app.route('/display_combinations')
def display():
    dice_dict=display_combinations()
    return render_template('displaytwo.html', dice_dict=dice_dict)

@app.route('/display_probability')
def probability():
    probabilities = calculate_probability()
    return render_template('displaythree.html', probabilities=probabilities)

@app.route('/')
def index():
    return render_template('index.html')
     

if __name__ == '__main__':
    app.run(debug=True)