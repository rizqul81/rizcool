from flask import Flask, render_template
import os
app = Flask(__name__)

# Route untuk halaman beranda
@app.route('/')
def home():
    return render_template('index.html')

# Route untuk halaman about me
@app.route('/about')
def about():
    return render_template('about.html')

# Route untuk halaman contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)