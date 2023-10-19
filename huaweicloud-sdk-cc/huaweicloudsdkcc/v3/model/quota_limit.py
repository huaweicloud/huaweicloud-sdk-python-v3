# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaLimit:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota_limit': 'int'
    }

    attribute_map = {
        'quota_limit': 'quota_limit'
    }

    def __init__(self, quota_limit=None):
        """QuotaLimit

        The model defined in huaweicloud sdk

        :param quota_limit: 配额大小。
        :type quota_limit: int
        """
        
        

        self._quota_limit = None
        self.discriminator = None

        self.quota_limit = quota_limit

    @property
    def quota_limit(self):
        """Gets the quota_limit of this QuotaLimit.

        配额大小。

        :return: The quota_limit of this QuotaLimit.
        :rtype: int
        """
        return self._quota_limit

    @quota_limit.setter
    def quota_limit(self, quota_limit):
        """Sets the quota_limit of this QuotaLimit.

        配额大小。

        :param quota_limit: The quota_limit of this QuotaLimit.
        :type quota_limit: int
        """
        self._quota_limit = quota_limit

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
        if not isinstance(other, QuotaLimit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
