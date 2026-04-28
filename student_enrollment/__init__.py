from flask import Blueprint, request, redirect, url_for

student_bp = Blueprint(
    "student_bp",
    __name__,
    template_folder="templates"
)

enrollments = []

courses = [
    "CPR Certification",
    "First Aid Training",
    "Workplace Safety",
    "Medical Assistant Basic"
]

@student_bp.route("/student-enrollment")
def bp_home():
    return """
    <h1>Student Enrollment</h1>
    <p>Welcome to the Student Enrollment module.</p>

    <ul>
        <li><a href="/student-enrollment/enroll">Enroll Student</a></li>
        <li><a href="/student-enrollment/list">View Enrollments</a></li>
    </ul>

    <a href="/dashboard">Back to Dashboard</a>
    """

@student_bp.route("/student-enrollment/enroll", methods=["GET", "POST"])
def enroll_student():
    if request.method == "POST":
        student_id = request.form.get("student_id")
        student_name = request.form.get("student_name")
        course = request.form.get("course")
        enrollment_date = request.form.get("enrollment_date")

        enrollments.append({
            "student_id": student_id,
            "student_name": student_name,
            "course": course,
            "enrollment_date": enrollment_date
        })

        return redirect(url_for("student_bp.view_enrollments"))

    course_options = ""
    for course in courses:
        course_options += f'<option value="{course}">{course}</option>'

    return f"""
    <h1>Enroll Student</h1>

    <form method="POST">
        <label>Student ID:</label><br>
        <input type="text" name="student_id" required><br><br>

        <label>Student Name:</label><br>
        <input type="text" name="student_name" required><br><br>

        <label>Course:</label><br>
        <select name="course" required>
            {course_options}
        </select><br><br>

        <label>Enrollment Date:</label><br>
        <input type="date" name="enrollment_date" required><br><br>

        <button type="submit">Enroll Student</button>
    </form>

    <br>
    <a href="/student-enrollment">Back to Student Enrollment</a>
    """

@student_bp.route("/student-enrollment/list")
def view_enrollments():
    rows = ""

    for enrollment in enrollments:
        rows += f"""
        <tr>
            <td>{enrollment["student_id"]}</td>
            <td>{enrollment["student_name"]}</td>
            <td>{enrollment["course"]}</td>
            <td>{enrollment["enrollment_date"]}</td>
        </tr>
        """

    return f"""
    <h1>Current Student Enrollments</h1>

    <table border="1" cellpadding="8">
        <tr>
            <th>Student ID</th>
            <th>Student Name</th>
            <th>Course</th>
            <th>Enrollment Date</th>
        </tr>
        {rows}
    </table>

    <br>
    <a href="/student-enrollment/enroll">Enroll Another Student</a><br>
    <a href="/student-enrollment">Back to Student Enrollment</a>
    """
