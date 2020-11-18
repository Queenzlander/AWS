import boto3

iam = boto3.client('iam', region_name = 'us-east-1') 

users = ""
users_list = []
username_list = []
accesskeyid_list = []
status_list = []
status_filter = "both"

# Get list of users and place in list called users_list
iamusers = iam.list_users()["Users"]
for iamuser in iamusers:
	for key, value in iamuser.items():
		if key == 'UserName':
			users_list.append(value)
print('--------------')
print('The Users are...')
print(users_list)


#get Access Key info based on users in user_list from above
for users in users_list:
	iamusers = iam.list_access_keys(UserName = users)["AccessKeyMetadata"]
	for iamuser in iamusers: 
		if iamuser['Status'] == status_filter or status_filter == 'both':
			for key, value in iamuser.items():
				if key == 'UserName':
					username_list.append(value)	
				elif key == 'AccessKeyId':
					accesskeyid_list.append(value)
				elif key == 'Status':
					status_list.append(value)

print('\n--------------')
print('The users; Name, Key Id and Status are...')
print(username_list, accesskeyid_list, status_list)
