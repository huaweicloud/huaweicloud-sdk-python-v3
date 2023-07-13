# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Quotas:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'quota': 'int',
        'min': 'int',
        'max': 'int',
        'used': 'int'
    }

    attribute_map = {
        'type': 'type',
        'quota': 'quota',
        'min': 'min',
        'max': 'max',
        'used': 'used'
    }

    def __init__(self, type=None, quota=None, min=None, max=None, used=None):
        """Quotas

        The model defined in huaweicloud sdk

        :param type: 配额类型。resource_share帐号创建资源共享的数量，resource_association资源共享关联的资源数量，principal_association资源共享关联的身份数量，permission_association资源共享关联的权限数量，tag_association资源共享关联的标签数量。
        :type type: str
        :param quota: 总配额数量。
        :type quota: int
        :param min: 最小配额。
        :type min: int
        :param max: 最大配额。
        :type max: int
        :param used: 已使用的配额数量。
        :type used: int
        """
        
        

        self._type = None
        self._quota = None
        self._min = None
        self._max = None
        self._used = None
        self.discriminator = None

        self.type = type
        self.quota = quota
        self.min = min
        self.max = max
        self.used = used

    @property
    def type(self):
        """Gets the type of this Quotas.

        配额类型。resource_share帐号创建资源共享的数量，resource_association资源共享关联的资源数量，principal_association资源共享关联的身份数量，permission_association资源共享关联的权限数量，tag_association资源共享关联的标签数量。

        :return: The type of this Quotas.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Quotas.

        配额类型。resource_share帐号创建资源共享的数量，resource_association资源共享关联的资源数量，principal_association资源共享关联的身份数量，permission_association资源共享关联的权限数量，tag_association资源共享关联的标签数量。

        :param type: The type of this Quotas.
        :type type: str
        """
        self._type = type

    @property
    def quota(self):
        """Gets the quota of this Quotas.

        总配额数量。

        :return: The quota of this Quotas.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this Quotas.

        总配额数量。

        :param quota: The quota of this Quotas.
        :type quota: int
        """
        self._quota = quota

    @property
    def min(self):
        """Gets the min of this Quotas.

        最小配额。

        :return: The min of this Quotas.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this Quotas.

        最小配额。

        :param min: The min of this Quotas.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        """Gets the max of this Quotas.

        最大配额。

        :return: The max of this Quotas.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this Quotas.

        最大配额。

        :param max: The max of this Quotas.
        :type max: int
        """
        self._max = max

    @property
    def used(self):
        """Gets the used of this Quotas.

        已使用的配额数量。

        :return: The used of this Quotas.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this Quotas.

        已使用的配额数量。

        :param used: The used of this Quotas.
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
        if not isinstance(other, Quotas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
