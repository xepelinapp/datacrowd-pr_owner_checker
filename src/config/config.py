from logging import INFO, DEBUG


# logging
LOGGING_LEVEL_LOGGER = INFO
LOGGING_LEVEL_CONSOLE = INFO
LOGGING_LEVEL_FILE = DEBUG
LOGGING_FMT = "%(asctime)s || %(process)d:%(processName)s > %(filename)s - %(funcName)s || %(levelname)s :: %(message)s"
# formats
DATE_FMT = "%Y%m%d"
DATETIME_FMT = ""
TIMESTAMP_FMT = ""
# targets
TARGET_TEAM = "data-crowd"
TARGET_BRANCH = "devel"
# test data
TARGET_PR = 2747
