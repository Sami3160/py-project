# Library Management System

This is a Python-based Library Management System that allows you to manage a library's administrative and customer-related tasks. The system is built using Python, MySQL, and utilizes various Python libraries for enhanced functionality.
Installation

To run this application, you need to install some Python libraries and set up the MySQL database. Follow these steps to get started:
1. Install Required Python Libraries

Make sure you have Python installed. You can download it from Python's official website.

Next, install the required Python libraries using pip:

    pip install mysql-connector-python rich prettytable

2. Set Up the MySQL Database

You need a MySQL database to run this system. You can set up a local MySQL server or use a cloud-based solution. You will also need to import the provided SQL files to set up the database schema.

Create a MySQL database named "library."

* Import the following SQL files to create tables and populate initial data:
  * books_details.sql: Contains all books details.
  * admin_details.sql: Contains admin user details.
  * customer_details.sql: Contains customer user details.

Example command to import an SQL file:

    mysql -u username -p library < library.sql

Replace username with your MySQL username. You will be prompted to enter your MySQL password.
Or you can import them by SQL Workbench by 'Service' menu item->'Import data'->Now select files from filemanager
3. Running the Application

You can run the application by executing the main Python script:

    python library_management.py

Usage

  The system allows both administrators and customers to perform various library-related tasks.
    Administrators can log in using their username or admin ID and password.
    Customers can log in using their first name.
    The system provides a user-friendly command-line interface (CLI) for interaction.

Contribution

Feel free to contribute to this project by creating issues, suggesting improvements, or making pull requests. We welcome your ideas and code contributions.
