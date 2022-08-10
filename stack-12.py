import numpy as np
import pandas as pd

df = pd.DataFrame({
"X":['',15,np.nan,33],
"Y":[22,45,67,89]})

print(df['X'].isnull())