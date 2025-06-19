# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SysRuleParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max': 'int',
        'min': 'int',
        'default_value': 'int',
        'desc': 'str'
    }

    attribute_map = {
        'max': 'max',
        'min': 'min',
        'default_value': 'defaultValue',
        'desc': 'desc'
    }

    def __init__(self, max=None, min=None, default_value=None, desc=None):
        r"""SysRuleParam

        The model defined in huaweicloud sdk

        :param max: 阀值上限
        :type max: int
        :param min: 阀值下限
        :type min: int
        :param default_value: 阀值默认值
        :type default_value: int
        :param desc: 描述
        :type desc: str
        """
        
        

        self._max = None
        self._min = None
        self._default_value = None
        self._desc = None
        self.discriminator = None

        if max is not None:
            self.max = max
        if min is not None:
            self.min = min
        if default_value is not None:
            self.default_value = default_value
        if desc is not None:
            self.desc = desc

    @property
    def max(self):
        r"""Gets the max of this SysRuleParam.

        阀值上限

        :return: The max of this SysRuleParam.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this SysRuleParam.

        阀值上限

        :param max: The max of this SysRuleParam.
        :type max: int
        """
        self._max = max

    @property
    def min(self):
        r"""Gets the min of this SysRuleParam.

        阀值下限

        :return: The min of this SysRuleParam.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this SysRuleParam.

        阀值下限

        :param min: The min of this SysRuleParam.
        :type min: int
        """
        self._min = min

    @property
    def default_value(self):
        r"""Gets the default_value of this SysRuleParam.

        阀值默认值

        :return: The default_value of this SysRuleParam.
        :rtype: int
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this SysRuleParam.

        阀值默认值

        :param default_value: The default_value of this SysRuleParam.
        :type default_value: int
        """
        self._default_value = default_value

    @property
    def desc(self):
        r"""Gets the desc of this SysRuleParam.

        描述

        :return: The desc of this SysRuleParam.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this SysRuleParam.

        描述

        :param desc: The desc of this SysRuleParam.
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
        if not isinstance(other, SysRuleParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
