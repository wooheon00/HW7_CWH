import pandas as pd
import numpy as np

def main():
    df = pd.read_csv('q4.csv', encoding='cp949')

    new_df = df[['2022년_계_총인구수','2022년_남_총인구수','2022년_여_총인구수']]
    new_df = new_df.rename(columns={'2022년_계_총인구수': 'total', '2022년_남_총인구수': 'Male', '2022년_여_총인구수': 'Female'})
    new_df = new_df.set_index(df['행정구역'])
    
    print(new_df)
if __name__ == "__main__":
    main()