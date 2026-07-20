from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        conn = sqlite3.connect("nagarseva.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:
            return redirect(url_for("dashboard"))
        else:
            return "Invalid Email or Password"

    return render_template("login.html")

# Register Page
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        print(request.form)

        fullname = request.form.get("fullname")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")

        
        
        conn = sqlite3.connect("nagarseva.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO users(fullname,email,phone,password)
            VALUES(?,?,?,?)
        """, (fullname, email, phone, password))

        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")
        
# Report Issue Page
@app.route("/report", methods=["GET", "POST"])
def report():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        issue = request.form.get("issue")
        location = request.form.get("location")
        description = request.form.get("description")

        # Get uploaded photo
        photo = request.files.get("photo")

        filename = ""

        if photo and photo.filename != "":
            filename = secure_filename(photo.filename)

            # Create folder if it doesn't exist
            os.makedirs(os.path.join("static", "uploads"), exist_ok=True)

            # Save image
            photo.save(os.path.join("static", "uploads", filename))

        conn = sqlite3.connect("nagarseva.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO complaints
            (name, email, issue_type, location, description, image)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, email, issue, location, description, filename))

        conn.commit()
        conn.close()

        return redirect(url_for("dashboard"))

    return render_template("report.html")

# Dashboard Page
@app.route("/dashboard")
def dashboard():

    conn = sqlite3.connect("nagarseva.db")
    cursor = conn.cursor()

    # Get all complaints
    cursor.execute("SELECT * FROM complaints")
    complaints = cursor.fetchall()

    # Total complaints
    cursor.execute("SELECT COUNT(*) FROM complaints")
    total = cursor.fetchone()[0]

    # Pending complaints
    cursor.execute("SELECT COUNT(*) FROM complaints WHERE status='Pending'")
    pending = cursor.fetchone()[0]

    # Resolved complaints
    cursor.execute("SELECT COUNT(*) FROM complaints WHERE status='Resolved'")
    resolved = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        complaints=complaints,
        total=total,
        pending=pending,
        resolved=resolved
    )

# Track Complaint Page
@app.route("/track", methods=["GET", "POST"])
def track():

    complaint = None

    if request.method == "POST":

        complaint_id = request.form.get("complaint_id")

        conn = sqlite3.connect("nagarseva.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM complaints WHERE id=?",
            (complaint_id,)
        )

        complaint = cursor.fetchone()

        conn.close()

    return render_template("track.html", complaint=complaint)

if __name__ == "__main__":
    app.run(debug=True)
