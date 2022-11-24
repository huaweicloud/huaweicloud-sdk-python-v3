# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TxLine:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tx_from_node': 'str',
        'tx_to_node': 'str',
        'invoke_count': 'int',
        'rt': 'float',
        'error_count': 'int',
        'type': 'str',
        'direction': 'str'
    }

    attribute_map = {
        'tx_from_node': 'tx_from_node',
        'tx_to_node': 'tx_to_node',
        'invoke_count': 'invoke_count',
        'rt': 'rt',
        'error_count': 'error_count',
        'type': 'type',
        'direction': 'direction'
    }

    def __init__(self, tx_from_node=None, tx_to_node=None, invoke_count=None, rt=None, error_count=None, type=None, direction=None):
        """TxLine

        The model defined in huaweicloud sdk

        :param tx_from_node: 开始节点。
        :type tx_from_node: str
        :param tx_to_node: 结束节点。
        :type tx_to_node: str
        :param invoke_count: 调用次数。
        :type invoke_count: int
        :param rt: 平均响应时间。
        :type rt: float
        :param error_count: 错误数。
        :type error_count: int
        :param type: 类型。
        :type type: str
        :param direction: 指向。
        :type direction: str
        """
        
        

        self._tx_from_node = None
        self._tx_to_node = None
        self._invoke_count = None
        self._rt = None
        self._error_count = None
        self._type = None
        self._direction = None
        self.discriminator = None

        if tx_from_node is not None:
            self.tx_from_node = tx_from_node
        if tx_to_node is not None:
            self.tx_to_node = tx_to_node
        if invoke_count is not None:
            self.invoke_count = invoke_count
        if rt is not None:
            self.rt = rt
        if error_count is not None:
            self.error_count = error_count
        if type is not None:
            self.type = type
        if direction is not None:
            self.direction = direction

    @property
    def tx_from_node(self):
        """Gets the tx_from_node of this TxLine.

        开始节点。

        :return: The tx_from_node of this TxLine.
        :rtype: str
        """
        return self._tx_from_node

    @tx_from_node.setter
    def tx_from_node(self, tx_from_node):
        """Sets the tx_from_node of this TxLine.

        开始节点。

        :param tx_from_node: The tx_from_node of this TxLine.
        :type tx_from_node: str
        """
        self._tx_from_node = tx_from_node

    @property
    def tx_to_node(self):
        """Gets the tx_to_node of this TxLine.

        结束节点。

        :return: The tx_to_node of this TxLine.
        :rtype: str
        """
        return self._tx_to_node

    @tx_to_node.setter
    def tx_to_node(self, tx_to_node):
        """Sets the tx_to_node of this TxLine.

        结束节点。

        :param tx_to_node: The tx_to_node of this TxLine.
        :type tx_to_node: str
        """
        self._tx_to_node = tx_to_node

    @property
    def invoke_count(self):
        """Gets the invoke_count of this TxLine.

        调用次数。

        :return: The invoke_count of this TxLine.
        :rtype: int
        """
        return self._invoke_count

    @invoke_count.setter
    def invoke_count(self, invoke_count):
        """Sets the invoke_count of this TxLine.

        调用次数。

        :param invoke_count: The invoke_count of this TxLine.
        :type invoke_count: int
        """
        self._invoke_count = invoke_count

    @property
    def rt(self):
        """Gets the rt of this TxLine.

        平均响应时间。

        :return: The rt of this TxLine.
        :rtype: float
        """
        return self._rt

    @rt.setter
    def rt(self, rt):
        """Sets the rt of this TxLine.

        平均响应时间。

        :param rt: The rt of this TxLine.
        :type rt: float
        """
        self._rt = rt

    @property
    def error_count(self):
        """Gets the error_count of this TxLine.

        错误数。

        :return: The error_count of this TxLine.
        :rtype: int
        """
        return self._error_count

    @error_count.setter
    def error_count(self, error_count):
        """Sets the error_count of this TxLine.

        错误数。

        :param error_count: The error_count of this TxLine.
        :type error_count: int
        """
        self._error_count = error_count

    @property
    def type(self):
        """Gets the type of this TxLine.

        类型。

        :return: The type of this TxLine.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TxLine.

        类型。

        :param type: The type of this TxLine.
        :type type: str
        """
        self._type = type

    @property
    def direction(self):
        """Gets the direction of this TxLine.

        指向。

        :return: The direction of this TxLine.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this TxLine.

        指向。

        :param direction: The direction of this TxLine.
        :type direction: str
        """
        self._direction = direction

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
        if not isinstance(other, TxLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
