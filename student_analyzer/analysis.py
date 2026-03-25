import pandas as pd

def compute_average(df):
    df["average"] = (df["math_score"] + df["science_score"]) / 2
    return df

def get_top_student(df):
    return df.loc[df["average"].idxmax()]

def get_low_performers(df):
    return df[df["average"] < 60]