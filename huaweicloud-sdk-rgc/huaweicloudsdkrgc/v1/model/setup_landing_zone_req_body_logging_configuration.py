# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetupLandingZoneReqBodyLoggingConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logging_bucket': 'LoggingBucketBaseline',
        'access_logging_bucket': 'AccessLoggingBucketBaseline'
    }

    attribute_map = {
        'logging_bucket': 'logging_bucket',
        'access_logging_bucket': 'access_logging_bucket'
    }

    def __init__(self, logging_bucket=None, access_logging_bucket=None):
        """SetupLandingZoneReqBodyLoggingConfiguration

        The model defined in huaweicloud sdk

        :param logging_bucket: 
        :type logging_bucket: :class:`huaweicloudsdkrgc.v1.LoggingBucketBaseline`
        :param access_logging_bucket: 
        :type access_logging_bucket: :class:`huaweicloudsdkrgc.v1.AccessLoggingBucketBaseline`
        """
        
        

        self._logging_bucket = None
        self._access_logging_bucket = None
        self.discriminator = None

        self.logging_bucket = logging_bucket
        self.access_logging_bucket = access_logging_bucket

    @property
    def logging_bucket(self):
        """Gets the logging_bucket of this SetupLandingZoneReqBodyLoggingConfiguration.

        :return: The logging_bucket of this SetupLandingZoneReqBodyLoggingConfiguration.
        :rtype: :class:`huaweicloudsdkrgc.v1.LoggingBucketBaseline`
        """
        return self._logging_bucket

    @logging_bucket.setter
    def logging_bucket(self, logging_bucket):
        """Sets the logging_bucket of this SetupLandingZoneReqBodyLoggingConfiguration.

        :param logging_bucket: The logging_bucket of this SetupLandingZoneReqBodyLoggingConfiguration.
        :type logging_bucket: :class:`huaweicloudsdkrgc.v1.LoggingBucketBaseline`
        """
        self._logging_bucket = logging_bucket

    @property
    def access_logging_bucket(self):
        """Gets the access_logging_bucket of this SetupLandingZoneReqBodyLoggingConfiguration.

        :return: The access_logging_bucket of this SetupLandingZoneReqBodyLoggingConfiguration.
        :rtype: :class:`huaweicloudsdkrgc.v1.AccessLoggingBucketBaseline`
        """
        return self._access_logging_bucket

    @access_logging_bucket.setter
    def access_logging_bucket(self, access_logging_bucket):
        """Sets the access_logging_bucket of this SetupLandingZoneReqBodyLoggingConfiguration.

        :param access_logging_bucket: The access_logging_bucket of this SetupLandingZoneReqBodyLoggingConfiguration.
        :type access_logging_bucket: :class:`huaweicloudsdkrgc.v1.AccessLoggingBucketBaseline`
        """
        self._access_logging_bucket = access_logging_bucket

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
        if not isinstance(other, SetupLandingZoneReqBodyLoggingConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
