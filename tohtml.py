import pandas as pd
import numpy as np


html = pd.read_csv("instructions/resources/cities.csv")

result = html.to_html()

htmlText = open("data1.html", "w")
htmlText.write(result)
htmlText.close()
