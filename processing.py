import pandas as pd
def preprocess(df, region):

    # filtering for summer olympics
    df = df[df["Season"] == "Summer"]
    # merging region with df on NOC
    df = df.merge(region, on="NOC", how='left')
    # dropping duplicate
    df.drop_duplicates(inplace=True)
    # one hot encoding
    df = pd.concat([df,pd.get_dummies(df["Medal"])], axis=1)
    return df



