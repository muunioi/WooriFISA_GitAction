# 🌞 오늘도 힘차게!

> 🌟 “오늘은 네가 빛날 차례야! 힘내, 파이팅!” 🌟

---

## 📚 어제의 학습 요약 (250805)

## TIL : 250805 – GitHub Actions 로 크론잡 자동화  

### 📌 GitHub Actions란?  
- GitHub 레포지토리 안에서 **CI/CD 파이프라인**을 정의·실행하는 도구  
- `workflow(.yml)` 로 **빌드·테스트·배포** 절차를 자동화  

---

## 🔑 핵심 개념  

| 구성요소 | 설명 |
|---|---|
| **Workflow** | `.github/workflows/` 아래에 저장되는 전체 자동화 정의 파일 |
| **Event** | 워크플로우 실행 트리거 (push, PR, `schedule` 등) |
| **Job** | 실행 단위, 여러 **Step** 으로 구성, 병렬·순차 실행 가능 |
| **Step** | 개별 명령어나 Action |
| **Action** | 재사용 가능한 작업 블록 (테스트, 빌드, 알림 등) |
| **Runner** | 워크플로우를 실제로 수행하는 가상머신 (GitHub‑hosted 또는 self‑hosted) |

---

## ⚙️ 프로젝트 구성  

### 1. `update_weather.py`  
- **역할**: OpenWeather API 로 서울 날씨를 받아 `README.md`에 최신 정보 기록  
- 주요 함수  
  - `get_weather()` – API 호출  
  - `update_readme()` – `README.md` 수정  

### 2. 워크플로우 파일 `.github/workflows/update_weather.yml`  
```yaml
on:
  schedule:
    - cron: "0 6 * * *"   # 매일 06:00 UTC (KST 15:00)
  workflow_dispatch:      # 수동 실행 가능
```
**주요 단계**  
1. 레포지토리 체크아웃  
2. Python 환경 셋업  
3. `update_weather.py` 실행  
4. 변경 내용 커밋 & 푸시  

---

## 🔐 Secrets 설정  
- `Settings > Secrets and variables > Actions` 에 **Repository Secret** 으로 `OPENWEATHER_API_KEY` 등록  

---

## 🔁 크론잡 흐름  

1. 지정된 시각에 GitHub Action 실행 → OpenWeather API 호출  
2. 받아온 날씨 정보를 `README.md`에 반영  
3. 파일 변경을 자동 커밋·푸시 → 레포지토리 업데이트  

---

### ✅ 결과  

- **매일 최신 날씨가 자동으로 README에 반영**  
- GitHub Actions 로 **전체 자동화(스케줄링 → 실행 → 커밋)** 흐름을 체험 가능  

---  

*위 내용은 원문을 마크다운 형식으로 핵심만 추려 요약한 것입니다.*

---

⏰ 자동 업데이트 시간: 2025-08-06 12:09:30 (KST)
