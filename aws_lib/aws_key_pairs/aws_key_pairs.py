import boto3
import logging
from botocore.exceptions import ClientError, ParamValidationError
from os import path


class AwsKeyPair(object):

    def __init__(self):
        self._ec2 = boto3.client('ec2')

    def describe_key_pair(self):
        return ec2.describe_key_pair()


    def _write_key_pair_to_file(self, key_name, key_pair):
        key_pair_out = str(key_pair['KeyMaterial'])

        # Check if key_name exists in ~/.ssh/
        key_file = key_name + str('.pem')
        key_file_path = path.join(path.expanduser("~"), '.ssh/' + key_file)
        with open(key_file_path, 'w+') as outfile:
            # Write key pair to file
            outfile.write(key_pair_out)


    def create_key_pair(self, key_name):
        # Reference:
        #https://books.google.dk/books?id=a9fHPSBxaGcC&pg=PA13&lpg=PA13&dq=Invalid+Key+Pair.Duplicate+try+catch+python&source=bl&ots=3DevqzhNlh&sig=ACfU3U0jsdDAymBx9pxM5rkBypK3jpKyAQ&hl=da&sa=X&ved=2ahUKEwjS6LTxsOThAhWFYlAKHbTTDk4Q6AEwA3oECAkQAQ#v=onepage&q=Invalid%20Key%20Pair.Duplicate%20try%20catch%20python&f=false
        # https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/key-pairs.html
        # Create key pair from key_name
        try:
            key_pair = self._ec2.create_key_pair(KeyName=key_name)
            self._write_key_pair_to_file(key_name, key_pair)
        except ClientError as e:
#            logging.error("Received error: %s", e, exc_info=True)
            if e.response['Error']['Code'] == 'InvalidKeyPair.Duplicate':
                print('Wee Duplicate')
                # Get existing key-pair
            else:
                print("Unexpected error: %s" % e)

