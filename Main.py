import requests import smtplib from email.mime.text import MIMEText from email.mime.multipart import MIMEMultipart import time

تنظیمات ایمیل

EMAIL_SENDER = 'your_email@gmail.com' EMAIL_PASSWORD = 'your_app_password' EMAIL_RECEIVER = 'Rezaie.omid59@gmail.com'

لیست ارزها برای تحلیل

SYMBOLS = ['bitcoin', 'dogecoin', 'arbitrum', 'alchemix', 'fartcoin']  # fartcoin نماد فرضی

تابع برای گرفتن قیمت

def get_price(symbol): url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd" response = requests.get(url) data = response.json() return data[symbol]['usd']

تابع تحلیل ساده و ساخت سیگنال فرضی

def analyze(symbol, price): # الگوریتم ساده: اگه قیمت کمتر از یه آستانه باشه، سیگنال خرید بده thresholds = { 'bitcoin': 67000, 'dogecoin': 0.18, 'arbitrum': 1.1, 'alchemix': 0.02, 'fartcoin': 0.00001 } if price < thresholds[symbol]: return f"[سیگنال خرید] {symbol.upper()}\nقیمت فعلی: {price} USD\nسیگنال: ورود به پوزیشن خرید\nاستاپ: بر اساس مدیریت سرمایه تعیین شود\n" return None

ارسال ایمیل سیگنال

def send_email(subject, body): msg = MIMEMultipart() msg['From'] = EMAIL_SENDER msg['To'] = EMAIL_RECEIVER msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(EMAIL_SENDER, EMAIL_PASSWORD)
server.send_message(msg)
server.quit()

اجرای پیوسته تحلیل

while True: full_report = '' for sym in SYMBOLS: try: price = get_price(sym) signal = analyze(sym, price) if signal: full_report += signal + "\n" except Exception as e: print(f"خطا در تحلیل {sym}: {e}")

if full_report:
    send_email("سیگنال‌های معاملاتی با عشق از خانومت", full_report)
    print("ایمیل ارسال شد!")

time.sleep(3600)  # هر یک ساعت یک بار

