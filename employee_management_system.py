class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee_id, name, position, salary):
        if employee_id not in self.employees:
            self.employees[employee_id] = {'name': name, 'position': position, 'salary': salary}
            print(f"Employee with ID {employee_id} added successfully.")
        else:
            print(f"Employee with ID {employee_id} already exists.")

    def display_employee(self, employee_id):
        if employee_id in self.employees:
            employee_info = self.employees[employee_id]
            print(f"Employee ID: {employee_id}")
            print(f"Name: {employee_info['name']}")
            print(f"Position: {employee_info['position']}")
            print(f"Salary: {employee_info['salary']}")
        else:
            print(f"Employee with ID {employee_id} not found.")

    def display_all_employees(self):
        if not self.employees:
            print("No employees in the system.")
        else:
            print("Employee List:")
            for employee_id, employee_info in self.employees.items():
                print(f"Employee ID: {employee_id}, Name: {employee_info['name']}, Position: {employee_info['position']}, Salary: {employee_info['salary']}")

    def remove_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            print(f"Employee with ID {employee_id} removed successfully.")
        else:
            print(f"Employee with ID {employee_id} not found.")

# Example Usage:
if __name__ == "__main__":
    ems = EmployeeManagementSystem()

    ems.add_employee(1, 'John Doe', 'Manager', 50000)
    ems.add_employee(2, 'Jane Doe', 'Developer', 40000)

    ems.display_all_employees()

    ems.display_employee(1)

    ems.remove_employee(2)

    ems.display_all_employees()
