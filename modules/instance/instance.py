import pandas as pd

regions = ['us-east-1','us-east-2']
indexd=['Instance-Id', 'Subnet-Id', 'Hostname', 'Public-Ip', 'Private-Ip', 'AMI-Id']

def create_instance_table(session):
    appended_data=[]
    for region in regions:
        ec2 = session.resource('ec2', region_name=region)
        for instance in ec2.instances.all(): 
            print("==============================================")
            print("Fetching Details for Instance- " + instance.id )
            
            df=  pd.DataFrame(indexd, columns=['Metadata'])
            df['Value'] = instance_detail(instance)
            appended_data.append(df)
    if not appended_data:
        detail = ['None','None','None','None','None','None']
        empty_data = pd.DataFrame(indexd,columns=['Metadata'])
        empty_data['Value'] = detail
        return empty_data
    data = pd.concat(appended_data)
    data.set_index('Metadata')
    return data


def create_instance_table2(session):
    df=  pd.DataFrame(indexd, columns=['Metadata'])
    for region in regions:
        ec2 = session.resource('ec2', region_name=region)
        for i,instance in enumerate(ec2.instances.all()):
            print("==============================================")
            print("Fetching Details for Instance- " + instance.id )
            df[f"Value_{i}"] = instance_detail(instance)
    df.set_index('Metadata')
    return df


def create_horizontal_instance_table(session):
    details=[]
    for region in regions:
        ec2 = session.resource('ec2', region_name=region)
        column=indexd
        for instance in ec2.instances.all():
            details.append(instance_detail(instance))
            print("==============================================")
            print("Fetching Details for Instance- " + instance.id )
    df =  pd.DataFrame(details, columns=column)
    return df


def instance_detail(instance):
    detail=[]
    detail.append(instance.id)
    detail.append(instance.subnet_id)
    detail.append(instance.private_dns_name)
    detail.append(instance.public_ip_address)
    detail.append(instance.private_ip_address)
    detail.append(instance.image_id)
    return detail
