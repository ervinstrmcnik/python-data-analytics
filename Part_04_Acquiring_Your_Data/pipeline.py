"""Web data Acquisition Pipeline."""

from __future__ import annotations  # Ne spremeni naše kde, samo pomaga, če kdo zaganja s starimi interpreterji.

import datetime
from pathlib import Path

from loguru import logger

# MAIN_DATA_DIR=Path(__file__) # To nam vrne lokacijo trenunega file-a

MAIN_DATA_DIR = Path(__file__).parent.parent / "data" / "project"  # gremo do nad nad mape
MERGED_RAW_LOGS_PATH = MAIN_DATA_DIR / "merged_raw_logs.txt"
MERGED_CSV_LOGS_PATH = MAIN_DATA_DIR / "merged_csv_logs.txt"


def get_all_logs_paths(main_dir: Path, pattern: str) -> list[Path]:
    """Get all log files paths"""
    return list(main_dir.rglob(pattern))


def merge_logs_and_remove_empty_lines(logs_paths: list[Path], output_path: Path) -> None:
    """Merge all logs files and remove empty lines"""
    with output_path.open("w") as output_file:
        for log_path in logs_paths:
            logger.debug(f"-->Merging {log_path.name}.")
            with log_path.open("r") as log_file:
                for line in log_file:
                    if line.strip():
                        output_file.write(line)


# Step 2
def convert_raw_logs_to_csv(input_path: Path, output_path: Path) -> None:
    """Convert raw logs to CSV"""
    with input_path.open("r") as input_file, output_path.open("w") as output_gile:
        for line in input_file:
            line_splitted = line.split("[")
            timestamp = datetime.datetime.strptime(line_splitted[1].split("]")[0], "%d/%b/%Y:%H:%M:%S %z")
            line_splitted = line.split(" ")

            # # Tukaj sem ostal
            # src_ip = line_splitted[0]
            # http_method=line_splitted[5].replace('"', "")

            # Implement your logic here
            print(line.split(" "))
            break


if __name__ == "__main__":  # main ali ime naše skripte
    logger.info("-----------------Running Web Data Acquisition Pipeline-------------------------")
    raw_log_paths = get_all_logs_paths(MAIN_DATA_DIR, "access.log.*")
    logger.info(f"-->Found {len(raw_log_paths)} log files.")
    logger.info(f"--> Merging all logs into {MERGED_RAW_LOGS_PATH}.")
    # merge_logs_and_remove_empty_lines(raw_log_paths, MERGED_RAW_LOGS_PATH)
    logger.info(f"--> Converting raw logs into CSV {MERGED_CSV_LOGS_PATH}.")
    convert_raw_logs_to_csv(MERGED_RAW_LOGS_PATH, MERGED_CSV_LOGS_PATH)
