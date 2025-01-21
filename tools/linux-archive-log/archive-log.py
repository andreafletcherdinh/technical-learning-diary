#!/usr/bin/env python3 

import os
import sys
import tarfile
from datetime import datetime

def archive_logs(log_directory):
    # Kiểm tra xem thư mục log có tồn tại không
    if not os.path.exists(log_directory):
        print(f"Error: The directory '{log_directory}' does not exist.")
        return

    # Tạo tên file archive dựa trên thời gian hiện tại
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    archive_name = f"logs_archive_{timestamp}.tar.gz"
    output_directory = "./archives"

    # Tạo thư mục lưu trữ nếu chưa tồn tại
    os.makedirs(output_directory, exist_ok=True)

    # Đường dẫn đầy đủ đến file archive
    archive_path = os.path.join(output_directory, archive_name)

    # Nén thư mục log
    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(log_directory, arcname=os.path.basename(log_directory))
    
    print(f"Logs have been archived to: {archive_path}")

    # Ghi log về thời gian nén
    log_file = os.path.join(output_directory, "archive_log.txt")
    with open(log_file, "a") as log:
        log.write(f"{timestamp} - Archived {log_directory} to {archive_name}\n")

    print(f"Archive log has been updated at: {log_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: log-archive <log-directory>")
        sys.exit(1)
    
    log_directory = sys.argv[1]
    archive_logs(log_directory)
