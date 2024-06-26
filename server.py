from flask import Flask, request, render_template
from datas import get_data

app = Flask(__name__,template_folder='templates')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/datas', methods=["POST"])
def get_email():
    email = request.form.get('email').strip()
    email_data = get_data(email)

    if "@" not in email:
        return render_template("error.html", email = email_data['email'])
    
    if email_data['is_valid_format']['text'] == 'TRUE':
        validity = "VALID"
    else:
        validity = "NOT valid"
    
    return render_template("result.html", email = email_data['email'], score = email_data['quality_score'], validity = validity)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

