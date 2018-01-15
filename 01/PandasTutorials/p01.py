import pandas as pd
df = pd.read_csv('Camera.csv', delimiter=';')
print "Price > 4500 : ", df[["Model", "Low resolution", "Price"]][df['Price'] > 4500].sortlevel()
print "mean : ", df['Low resolution'].mean()
df.fillna(0, inplace=True)
print "mean after cleaning : ", df['Low resolution'].mean()

df


# cleaning | data munging / data wrangling

