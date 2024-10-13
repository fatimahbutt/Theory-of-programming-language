import os
import math
import csv

# Set the path for the input log file
logfile_path = r'C:\Users\Asus\PycharmProjects\Assignment1\logfile_2024_09_23_11_58_27.txt'

# Create directories to store the text and CSV files
txt_output_dir = 'sensor_data_txt'
csv_output_dir = 'sensor_data_csv'
os.makedirs(txt_output_dir, exist_ok=True)
os.makedirs(csv_output_dir, exist_ok=True)

# Dictionary to hold file handles for text files based on sensor prefixes
sensor_txt_files = {}

# Function to compute the magnitude from x, y, and z components
def calculate_magnitude(x, y, z):
    return math.sqrt(x ** 2 + y ** 2 + z ** 2)

# Dictionary to hold CSV writers and their file handles for each sensor type
sensor_csv_files = {}
csv_headers = ['AppTimestamp(s)', 'SensorTimestamp(s)', 'X', 'Y', 'Z', 'Accuracy', 'Magnitude']

try:
    # Open the log file to read data
    with open(logfile_path, 'r') as log_file:
        # Process the file line by line
        for line in log_file:
            # Skip lines starting with '%' as they are comments or empty
            if line.startswith('%') or not line.strip():
                continue

            # Determine the sensor type from the first four characters
            sensor_type = line[:4]

            # Set the output file names based on the sensor type
            if sensor_type == 'ACCE':
                file_name = 'Accelerometer.txt'
                csv_file_name = 'Accelerometer.csv'
            elif sensor_type == 'GYRO':
                file_name = 'Gyroscope.txt'
                csv_file_name = 'Gyroscope.csv'
            elif sensor_type == 'MAGN':
                file_name = 'Magnetometer.txt'
                csv_file_name = 'Magnetometer.csv'
            elif sensor_type == 'PRES':
                file_name = 'Pressure.txt'  # No magnitude needed
            elif sensor_type == 'LIGH':
                file_name = 'Light.txt'  # No magnitude needed
            elif sensor_type == 'PROX':
                file_name = 'Proximity.txt'
            elif sensor_type == 'HUMI':
                file_name = 'Humidity.txt'
            elif sensor_type == 'TEMP':
                file_name = 'Temperature.txt'
            elif sensor_type == 'AHRS':
                file_name = 'Orientation.txt'
                csv_file_name = 'Orientation.csv'
            elif sensor_type == 'GNSS':
                file_name = 'GPS.txt'
            elif sensor_type == 'WIFI':
                file_name = 'WiFi.txt'
            elif sensor_type == 'BLUE':
                file_name = 'Bluetooth.txt'
            elif sensor_type == 'SOUN':
                file_name = 'Sound.txt'
            elif sensor_type == 'RFID':
                file_name = 'RFID.txt'
            elif sensor_type == 'IMUX':
                file_name = 'IMU_XSens.txt'
                csv_file_name = 'IMU_XSens.csv'
            elif sensor_type == 'IMUL':
                file_name = 'IMU_LPMS.txt'
                csv_file_name = 'IMU_LPMS.csv'
            else:
                # Ignore any unsupported sensor types
                continue

            # Construct the full path for the text output file
            full_txt_file_path = os.path.join(txt_output_dir, file_name)

            # Write to the corresponding text file
            if full_txt_file_path not in sensor_txt_files:
                sensor_txt_files[full_txt_file_path] = open(full_txt_file_path, 'w')
            sensor_txt_files[full_txt_file_path].write(line)

            # For sensors with X, Y, Z values, compute the magnitude and write to CSV
            if sensor_type in ['ACCE', 'GYRO', 'MAGN']:
                # Split the line into data fields (assumed to be semi-colon separated)
                data = line.strip().split(';')

                try:
                    app_timestamp = data[1]
                    sensor_timestamp = data[2]
                    x = float(data[3])
                    y = float(data[4])
                    z = float(data[5])
                    accuracy = data[6] if len(data) > 6 else None

                    # Calculate the magnitude
                    magnitude = calculate_magnitude(x, y, z)

                    # Write the data to the corresponding CSV file
                    full_csv_file_path = os.path.join(csv_output_dir, csv_file_name)

                    if full_csv_file_path not in sensor_csv_files:
                        csv_file = open(full_csv_file_path, 'w', newline='')
                        writer = csv.writer(csv_file)
                        writer.writerow(csv_headers)
                        sensor_csv_files[full_csv_file_path] = (csv_file, writer)  # Store the file and writer

                    # Log the data in CSV format
                    sensor_csv_files[full_csv_file_path][1].writerow(
                        [app_timestamp, sensor_timestamp, x, y, z, accuracy, magnitude])

                except ValueError:
                    # Handle any parsing errors gracefully
                    continue

finally:
    # Close all text and CSV files
    for file in sensor_txt_files.values():
        file.close()
    for csv_file, _ in sensor_csv_files.values():
        csv_file.close()  # Close the CSV file instead of the writer
