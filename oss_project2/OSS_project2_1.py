import pandas as pd 
from pandas import Series, DataFrame

def requirement_1(df):
	y_2015 = df[df['year'] == 2015]
	y_2016 = df[df['year'] == 2016]
	y_2017 = df[df['year'] == 2017]
	y_2018 = df[df['year'] == 2018]
	
	print("< Requirement 1 >")
	print("==========top 10 players in hits in 2015=========")
	print(y_2015.sort_values(by=['H'], ascending=False).head(10)[['batter_name', 'H']])
	print("==========top 10 players in batting average in 2015=========")
	print(y_2015.sort_values(by=['avg'], ascending=False).head(10)[['batter_name', 'avg']])
	print("==========top 10 players in homerun in 2015=========")
	print(y_2015.sort_values(by=['HR'], ascending=False).head(10)[['batter_name', 'HR']])	
	print("==========top 10 players in on-base percentage in 2015=========")
	print(y_2015.sort_values(by=['OBP'], ascending=False).head(10)[['batter_name', 'OBP']])
	print("==========top 10 players in hits in 2016=========")
	print(y_2016.sort_values(by=['H'], ascending=False).head(10)[['batter_name', 'H']])
	print("==========top 10 players in batting average in 2016=========")
	print(y_2016.sort_values(by=['avg'], ascending=False).head(10)[['batter_name', 'avg']])
	print("==========top 10 players in homerun in 2016=========")
	print(y_2016.sort_values(by=['HR'], ascending=False).head(10)[['batter_name', 'HR']])
	print("==========top 10 players in on-base percentage in 2016=========")
	print(y_2016.sort_values(by=['OBP'], ascending=False).head(10)[['batter_name', 'OBP']])
	print("==========top 10 players in hits in 2017=========")
	print(y_2017.sort_values(by=['H'], ascending=False).head(10)[['batter_name', 'H']])
	print("==========top 10 players in batting average in 2017=========")
	print(y_2017.sort_values(by=['avg'], ascending=False).head(10)[['batter_name', 'avg']])
	print("==========top 10 players in homerun in 2017=========")
	print(y_2017.sort_values(by=['HR'], ascending=False).head(10)[['batter_name', 'HR']])
	print("==========top 10 players in on-base percentage in 2017=========")
	print(y_2017.sort_values(by=['OBP'], ascending=False).head(10)[['batter_name', 'OBP']])
	print("==========top 10 players in hits in 2018=========")
	print(y_2018.sort_values(by=['H'], ascending=False).head(10)[['batter_name', 'H']])
	print("==========top 10 players in batting average in 2018=========")
	print(y_2018.sort_values(by=['avg'], ascending=False).head(10)[['batter_name', 'avg']])
	print("==========top 10 players in homerun in 2018=========")
	print(y_2018.sort_values(by=['HR'], ascending=False).head(10)[['batter_name', 'HR']])
	print("==========top 10 players in on-base percentage in 2018=========")
	print(y_2018.sort_values(by=['OBP'], ascending=False).head(10)[['batter_name', 'OBP']])
def requirement_2(df):
	y_2018 = df[df['p_year'] == 2018]
	
	print("< Requirement 2 >")
	print("=======highest war by 포수 in 2018=========")
	print(y_2018[y_2018['cp'] == "포수"].sort_values(by=['war']).tail(1)[['batter_name','war', 'cp']])
	print("=======highest war by 1루수 in 2018=========")
	print(y_2018[y_2018['cp'] == "1루수"].sort_values(by=['war']).tail(1)[['batter_name','war', 'cp']])
	print("=======highest war by 2루수 in 2018=========")
	print(y_2018[y_2018['cp'] == "2루수"].sort_values(by=['war']).tail(1)[['batter_name','war', 'cp']])
	print("=======highest war by 3루수 in 2018=========")
	print(y_2018[y_2018['cp'] == "3루수"].sort_values(by=['war']).tail(1)[['batter_name','war', 'cp']])
	print("=======highest war by 유격수 in 2018=========")
	print(y_2018[y_2018['cp'] == "유격수"].sort_values(by=['war']).tail(1)[['batter_name','war', 'cp']])
	print("=======highest war by 좌익수 in 2018=========")
	print(y_2018[y_2018['cp'] == "좌익수"].sort_values(by=['war']).tail(1)[['batter_name','war', 'cp']])
	print("=======highest war by 중견수 in 2018=========")
	print(y_2018[y_2018['cp'] == "중견수"].sort_values(by=['war']).tail(1)[['batter_name','war', 'cp']])
	print("=======highest war by 우익수 in 2018=========")
	print(y_2018[y_2018['cp'] == "우익수"].sort_values(by=['war']).tail(1)[['batter_name','war', 'cp']])
def requirement_3(df):
	corr_R = df['R'].corr(df['salary'])
	corr_H = df['H'].corr(df['salary'])
	corr_HR = df['HR'].corr(df['salary'])
	corr_RBI = df['RBI'].corr(df['salary'])
	corr_SB = df['SB'].corr(df['salary'])
	corr_war = df['war'].corr(df['salary'])
	corr_avg = df['avg'].corr(df['salary'])
	corr_OBP = df['OBP'].corr(df['salary'])
	corr_SLG = df['SLG'].corr(df['salary'])

	obj_corr = pd.Series([corr_R, corr_H, corr_HR, corr_RBI, corr_SB, corr_war, corr_avg, corr_OBP, corr_SLG])

	obj_corr.index = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']
	print("< Requirement 3 >")
	print("=========== correlation with salary ============")
	print(obj_corr)
	print("the highest correlation with salary : ", obj_corr.idxmax())
if __name__ == "__main__":
	data = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
	requirement_1(data)
	print("\n")
	requirement_2(data)
	print("\n")
	requirement_3(data)
