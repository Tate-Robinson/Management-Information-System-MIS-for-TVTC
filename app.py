from flask import Flask, render_template_string, request, redirect, url_for, session
from admin_integration import admin_bp
from student_enrollment import student_bp
from billing_reports import billing_bp
from instructor_course import instructor_bp

app = Flask(__name__)
app.secret_key = 'tvtcmisproject'

# registering everyones modules
app.register_blueprint(admin_bp)
app.register_blueprint(student_bp)
app.register_blueprint(billing_bp)
app.register_blueprint(instructor_bp)
from base_template import BASE_HTML

# hardcoded users for now, can be swapped out for a database later
USERS = {
    'admin': {'password': 'admin123', 'role': 'Administrator'},
    'instructor': {'password': 'teach123', 'role': 'Instructor'},
    'student': {'password': 'learn123', 'role': 'Student'}
}


@app.route('/', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = USERS.get(username)
        if user and user['password'] == password:
            session['user'] = username
            session['role'] = user['role']
            return redirect(url_for('dashboard'))
        error = 'Invalid login credentials.'
    content = f'''
    <div class="card" style="max-width:420px;margin:auto;">
      <h2>TVTC MIS Login</h2>
      <p class="small">Use admin / admin123</p>
      <form method="post">
        <input name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
      </form>
      <p class="error">{error}</p>
    </div>
    '''
    return render_template_string(BASE_HTML, title='Login', content=content)


@app.route('/dashboard')
def dashboard():
    # redirect to login if not logged in
    if not session.get('user'):
        return redirect(url_for('login'))
    content = f'''
    <div class="card">
      <h2>Welcome, {session['user'].title()}</h2>
      <p>Role: {session['role']}</p>
    </div>
    <div class="grid">
      <div class="card"><div class="metric">142</div><div class="small">Students</div></div>
      <div class="card"><div class="metric">12</div><div class="small">Instructors</div></div>
      <div class="card"><div class="metric">18</div><div class="small">Active Courses</div></div>
      <div class="card"><div class="metric">$24,500</div><div class="small">Revenue</div></div>
    </div>
    '''
    return render_template_string(BASE_HTML, title='Dashboard', content=content)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)