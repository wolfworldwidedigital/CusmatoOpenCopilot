import os
import configparser


def get_mysql_uri():
    mysql_uri = os.getenv("MYSQL_URI", "mysql://dbuser:dbpass@mysql:3306/opencopilot")
    if not mysql_uri:
        raise ValueError("MYSQL_URI environment variable is not set")

    # Assuming the MYSQL_URI is in the format: mysql://username:password@host:port/database
    # You may need to adjust the parsing based on the actual format of your MYSQL_URI
    components = mysql_uri.split("://")[1].split("@")
    user_pass, host_port_db = components[0], components[1]

    # Adjusting the parsing based on the expected format
    username, password = user_pass.split(":")
    host_port, database = host_port_db.split("/")

    # Adjusting further to handle the case where host and port are separated by a ":"
    host_port_components = host_port.split(":")
    if len(host_port_components) == 2:
        host, port = host_port_components
    else:
        host = host_port_components[0]
        port = "3306"  # Default MySQL port if not specified

    # Creating pymysql format string
    pymysql_uri = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"

    return pymysql_uri


# Read the alembic.ini file
config = configparser.ConfigParser()
config.read("alembic.ini")

# Set the dynamic URL in the [alembic] section
config.set("alembic", "sqlalchemy.url", get_mysql_uri())

# Write the modified configuration back to alembic.ini
with open("alembic.ini", "w") as config_file:
    config.write(config_file)
