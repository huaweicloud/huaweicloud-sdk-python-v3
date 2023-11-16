# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityRuleCve:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'values': 'list[str]'
    }

    attribute_map = {
        'enable': 'enable',
        'values': 'values'
    }

    def __init__(self, enable=None, values=None):
        """SecurityRuleCve

        The model defined in huaweicloud sdk

        :param enable: 是否启用
        :type enable: bool
        :param values: 漏洞编号
        :type values: list[str]
        """
        
        

        self._enable = None
        self._values = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if values is not None:
            self.values = values

    @property
    def enable(self):
        """Gets the enable of this SecurityRuleCve.

        是否启用

        :return: The enable of this SecurityRuleCve.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this SecurityRuleCve.

        是否启用

        :param enable: The enable of this SecurityRuleCve.
        :type enable: bool
        """
        self._enable = enable

    @property
    def values(self):
        """Gets the values of this SecurityRuleCve.

        漏洞编号

        :return: The values of this SecurityRuleCve.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this SecurityRuleCve.

        漏洞编号

        :param values: The values of this SecurityRuleCve.
        :type values: list[str]
        """
        self._values = values

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
        if not isinstance(other, SecurityRuleCve):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
