from aws_lib.aws_config.aws_config_reader import AwsConfigurationReader
from aws_lib.aws_ec2.aws_ec2_instance import EC2Instance
from aws_lib.aws_key_pairs.aws_key_pairs import AwsKeyPair


def test_configuration_reader():
    print('Test configuration reader')
    reader = AwsConfigurationReader()
    print(reader.config)
    print(reader.credentials)

def test_key_pair():
    print('Test key pair')
    aws_key_pair = AwsKeyPair()
    aws_key_pair.create_key_pair(key_name='MyTestKey')

if __name__ == "__main__":

    test_configuration_reader()
    test_key_pair()

    #foo = EC2Instance()
    #foo.create_instance()
