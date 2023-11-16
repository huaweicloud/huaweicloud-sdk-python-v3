# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBuildJobParameterParam:

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
        'limits': 'list[LimitsParam]'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'limits': 'limits'
    }

    def __init__(self, name=None, value=None, limits=None):
        """CreateBuildJobParameterParam

        The model defined in huaweicloud sdk

        :param name: 参数字段名
        :type name: str
        :param value: 参数字段值
        :type value: str
        :param limits: 枚举类参数限制
        :type limits: list[:class:`huaweicloudsdkcodeartsbuild.v3.LimitsParam`]
        """
        
        

        self._name = None
        self._value = None
        self._limits = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if limits is not None:
            self.limits = limits

    @property
    def name(self):
        """Gets the name of this CreateBuildJobParameterParam.

        参数字段名

        :return: The name of this CreateBuildJobParameterParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateBuildJobParameterParam.

        参数字段名

        :param name: The name of this CreateBuildJobParameterParam.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this CreateBuildJobParameterParam.

        参数字段值

        :return: The value of this CreateBuildJobParameterParam.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CreateBuildJobParameterParam.

        参数字段值

        :param value: The value of this CreateBuildJobParameterParam.
        :type value: str
        """
        self._value = value

    @property
    def limits(self):
        """Gets the limits of this CreateBuildJobParameterParam.

        枚举类参数限制

        :return: The limits of this CreateBuildJobParameterParam.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.LimitsParam`]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this CreateBuildJobParameterParam.

        枚举类参数限制

        :param limits: The limits of this CreateBuildJobParameterParam.
        :type limits: list[:class:`huaweicloudsdkcodeartsbuild.v3.LimitsParam`]
        """
        self._limits = limits

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
        if not isinstance(other, CreateBuildJobParameterParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
