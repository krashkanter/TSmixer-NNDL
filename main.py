import pandas as pd
import numpy as np


def main():
    data = pd.read_csv("datasets/559_train.csv")
    df = pd.DataFrame(data)
    df.head()


if __name__ == "__main__":
    main()
