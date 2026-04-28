from flask import Blueprint

student_bp = Blueprint('student', __name__)

@student_bp.route('/students')
def students():
    return 'Students page - add code here'