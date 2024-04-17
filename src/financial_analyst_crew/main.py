
from crew import FinancialAnalystCrew

def run():
    stock_tickers = ["TSLA", "AAPL"]
    FinancialAnalystCrew().crew().kickoff(stock_tickers)

if __name__ == "__main__":
    run()




