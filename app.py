from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Trang login
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Kiểm tra username, password đơn giản
        if username == "admin" and password == "123":
            return redirect(url_for("success"))
        else:
            return render_template("login.html", error="Sai tài khoản hoặc mật khẩu!")

    return render_template("login.html")

# Trang success
@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

