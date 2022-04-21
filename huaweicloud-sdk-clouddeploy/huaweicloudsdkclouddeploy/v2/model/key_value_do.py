# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeyValueDO:

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
        'limits': 'list[ParamTypeLimits]'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'limits': 'limits'
    }

    def __init__(self, name=None, value=None, limits=None):
        """KeyValueDO

        The model defined in huaweicloud sdk

        :param name: 执行部署任务时传递的参数名称
        :type name: str
        :param value: 执行部署任务时传递的参数值
        :type value: str
        :param limits: 参数值为枚举类型时，返回可选值列表
        :type limits: list[:class:`huaweicloudsdkclouddeploy.v2.ParamTypeLimits`]
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
        """Gets the name of this KeyValueDO.

        执行部署任务时传递的参数名称

        :return: The name of this KeyValueDO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KeyValueDO.

        执行部署任务时传递的参数名称

        :param name: The name of this KeyValueDO.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this KeyValueDO.

        执行部署任务时传递的参数值

        :return: The value of this KeyValueDO.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this KeyValueDO.

        执行部署任务时传递的参数值

        :param value: The value of this KeyValueDO.
        :type value: str
        """
        self._value = value

    @property
    def limits(self):
        """Gets the limits of this KeyValueDO.

        参数值为枚举类型时，返回可选值列表

        :return: The limits of this KeyValueDO.
        :rtype: list[:class:`huaweicloudsdkclouddeploy.v2.ParamTypeLimits`]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this KeyValueDO.

        参数值为枚举类型时，返回可选值列表

        :param limits: The limits of this KeyValueDO.
        :type limits: list[:class:`huaweicloudsdkclouddeploy.v2.ParamTypeLimits`]
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
        if not isinstance(other, KeyValueDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
