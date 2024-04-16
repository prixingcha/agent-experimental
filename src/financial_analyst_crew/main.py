import os
from crew import FinancialAnalystCrew

def run():
    inputs = {
        'company_name': 'Tesla',
    }
    FinancialAnalystCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
