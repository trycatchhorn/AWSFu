#import boto3
from lib.aws_config_reader.aws_config import AwsConfiguration
from lib.aws_config_reader.aws_config import AwsConfigurationReader

if __name__ == "__main__":
    print('hello')
    reader = AwsConfigurationReader()
    print(reader.config)
    print(reader.credentials)

