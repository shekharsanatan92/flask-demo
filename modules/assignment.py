import boto3
import pandas as pd
import datetime

regions = ['us-east-1','us-east-2']

def create_instance_table():
    appended_data=[]
    for region in regions:
        indexd=['Instance-Id', 'Subnet-Id', 'Hostname', 'Public-Ip', 'Private-Ip', 'AMI-Id']
        session = boto3.session.Session()
        ec2 = session.resource('ec2', region_name=region)
        for instance in ec2.instances.all():
            detail=[]
            detail.append(instance.id)
            detail.append(instance.subnet_id)
            detail.append(instance.private_dns_name)
            detail.append(instance.public_ip_address)
            detail.append(instance.private_ip_address)
            detail.append(instance.image_id)
            
            print("==============================================")
            print("Fetching Details for Instance- " + instance.id )
            
            df=  pd.DataFrame(indexd, columns=['Metadata'])
            df['Value'] = detail
            appended_data.append(df)
    if not appended_data:
        detail = ['None','None','None','None','None','None']
        empty_data = pd.DataFrame(indexd,columns=['Metadata'])
        empty_data['Value'] = detail
        return empty_data
    data = pd.concat(appended_data)
    data.set_index('Metadata')
    return data


def create_horizontal_instance_table():
    details=[]
    for region in regions:
        session = boto3.session.Session()
        ec2 = session.resource('ec2', region_name=region)
        column=['Instance-Id', 'Subnet-Id', 'Hostname', 'Public-Ip', 'Private-Ip', 'AMI-Id']
        for instance in ec2.instances.all():
            detail=[]
            detail.append(instance.id)
            detail.append(instance.subnet_id)
            detail.append(instance.private_dns_name)
            detail.append(instance.public_ip_address)
            detail.append(instance.private_ip_address)
            detail.append(instance.image_id)
            details.append(detail)
            print("==============================================")
            print("Fetching Details for Instance- " + instance.id )
    df =  pd.DataFrame(details, columns=column)
    return df


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d hour %02d minutes %02d seconds" % (hour, minutes, seconds)


def emr_details():
    lessthan24=[]
    morethan24=[]
    for region in regions:
        session = boto3.session.Session()
        client = session.client('emr',region_name=region)
        response = client.list_clusters(
            ClusterStates=['STARTING','BOOTSTRAPPING','RUNNING','WAITING','TERMINATED_WITH_ERRORS','TERMINATED'])

        column=['EMR_ID', 'Creation_Date', 'Elapsed_Time']

        for each in response['Clusters']:

            detail=[]
            detail.append(each['Id'])
            
            ct=each['Status']['Timeline']['CreationDateTime']
            naive=ct.replace(tzinfo=None)
            detail.append(naive)
            
            diff = datetime.datetime.now() - naive
            et= str(diff.days) + " day, " + convert(int(diff.seconds))
            detail.append(et)
            
            if int(diff.days)>0:
                morethan24.append(detail)
            else:
                lessthan24.append(detail)

    df1 = pd.DataFrame(lessthan24, columns=column)
    df2 = pd.DataFrame(morethan24, columns=column)
    return df1,df2
