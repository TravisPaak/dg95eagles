import gspread
import json

gc = gspread.service_account(filename='credentials.json')

# ★ 여기에 기존에 잘 되던 시트 이름이나 주소를 다시 넣어주세요!
sh = gc.open('강덕구 대시보드') 

worksheet_match = sh.get_worksheet(0) 
match_data = worksheet_match.get_all_records()

worksheet_summary = sh.worksheet('전적요약')
summary_data = worksheet_summary.get_all_records()

with open('data.js', 'w', encoding='utf-8') as f:
    f.write("const matchData = " + json.dumps(match_data, ensure_ascii=False) + ";\n")
    f.write("const summaryData = " + json.dumps(summary_data, ensure_ascii=False) + ";\n")

print("✅ 데이터 다운로드 완료!")