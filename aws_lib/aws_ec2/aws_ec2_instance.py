import boto3
from aws_lib.aws_config.aws_config_reader import AwsConfigurationReader

class EC2Instance(object):

    def __init__(self):
        aws_config_reader = AwsConfigurationReader()

        session = boto3.Session(
            aws_access_key_id=aws_config_reader.credentials.aws_access_key_id,
            aws_secret_access_key=aws_config_reader.credentials.aws_secret_access_key
            )
        print(session)


    def create_instance(self):
        ec2 = boto3.resource('ec2')
        instance = ec2.create_instances(
            ImageId = 'ami-05af84768964d3dc0',
            MinCount = 1,
            MaxCount = 1,
            InstanceType = 't2.micro'
            )
        print(instance[0].id)

