from flask import Blueprint, request, redirect, url_for, render_template_string
from base_template import BASE_HTML

admin_bp = Blueprint(
    "admin_bp",
    __name__,
    template_folder="templates"
)

users = []

roles = [
    "Administrator",
    "Instructor",
    "Student",
    "Billing Staff"
]


@admin_bp.route("/admin")
def admin_home():
    content = """
    <div class="card">
        <h1>Admin Module</h1>
        <p>Welcome to the Admin module.</p>

        <ul>
            <li><a href="/admin/add-user">Add User</a></li>
            <li><a href="/admin/users">View Users</a></li>
        </ul>

        <a href="/dashboard">Back to Dashboard</a>
    </div>
    """

    return render_template_string(BASE_HTML, title="Admin", content=content)


@admin_bp.route("/admin/add-user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        username = request.form.get("username")
        full_name = request.form.get("full_name")
        role = request.form.get("role")
        status = request.form.get("status")

        users.append({
            "username": username,
            "full_name": full_name,
            "role": role,
            "status": status
        })

        return redirect(url_for("admin_bp.view_users"))

    role_options = ""
    for role in roles:
        role_options += f'<option value="{role}">{role}</option>'

    content = f"""
    <div class="card">
        <h1>Add User</h1>

        <form method="POST">
            <label>Username:</label><br>
            <input type="text" name="username" required><br><br>

            <label>Full Name:</label><br>
            <input type="text" name="full_name" required><br><br>

            <label>Role:</label><br>
            <select name="role" required>
                {role_options}
            </select><br><br>

            <label>Status:</label><br>
            <select name="status" required>
                <option value="Active">Active</option>
                <option value="Inactive">Inactive</option>
            </select><br><br>

            <button type="submit">Add User</button>
        </form>

        <br>
        <a href="/admin">Back to Admin</a>
    </div>
    """

    return render_template_string(BASE_HTML, title="Add User", content=content)


@admin_bp.route("/admin/users")
def view_users():
    rows = ""

    for user in users:
        rows += f"""
        <tr>
            <td>{user["username"]}</td>
            <td>{user["full_name"]}</td>
            <td>{user["role"]}</td>
            <td>{user["status"]}</td>
        </tr>
        """

    content = f"""
    <div class="card">
        <h1>Current Users</h1>

        <table>
            <tr>
                <th>Username</th>
                <th>Full Name</th>
                <th>Role</th>
                <th>Status</th>
            </tr>
            {rows}
        </table>

        <br>
        <a href="/admin/add-user">Add Another User</a><br>
        <a href="/admin">Back to Admin</a>
    </div>
    """

    return render_template_string(BASE_HTML, title="Users", content=content)