import boto3
import datetime

def time_diff(time):
    diff = datetime.datetime.now() - time
    seconds = int(diff.seconds)
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    elapsed_time=str(diff.days) + " day, " + "%d hour %02d minutes %02d seconds" % (hour, minutes, seconds)
    return elapsed_time,diff


def establish_session():
    return boto3.session.Session()