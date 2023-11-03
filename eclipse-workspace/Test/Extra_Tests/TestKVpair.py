import psycopg2

# Database connection parameters
db_params = {
    "host" : "localhost",
    "user" : "postgres",
    "password" : "12345678",
    "database" : "BestEx_Users",
    "port" : 5432,
}

# Connect to the database
conn = psycopg2.connect(**db_params)

# Create a cursor to interact with the database
cursor = conn.cursor()

username = "chaitra@br.com"
# Execute a SQL query to extract only the keys from the key-value pairs in your table
query = "select permissions_json from websocket_permissions_details where email_id = %s"
cursor.execute(query, (username,))

# Fetch the results as a list of keys
results = cursor.fetchall()

# Close the cursor and connection when you're done
cursor.close()
conn.close()

# Now you have a list of keys extracted from the key-value pairs
reslist = list(results)

print(reslist)

flattened_list = [item for sublist in reslist for item in sublist]

print(flattened_list)

combined_dict = {}

# Iterate through the list and update the combined_dict
for dictionary in flattened_list:
    combined_dict.update(dictionary)

print(combined_dict)

keys_view = combined_dict.keys()

# Convert the view object to a list if needed
keys_list = list(keys_view)

print(keys_list)

my_list_of_strings = ["data_permissions", "permit_actions"]

for key in combined_dict.keys():
    if key in my_list_of_strings:
        print("contains")
    
    