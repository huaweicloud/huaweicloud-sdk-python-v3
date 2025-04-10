# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvRequestBodyParams:

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
        'type': 'str',
        'value': 'str',
        'desc': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'value': 'value',
        'desc': 'desc'
    }

    def __init__(self, name=None, type=None, value=None, desc=None):
        r"""EnvRequestBodyParams

        The model defined in huaweicloud sdk

        :param name: 环境变量名称
        :type name: str
        :param type: 环境变量类型
        :type type: str
        :param value: 环境变量值
        :type value: str
        :param desc: 描述信息
        :type desc: str
        """
        
        

        self._name = None
        self._type = None
        self._value = None
        self._desc = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if desc is not None:
            self.desc = desc

    @property
    def name(self):
        r"""Gets the name of this EnvRequestBodyParams.

        环境变量名称

        :return: The name of this EnvRequestBodyParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EnvRequestBodyParams.

        环境变量名称

        :param name: The name of this EnvRequestBodyParams.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this EnvRequestBodyParams.

        环境变量类型

        :return: The type of this EnvRequestBodyParams.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EnvRequestBodyParams.

        环境变量类型

        :param type: The type of this EnvRequestBodyParams.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this EnvRequestBodyParams.

        环境变量值

        :return: The value of this EnvRequestBodyParams.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this EnvRequestBodyParams.

        环境变量值

        :param value: The value of this EnvRequestBodyParams.
        :type value: str
        """
        self._value = value

    @property
    def desc(self):
        r"""Gets the desc of this EnvRequestBodyParams.

        描述信息

        :return: The desc of this EnvRequestBodyParams.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this EnvRequestBodyParams.

        描述信息

        :param desc: The desc of this EnvRequestBodyParams.
        :type desc: str
        """
        self._desc = desc

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
        if not isinstance(other, EnvRequestBodyParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
