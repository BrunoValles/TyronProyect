from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

# Function to retrieve and process employee data
def retrieve_employee_data():
    conn = sqlite3.connect('employee_database.db')  # Replace with the path to your database file
    query = "SELECT * FROM employees"
    employee_data = pd.read_sql_query(query, conn)
    conn.close()
    return employee_data

# Function to retrieve and process attendance data
def retrieve_attendance_data():
    conn = sqlite3.connect('employee_database.db')  # Replace with the path to your database file
    query = "SELECT * FROM attendance"
    attendance_data = pd.read_sql_query(query, conn)
    conn.close()
    return attendance_data

# Function to generate employee report in JSON format
def generate_employee_report():
    employee_data = retrieve_employee_data()
    return employee_data.to_json(orient='records')

# Function to generate attendance report in JSON format
def generate_attendance_report():
    attendance_data = retrieve_attendance_data()
    return attendance_data.to_json(orient='records')

@app.route('/get_employee_report', methods=['GET'])
def get_employee_report():
    employee_report = generate_employee_report()
    response = jsonify(json.loads(employee_report))
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:8000")
    return response

@app.route('/get_attendance_report', methods=['GET'])
def get_attendance_report():
    attendance_report = generate_attendance_report()
    response = jsonify(json.loads(attendance_report))
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:8000")
    return response 

if __name__ == '__main__':
    app.run(debug=True)
