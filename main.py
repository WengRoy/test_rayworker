import pandas as pd
import time
import ssl
import sys

def read_csv_and_count_rows(url):
    # Avoid SSL: CERTIFICATE_VERIFY_FAILED
    ssl._create_default_https_context = ssl._create_unverified_context

    # 讀取 CSV.gz 檔案並計算行數
    df = pd.read_csv(url, compression='gzip')
    row_count = len(df.index)
    return row_count

def main():
    # 使用範例
    # 讀取命令行參數
    url = sys.argv[1]
    row_count = read_csv_and_count_rows(url)
    print(f"Downloaded and extracted CSV file, with {row_count} rows.")
    return row_count

if __name__ == '__main__':
    # For Test, the start time
    start_time = time.time()

    main()

    # For Test, the execute time
    print(f"""Execute time= {time.time() - start_time}""")