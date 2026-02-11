from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import initialize_db, User, Class, Student, Attendance
from peewee import IntegrityError

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]
        user = User.get_or_none(User.login == login, User.password == password)
        if user:
            session["user_id"] = user.id_user
            session["user_name"] = user.name
            return redirect(url_for("admin" if user.id_user == 1 else "teacher"))
        else:
            flash("Invalid login or password")
            return redirect(url_for("login"))
    return render_template("Login_page.html")

@app.route("/admin")
def admin():
    if session.get("user_id") != 1:
        flash("You cannot access this page.")
        return redirect(url_for("login"))

    teachers = User.select().where(User.id_user != 1)
    classes = Class.select()
    students = Student.select()

    return render_template("Admin_page.html", teachers=teachers, classes=classes, students=students)

@app.route("/add_prof", methods=["POST"])
def add_prof():
    if session.get("user_id") != 1:
        flash("Access denied.")
        return redirect(url_for("login"))

    prof_name = request.form.get("prof_name")
    prof_login = request.form.get("prof_login")
    prof_password = request.form.get("prof_password")

    if prof_name and prof_login and prof_password:
        try:
            User.create(
                name=prof_name, 
                login=prof_login, 
                password=prof_password
                )
            flash("Professor registered successfully!", "success")
        except IntegrityError:
            flash("Error: Login already exists.", "error")
        except Exception as e:
            print(f"Error registering professor: {e}", "error")
            flash("Error registering professor.", "error")

    return redirect(url_for("admin"))

@app.route("/add_student", methods=["POST"])
def add_student():
    if session.get("user_id") != 1:
        flash("Access denied.")
        return redirect(url_for("login"))
    
    student_name = request.form.get("student_name")
    student_email = request.form.get("student_email")
    student_phone = request.form.get("student_phone")
    student_birthdate = request.form.get("student_birthdate")
    class_ids = request.form.getlist("class_ids")

    if student_name and student_email and student_phone and student_birthdate:
        try:
            student = Student.create(
                name=student_name,
                email=student_email,
                phone=student_phone,
                birthdate=student_birthdate
            )

            for class_id in class_ids:
                Attendance.create(
                    id_class=class_id,
                    id_student=student.id_student,
                    attend=False
                )

            flash("Student registered successfully!", "success")
        except IntegrityError:
            flash("Error: Email already exists or student already enrolled in this class.", "error")
        except Exception as e:
            print(f"Error registering student: {e}", "error")
            flash("Error registering student.", "error")

    return redirect(url_for("admin"))

@app.route("/add_class", methods=["POST"])
def add_class():
    if session.get("user_id") != 1:
        flash("Access denied.")
        return redirect(url_for("login"))
    
    class_name = request.form.get("class_name")
    teacher_login = request.form.get("teacher_login")
    class_date = request.form.get("class_date")
    class_time = request.form.get("class_time")

    teacher = User.get_or_none(User.login == teacher_login)
    if class_name and teacher and class_date and class_time:
        try:
            Class.create(
                class_name=class_name, 
                id_user=teacher, 
                date=class_date, 
                time=class_time
                )
            flash("Class registered successfully!", "success")
        except IntegrityError:
            flash("Error: Class already exists or teacher does not exist.", "error")
        except Exception as e:
            print(f"Error registering class: {e}","error")
            flash("Error registering class.","error")
            
    return redirect(url_for("admin"))

@app.route("/teacher")
def teacher():
    if not session.get("user_id") or session.get("user_id") == 1:
        flash("You cannot access this page.")
        return redirect(url_for("login"))

    user = User.get_by_id(session.get("user_id"))
    classes = Class.select().where(Class.id_user == user.id_user)

    class_id = request.args.get("class_id")
    if class_id:
        students = Student.select().join(Attendance).where(Attendance.id_class == class_id).distinct()
    else:
        students = []

    return render_template(
        "Teacher_page.html",
        classes=classes,
        students=students,
        selected_class_id=class_id
    )

@app.route("/mark_attendance", methods=["POST"])
def mark_attendance():
    if not session.get("user_id") or session.get("user_id") == 1:
        flash("You cannot access this page.")
        return redirect(url_for("login"))

    class_id = request.form.get("class_id")
    if not class_id:
        flash("Class not selected.")
        return redirect(url_for("teacher"))

    students = Student.select().join(Attendance).where(Attendance.id_class == class_id)

    for student in students:
        checkbox_name = f"attendance_{student.id_student}"
        is_present = checkbox_name in request.form

        attendance, created = Attendance.get_or_create(
            id_class=class_id,
            id_student=student.id_student,
            defaults={'attend': is_present}
        )

        if not created:
            attendance.attend = is_present
            attendance.save()

    flash("Attendance marked successfully.")
    return redirect(url_for("teacher", class_id=class_id))

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out. Session ended.")
    return redirect(url_for("login"))

if __name__ == "__main__":
    initialize_db()

    if not User.select().where(User.login == "admin@novaims.unl.pt").exists():
        User.create(name="Admin", login="admin@novaims.unl.pt", password="adminims")

    app.run(debug=True)