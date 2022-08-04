import pandas as pd

df = pd.DataFrame({
"X":[10,15,13,33],
"Y":[22,45,67,89]})

print(df/df.sum(axis=0))