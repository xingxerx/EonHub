import logging
import datetime

def setup_security_logging():
    """Sets up the security logging configuration."""
    log_filename = "security_log.txt"
    logging.basicConfig(filename=log_filename, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Security logging started.")

def log_security_event(event_type, message):
    """Logs a security event with a timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"
    if event_type == "INFO":
        logging.info(log_message)
    elif event_type == "WARNING":
        logging.warning(log_message)
    elif event_type == "ERROR":
        logging.error(log_message)
    else:
        logging.info(log_message)
