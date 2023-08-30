import argparse
import schedule
import requests
import time

def perform_request(url, log_file):
    try:
        response = requests.get(url)
        response.raise_for_status()
        log_message = f"Запрос выполнен успешно. Статус код: {response.status_code}"
        print(log_message)
        log_file.write(log_message + "\n")
    except requests.exceptions.RequestException as e:
        log_message = f"Произошла ошибка: {e}"
        print(log_message)
        log_file.write(log_message + "\n")
    
def main(url, initial_delay, interval):
    log_filename = "http_request_logs.txt"
    log_file = open(log_filename, "a")
    schedule.every(interval).seconds.do(lambda: perform_request(url, log_file))
    time.sleep(initial_delay)

    while True:
        try:
            schedule.run_pending()
        except requests.exceptions.RequestException as e:
            log_message = f"Произошла ошибка: {e}"
            print(log_message)
            log_file.write(log_message + "\n")
            time.sleep(5)  
        except KeyboardInterrupt:
            log_file.close()
            break

        time.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP запрос планировщик")
    parser.add_argument("url", type=str, help="URL для выполнения запросов")
    parser.add_argument("initial_delay", type=int, help="Начальная задержка в секундах")
    parser.add_argument("interval", type=int, help="Интервал между запросами в секундах")
    args = parser.parse_args()

main(args.url, args.initial_delay, args.interval)