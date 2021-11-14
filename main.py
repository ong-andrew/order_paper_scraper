from scraper import scraper
from compare_txt import compare_txt
from send_email import send_email

if __name__ == '__main__':
    scraper()
    x = compare_txt()
    if x != None:
        send_email(x)
