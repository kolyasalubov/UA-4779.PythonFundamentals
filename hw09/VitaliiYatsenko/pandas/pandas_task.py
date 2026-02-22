import pandas as pd 

data = pd.read_csv('data.csv', skipinitialspace=True)


# print(data.columns.tolist()) #['IP', ' Number of bytes', ' Country', ' Username']

data.columns = data.columns.str.strip()

# print(data.columns.tolist()) #['IP', 'Number of bytes', 'Country', 'Username']


total_used_bytes = data['Number of bytes'].sum() #the total number of bytes used

print(total_used_bytes)

count_used_bytes = data['Number of bytes'].count()


avg_used_bytes = total_used_bytes / count_used_bytes #the average number of bytes per request

print(avg_used_bytes)

country = data.groupby('Country').size()
res_country = country.sort_values(ascending=False)

most_popular_country = res_country.index[0]

print(most_popular_country) #the most popular country (by the number of requests)

users = data.groupby('Username')['Number of bytes'].sum()

res_users = users.sort_values(ascending=False)

third_user = res_users.index[2] 

print(third_user) #the user who is on the 3rd place by the number of bytes

group_by_country = data.groupby("Country")['Number of bytes'].agg(['nunique', 'sum'])

# group_by_country = data.groupby("Country").agg({'Number of bytes': 'sum', 'Username': 'count'})



bytes_ukraine = group_by_country.loc['Ukraine'] 

print(bytes_ukraine['sum']) #the number of bytes used by users from Ukraine

bytes_uk = group_by_country.loc['UK'] 



uniq_user = data['Username'].nunique() 

print(uniq_user) #number of unique users


number_of_request = data.groupby('Country').size()

num_of_requests_ua = number_of_request.loc['Ukraine']



num_of_requests_uk = number_of_request.loc['UK']

avg_bytes_ua = bytes_ukraine / num_of_requests_ua 

avg_bytes_ua['sum'] #490.8095238095238

avg_bytes_uk = bytes_uk / num_of_requests_uk 

avg_bytes_uk['sum'] #524.1428571428571

diff = avg_bytes_ua['sum'] - avg_bytes_uk['sum']

rounded_diff = round(diff) 

print(rounded_diff) #the difference between the average number of bytes per request between users from Ukraine and the UK (rounded to the nearest whole number)d


group_by_ip = data.groupby('IP')['Number of bytes'].sum() 


ip = data['IP'].nunique()

df = pd.DataFrame(group_by_ip)

sum_of_bytes = df['Number of bytes'].sum()

avg_bytes_per_ip = round(sum_of_bytes / ip)


print(avg_bytes_per_ip) #average number of bytes per IP address


users_in_country = data.groupby('Country')['Username'].nunique()



total = (users_in_country['Ukraine'] + users_in_country['UK'] 
         + users_in_country['France'] + users_in_country['Germany'] + users_in_country['Poland'])


print(total)


results = pd.DataFrame({'The total number of bytes used': [total_used_bytes],
                         'The average number of bytes per request': [avg_used_bytes],
                         'The most popular country': [most_popular_country],
                         'The user who is on the 3rd place by the number of bytes': [third_user],
                         'The number of bytes used by users from Ukraine': [bytes_ukraine['sum']],
                         'The number of unique users': [uniq_user],
                         'The difference between the average number of bytes per request between users \
                            from Ukraine and the UK': [rounded_diff],
                            'The average number of bytes per IP address': [avg_bytes_per_ip],
                            'The total number of users from Europe': [total]})

results.to_csv('results11.csv', index=False)

print(results)




# 500516
# 500.516
# India
# fjfyqotm
# 51535
# 500
# -33
# 500
# 1001
# 242




