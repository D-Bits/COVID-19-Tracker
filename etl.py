from config import summary_json
import pandas as pd


def etl():

    df = pd.DataFrame(summary_json['Countries'])
    # Drop slug field
    cleaned_data = df.drop(['Slug'], axis=1)


    print(cleaned_data)


etl()