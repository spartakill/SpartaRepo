import boto3
import pprint as pp
import json
import pandas
import pandas as pd
import io

import s3transfer.processpool

# s3_client = boto3.client('s3')
# s3_resource = boto3.resource('s3')
#
# # bucket_list = s3_client.list_buckets()
# bucket_name = 'data-eng-resources'
# bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name, Prefix='big-data/Adventure Works')

# bucket = s3_resource.Bucket(bucket_name)
# print(bucket)
# objects = bucket.objects.all()
# print(object)
# for obj in objects:
#     print(obj.key)

# client is simpler and gets stuff done quicker, more documentation too

# s3_object = s3_client.get_object(Bucket=bucket_name, Key='python/chatbot-intent.json')
# pp.pprint(s3_object)

# strbody = s3_object['Body'].read()
# # print(strbody)
# body = json.loads(strbody)
# pp.pprint(body)

# s3_object = s3_client.get_object(Bucket=bucket_name, Key='python/happiness-2019.csv')
# pp.pprint(s3_object) # csv file not json so need to import pandas package to interpret csv

# pp.pprint(s3_object['Body'].read())

# df = pd.read_csv(s3_object['Body'])
# print(df)

dict_to_upload = {'name': 'data', 'status': 1}

# s3_client.put_object(Body=json.dumps(dict_to_upload), # needs to include json.dumps
#                      Bucket=bucket_name,
#                      Key='Test249/killian.json')
# s3_client.upload_file(Filename='new_json.json',
#                       Bucket=bucket_name,
#                       Key='Test249/killian2.json')

# if we uploaded a dataframe we need a string buffer to upload
#
# df = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,1]])
# str_buffer = io.StringIO()
# df.to_csv(str_buffer)
# s3_client.put_object(Body=str_buffer.getvalue(),
#                      Bucket=bucket_name,
#                      Key='Test249/killian.csv')

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

bucket_name = 'data-eng-resources'

bucket = s3_resource.Bucket(bucket_name)
print(bucket)
objects = bucket.objects.all()
print(object)
for obj in objects:
    print(obj.key)

s3_object = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market.csv')
s3_object_1 = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market-mon.csv')
s3_object_2 = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market-tues.csv')

df_fish = pd.read_csv(s3_object['Body'])
df_fish_1 = pd.read_csv(s3_object_1['Body'])
df_fish_2 = pd.read_csv(s3_object_2['Body'])


df1 = pd.concat([df_fish, df_fish_1, df_fish_2])

grouped_fish = df1.groupby('Species')
fish = grouped_fish.mean()
print(fish)

str_buffer = io.StringIO()
fish.to_csv(str_buffer)
s3_client.put_object(Body=str_buffer.getvalue(),
                     Bucket=bucket_name,
                     Key='Data249/fish/killian.csv')