import pandas as pd

file_path = 'departments.csv'

df = pd.read_csv(file_path)
import pandas as pd
import os

directory_path = "/Users/miztirmizi/Desktop/Starter_Code 5/data"  

# Get a list of all CSV files in the directory
csv_files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]

# Initialize an empty dictionary to store DataFrames
dataframes = {}

# Loop through the list of CSV files and read them into DataFrames
for csv_file in csv_files:
    file_path = os.path.join(directory_path, csv_file)
    df_name = os.path.splitext(csv_file)[0]  # Use the filename (without extension) as the DataFrame name
    dataframes[df_name] = pd.read_csv(file_path)

import pandas as pd
import os

# Specify the directory where your CSV files are located
directory_path = "/Users/miztirmizi/Desktop/Starter_Code 5/data"

# Get a list of all CSV files in the directory
csv_files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]

# Initialize an empty dictionary to store DataFrames
dataframes = {}

# Loop through the list of CSV files and read them into DataFrames
for csv_file in csv_files:
    file_path = os.path.join(directory_path, csv_file)
    df_name = os.path.splitext(csv_file)[0]  # Use the filename (without extension) as the DataFrame name
    dataframes[df_name] = pd.read_csv(file_path)

# Now, you have a dictionary 'dataframes' where each key is the DataFrame name
# and the corresponding value is the DataFrame containing the data from the CSV file

# You can access the data from each CSV file as follows:
# dataframes['departments'] for 'departments.csv'
# dataframes['dept_emp'] for 'dept_emp.csv'
# dataframes['dept_manager'] for 'dept_manager.csv'
# dataframes['employee'] for 'employee.csv'
# dataframes['salaries'] for 'salaries.csv'
# dataframes['titles'] for 'titles.csv'
# Access the data from 'departments.csv'
departments_data = dataframes['departments']

# Access the data from 'dept_emp.csv'
dept_emp_data = dataframes['dept_emp']

# Access the data from 'dept_manager.csv'
dept_manager_data = dataframes['dept_manager']

# Access the data from 'employee.csv'
employee_data = dataframes['employees']

# Access the data from 'salaries.csv'
salaries_data = dataframes['salaries']

# Access the data from 'titles.csv'
titles_data = dataframes['titles']

