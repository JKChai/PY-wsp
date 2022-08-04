import numpy as np
import pandas as pd

df = pd.DataFrame(
    [{'0': np.nan,
  '1': 'Baseline',
  '2': 'Baseline',
  '3': 'Baseline',
  '4': 'V1',
  '5': 'V1',
  '6': 'V1',
  '7': 'V2',
  '8': 'V2',
  '9': 'V2'},
 {'0': 'UID',
  '1': 'test1',
  '2': 'test2',
  '3': 'test3',
  '4': 'test1',
  '5': 'test2',
  '6': 'test3',
  '7': 'test1',
  '8': 'test2',
  '9': 'test3'},
 {'0': 'xyzarf',
  '1': 'date1',
  '2': 'date2',
  '3': 'date3',
  '4': 'date4',
  '5': 'date5',
  '6': 'date2',
  '7': 'date6',
  '8': 'date7',
  '9': 'date8'},
 {'0': 'abcwer',
  '1': 'date9',
  '2': 'date10',
  '3': 'date11',
  '4': 'date1',
  '5': 'date3',
  '6': 'date5',
  '7': 'date6',
  '8': 'date9',
  '9': 'date8'},
 {'0': 'defdsg',
  '1': 'date1',
  '2': 'date2',
  '3': 'date3',
  '4': 'date4',
  '5': 'date5',
  '6': 'date2',
  '7': 'date6',
  '8': 'date7',
  '9': 'date8'}])

## clean null values
df = df.fillna("")

## combine 2 rows to 1 as a header
df.columns = (df.iloc[0] + " " + df.iloc[1]).str.strip()
df.columns.name = ""
df = df.drop([df.index[0],df.index[1]]) ## drop both rows
df = df.reset_index(drop=True) ## reset index

## unpivot data frame
df = pd.melt(df, id_vars=["UID"], var_name = "mash", value_name="test_date")

## expand 1 column into 2
df[["visit","type_of_test"]] = df["mash"].str.split(expand=True)

## rearrange and reorder data frame
df = df[["UID", "visit", "type_of_test", "test_date"]].sort_values(
    by = ["UID","visit", "type_of_test"]).reset_index(drop=True)
