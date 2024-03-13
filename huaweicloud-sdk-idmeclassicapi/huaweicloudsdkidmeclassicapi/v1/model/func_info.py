# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FuncInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'func': 'str',
        'func_by': 'str'
    }

    attribute_map = {
        'func': 'func',
        'func_by': 'funcBy'
    }

    def __init__(self, func=None, func_by=None):
        """FuncInfo

        The model defined in huaweicloud sdk

        :param func: 指定简单函数名称。 - AVG：求平均值。 - COUNT：求总数。 - MAX：求最大值。 - MIX：求最小值。
        :type func: str
        :param func_by: 指定简单函数以哪个属性为维度操作。
        :type func_by: str
        """
        
        

        self._func = None
        self._func_by = None
        self.discriminator = None

        self.func = func
        self.func_by = func_by

    @property
    def func(self):
        """Gets the func of this FuncInfo.

        指定简单函数名称。 - AVG：求平均值。 - COUNT：求总数。 - MAX：求最大值。 - MIX：求最小值。

        :return: The func of this FuncInfo.
        :rtype: str
        """
        return self._func

    @func.setter
    def func(self, func):
        """Sets the func of this FuncInfo.

        指定简单函数名称。 - AVG：求平均值。 - COUNT：求总数。 - MAX：求最大值。 - MIX：求最小值。

        :param func: The func of this FuncInfo.
        :type func: str
        """
        self._func = func

    @property
    def func_by(self):
        """Gets the func_by of this FuncInfo.

        指定简单函数以哪个属性为维度操作。

        :return: The func_by of this FuncInfo.
        :rtype: str
        """
        return self._func_by

    @func_by.setter
    def func_by(self, func_by):
        """Sets the func_by of this FuncInfo.

        指定简单函数以哪个属性为维度操作。

        :param func_by: The func_by of this FuncInfo.
        :type func_by: str
        """
        self._func_by = func_by

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
        if not isinstance(other, FuncInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
