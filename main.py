from config import summary_json, usa_json
from etl import summary_etl, data_etl


if __name__ == "__main__":
    
    # Load data from the summary API into summary table
    data_etl(summary_json['Countries'], 'summary', [93, 98, 165, 171, 199, 219])
    # Load data for confirmed US cases into us_cases table
    data_etl(usa_json, 'us_cases', 0)