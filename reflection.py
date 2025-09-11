import requests
import threading
import argparse
from urllib.parse import urlparse, parse_qs, urlunparse, urlencode
import time

# Set the timeout limit (in seconds)
TIMEOUT = 10

# Global variables to track progress
total_urls = 0
processed_urls = 0

# ANSI escape sequences for color
BOLD = '\033[1m'
RED = '\033[91m'
BOLD_RED = '\033[1;91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_banner():
    banner = f"""
    {GREEN}#########################################{RESET}
    {GREEN}#                                       #{RESET}
    {GREEN}#        {BOLD}XSS Reflection Checker V2 {RESET}{GREEN}        #{RESET}
    {GREEN}#        {BOLD}Developed by Fagun{RESET}{GREEN}        #{RESET}
    {GREEN}#                                       #{RESET}
    {GREEN}#########################################{RESET}
    {BOLD}Usage:{RESET}                                #
    python reflection.py urls.txt --threads 2
    """
    print(banner)

def save_reflected_url(original_url, param_name, modified_params, output_file):
    """Save the modified URL with {payload} replacing the specific parameter."""
    temp_params = modified_params.copy()

    # Save with {payload} in place of the current parameter without encoding
    temp_params[param_name] = "{payload}"
    query = "&".join(f"{k}={','.join(v)}" if isinstance(v, list) else f"{k}={v}" for k, v in temp_params.items())
    payload_url = urlunparse(urlparse(original_url)._replace(query=query))

    # Save the clean payload URL to the output file
    with open(output_file, 'a') as f:
        f.write(payload_url + '\n')

    print(f"{GREEN}[SAVED] {payload_url}{RESET}")

def check_reflection(url, output_file):
    global processed_urls

    try:
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        # Ensure empty parameters are handled
        for param in parsed_url.query.split("&"):
            key_value = param.split("=")
            if len(key_value) == 1 or key_value[1] == "":
                query_params[key_value[0]] = ""

        original_params = {k: v[0] if isinstance(v, list) else v for k, v in query_params.items()}

        for param_name in original_params.keys():
            modified_params = original_params.copy()
            modified_params[param_name] = "{payload}"
            save_reflected_url(url, param_name, modified_params, output_file)

        print(f"{BLUE}[INFO] Processed URL: {url}{RESET}")
    except Exception as e:
        print(f"{RED}[ERROR] Failed to process URL {url}: {e}{RESET}")
    finally:
        processed_urls += 1

def process_urls(urls, threads, output_file):
    global total_urls
    total_urls = len(urls)

    def worker(sublist):
        for url in sublist:
            check_reflection(url, output_file)

    chunk_size = max(1, len(urls) // threads)
    thread_list = []

    for i in range(0, len(urls), chunk_size):
        t = threading.Thread(target=worker, args=(urls[i:i + chunk_size],))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    print(f"{BOLD_RED}Processing complete! Total: {total_urls}, Processed: {processed_urls}{RESET}")

def main():
    parser = argparse.ArgumentParser(description='XSS Reflection Checker V2')
    parser.add_argument('urls_file', help='Path to the file containing URLs')
    parser.add_argument('--threads', type=int, default=2, help='Number of threads to use (default: 2)')
    parser.add_argument('--output', type=str, default='output_reflection.txt', help='Output file name (default: output_reflection.txt)')

    args = parser.parse_args()

    with open(args.urls_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]

    print_banner()

    start_time = time.time()
    process_urls(urls, args.threads, args.output)
    end_time = time.time()

    print(f"{BOLD}Time taken: {end_time - start_time:.2f} seconds{RESET}")

if __name__ == '__main__':
    main()
