from flask import Blueprint

instructor_bp = Blueprint('instructor', __name__)

@instructor_bp.route('/courses')
def courses():
    return 'Courses page - add code here'