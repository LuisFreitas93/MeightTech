import pandas as pd
import numpy as np
import snowflake.connector
import snowflake.connector.pandas_tools as pd_tools

###### EXTRACT ######
# 1 . Load CSV data for testing and first import
#df = pd.read_csv('/Users/luis.freitas/Desktop/Workspace/challenge_dataset.csv')


# 2 . Sintetic data for mock API (not quite, but will serve)
num_records = 1000

# Generate synthetic data
data = {
    'service_type': np.random.choice(['full_truck_load', 'less_truck_load', None, 'full_truck_lod'], num_records),
    'pickup_coordinate': [(np.random.uniform(-90, 90), np.random.uniform(-180, 180)) for _ in range(num_records)],
    'delivery_coordinate': [(np.random.uniform(-90, 90), np.random.uniform(-180, 180)) for _ in range(num_records)],
    'price': np.random.uniform(100, 1000, num_records),
    'trailer_type': np.random.choice(['refrigerated', 'flatbed', None, 'rigid'], num_records)
}

df = pd.DataFrame(data)
###### TRANSFORM ######
# 1. Clean service_type
df = df.replace('full_truck_lod', 'full_truck_load')


# 2. Drop missing values (any column)
df = df.dropna()

# 3. Apply IQR
#The IQR is the range between the first quartile (25th percentile) and the third quartile (75th percentile) in a dataset. Data points that fall outside of 1.5 times the IQR below the first quartile or above the third quartile are often considered outliers.
# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1

# Define bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers
df = df[(df['price'] >= lower_bound) & (df['price'] <= upper_bound)]
###### LOAD ######

# 1. Define Snowflake connection details
conn = snowflake.connector.connect(
    user='LFREITASTRIAL',
    password='MeightTest1',
    account='hx19838.eu-west-2',
    warehouse='COMPUTE_WH',
    database='MEIGHT',
    schema='PUBLIC'
)

# Step 3: Create a cursor object to interact with Snowflake
cur = conn.cursor()

# Step 5: Ensure DataFrame columns match the Snowflake table
df = df[['service_type', 'pickup_coordinate', 'delivery_coordinate', 'price', 'trailer_type']]

# Step 6: Load the DataFrame into Snowflake
success, nchunks, nrows, _ = pd_tools.write_pandas(conn, df, 'FREIGHT_DATA')

# Check if the data load was successful
if success:
    print(f"Successfully loaded {nrows} rows into Snowflake.")
else:
    print("Failed to load data into Snowflake.")
