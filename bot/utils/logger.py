import logging
import sys

# ANSI color codes
RESET = "\033[0m"
COLORS = {
    "DEBUG": "\033[36m",     # Cyan
    "INFO": "\033[32m",      # Green
    "WARNING": "\033[33m",   # Yellow
    "ERROR": "\033[31m",     # Red
    "CRITICAL": "\033[1;31m" # Bold Red
}

class ColorFormatter(logging.Formatter):
    def format(self, record):
        log_color = COLORS.get(record.levelname, "")
        record.levelname = f"{log_color}{record.levelname}{RESET}"
        return super().format(record)

def setup_logger():
    # Remove default handlers so we can customize
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(ColorFormatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    ))

    logging.basicConfig(level=logging.INFO, handlers=[handler])
