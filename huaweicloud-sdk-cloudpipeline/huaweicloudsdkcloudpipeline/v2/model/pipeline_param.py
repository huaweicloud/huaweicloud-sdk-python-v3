# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineParam:

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
        'description': 'str',
        'param_type': 'str',
        'is_static': 'bool',
        'is_default': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'description': 'description',
        'param_type': 'param_type',
        'is_static': 'is_static',
        'is_default': 'is_default'
    }

    def __init__(self, name=None, value=None, description=None, param_type=None, is_static=None, is_default=None):
        """PipelineParam

        The model defined in huaweicloud sdk

        :param name: 流水线参数名字
        :type name: str
        :param value: 流水线参数值
        :type value: str
        :param description: 流水线参数描述
        :type description: str
        :param param_type: 流水线参数类型
        :type param_type: str
        :param is_static: 是否静态参数
        :type is_static: bool
        :param is_default: 是否默认参数
        :type is_default: bool
        """
        
        

        self._name = None
        self._value = None
        self._description = None
        self._param_type = None
        self._is_static = None
        self._is_default = None
        self.discriminator = None

        self.name = name
        self.value = value
        self.description = description
        self.param_type = param_type
        self.is_static = is_static
        self.is_default = is_default

    @property
    def name(self):
        """Gets the name of this PipelineParam.

        流水线参数名字

        :return: The name of this PipelineParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelineParam.

        流水线参数名字

        :param name: The name of this PipelineParam.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this PipelineParam.

        流水线参数值

        :return: The value of this PipelineParam.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PipelineParam.

        流水线参数值

        :param value: The value of this PipelineParam.
        :type value: str
        """
        self._value = value

    @property
    def description(self):
        """Gets the description of this PipelineParam.

        流水线参数描述

        :return: The description of this PipelineParam.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PipelineParam.

        流水线参数描述

        :param description: The description of this PipelineParam.
        :type description: str
        """
        self._description = description

    @property
    def param_type(self):
        """Gets the param_type of this PipelineParam.

        流水线参数类型

        :return: The param_type of this PipelineParam.
        :rtype: str
        """
        return self._param_type

    @param_type.setter
    def param_type(self, param_type):
        """Sets the param_type of this PipelineParam.

        流水线参数类型

        :param param_type: The param_type of this PipelineParam.
        :type param_type: str
        """
        self._param_type = param_type

    @property
    def is_static(self):
        """Gets the is_static of this PipelineParam.

        是否静态参数

        :return: The is_static of this PipelineParam.
        :rtype: bool
        """
        return self._is_static

    @is_static.setter
    def is_static(self, is_static):
        """Sets the is_static of this PipelineParam.

        是否静态参数

        :param is_static: The is_static of this PipelineParam.
        :type is_static: bool
        """
        self._is_static = is_static

    @property
    def is_default(self):
        """Gets the is_default of this PipelineParam.

        是否默认参数

        :return: The is_default of this PipelineParam.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this PipelineParam.

        是否默认参数

        :param is_default: The is_default of this PipelineParam.
        :type is_default: bool
        """
        self._is_default = is_default

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
        if not isinstance(other, PipelineParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
