from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "levidove_secret_key"

@app.route('/')
def home():
    return render_template('index.html', title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="About Us")

@app.route('/services')
def services():
    return render_template('services.html', title="Our Services")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # You can later send this data via email or store it in a DB
        print(f"📩 Message from {name} ({email}): {message}")

        flash("Your message has been sent successfully!", "success")
        return redirect(url_for('contact'))

    return render_template('contact.html', title="Contact Us")

if __name__ == '__main__':
    app.run(debug=True)
