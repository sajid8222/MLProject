import logging  # Import the logging module for creating and managing log messages.
import os  # Import the os module for interacting with the operating system.
from datetime import datetime  # Import datetime for generating timestamped log filenames.

# Generate a unique log file name based on the current date and time.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

# Create the full path for the logs directory and the log file.
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)  # Combine the current working directory with 'logs' folder and log file name.
os.makedirs(logs_path, exist_ok=True)  # Create the 'logs' directory if it doesn't exist (exist_ok prevents errors if the directory exists).

# Define the full file path for the log file.
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging system.
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Specify the log file to write messages to.
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Define the log message format.
    level=logging.INFO,  # Set the minimum log level to INFO (logs INFO, WARNING, ERROR, and CRITICAL messages).
)

# Main execution block
if __name__ == "__main__":
    logging.info("Logging has started")  # Log an informational message indicating that logging has started.
