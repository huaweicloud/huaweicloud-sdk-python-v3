# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopoLine:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'from_node': 'str',
        'to_node': 'str',
        'direction': 'str',
        'collector': 'str',
        'target_env_id': 'int',
        'hints': 'dict(str, str)',
        'filter_value': 'str'
    }

    attribute_map = {
        'from_node': 'from_node',
        'to_node': 'to_node',
        'direction': 'direction',
        'collector': 'collector',
        'target_env_id': 'target_env_id',
        'hints': 'hints',
        'filter_value': 'filter_value'
    }

    def __init__(self, from_node=None, to_node=None, direction=None, collector=None, target_env_id=None, hints=None, filter_value=None):
        r"""TopoLine

        The model defined in huaweicloud sdk

        :param from_node: 开始节点。
        :type from_node: str
        :param to_node: 结束节点。
        :type to_node: str
        :param direction: 指向。
        :type direction: str
        :param collector: 采集器名称。
        :type collector: str
        :param target_env_id: 环境id。
        :type target_env_id: int
        :param hints: 线条上的提示信息。
        :type hints: dict(str, str)
        :param filter_value: 过滤值。
        :type filter_value: str
        """
        
        

        self._from_node = None
        self._to_node = None
        self._direction = None
        self._collector = None
        self._target_env_id = None
        self._hints = None
        self._filter_value = None
        self.discriminator = None

        if from_node is not None:
            self.from_node = from_node
        if to_node is not None:
            self.to_node = to_node
        if direction is not None:
            self.direction = direction
        if collector is not None:
            self.collector = collector
        if target_env_id is not None:
            self.target_env_id = target_env_id
        if hints is not None:
            self.hints = hints
        if filter_value is not None:
            self.filter_value = filter_value

    @property
    def from_node(self):
        r"""Gets the from_node of this TopoLine.

        开始节点。

        :return: The from_node of this TopoLine.
        :rtype: str
        """
        return self._from_node

    @from_node.setter
    def from_node(self, from_node):
        r"""Sets the from_node of this TopoLine.

        开始节点。

        :param from_node: The from_node of this TopoLine.
        :type from_node: str
        """
        self._from_node = from_node

    @property
    def to_node(self):
        r"""Gets the to_node of this TopoLine.

        结束节点。

        :return: The to_node of this TopoLine.
        :rtype: str
        """
        return self._to_node

    @to_node.setter
    def to_node(self, to_node):
        r"""Sets the to_node of this TopoLine.

        结束节点。

        :param to_node: The to_node of this TopoLine.
        :type to_node: str
        """
        self._to_node = to_node

    @property
    def direction(self):
        r"""Gets the direction of this TopoLine.

        指向。

        :return: The direction of this TopoLine.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this TopoLine.

        指向。

        :param direction: The direction of this TopoLine.
        :type direction: str
        """
        self._direction = direction

    @property
    def collector(self):
        r"""Gets the collector of this TopoLine.

        采集器名称。

        :return: The collector of this TopoLine.
        :rtype: str
        """
        return self._collector

    @collector.setter
    def collector(self, collector):
        r"""Sets the collector of this TopoLine.

        采集器名称。

        :param collector: The collector of this TopoLine.
        :type collector: str
        """
        self._collector = collector

    @property
    def target_env_id(self):
        r"""Gets the target_env_id of this TopoLine.

        环境id。

        :return: The target_env_id of this TopoLine.
        :rtype: int
        """
        return self._target_env_id

    @target_env_id.setter
    def target_env_id(self, target_env_id):
        r"""Sets the target_env_id of this TopoLine.

        环境id。

        :param target_env_id: The target_env_id of this TopoLine.
        :type target_env_id: int
        """
        self._target_env_id = target_env_id

    @property
    def hints(self):
        r"""Gets the hints of this TopoLine.

        线条上的提示信息。

        :return: The hints of this TopoLine.
        :rtype: dict(str, str)
        """
        return self._hints

    @hints.setter
    def hints(self, hints):
        r"""Sets the hints of this TopoLine.

        线条上的提示信息。

        :param hints: The hints of this TopoLine.
        :type hints: dict(str, str)
        """
        self._hints = hints

    @property
    def filter_value(self):
        r"""Gets the filter_value of this TopoLine.

        过滤值。

        :return: The filter_value of this TopoLine.
        :rtype: str
        """
        return self._filter_value

    @filter_value.setter
    def filter_value(self, filter_value):
        r"""Sets the filter_value of this TopoLine.

        过滤值。

        :param filter_value: The filter_value of this TopoLine.
        :type filter_value: str
        """
        self._filter_value = filter_value

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
        if not isinstance(other, TopoLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
