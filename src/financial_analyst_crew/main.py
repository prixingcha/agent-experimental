
from crew import FinancialAnalystCrew

def run():
    company_names = ["Tesla", "Apple"]
    for company_name in company_names:
        inputs = {
            "company_name": company_name,
        }
        FinancialAnalystCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
