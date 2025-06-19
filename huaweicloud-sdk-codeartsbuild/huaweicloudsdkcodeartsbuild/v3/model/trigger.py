# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Trigger:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parameters': 'list[ParameterItem]',
        'name': 'str'
    }

    attribute_map = {
        'parameters': 'parameters',
        'name': 'name'
    }

    def __init__(self, parameters=None, name=None):
        r"""Trigger

        The model defined in huaweicloud sdk

        :param parameters: 自定义参数
        :type parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.ParameterItem`]
        :param name: 触发器类型
        :type name: str
        """
        
        

        self._parameters = None
        self._name = None
        self.discriminator = None

        self.parameters = parameters
        self.name = name

    @property
    def parameters(self):
        r"""Gets the parameters of this Trigger.

        自定义参数

        :return: The parameters of this Trigger.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.ParameterItem`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this Trigger.

        自定义参数

        :param parameters: The parameters of this Trigger.
        :type parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.ParameterItem`]
        """
        self._parameters = parameters

    @property
    def name(self):
        r"""Gets the name of this Trigger.

        触发器类型

        :return: The name of this Trigger.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Trigger.

        触发器类型

        :param name: The name of this Trigger.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, Trigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
