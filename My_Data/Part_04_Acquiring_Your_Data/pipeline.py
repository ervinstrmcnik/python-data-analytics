"""Web data Acquisition Pipeline."""

from __future__ import annotations

import csv
import datetime
import os
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

MAIN_DATA_DIR = Path(__file__).parent.parent / "data" / "project"
MERGED_RAW_LOGS_PATH = MAIN_DATA_DIR / "merged_raw_logs.txt"
MERGED_CSV_LOGS_PATH = MAIN_DATA_DIR / "merged_logs.csv"
IP_INFO_CSV = MAIN_DATA_DIR / "ip_info.csv"
IP_API_IS_API_KEY = os.getenv("IP_API_IS_API_KEY")


def get_all_logs_paths(main_dir: Path, pattern: str) -> list[Path]:
    """Get all log files paths."""
    return list(main_dir.rglob(pattern))


def merge_logs_and_remove_empty_lines(logs_paths: list[Path], output_path: Path) -> None:
    """Merge all logs files and remove empty lines."""
    with output_path.open("w") as output_file:
        for log_path in logs_paths:
            logger.debug(f"--> Merging {log_path.name}.")
            with log_path.open("r") as log_file:
                for line in log_file:
                    if line.strip():
                        output_file.write(line)


def convert_raw_logs_to_csv(input_path: Path, output_path: Path) -> None:
    """Convert raw logs to CSV."""
    header = ["timestamp", "src_ip", "http_method", "http_path", "http_protocol_version", "http_status_code", "http_response_size", "referrer", "user_agent"]
    with input_path.open("r") as input_file, output_path.open("w", newline="") as output_file:
        csv_writer = csv.writer(output_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(header)
        for line in input_file:
            try:
                line_splitted = line.split("[")
                timestamp = datetime.datetime.strptime(line_splitted[1].split("]")[0], "%d/%b/%Y:%H:%M:%S %z")
                line_splitted = line.split(" ")
                src_ip = line_splitted[0]
                http_method = line_splitted[5].replace('"', "")
                http_path = line_splitted[6]
                http_protocol_version = line_splitted[7].replace('"', "")
                http_status_code = int(line_splitted[8])
                http_response_size = int(line_splitted[9])
                line_splitted = line.split('"')
                referrer = line_splitted[3].strip()
                user_agent = line_splitted[5].strip()
            except ValueError as err:  # noqa: PERF203
                if "HTTP/1.1" not in line:
                    logger.warning(f"Malformed line, missing HTTP protocol version: {line}")
                    http_protocol_version = None
                    http_status_code = int(line_splitted[-4])
                    http_response_size = int(line_splitted[-3])
                    line_splitted = line.split('"')
                    referrer = line_splitted[3].strip()
                    user_agent = line_splitted[5].strip()
                else:
                    logger.error(f"Malformed line: {line}")
                    raise ValueError from err
            finally:
                csv_writer.writerow([timestamp, src_ip, http_method, http_path, http_protocol_version, http_status_code, http_response_size, referrer, user_agent])


def extract_unique_ips(input_path: Path) -> list[str]:
    """Extract unique IPs from logs."""
    unique_ips = set()
    with input_path.open("r") as input_file:
        for line in input_file:
            line_splitted = line.split(",")
            unique_ips.add(line_splitted[1])
    return list(unique_ips)


def generate_ip_info_dataset(unique_ips: list[str], output_path: Path) -> None:
    """Generate IP info dataset and save it to CSV."""
    header = (
        "ip",
        "rir",
        "is_mobile",
        "is_crawler",
        "is_datacenter",
        "is_tor",
        "is_proxy",
        "is_vpn",
        "is_abuser",
        "datacenter_name",
        "company_name",
        "company_abuser_score",
        "company_type",
        "country",
        "city",
        "latitude",
        "longitude",
    )
    ip_data = []
    for unique_ip in unique_ips:
        try:
            url = f"https://api.ipapi.is?q={unique_ip}&key={IP_API_IS_API_KEY}"
            data = requests.get(url, timeout=15)
            if data.status_code == requests.codes.ok:
                logger.debug(f"---> Processing IP {unique_ip}.")
                data = data.json()
                ip = data.get("ip")
                if not ip:
                    logger.error(f"IP {unique_ip} not found in response.")
                    continue
                rir = data.get("rir")
                is_mobile = data.get("is_mobile")
                is_crawler = data.get("is_crawler")
                is_datacenter = data.get("is_datacenter")
                is_tor = data.get("is_tor")
                is_proxy = data.get("is_proxy")
                is_vpn = data.get("is_vpn")
                is_abuser = data.get("is_abuser")
                datacenter_name = data.get("datacenter", {}).get("datacenter")
                company_name = data.get("company", {}).get("name")
                company_abuser_score = data.get("company", {}).get("abuser_score")
                company_type = data.get("company", {}).get("type")
                country = data.get("location", {}).get("country")
                city = data.get("location", {}).get("city")
                latitude = data.get("location", {}).get("latitude")
                longitude = data.get("location", {}).get("longitude")
                ip_data.append(
                    (
                        ip,
                        rir,
                        is_mobile,
                        is_crawler,
                        is_datacenter,
                        is_tor,
                        is_proxy,
                        is_vpn,
                        is_abuser,
                        datacenter_name,
                        company_name,
                        company_abuser_score,
                        company_type,
                        country,
                        city,
                        latitude,
                        longitude,
                    ),
                )
            else:
                logger.error(f"Error while processing IP {unique_ip}: {data.status_code}. Details: {data.text}")
                continue
        except Exception as err:  # noqa: BLE001
            logger.error(f"Error while processing IP {unique_ip}: {err}")

    ip_data_df = pd.DataFrame(ip_data, columns=header)
    ip_data_df.to_csv(output_path, index=False)


if __name__ == "__main__":
    logger.info("--------- Running Web Data Acquisition Pipeline ---------")
    raw_logs_paths = get_all_logs_paths(MAIN_DATA_DIR, "access.log.*")
    logger.info(f"--> Found {len(raw_logs_paths)} log files.")
    logger.info(f"--> Merging all logs into {MERGED_RAW_LOGS_PATH}.")
    merge_logs_and_remove_empty_lines(raw_logs_paths, MERGED_RAW_LOGS_PATH)
    logger.info(f"--> Converting raw logs into CSV: {MERGED_CSV_LOGS_PATH}.")
    convert_raw_logs_to_csv(MERGED_RAW_LOGS_PATH, MERGED_CSV_LOGS_PATH)
    logger.info("--> Extracting unique IPs from logs.")
    unique_ips = extract_unique_ips(MERGED_CSV_LOGS_PATH)
    logger.info(f"--> Found {len(unique_ips)} unique IPs. First 5: {unique_ips[:5]}")
    generate_ip_info_dataset(unique_ips, IP_INFO_CSV)
    logger.info("--------- Web Data Acquisition Pipeline Finished ---------")
