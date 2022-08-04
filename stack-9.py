import pandas as pd

df = pd.DataFrame({
"Calendar":["2020-01-01","2020-02-01","2020-03-01","2020-04-01"],
"X":[10,15,13,33],
"Y":[22,45,67,89]})


print(pd.melt(df, id_vars="Calendar", var_name="Type",value_name="Act_value"))