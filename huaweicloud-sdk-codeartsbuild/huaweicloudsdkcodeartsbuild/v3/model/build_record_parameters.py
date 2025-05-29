# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildRecordParameters:

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
        'secret': 'bool',
        'value': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'secret': 'secret',
        'value': 'value',
        'type': 'type'
    }

    def __init__(self, name=None, secret=None, value=None, type=None):
        r"""BuildRecordParameters

        The model defined in huaweicloud sdk

        :param name: 参数名
        :type name: str
        :param secret: 是否为私密参数
        :type secret: bool
        :param value: 参数值
        :type value: str
        :param type: 类型
        :type type: str
        """
        
        

        self._name = None
        self._secret = None
        self._value = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if secret is not None:
            self.secret = secret
        if value is not None:
            self.value = value
        if type is not None:
            self.type = type

    @property
    def name(self):
        r"""Gets the name of this BuildRecordParameters.

        参数名

        :return: The name of this BuildRecordParameters.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BuildRecordParameters.

        参数名

        :param name: The name of this BuildRecordParameters.
        :type name: str
        """
        self._name = name

    @property
    def secret(self):
        r"""Gets the secret of this BuildRecordParameters.

        是否为私密参数

        :return: The secret of this BuildRecordParameters.
        :rtype: bool
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        r"""Sets the secret of this BuildRecordParameters.

        是否为私密参数

        :param secret: The secret of this BuildRecordParameters.
        :type secret: bool
        """
        self._secret = secret

    @property
    def value(self):
        r"""Gets the value of this BuildRecordParameters.

        参数值

        :return: The value of this BuildRecordParameters.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this BuildRecordParameters.

        参数值

        :param value: The value of this BuildRecordParameters.
        :type value: str
        """
        self._value = value

    @property
    def type(self):
        r"""Gets the type of this BuildRecordParameters.

        类型

        :return: The type of this BuildRecordParameters.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BuildRecordParameters.

        类型

        :param type: The type of this BuildRecordParameters.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, BuildRecordParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
