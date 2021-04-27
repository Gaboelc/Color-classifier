# This bot is responsible for obtaining the data
# from all the color tables on the next page: https://web.njit.edu/~walsh/rgb_nobg/

import pandas as pd


class color_bot():
    
    def __init__(self):
        tables = pd.read_html('https://web.njit.edu/~walsh/rgb_nobg/')
        
	def get_tables(self, metadata=True):
     
		'''
		parameters:\n
  			metadata: Boolean parameter, decide whether to return the metadata lists. Default: True\n
		Return:\n
			if metadata = True:
					returns black/gray, blue, brown, green, orenge, red, violet, white, yellow, metal, metadata, credit metadata tables.\n
			if metadata = False:
					returns black/gray, blue, brown, green, orenge, red, violet, white, yellow, metal.
		'''
  
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

		if metadata:
			return blackGray_table, blue_table, brown_table, green_table, orange_table, red_table, violet_table, white_table, yellow_table, metal_table, metaData_table, creditsMetaData_table
		else:
			return blackGray_table, blue_table, brown_table, green_table, orange_table, red_table, violet_table, white_table, yellow_table, metal_table
