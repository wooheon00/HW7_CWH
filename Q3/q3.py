import pandas as pd
import numpy as np

def main():
    
    df = pd.DataFrame([[1000,25],[280,120],[900,30]], index=['store1','store2','store3'], columns=['unit price', 'number'])
    print(df)
    print("\n")
    
    df['total price'] = df['unit price']*df['number']
    print(df)
    print("\n")
    
    df_sort = df.sort_values(by='total price',ascending=False)
    print(df_sort[0:2])

    
if __name__ == "__main__":
    main()