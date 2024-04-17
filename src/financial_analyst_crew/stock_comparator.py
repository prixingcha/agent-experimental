
class StockComparator:
    def compare_stocks(self, stock_data):
        results = {}
        for stock, metrics in stock_data.items():
            pe_ratio = metrics['earnings'] / metrics['share_price']
            results[stock] = {'PE_ratio': pe_ratio}
        better_stock = max(results, key=lambda x: results[x]['PE_ratio'])
        return better_stock, results

def run_comparison():
    comparator = StockComparator()
    better_stock, analysis = comparator.compare_stocks(results)
    print(f"Better stock: {better_stock}")
    print("Detailed Analysis:")
    for stock, metrics in analysis.items():
        print(f"{stock}: {metrics}")
