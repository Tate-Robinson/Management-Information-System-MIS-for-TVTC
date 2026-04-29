BASE_HTML = '''
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ title }}</title>
<link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
{% if session.get('user') %}
<nav>
  <a href="/dashboard">Dashboard</a>
  <a href="/student-enrollment">Students</a>
  <a href="/courses">Courses</a>
  <a href="/billing">Billing</a>
  <a href="/admin">Admin</a>
  <a href="/logout">Logout</a>
</nav>
{% endif %}
<div class="container">{{ content|safe }}</div>
</body>
</html>
'''