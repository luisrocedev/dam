import pandas as pd
import matplotlib.pyplot as plt

# File path
file_path = 'server_data.csv'  # Replace with your actual file path

# Read the file with error handling for malformed rows
try:
    server_data = pd.read_csv(file_path, sep='|', on_bad_lines='skip')  # New syntax for skipping bad lines
except Exception as e:
    print(f"Error loading file: {e}")
    exit()

# Preprocessing: Extract and clean relevant columns
server_data['REQUEST_TIME'] = pd.to_datetime(server_data['REQUEST_TIME'], unit='s', errors='coerce')
server_data['BROWSER'] = server_data['HTTP_USER_AGENT'].str.split(' ').str[0]
server_data['PAGE'] = server_data['REQUEST_URI']
server_data['IP'] = server_data['REMOTE_ADDR']

# Filter valid rows
server_data = server_data.dropna(subset=['REQUEST_TIME'])

# 1. Visitor count over the last 24 hours
last_24_hours = server_data[server_data['REQUEST_TIME'] >= server_data['REQUEST_TIME'].max() - pd.Timedelta(hours=24)]
visitor_counts = last_24_hours.groupby(last_24_hours['REQUEST_TIME'].dt.hour).size()

plt.figure(figsize=(10, 6))
plt.plot(visitor_counts.index, visitor_counts.values, marker='o')
plt.title("Visitor Count Over the Last 24 Hours")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Visitors")
plt.grid(True)
plt.show()

# 2. Brands of browsers
browser_counts = server_data['BROWSER'].value_counts()

plt.figure(figsize=(10, 6))
browser_counts[:10].plot(kind='bar')
plt.title("Top 10 Browsers")
plt.xlabel("Browser")
plt.ylabel("Number of Requests")
plt.grid(axis='y')
plt.show()

# 3. Count of distinct IPs
distinct_ips = server_data['IP'].nunique()

# 4. Count of distinct pages viewed
distinct_pages = server_data['PAGE'].nunique()

print(f"Distinct IPs: {distinct_ips}")
print(f"Distinct Pages Viewed: {distinct_pages}")
