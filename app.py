from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# Data storage file
DATA_FILE = 'students.json'

def load_students():
    """Load students from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_students(students):
    """Save students to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(students, f, indent=2)

@app.route('/')
def index():
    """Home page - Display all students"""
    students = load_students()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    """Add a new student"""
    if request.method == 'POST':
        students = load_students()
        
        new_student = {
            'id': len(students) + 1,
            'name': request.form['name'],
            'roll_number': request.form['roll_number'],
            'department': request.form['department'],
            'email': request.form['email'],
            'added_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        students.append(new_student)
        save_students(students)
        
        return redirect(url_for('index'))
    
    return render_template('add_student.html')

@app.route('/delete/<int:student_id>')
def delete_student(student_id):
    """Delete a student by ID"""
    students = load_students()
    students = [s for s in students if s['id'] != student_id]
    save_students(students)
    return redirect(url_for('index'))

@app.route('/api/students')
def api_students():
    """API endpoint to get all students"""
    students = load_students()
    return jsonify(students)

@app.route('/health')
def health():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'total_students': len(load_students())
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
