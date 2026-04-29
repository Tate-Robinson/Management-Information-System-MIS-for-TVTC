from flask import Blueprint, request, redirect, url_for, render_template_string
from base_template import BASE_HTML

billing_bp = Blueprint(
    "billing_bp",
    __name__,
    template_folder="templates"
)

payments = []

statuses = [
    "Paid",
    "Unpaid",
    "Pending"
]


@billing_bp.route("/billing")
def billing_home():
    content = """
    <div class="card">
        <h1>Billing and Reports</h1>
        <p>Welcome to the Billing and Reports module.</p>

        <ul>
            <li><a href="/billing/add-payment">Add Payment</a></li>
            <li><a href="/billing/list">View Payments</a></li>
        </ul>

        <a href="/dashboard">Back to Dashboard</a>
    </div>
    """

    return render_template_string(BASE_HTML, title="Billing", content=content)


@billing_bp.route("/billing/add-payment", methods=["GET", "POST"])
def add_payment():
    if request.method == "POST":
        student_id = request.form.get("student_id")
        student_name = request.form.get("student_name")
        amount = request.form.get("amount")
        status = request.form.get("status")

        payments.append({
            "student_id": student_id,
            "student_name": student_name,
            "amount": amount,
            "status": status
        })

        return redirect(url_for("billing_bp.view_payments"))

    status_options = ""
    for status in statuses:
        status_options += f'<option value="{status}">{status}</option>'

    content = f"""
    <div class="card">
        <h1>Add Payment</h1>

        <form method="POST">
            <label>Student ID:</label><br>
            <input type="text" name="student_id" required><br><br>

            <label>Student Name:</label><br>
            <input type="text" name="student_name" required><br><br>

            <label>Amount:</label><br>
            <input type="number" name="amount" required><br><br>

            <label>Status:</label><br>
            <select name="status" required>
                {status_options}
            </select><br><br>

            <button type="submit">Add Payment</button>
        </form>

        <br>
        <a href="/billing">Back to Billing</a>
    </div>
    """

    return render_template_string(BASE_HTML, title="Add Payment", content=content)


@billing_bp.route("/billing/list")
def view_payments():
    rows = ""
    total = 0

    for payment in payments:
        total += float(payment["amount"])

        rows += f"""
        <tr>
            <td>{payment["student_id"]}</td>
            <td>{payment["student_name"]}</td>
            <td>${payment["amount"]}</td>
            <td>{payment["status"]}</td>
        </tr>
        """

    content = f"""
    <div class="card">
        <h1>Current Payments</h1>
        <p><b>Total:</b> ${total:.2f}</p>

        <table>
            <tr>
                <th>Student ID</th>
                <th>Student Name</th>
                <th>Amount</th>
                <th>Status</th>
            </tr>
            {rows}
        </table>

        <br>
        <a href="/billing/add-payment">Add Another Payment</a><br>
        <a href="/billing">Back to Billing</a>
    </div>
    """

    return render_template_string(BASE_HTML, title="Payments", content=content)