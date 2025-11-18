import pandas

def save_to_csv(filename, row_dict):
    df = pandas.DataFrame([row_dict])
    sep = " "

    df.to_csv(filename, mode="a", header=False, index=False, sep=sep)
