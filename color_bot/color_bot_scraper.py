# This bot is responsible for obtaining the data
# from all the color tables on the next page: https://web.njit.edu/~walsh/rgb_nobg/

import pandas as pd

class color_bot:
    
    def __init__(self, link='https://web.njit.edu/~walsh/rgb_nobg/'):
        tables = pd.read_html(link)
        
        self.blackGray_table = tables[2]
        self.blue_table = tables[3]
        self.brown_table = tables[4]
        self.green_table = tables[5]
        self.orange_table = tables[6]
        self.red_table = tables[7]
        self.violet_table = tables[8]
        self.white_table = tables[9]
        self.yellow_table = tables[10]
        self.metal_table = tables[12]
        self.metaData_table = tables[11]
        self.creditsMetaData_table = tables[14]
        
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

        if metadata == True:
            return self.blackGray_table, self.blue_table, self.brown_table, self.green_table, self.orange_table, self.red_table, self.violet_table, self.white_table, self.yellow_table, self.metal_table, self.metaData_table, self.creditsMetaData_table
        else:
            return self.blackGray_table, self.blue_table, self.brown_table, self.green_table, self.orange_table, self.red_table, self.violet_table, self.white_table, self.yellow_table, self.metal_table


    def export_tables(self, path='', metadata=False):
        '''
        Export all tables as csv\n
        parameters:\n
			path: String parameter, Specify the path in which the files will be exported.
            metadata: Boolean parameter, decide whether to export the metadata lists. Default: False
		return:
			None
        '''
        if metadata == True:
            self.blackGray_table.to_csv(path + 'Black_gray.csv')
            self.blue_table.to_csv(path + 'Blue.csv')
            self.brown_table.to_csv(path + 'Brown.csv')
            self.green_table.to_csv(path + 'Green.csv')
            self.orange_table.to_csv(path + 'Orange.csv')
            self.red_table.to_csv(path + 'Red.csv')
            self.violet_table.to_csv(path + 'Violet.csv')
            self.white_table.to_csv(path + 'White.csv')
            self.yellow_table.to_csv(path + 'Yellow.csv')
            self.metal_table.to_csv(path + 'Metal_colors.csv')
            self.metaData_table.to_csv(path + 'Meta_data.csv')
            self.creditsMetaData_table.to_csv(path + 'Credits_meta_data.csv')
        else:
            self.blackGray_table.to_csv(path + 'Black_gray.csv')
            self.blue_table.to_csv(path + 'Blue.csv')
            self.brown_table.to_csv(path + 'Brown.csv')
            self.green_table.to_csv(path + 'Green.csv')
            self.orange_table.to_csv(path + 'Orange.csv')
            self.red_table.to_csv(path + 'Red.csv')
            self.violet_table.to_csv(path + 'Violet.csv')
            self.white_table.to_csv(path + 'White.csv')
            self.yellow_table.to_csv(path + 'Yellow.csv')
            self.metal_table.to_csv(path + 'Metal_colors.csv')
        
        print('All files were exported!')