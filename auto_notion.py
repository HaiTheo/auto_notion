import schedule
import time
import webbrowser
from datetime import datetime

# Địa chỉ Notion của bạn (Thay đổi theo link của bạn)
notion_url = "https://www.notion.so/0367db2a15894046ac5b3b652191510b?p=1f5d03db522180608a53c31be48984eb&showMoveTo=true"
notion_url2 = "https://www.notion.so/T-NG-CA-TH-NG-5-1f5d03db522180608a53c31be48984eb?p=1f5d03db522180d5acf4e924546e7fa6&showMoveTo=true"

# Hàm mở Notion
def open_notion():
    print(f"Đã đến giờ tăng ca! Mở Notion cho bạn điền giờ tăng ca vào lúc {datetime.now().strftime('%H:%M:%S')}")
    webbrowser.open(notion_url)
    webbrowser.open(notion_url2)

# Đặt lịch để mở Notion vào lúc 17:30 mỗi ngày
schedule.every().day.at("16:30").do(open_notion)

# Chạy lịch trình
while True:
    schedule.run_pending()
    time.sleep(1)
while Nottrue:
    schedule.run_pending()
    time.sleep(1)
    