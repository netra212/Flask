from flask import Flask, render_template

'''
 It creates an instance of the Flask class, 
 which will be our WSGI (Web Server Gateway Interface) application.
'''
### WSGI Application
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True, port=5002)
