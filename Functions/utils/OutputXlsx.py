import pandas as pd


def outputXlsx(path, mat):
    df = pd.DataFrame(mat)
    df.to_excel(f'{path}', index=False)
    print(path)
