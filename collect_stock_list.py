import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup

# 미국 주식(나스닥, S&P500, 다우존스) 종목 리스트 수집 함수
def get_us_stocks():
    # S&P500
    sp500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    sp500_table = pd.read_html(sp500_url)[0]
    sp500 = sp500_table[['Symbol', 'Security']]
    sp500['Market'] = 'S&P500'

    # 나스닥 (yfinance 활용)
    nasdaq = yf.download('^IXIC', period='1d')  # 단순히 yfinance가 동작하는지 확인용
    # 실제 나스닥 종목 전체는 별도 파일/서비스 필요, 예시로 주요 종목만
    nasdaq_symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']
    nasdaq_list = []
    for symbol in nasdaq_symbols:
        info = yf.Ticker(symbol).info
        nasdaq_list.append({'Symbol': symbol, 'Security': info.get('shortName', ''), 'Market': 'NASDAQ'})
    nasdaq_df = pd.DataFrame(nasdaq_list)

    # 다우존스
    dow_url = 'https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average'
    # 2번째 테이블이 실제 종목 테이블임
    dow_table = pd.read_html(dow_url)[2]
    # 컬럼: Company, Symbol, ...
    dow = dow_table[['Symbol', 'Company']]
    dow.columns = ['Symbol', 'Security']
    dow['Market'] = 'DOWJONES'

    # 통합
    us_stocks = pd.concat([sp500, nasdaq_df, dow], ignore_index=True)
    us_stocks.to_csv('us_stocks.csv', index=False)
    print('미국 주식 종목 리스트(us_stocks.csv) 저장 완료')

# 한국 주식(코스피) 종목 리스트 수집 함수
def get_kospi_stocks():
    # 네이버 금융에서 코스피 전체 페이지 반복 크롤링
    import math
    base_url = 'https://finance.naver.com/sise/sise_market_sum.naver?sosok=0&page={}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    # 1페이지에서 전체 페이지 수 추출
    r = requests.get(base_url.format(1), headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    page_last = soup.select('td.pgRR a')
    if page_last:
        last_page = int(page_last[0]['href'].split('=')[-1])
    else:
        last_page = 1
    data = []
    for page in range(1, last_page + 1):
        r = requests.get(base_url.format(page), headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('table', class_='type_2')
        rows = table.find_all('tr')[2:]
        for row in rows:
            cols = row.find_all('td')
            if len(cols) > 1 and cols[1].find('a'):
                name = cols[1].get_text(strip=True)
                code = cols[1].find('a')['href'].split('=')[-1]
                data.append({'Symbol': code, 'Security': name, 'Market': 'KOSPI'})
    kospi = pd.DataFrame(data)
    kospi.to_csv('kospi_stocks.csv', index=False)
    print(f'코스피 전체 종목 리스트({len(kospi)}개, kospi_stocks.csv) 저장 완료')

if __name__ == '__main__':
    get_us_stocks()
    get_kospi_stocks()
