from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("🚀 강덕구 크롤러 V7 (스나이퍼 추적 엔진) 가동 시작!")

url = "https://ch.sooplive.co.kr/sdkels"

try:
    options = Options()
    options.add_argument("--start-maximized") 
    driver = webdriver.Chrome(options=options)
    
    driver.get(url)

    print("⏳ 로봇이 사이트에 접속했습니다. 데이터를 찾는 중...")
    
    # 🎯 핵심 기술: 암호를 무시하는 스나이퍼 추적 주소 (XPath)
    # 해석: "클래스 이름에 'GiftMenu_subscription'이 포함된 버튼을 찾고, 그 안의 글자(span)를 가져와!"
    target_address = "//button[contains(@class, 'GiftMenu_subscription')]//span"
    
    # 스나이퍼 주소로 타겟 조준!
    target_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, target_address))
    )
    
    crawled_data = target_element.text.strip()

    print("✅ 데이터 수집 성공!")
    print(f"📌 긁어온 알맹이 데이터: {crawled_data}")

    time.sleep(1)
    driver.quit()

except Exception as e:
    print(f"❌ 에러가 발생했습니다: {e}")
    driver.quit()