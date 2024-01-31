from flask import Flask, render_template,abort
from problemtwo import display_combinations
from problemthree import calculate_probability
from problemone import Total_Outcomes

app = Flask(__name__)

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error_code=404, error_message="Not Found"), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error_code=500, error_message="Internal Server Error"), 500

# Your existing routes
@app.route('/total_outcomes')
def Total_outcomes():
    try:
        ans = Total_Outcomes()
        return render_template('displayone.html', ans=ans)
    except Exception as e:
        # Log the exception if needed
        app.logger.error(f"An error occurred: {str(e)}")
        # Redirect to the error page with a 500 Internal Server Error
        abort(500)

@app.route('/display_combinations')
def display():
    try:
        dice_dict = display_combinations()
        return render_template('displaytwo.html', dice_dict=dice_dict)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        abort(500)

@app.route('/display_probability')
def probability():
    try:
        probabilities = calculate_probability()
        return render_template('displaythree.html', probabilities=probabilities)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        abort(500)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# app = Flask(__name__)

# @app.route('/total_outcomes')
# def Total_outcomes():
#     ans=Total_Outcomes()
#     return render_template('displayone.html',ans=ans)
# @app.route('/display_combinations')
# def display():
#     dice_dict=display_combinations()
#     return render_template('displaytwo.html', dice_dict=dice_dict)

# @app.route('/display_probability')
# def probability():
#     probabilities = calculate_probability()
#     return render_template('displaythree.html', probabilities=probabilities)

# @app.route('/')
# def index():
#     return render_template('index.html')
     

# if __name__ == '__main__':
#     app.run(debug=True)