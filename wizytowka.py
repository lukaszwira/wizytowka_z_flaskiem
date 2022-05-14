from flask import Flask, request, redirect, render_template
app = Flask(__name__)

@app.route('/mypage/me')
def me():
    return render_template("wizytowka.html")

@app.route('/mypage/contact', methods=['GET'])
def contact():
    print(request)
    return render_template("wizytowka2.html")
