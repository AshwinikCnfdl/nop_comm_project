import pandas as pd
from pandas.io.common import file_exists


class Read_write_csv_file:

    @staticmethod
    def write_test_data(data):
        df = pd.DataFrame(data)
        df.to_csv(
           "C:/Users/hp/PycharmProjects/nop_comm_project/TestData/TestData.csv",
            mode="a",  # Append mode
            index=False,
            header=not file_exists,  # Write header only if the file doesn't exist
            encoding="utf-8"
        )

    @staticmethod
    def read_test_data(path):
        file_path = path
        df = pd.read_csv(path)
        return df

