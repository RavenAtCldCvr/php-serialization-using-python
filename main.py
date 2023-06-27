from IPython.display import display
import pandas as pd
import phpserialize
import os
import argparse

def read_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() == '.csv':
        return pd.read_csv(file_path)
    elif file_extension.lower() == '.parquet':
        return pd.read_parquet(file_path)
    else:
        raise ValueError('Invalid file type. Only CSV and Parquet files are supported.')

def expand_php_values_into_dataframe(dataframe, column_name, output_file):
    try:
        dataframe[column_name] = dataframe[column_name].apply(lambda x: phpserialize.loads(x.encode()))
        print_serialized_php_object(dataframe, column_name)
        df2 = expand_dict(dataframe, column_name)
        display(df2)
        df2.to_csv(output_file, index=False)
    except KeyError:
        print(f"Column '{column_name}' not found in dataframe.")
    except Exception as e:
        print("An error occurred during deserialization:", str(e))

def print_serialized_php_object(dataframe, column_name):
    for idx, row in dataframe.iterrows():
            serialized_dict = row[column_name]  # assuming column_name is the column with the serialized data
            if isinstance(serialized_dict, dict):
                for key, value in serialized_dict.items():
                    print(f"Key: {key.decode('utf-8')}, Value: {value}")  # decode the byte string key to a normal string

def expand_dict(dataframe, column_name):
    # Check if the column exists in the DataFrame
    if column_name in dataframe.columns:
        # Apply a function that creates new columns for each key in the dictionary
        dataframe = dataframe.join(dataframe[column_name].apply(lambda x: pd.Series({k.decode('utf-8'): v for k, v in x.items()})))
        # Drop the original column
        dataframe = dataframe.drop(columns=[column_name])
    else:
        print(f"Column '{column_name}' not found in dataframe.")
    return dataframe

def main(file_path, column_name, output_file):
    df = read_file(file_path)
    expand_php_values_into_dataframe(df, column_name, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Path to the CSV or Parquet file")
    parser.add_argument("column_name", help="Name of the column containing PHP serialized data")
    parser.add_argument("output_file", help="Path to store the expanded CSV or Parquet file")
    args = parser.parse_args()
    main(args.file_path, args.column_name, args.output_file)
