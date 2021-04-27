# 

import pandas as pd

tables = pd.read_html('https://web.njit.edu/~walsh/rgb_nobg/')

blackGray_table = tables[2]
blue_table = tables[3]
brown_table = tables[4]
green_table = tables[5]
orange_table = tables[6]
red_table = tables[7]
violet_table = tables[8]
white_table = tables[9]
yellow_table = tables[10]
metal_table = tables[12]
metaData_table = tables[11]
creditsMetaData_table = tables[14]