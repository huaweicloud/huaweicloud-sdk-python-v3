# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecutionDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'last_execution_time': 'str',
        'items': 'list[ComponentExecutionResult]'
    }

    attribute_map = {
        'last_execution_time': 'last_execution_time',
        'items': 'items'
    }

    def __init__(self, last_execution_time=None, items=None):
        r"""ExecutionDetails

        The model defined in huaweicloud sdk

        :param last_execution_time: 启停策略执行时间。
        :type last_execution_time: str
        :param items: 组件启停规则执行结果列表。
        :type items: list[:class:`huaweicloudsdkcae.v1.ComponentExecutionResult`]
        """
        
        

        self._last_execution_time = None
        self._items = None
        self.discriminator = None

        if last_execution_time is not None:
            self.last_execution_time = last_execution_time
        if items is not None:
            self.items = items

    @property
    def last_execution_time(self):
        r"""Gets the last_execution_time of this ExecutionDetails.

        启停策略执行时间。

        :return: The last_execution_time of this ExecutionDetails.
        :rtype: str
        """
        return self._last_execution_time

    @last_execution_time.setter
    def last_execution_time(self, last_execution_time):
        r"""Sets the last_execution_time of this ExecutionDetails.

        启停策略执行时间。

        :param last_execution_time: The last_execution_time of this ExecutionDetails.
        :type last_execution_time: str
        """
        self._last_execution_time = last_execution_time

    @property
    def items(self):
        r"""Gets the items of this ExecutionDetails.

        组件启停规则执行结果列表。

        :return: The items of this ExecutionDetails.
        :rtype: list[:class:`huaweicloudsdkcae.v1.ComponentExecutionResult`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ExecutionDetails.

        组件启停规则执行结果列表。

        :param items: The items of this ExecutionDetails.
        :type items: list[:class:`huaweicloudsdkcae.v1.ComponentExecutionResult`]
        """
        self._items = items

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
        if not isinstance(other, ExecutionDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
