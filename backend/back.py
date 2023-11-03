from flask import Flask, jsonify
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route('/get_employee_report', methods=['GET'])
def get_employee_report():
    # Connect to the SQLite database
    conn = sqlite3.connect('../employee_database.db')  # Replace with your database file

    # Query to retrieve employee attendance data
    query = """
    SELECT employees.id, employees.name, employees.last_name, attendance.date, attendance.status
    FROM employees
    JOIN attendance ON employees.id = attendance.employee_id;
    """

    # Fetch data from the database and load it into a DataFrame
    data = pd.read_sql_query(query, conn)

    # Close the database connection
    conn.close()

    # Generate a report using pandas
    report = data.groupby(['id', 'name', 'last_name', 'status']).size().unstack(fill_value=0)

    # Convert the report to JSON
    report_json = report.to_json()

    return jsonify(report_json)

if __name__ == '__main__':
    app.run(debug=True)
