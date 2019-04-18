from aws_lib.aws_config.aws_config_reader import AwsConfigurationReader

if __name__ == "__main__":
    
    reader = AwsConfigurationReader()
    print(reader.config)
    print(reader.credentials)
