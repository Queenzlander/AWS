import boto3

client = boto3.client('ec2')
ec2 = boto3.resource('ec2')

vpcid_list = []
subnetid_list = []

response = client.describe_vpcs()['Vpcs']
for respond in response:
#	print(respond['VpcId'])
	vpcid_list.append(respond['VpcId'])

print('--------------')
print('The VPC Ids are...')
print(vpcid_list)
print('--------------')
response = client.describe_subnets()['Subnets']
for respond in response:
#	print(respond)
#	print(respond.keys())
	subnetid_list.append(respond.get('SubnetId'))

print('list of Subnet Ids is ')
print(subnetid_list)	
