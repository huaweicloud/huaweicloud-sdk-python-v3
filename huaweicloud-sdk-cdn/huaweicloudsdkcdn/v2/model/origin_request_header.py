# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OriginRequestHeader:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'value': 'str',
        'action': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'action': 'action'
    }

    def __init__(self, name=None, value=None, action=None):
        """OriginRequestHeader

        The model defined in huaweicloud sdk

        :param name: 设置回源请求头参数。格式要求：由数字，大小写字母，中划线组成，只能以字母开头。
        :type name: str
        :param value: 设置回源请求头参数的值。当为删除动作时，可不填。格式要求：长度1~512。不支持中文，不支持变量配置，如：$client_ip,$remote_port等。
        :type value: str
        :param action: 回源请求头设置类型。delete：删除，set：设置。同一个请求头字段只允许删除或者设置。设置：若原始回源请求中不存在该字段，先执行新增再执行设置。
        :type action: str
        """
        
        

        self._name = None
        self._value = None
        self._action = None
        self.discriminator = None

        self.name = name
        if value is not None:
            self.value = value
        self.action = action

    @property
    def name(self):
        """Gets the name of this OriginRequestHeader.

        设置回源请求头参数。格式要求：由数字，大小写字母，中划线组成，只能以字母开头。

        :return: The name of this OriginRequestHeader.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OriginRequestHeader.

        设置回源请求头参数。格式要求：由数字，大小写字母，中划线组成，只能以字母开头。

        :param name: The name of this OriginRequestHeader.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this OriginRequestHeader.

        设置回源请求头参数的值。当为删除动作时，可不填。格式要求：长度1~512。不支持中文，不支持变量配置，如：$client_ip,$remote_port等。

        :return: The value of this OriginRequestHeader.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OriginRequestHeader.

        设置回源请求头参数的值。当为删除动作时，可不填。格式要求：长度1~512。不支持中文，不支持变量配置，如：$client_ip,$remote_port等。

        :param value: The value of this OriginRequestHeader.
        :type value: str
        """
        self._value = value

    @property
    def action(self):
        """Gets the action of this OriginRequestHeader.

        回源请求头设置类型。delete：删除，set：设置。同一个请求头字段只允许删除或者设置。设置：若原始回源请求中不存在该字段，先执行新增再执行设置。

        :return: The action of this OriginRequestHeader.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this OriginRequestHeader.

        回源请求头设置类型。delete：删除，set：设置。同一个请求头字段只允许删除或者设置。设置：若原始回源请求中不存在该字段，先执行新增再执行设置。

        :param action: The action of this OriginRequestHeader.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, OriginRequestHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
