
import aiohttp
import asyncio
from sec_api import QueryApi

class SECTools:
    async def fetch_filing_details(self, stock):
        query_api = QueryApi(api_key=os.environ['SEC_API_API_KEY'])
        query = {
            "query": {
                "query_string": {
                    "query": f"ticker:{stock} AND formType:\"10-Q\""
                }
            },
            "from": "0",
            "size": "1",
            "sort": [{"filedAt": {"order": "desc"}}]
        }
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.sec-api.io', params=query) as response:
                data = await response.json()
                return data['filings'][0]['linkToFilingDetails'] if data['filings'] else None

async def main():
    sec_tools = SECTools()
    stocks = ['AAPL', 'TSLA']
    tasks = [sec_tools.fetch_filing_details(stock) for stock in stocks]
    results = await asyncio.gather(*tasks)
    print(results)

if __name__ == '__main__':
    asyncio.run(main())
