const employeeTable = document.getElementById('employeeTable');

// Function to populate the employee table with data
function populateEmployeeTable(data) {
    for (const employee of data) {
        const row = employeeTable.insertRow();
        const idCell = row.insertCell(0);
        const nameCell = row.insertCell(1);
        const lastNameCell = row.insertCell(2);

        idCell.innerText = employee.id;
        nameCell.innerText = employee.name;
        lastNameCell.innerText = employee.last_name;
    }
}

// Function to fetch employee data from the database
async function fetchEmployeeData() {
    try {
        const response = await fetch('/get_employee_data'); // Replace with the appropriate endpoint
        if (response.ok) {
            const data = await response.json();
            populateEmployeeTable(data);
        } else {
            console.error('Failed to fetch employee data.');
        }
    } catch (error) {
        console.error('An error occurred while fetching employee data:', error);
    }
}

// Populate the table with employee data from the database
fetchEmployeeData();

const employeeTable = document.getElementById('employeeTable');

// Function to fetch and display the employee report
async function fetchEmployeeReport() {
    try {
        const response = await fetch('/get_employee_report'); // Fetch report data from the server
        if (response.ok) {
            const reportData = await response.json();
            
            // Process and display the reportData as needed on your web page
            // Example: console.log(reportData);
        } else {
            console.error('Failed to fetch the employee report.');
        }
    } catch (error) {
        console.error('An error occurred while fetching the employee report:', error);
    }
}

// Fetch and display the employee report
fetchEmployeeReport();
