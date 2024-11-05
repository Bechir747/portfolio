from flask import Flask, render_template

app = Flask(__name__)


data = {
    "Programming Languages": [("Java", 90), ("JavaScript", 75), ("Python", 75), ("C++", 80)],
    "Front-end Frameworks": [("React", 45), ("Angular", 85)],
    "Back-end Frameworks": [("Spring Boot", 45), ("Express.js", 85), ("Flask", 75)],
    "Databases": [("MySQL", 70), ("PostgreSQL", 85), ("MongoDB", 44)],
    "Containerization": [("Docker", 72), ("Kubernetes", 57)]
}

education = {

}



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/skills")
def skills():
    return render_template("skills.html", style = "skills", data = data)

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")




if __name__ == "__main__":
    app.run(debug=True)