# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessLoggingBucketBaseline:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'retention_days': 'int'
    }

    attribute_map = {
        'retention_days': 'retention_days'
    }

    def __init__(self, retention_days=None):
        """AccessLoggingBucketBaseline

        The model defined in huaweicloud sdk

        :param retention_days: 桶保留天数。
        :type retention_days: int
        """
        
        

        self._retention_days = None
        self.discriminator = None

        self.retention_days = retention_days

    @property
    def retention_days(self):
        """Gets the retention_days of this AccessLoggingBucketBaseline.

        桶保留天数。

        :return: The retention_days of this AccessLoggingBucketBaseline.
        :rtype: int
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        """Sets the retention_days of this AccessLoggingBucketBaseline.

        桶保留天数。

        :param retention_days: The retention_days of this AccessLoggingBucketBaseline.
        :type retention_days: int
        """
        self._retention_days = retention_days

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
        if not isinstance(other, AccessLoggingBucketBaseline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
