# Stock AI Website

A professional, free, AI-powered stock analysis website supporting US (NASDAQ, S&P500, Dow Jones, NYSE) and Korean (KOSPI, KOSDAQ) stocks.  
미국(NASDAQ, S&P500, 다우존스, NYSE) 및 한국(KOSPI, KOSDAQ) 주식을 지원하는 무료 AI 기반 주식 분석 웹사이트입니다.

---

## Features  
## 주요 기능

- Search stocks by ticker or company name (US & Korea)  
  미국/한국 종목 코드 또는 회사명으로 검색
- Analyze up to 5 years of historical data  
  최대 5년치 과거 데이터 분석
- Real AI prediction (Prophet) for up to 3 years into the future  
  Prophet 기반 AI로 향후 3년 예측
- All stocks for each market are auto-collected and managed as CSVs  
  각 시장의 전체 종목을 자동 수집 및 CSV로 관리
- Advanced, modern UI/UX (React + Vite)  
  최신 UI/UX (React + Vite)
- Real-time price and AI analysis (FastAPI backend)  
  실시간 가격 및 AI 분석 (FastAPI 백엔드)
- Publicly accessible (Vercel/Render/GitHub)  
  누구나 접속 가능 (Vercel/Render/GitHub)
- Automated deployment (CI/CD)  
  자동 배포(CI/CD)

---

## Demo  
## 데모

- **Frontend:** [https://stock-ai-website.vercel.app](https://stock-ai-website.vercel.app)
- **Backend API:** [https://stock-ai-website-backend.onrender.com](https://stock-ai-website-backend.onrender.com)

---

## How to Use  
## 사용 방법

1. Search for a stock by ticker or company name.  
   종목 코드 또는 회사명으로 검색하세요.
2. Select a stock to view the latest price and run AI analysis.  
   종목을 선택하면 최신 가격과 AI 예측을 볼 수 있습니다.
3. Click "AI 분석하기" to get a 3-year forecast chart and summary.  
   "AI 분석하기" 버튼을 누르면 3년 예측 차트와 요약이 표시됩니다.

---

## Tech Stack  
## 기술 스택

- **Frontend:** React, Vite, TypeScript, Recharts
- **Backend:** FastAPI, Python, yfinance, Prophet, pandas, BeautifulSoup
- **Deployment:** Vercel (frontend), Render (backend), GitHub

---

## Local Development  
## 로컬 개발 방법

```bash
# 1. Clone the repository
git clone https://github.com/minsk0429/stock-ai-website.git
cd stock-ai-website

# 2. Install frontend dependencies
cd frontend
npm install

# 3. Install backend dependencies
cd ../backend
pip install -r requirements.txt

# 4. Run backend (FastAPI)
uvicorn app.main:app --reload

# 5. Run frontend (Vite)
cd ../frontend
npm run dev
```

---

## Data Collection  
## 데이터 수집

- Run `collect_stock_list.py` to auto-collect all stock lists (US & Korea) and generate CSVs.  
  `collect_stock_list.py`를 실행하면 미국/한국 전체 종목 리스트가 자동으로 수집되어 CSV로 저장됩니다.

---

## AI Model Notice  
## AI 모델 안내

> Prophet is a statistical time series model for forecasting based on past data patterns. Sudden events are not reflected, and errors increase for long-term forecasts.  
> Prophet은 과거 데이터 패턴을 기반으로 미래를 예측하는 통계적 시계열 모델입니다. 갑작스러운 이벤트는 반영하지 못하며, 중장기 예측일수록 오차가 커질 수 있습니다.

---

## License  

MIT License
