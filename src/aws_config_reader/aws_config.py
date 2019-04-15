from ConfigParser import ConfigParser
from ConfigParser import ParsingError
from ConfigParser import NoOptionError
from ConfigParser import NoSectionError
from os import path


class AwsConfiguration(object):

    def __init__(self):
        self._aws_configuration = ConfigParser()

    def get_property(self, property_name):
        return self._aws_configuration.get('default', property_name)


class AwsConfig(AwsConfiguration):

    def __init__(self):
        super(AwsConfig, self).__init__()
        self._aws_configuration.read([path.join(path.expanduser("~"),'.aws/config')])

    def __unicode__(self):
        return u'Config: (region = {}, output = {})'.format(self.region, self.output)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __repr__(self):
        return '(region = %s, config = %s)' % (self.region, self.output)

    @property
    def region(self):
        return self.get_property('region')

    @property
    def output(self):
        return self.get_property('output')


class AwsCredentials(AwsConfiguration):

    def __init__(self):
        super(AwsCredentials, self).__init__()
        self._aws_configuration.read([path.join(path.expanduser("~"),'.aws/credentials')])

    def __unicode__(self):
        return u'Credentials: (aws_access_key_id = {}, aws_secret_access_key = {})'.format(self.aws_access_key_id, self.aws_secret_access_key)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __repr__(self):
        return '(aws_access_key_id = %s, aws_secret_access_key = %s)' % (self.aws_access_key_id, self.aws_secret_access_key)

    @property
    def aws_access_key_id(self):
        return self.get_property('aws_access_key_id')

    @property
    def aws_secret_access_key(self):
        return self.get_property('aws_secret_access_key')



class AwsConfigurationReader(object):

    def __init__(self):
        self._config = AwsConfig()
        self._credentials = AwsCredentials()

    @property
    def config(self):
        return self._config

    @property
    def credentials(self):
        return self._credentials

if __name__ == "__main__":

    reader = AwsConfigurationReader()
    print reader.config
    print reader.config.region
    print reader.config.output
    print repr(reader.config)
    print reader.credentials
    print reader.credentials.aws_access_key_id
    print reader.credentials.aws_secret_access_key
    print repr(reader.credentials)
