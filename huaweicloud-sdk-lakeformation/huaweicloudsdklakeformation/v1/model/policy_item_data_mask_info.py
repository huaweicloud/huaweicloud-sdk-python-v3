# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyItemDataMaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'condition_expr': 'str',
        'data_mask_type': 'str',
        'value_expr': 'str'
    }

    attribute_map = {
        'condition_expr': 'condition_expr',
        'data_mask_type': 'data_mask_type',
        'value_expr': 'value_expr'
    }

    def __init__(self, condition_expr=None, data_mask_type=None, value_expr=None):
        """PolicyItemDataMaskInfo

        The model defined in huaweicloud sdk

        :param condition_expr: 条件表达式
        :type condition_expr: str
        :param data_mask_type: 列掩码类型
        :type data_mask_type: str
        :param value_expr: 列掩码表达式
        :type value_expr: str
        """
        
        

        self._condition_expr = None
        self._data_mask_type = None
        self._value_expr = None
        self.discriminator = None

        if condition_expr is not None:
            self.condition_expr = condition_expr
        if data_mask_type is not None:
            self.data_mask_type = data_mask_type
        if value_expr is not None:
            self.value_expr = value_expr

    @property
    def condition_expr(self):
        """Gets the condition_expr of this PolicyItemDataMaskInfo.

        条件表达式

        :return: The condition_expr of this PolicyItemDataMaskInfo.
        :rtype: str
        """
        return self._condition_expr

    @condition_expr.setter
    def condition_expr(self, condition_expr):
        """Sets the condition_expr of this PolicyItemDataMaskInfo.

        条件表达式

        :param condition_expr: The condition_expr of this PolicyItemDataMaskInfo.
        :type condition_expr: str
        """
        self._condition_expr = condition_expr

    @property
    def data_mask_type(self):
        """Gets the data_mask_type of this PolicyItemDataMaskInfo.

        列掩码类型

        :return: The data_mask_type of this PolicyItemDataMaskInfo.
        :rtype: str
        """
        return self._data_mask_type

    @data_mask_type.setter
    def data_mask_type(self, data_mask_type):
        """Sets the data_mask_type of this PolicyItemDataMaskInfo.

        列掩码类型

        :param data_mask_type: The data_mask_type of this PolicyItemDataMaskInfo.
        :type data_mask_type: str
        """
        self._data_mask_type = data_mask_type

    @property
    def value_expr(self):
        """Gets the value_expr of this PolicyItemDataMaskInfo.

        列掩码表达式

        :return: The value_expr of this PolicyItemDataMaskInfo.
        :rtype: str
        """
        return self._value_expr

    @value_expr.setter
    def value_expr(self, value_expr):
        """Sets the value_expr of this PolicyItemDataMaskInfo.

        列掩码表达式

        :param value_expr: The value_expr of this PolicyItemDataMaskInfo.
        :type value_expr: str
        """
        self._value_expr = value_expr

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
        if not isinstance(other, PolicyItemDataMaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
