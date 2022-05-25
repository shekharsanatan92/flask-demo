import pandas as pd
from modules.generic.generic import time_diff


regions = ['us-east-1','us-east-2']

def create_emr_table(session):
    lessthan24=[]
    morethan24=[]
    column=['EMR_ID', 'Creation_Date', 'Elapsed_Time']
    for region in regions:    
        client = session.client('emr',region_name=region)
        response = client.list_clusters(
            ClusterStates=['STARTING','BOOTSTRAPPING','RUNNING','WAITING','TERMINATED_WITH_ERRORS','TERMINATED'])

        for cluster in response['Clusters']:
            emr_cluster_detail(cluster,lessthan24,morethan24)

    df1 = pd.DataFrame(lessthan24, columns=column)
    df2 = pd.DataFrame(morethan24, columns=column)
    return df1,df2


def emr_cluster_detail(cluster,lessthan24,morethan24):
    elapsed_time,diff=time_diff(emr_creation_time(cluster))
    detail=[]
    detail.append(cluster['Id'])
    detail.append(emr_creation_time(cluster))
    detail.append(elapsed_time)
    if int(diff.days)>0:
        morethan24.append(detail)
    else:
        lessthan24.append(detail)


def emr_creation_time(cluster):
    ct= cluster['Status']['Timeline']['CreationDateTime']
    naive=ct.replace(tzinfo=None)
    return naive