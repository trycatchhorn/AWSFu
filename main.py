from aws_lib.aws_config.aws_config_reader import AwsConfigurationReader
from aws_lib.aws_ec2.aws_ec2_instance import EC2Instance

if __name__ == "__main__":

    reader = AwsConfigurationReader()
    print(reader.config)
    print(reader.credentials)

    foo = EC2Instance()

    foo.create_instance()
