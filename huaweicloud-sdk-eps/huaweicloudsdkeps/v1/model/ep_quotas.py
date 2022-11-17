# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EpQuotas:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota': 'int',
        'type': 'str',
        'used': 'int'
    }

    attribute_map = {
        'quota': 'quota',
        'type': 'type',
        'used': 'used'
    }

    def __init__(self, quota=None, type=None, used=None):
        """EpQuotas

        The model defined in huaweicloud sdk

        :param quota: 总配额
        :type quota: int
        :param type: qutoa的资源类型
        :type type: str
        :param used: 配额使用量
        :type used: int
        """
        
        

        self._quota = None
        self._type = None
        self._used = None
        self.discriminator = None

        self.quota = quota
        self.type = type
        self.used = used

    @property
    def quota(self):
        """Gets the quota of this EpQuotas.

        总配额

        :return: The quota of this EpQuotas.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this EpQuotas.

        总配额

        :param quota: The quota of this EpQuotas.
        :type quota: int
        """
        self._quota = quota

    @property
    def type(self):
        """Gets the type of this EpQuotas.

        qutoa的资源类型

        :return: The type of this EpQuotas.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EpQuotas.

        qutoa的资源类型

        :param type: The type of this EpQuotas.
        :type type: str
        """
        self._type = type

    @property
    def used(self):
        """Gets the used of this EpQuotas.

        配额使用量

        :return: The used of this EpQuotas.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this EpQuotas.

        配额使用量

        :param used: The used of this EpQuotas.
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
        if not isinstance(other, EpQuotas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
