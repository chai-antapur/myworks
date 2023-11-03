import bcrypt
import psycopg2

# Database connection parameters
db_params = {
    "host" : "localhost",
    "user" : "postgres",
    "password" : "12345678",
    "database" : "BestEx_Users",
    "port" : 5432,
}

# Define the username for which you want to retrieve the password
username = "chaitra@br.com"
password = "123456"

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(**db_params)
    
    # Create a cursor to interact with the database
    cursor = conn.cursor()
    
    # Execute a query to retrieve the salted and hashed password for the specified user
    query = "SELECT salted_hash_of_password FROM websocket_authentication_details WHERE email_id = %s"
    cursor.execute(query, (username,))
    
    # Fetch the result
    result = cursor.fetchone()
    
    if result:
        stored_password_hash = result[0]
        user_input_password = password.encode('utf-8')
        
        # Verify the user's input password against the stored hash
        if bcrypt.checkpw(user_input_password, stored_password_hash.encode('utf-8')):
            print("Password is correct")
        else:
            print("Password is incorrect")
    else:
        print(f"No user found with username: {username}")

except psycopg2.Error as e:
    print(f"Error: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()






