import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV files
df_proximity = pd.read_csv('proximity_sensor_data.csv')
df_gesture = pd.read_csv('proximity_with_gesture_data.csv')
df_screen = pd.read_csv('screen_proximity_data.csv')
df_detection = pd.read_csv('object_detection_data.csv')

# Convert 'Timestamp' column to datetime for proper plotting
df_proximity['Timestamp'] = pd.to_datetime(df_proximity['Timestamp'])
df_gesture['Timestamp'] = pd.to_datetime(df_gesture['Timestamp'])
df_screen['Timestamp'] = pd.to_datetime(df_screen['Timestamp'])
df_detection['Timestamp'] = pd.to_datetime(df_detection['Timestamp'])

# --- 1. Proximity Sensor Data Over Time ---
plt.figure(figsize=(10, 6))
plt.plot(df_proximity['Timestamp'], df_proximity['Proximity Value'], label='Proximity Value', color='b', marker='o')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Proximity Value', fontsize=12)
plt.title('Proximity Sensor Data Over Time', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# --- 2. Proximity with Gesture Recognition Over Time ---
plt.figure(figsize=(10, 6))
for gesture in df_gesture['Gesture Type'].unique():
    subset = df_gesture[df_gesture['Gesture Type'] == gesture]
    plt.plot(subset['Timestamp'], subset['Proximity Value'], marker='o', label=gesture)
plt.xticks(rotation=45)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Proximity Value', fontsize=12)
plt.title('Proximity with Gesture Recognition Over Time', fontsize=14)
plt.legend(title='Gesture Type')
plt.grid(True)
plt.tight_layout()
plt.show()

# --- 3. Screen On/Off Transitions and Proximity Over Time ---
plt.figure(figsize=(10, 6))
colors = {'Off': 'red', 'On': 'green'}
for status in df_screen['Screen On/Off'].unique():
    subset = df_screen[df_screen['Screen On/Off'] == status]
    plt.plot(subset['Timestamp'], subset['Proximity Value'], marker='o', color=colors[status], label=status)
plt.xticks(rotation=45)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Proximity Value', fontsize=12)
plt.title('Screen On/Off Status with Proximity Over Time', fontsize=14)
plt.legend(title='Screen On/Off')
plt.grid(True)
plt.tight_layout()
plt.show()

# --- 4. Object Detection (Scatter Plot) ---
plt.figure(figsize=(10, 6))
for obj in df_detection['Object Detected'].unique():
    subset = df_detection[df_detection['Object Detected'] == obj]
    plt.scatter(subset['Timestamp'], subset['Proximity Value'], label=obj, s=100)
plt.xticks(rotation=45)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Proximity Value', fontsize=12)
plt.title('Proximity Values with Object Detection Over Time', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.legend(title='Object Detected')
plt.show()
