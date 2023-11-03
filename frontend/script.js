function fetchAndDisplayData(endpoint, containerId) {
    fetch(endpoint)
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById(containerId);
            const table = container.querySelector("table");
            const tbody = container.querySelector("tbody");
            tbody.innerHTML = "";

            if (data && data.length > 0) {
                // Create table header based on the first data item
                const tableHeader = document.createElement("tr");
                for (const key in data[0]) {
                    const th = document.createElement("th");
                    th.textContent = key;
                    tableHeader.appendChild(th);
                }
                tbody.appendChild(tableHeader);

                // Populate the table with data
                data.forEach(item => {
                    const row = document.createElement("tr");
                    for (const key in item) {
                        const cell = document.createElement("td");
                        cell.textContent = item[key];
                        row.appendChild(cell);
                    }
                    tbody.appendChild(row);
                });
            } else {
                tbody.innerHTML = "<tr><td colspan='3'>No data available</td></tr>";
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Fetch and display employee report
fetchAndDisplayData('http://localhost:5000/get_employee_report', 'employee-report');

// Fetch and display attendance report
fetchAndDisplayData('http://localhost:5000/get_attendance_report', 'attendance-report');
