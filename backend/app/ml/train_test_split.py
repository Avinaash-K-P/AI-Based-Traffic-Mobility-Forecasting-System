import pandas as pd

def split_dataset(
    df: pd.DataFrame,
    train_ratio: float = 0.8      
):
    split_index = int(len(df) * train_ratio)

    train_df = df.iloc[:split_index].copy()

    test_df = df.iloc[split_index:].copy()

    return train_df, test_df  
     