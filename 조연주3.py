import pandas as pd

call_df=pd.read_csv('Calldata_2008.csv',encoding='utf-8',parse_dates=['일자(YYYYMMDD)'])
call_df.columns=['일자','연령','성별','발신자1','발신자2','대분류','중분류','통화비율']
#print(call_df)
rain_df=pd.read_csv('Raindata_2008.csv',encoding='cp949',parse_dates=['일시'])
rain_df.columns=['지점번호','지점명','일자','강수량','1시간최대강수량','1시간최대강수량시각']
#print(rain_df)
#print(call_df['대분류'].unique())
is_true=(call_df['발신자1']=='서울')&(call_df['대분류']=='음식점')
call_df=call_df[is_true]
print(call_df)
print(call_df['중분류'].unique())
call_df=call_df.drop(columns=['연령','성별','발신자1','발신자2','통화비율','대분류'])
print(call_df)
rain_df=rain_df.drop(columns=['지점번호','지점명','1시간최대강수량','1시간최대강수량시각'])
print(rain_df)
rain_df['강수량']=rain_df['강수량'].fillna(0)
print(rain_df)
tot_df=pd.merge(call_df,rain_df,on='일자')
print(tot_df)
no_rain=tot_df[tot_df['강수량']==0]
no_rain=pd.DataFrame(no_rain['중분류'].value_counts())
print(no_rain)
yes_rain=tot_df[tot_df['강수량']>=50]
yea_rain=pd.DataFrame(yes_rain['중분류'].value_counts())
print(yes_rain)

























































