# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RespQuotaSet:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource': 'str',
        'hard_limit': 'int',
        'used': 'int'
    }

    attribute_map = {
        'resource': 'resource',
        'hard_limit': 'hard_limit',
        'used': 'used'
    }

    def __init__(self, resource=None, hard_limit=None, used=None):
        """RespQuotaSet

        The model defined in huaweicloud sdk

        :param resource: 配额类别。
        :type resource: str
        :param hard_limit: 配额最大限制。  “-1”表示资源配额不受限制。
        :type hard_limit: int
        :param used: 已使用配额数量。
        :type used: int
        """
        
        

        self._resource = None
        self._hard_limit = None
        self._used = None
        self.discriminator = None

        self.resource = resource
        self.hard_limit = hard_limit
        self.used = used

    @property
    def resource(self):
        """Gets the resource of this RespQuotaSet.

        配额类别。

        :return: The resource of this RespQuotaSet.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this RespQuotaSet.

        配额类别。

        :param resource: The resource of this RespQuotaSet.
        :type resource: str
        """
        self._resource = resource

    @property
    def hard_limit(self):
        """Gets the hard_limit of this RespQuotaSet.

        配额最大限制。  “-1”表示资源配额不受限制。

        :return: The hard_limit of this RespQuotaSet.
        :rtype: int
        """
        return self._hard_limit

    @hard_limit.setter
    def hard_limit(self, hard_limit):
        """Sets the hard_limit of this RespQuotaSet.

        配额最大限制。  “-1”表示资源配额不受限制。

        :param hard_limit: The hard_limit of this RespQuotaSet.
        :type hard_limit: int
        """
        self._hard_limit = hard_limit

    @property
    def used(self):
        """Gets the used of this RespQuotaSet.

        已使用配额数量。

        :return: The used of this RespQuotaSet.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this RespQuotaSet.

        已使用配额数量。

        :param used: The used of this RespQuotaSet.
        :type used: int
        """
        self._used = used

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
        if not isinstance(other, RespQuotaSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
