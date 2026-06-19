import gspread
import json
from datetime import datetime # 💡 1. 날짜 기능을 사용하기 위해 이 줄이 맨 위에 꼭 필요합니다!

gc = gspread.service_account(filename='credentials.json')

# ★ 여기에 기존에 잘 되던 시트 이름이나 주소를 다시 넣어주세요!
sh = gc.open('강덕구 대시보드') 

worksheet_match = sh.get_worksheet(0) 
match_data = worksheet_match.get_all_records()

worksheet_summary = sh.worksheet('전적요약')
summary_data = worksheet_summary.get_all_records()

# 💡 2. 파이썬에게 현재 컴퓨터 날짜를 '26.06.19' 형태로 먼저 계산하라고 명령하는 핵심 줄입니다!
current_date = datetime.now().strftime("%y.%m.%d")

with open('data.js', 'w', encoding='utf-8') as f:
    f.write("const matchData = " + json.dumps(match_data, ensure_ascii=False) + ";\n")
    f.write("const summaryData = " + json.dumps(summary_data, ensure_ascii=False) + ";\n")
    f.write(f'const lastUpdate = "{current_date}";\n') 

print(f"✅ 데이터 다운로드 완료! (업데이트 날짜: {current_date})")