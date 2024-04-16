from detection import Detect
import schedule
import time

if __name__ == '__main__':
    # 1 раз в час будет проводиться проверка в выбранных группах
    start = Detect()
    schedule.every().hour.do(start.run)
    while True:
        schedule.run_pending()
        time.sleep(1)
