# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Filter:

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
        'value': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, type=None, value=None):
        r"""Filter

        The model defined in huaweicloud sdk

        :param type: 过滤类型，可选name，tag
        :type type: str
        :param value: 过滤类型对应的正则表达式(name对应的是命名空间及制品仓库，例如library/**tag对应的是版本，例如：**repo和tag正则表达式有多个时，用逗号分隔，且在最外层加{}，如library/{test,test*,*test})
        :type value: str
        """
        
        

        self._type = None
        self._value = None
        self.discriminator = None

        self.type = type
        self.value = value

    @property
    def type(self):
        r"""Gets the type of this Filter.

        过滤类型，可选name，tag

        :return: The type of this Filter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Filter.

        过滤类型，可选name，tag

        :param type: The type of this Filter.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this Filter.

        过滤类型对应的正则表达式(name对应的是命名空间及制品仓库，例如library/**tag对应的是版本，例如：**repo和tag正则表达式有多个时，用逗号分隔，且在最外层加{}，如library/{test,test*,*test})

        :return: The value of this Filter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Filter.

        过滤类型对应的正则表达式(name对应的是命名空间及制品仓库，例如library/**tag对应的是版本，例如：**repo和tag正则表达式有多个时，用逗号分隔，且在最外层加{}，如library/{test,test*,*test})

        :param value: The value of this Filter.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, Filter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
