# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoggingConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logging_bucket_name': 'str',
        'access_logging_bucket': 'AccessLoggingBucketBaseline',
        'logging_bucket': 'LoggingBucketBaseline'
    }

    attribute_map = {
        'logging_bucket_name': 'logging_bucket_name',
        'access_logging_bucket': 'access_logging_bucket',
        'logging_bucket': 'logging_bucket'
    }

    def __init__(self, logging_bucket_name=None, access_logging_bucket=None, logging_bucket=None):
        r"""LoggingConfiguration

        The model defined in huaweicloud sdk

        :param logging_bucket_name: 日志桶名称。
        :type logging_bucket_name: str
        :param access_logging_bucket: 
        :type access_logging_bucket: :class:`huaweicloudsdkrgc.v1.AccessLoggingBucketBaseline`
        :param logging_bucket: 
        :type logging_bucket: :class:`huaweicloudsdkrgc.v1.LoggingBucketBaseline`
        """
        
        

        self._logging_bucket_name = None
        self._access_logging_bucket = None
        self._logging_bucket = None
        self.discriminator = None

        if logging_bucket_name is not None:
            self.logging_bucket_name = logging_bucket_name
        if access_logging_bucket is not None:
            self.access_logging_bucket = access_logging_bucket
        if logging_bucket is not None:
            self.logging_bucket = logging_bucket

    @property
    def logging_bucket_name(self):
        r"""Gets the logging_bucket_name of this LoggingConfiguration.

        日志桶名称。

        :return: The logging_bucket_name of this LoggingConfiguration.
        :rtype: str
        """
        return self._logging_bucket_name

    @logging_bucket_name.setter
    def logging_bucket_name(self, logging_bucket_name):
        r"""Sets the logging_bucket_name of this LoggingConfiguration.

        日志桶名称。

        :param logging_bucket_name: The logging_bucket_name of this LoggingConfiguration.
        :type logging_bucket_name: str
        """
        self._logging_bucket_name = logging_bucket_name

    @property
    def access_logging_bucket(self):
        r"""Gets the access_logging_bucket of this LoggingConfiguration.

        :return: The access_logging_bucket of this LoggingConfiguration.
        :rtype: :class:`huaweicloudsdkrgc.v1.AccessLoggingBucketBaseline`
        """
        return self._access_logging_bucket

    @access_logging_bucket.setter
    def access_logging_bucket(self, access_logging_bucket):
        r"""Sets the access_logging_bucket of this LoggingConfiguration.

        :param access_logging_bucket: The access_logging_bucket of this LoggingConfiguration.
        :type access_logging_bucket: :class:`huaweicloudsdkrgc.v1.AccessLoggingBucketBaseline`
        """
        self._access_logging_bucket = access_logging_bucket

    @property
    def logging_bucket(self):
        r"""Gets the logging_bucket of this LoggingConfiguration.

        :return: The logging_bucket of this LoggingConfiguration.
        :rtype: :class:`huaweicloudsdkrgc.v1.LoggingBucketBaseline`
        """
        return self._logging_bucket

    @logging_bucket.setter
    def logging_bucket(self, logging_bucket):
        r"""Sets the logging_bucket of this LoggingConfiguration.

        :param logging_bucket: The logging_bucket of this LoggingConfiguration.
        :type logging_bucket: :class:`huaweicloudsdkrgc.v1.LoggingBucketBaseline`
        """
        self._logging_bucket = logging_bucket

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LoggingConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
