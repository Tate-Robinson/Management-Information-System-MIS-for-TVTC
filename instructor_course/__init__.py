from flask import Blueprint, request, redirect, url_for, render_template_string
from base_template import BASE_HTML

instructor_bp = Blueprint(
    "instructor_bp",
    __name__,
    template_folder="templates"
)

course_assignments = []

courses = [
    "CPR Certification",
    "First Aid Training",
    "Workplace Safety",
    "Medical Assistant Basic"
]


@instructor_bp.route("/courses")
def courses_home():
    content = """
    <div class="card">
        <h1>Instructor and Course Module</h1>
        <p>Welcome to the Instructor and Course module.</p>

        <ul>
            <li><a href="/courses/assign">Assign Instructor</a></li>
            <li><a href="/courses/list">View Course Assignments</a></li>
        </ul>

        <a href="/dashboard">Back to Dashboard</a>
    </div>
    """

    return render_template_string(BASE_HTML, title="Courses", content=content)


@instructor_bp.route("/courses/assign", methods=["GET", "POST"])
def assign_instructor():
    if request.method == "POST":
        course = request.form.get("course")
        instructor_name = request.form.get("instructor_name")
        room = request.form.get("room")
        meeting_time = request.form.get("meeting_time")

        course_assignments.append({
            "course": course,
            "instructor_name": instructor_name,
            "room": room,
            "meeting_time": meeting_time
        })

        return redirect(url_for("instructor_bp.view_course_assignments"))

    course_options = ""
    for course in courses:
        course_options += f'<option value="{course}">{course}</option>'

    content = f"""
    <div class="card">
        <h1>Assign Instructor</h1>

        <form method="POST">
            <label>Course:</label><br>
            <select name="course" required>
                {course_options}
            </select><br><br>

            <label>Instructor Name:</label><br>
            <input type="text" name="instructor_name" required><br><br>

            <label>Room:</label><br>
            <input type="text" name="room" required><br><br>

            <label>Meeting Time:</label><br>
            <input type="text" name="meeting_time" required><br><br>

            <button type="submit">Assign Instructor</button>
        </form>

        <br>
        <a href="/courses">Back to Courses</a>
    </div>
    """

    return render_template_string(BASE_HTML, title="Assign Instructor", content=content)


@instructor_bp.route("/courses/list")
def view_course_assignments():
    rows = ""

    for assignment in course_assignments:
        rows += f"""
        <tr>
            <td>{assignment["course"]}</td>
            <td>{assignment["instructor_name"]}</td>
            <td>{assignment["room"]}</td>
            <td>{assignment["meeting_time"]}</td>
        </tr>
        """

    content = f"""
    <div class="card">
        <h1>Current Course Assignments</h1>

        <table>
            <tr>
                <th>Course</th>
                <th>Instructor</th>
                <th>Room</th>
                <th>Meeting Time</th>
            </tr>
            {rows}
        </table>

        <br>
        <a href="/courses/assign">Assign Another Instructor</a><br>
        <a href="/courses">Back to Courses</a>
    </div>
    """

    return render_template_string(BASE_HTML, title="Course Assignments", content=content)