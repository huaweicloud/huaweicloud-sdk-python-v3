# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProvisionedThroughput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rcu': 'int',
        'wcu': 'int'
    }

    attribute_map = {
        'rcu': 'rcu',
        'wcu': 'wcu'
    }

    def __init__(self, rcu=None, wcu=None):
        r"""ProvisionedThroughput

        The model defined in huaweicloud sdk

        :param rcu: 预置表级读请求单元数
        :type rcu: int
        :param wcu: 预置表级写请求单元数
        :type wcu: int
        """
        
        

        self._rcu = None
        self._wcu = None
        self.discriminator = None

        self.rcu = rcu
        self.wcu = wcu

    @property
    def rcu(self):
        r"""Gets the rcu of this ProvisionedThroughput.

        预置表级读请求单元数

        :return: The rcu of this ProvisionedThroughput.
        :rtype: int
        """
        return self._rcu

    @rcu.setter
    def rcu(self, rcu):
        r"""Sets the rcu of this ProvisionedThroughput.

        预置表级读请求单元数

        :param rcu: The rcu of this ProvisionedThroughput.
        :type rcu: int
        """
        self._rcu = rcu

    @property
    def wcu(self):
        r"""Gets the wcu of this ProvisionedThroughput.

        预置表级写请求单元数

        :return: The wcu of this ProvisionedThroughput.
        :rtype: int
        """
        return self._wcu

    @wcu.setter
    def wcu(self, wcu):
        r"""Sets the wcu of this ProvisionedThroughput.

        预置表级写请求单元数

        :param wcu: The wcu of this ProvisionedThroughput.
        :type wcu: int
        """
        self._wcu = wcu

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
        if not isinstance(other, ProvisionedThroughput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
