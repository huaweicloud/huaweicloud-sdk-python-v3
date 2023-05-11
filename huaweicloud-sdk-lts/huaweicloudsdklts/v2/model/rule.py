# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Rule:

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
        'param': 'str'
    }

    attribute_map = {
        'type': 'type',
        'param': 'param'
    }

    def __init__(self, type=None, param=None):
        """Rule

        The model defined in huaweicloud sdk

        :param type: 内置系统模板类型。
        :type type: str
        :param param: 系统iton模板名称。
        :type param: str
        """
        
        

        self._type = None
        self._param = None
        self.discriminator = None

        self.type = type
        self.param = param

    @property
    def type(self):
        """Gets the type of this Rule.

        内置系统模板类型。

        :return: The type of this Rule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Rule.

        内置系统模板类型。

        :param type: The type of this Rule.
        :type type: str
        """
        self._type = type

    @property
    def param(self):
        """Gets the param of this Rule.

        系统iton模板名称。

        :return: The param of this Rule.
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param):
        """Sets the param of this Rule.

        系统iton模板名称。

        :param param: The param of this Rule.
        :type param: str
        """
        self._param = param

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
        if not isinstance(other, Rule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
