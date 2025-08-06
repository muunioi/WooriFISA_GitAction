import os
from datetime import datetime, timedelta
from openai import OpenAI

# Hugging Face API 설정
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_API_KEY"],
)

# 전날 날짜 계산
today = datetime.utcnow() + timedelta(hours=9)  # 한국 시간 기준 (KST)
yesterday = today - timedelta(days=1)
file_date = yesterday.strftime("%y%m%d")
til_path = f"TIL/TIL:{file_date}.md"

# README 기본 정보
timestamp = today.strftime("%Y-%m-%d %H:%M:%S")
readme_path = "README.md"

# TIL 파일 존재 여부 확인
if not os.path.exists(til_path):
    readme_content = f"""# 🌞 오늘도 힘차게!

> 어제는 학습 기록이 없었습니다. 하루를 어떻게 보냈는지 되돌아보는 것도 의미 있는 복습입니다!

---

## 📚 어제의 학습 요약 ({file_date})

❌ TIL 파일이 존재하지 않아 요약을 건너뜁니다.

---

⏰ 자동 업데이트 시간: {timestamp} (KST)
"""
else:
    # TIL 파일 로딩
    with open(til_path, "r", encoding="utf-8") as file:
        content = file.read()

    # 요약 요청
    summary_prompt = f"""
다음 내용을 마크다운 형식으로 요약해줘:

{content}
"""
    summary_completion = client.chat.completions.create(
        model="openai/gpt-oss-120b:hf-inference",
        messages=[{"role": "user", "content": summary_prompt}],
    )
    summary_text = summary_completion.choices[0].message.content.strip()

    # 응원 메시지 요청
    cheer_prompt = "하루를 기분 좋게 시작할 수 있는 희망찬 한국어 응원 한마디를 해줘. 간결하고 힘이 나는 말로 부탁해."
    cheer_completion = client.chat.completions.create(
        model="openai/gpt-oss-120b:hf-inference",
        messages=[{"role": "user", "content": cheer_prompt}],
    )
    cheer_text = cheer_completion.choices[0].message.content.strip()

    # README 구성
    readme_content = f"""# 🌞 오늘도 힘차게!

> {cheer_text}

---

## 📚 어제의 학습 요약 ({file_date})

{summary_text}

---

⏰ 자동 업데이트 시간: {timestamp} (KST)
"""

# README 저장
with open(readme_path, "w", encoding="utf-8") as file:
    file.write(readme_content)
