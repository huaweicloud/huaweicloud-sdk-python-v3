# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Shards:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'component_id': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'component_id': 'component_id'
    }

    def __init__(self, node_id=None, component_id=None):
        """Shards

        The model defined in huaweicloud sdk

        :param node_id: 节点Id。
        :type node_id: str
        :param component_id: 组件Id。最大长度7个字符，不能为null或者空字符串，不能为空格，校验和使用之前会自动过滤掉前后空格。至少包含大写字母（A-Z），小写字母（a-z），数字（0-9），非字母数字字符（限定为_）四类字符中的三类字符。组件id通过查询实例的组件列表接口（ListComponentInfos）获取
        :type component_id: str
        """
        
        

        self._node_id = None
        self._component_id = None
        self.discriminator = None

        self.node_id = node_id
        self.component_id = component_id

    @property
    def node_id(self):
        """Gets the node_id of this Shards.

        节点Id。

        :return: The node_id of this Shards.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this Shards.

        节点Id。

        :param node_id: The node_id of this Shards.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def component_id(self):
        """Gets the component_id of this Shards.

        组件Id。最大长度7个字符，不能为null或者空字符串，不能为空格，校验和使用之前会自动过滤掉前后空格。至少包含大写字母（A-Z），小写字母（a-z），数字（0-9），非字母数字字符（限定为_）四类字符中的三类字符。组件id通过查询实例的组件列表接口（ListComponentInfos）获取

        :return: The component_id of this Shards.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this Shards.

        组件Id。最大长度7个字符，不能为null或者空字符串，不能为空格，校验和使用之前会自动过滤掉前后空格。至少包含大写字母（A-Z），小写字母（a-z），数字（0-9），非字母数字字符（限定为_）四类字符中的三类字符。组件id通过查询实例的组件列表接口（ListComponentInfos）获取

        :param component_id: The component_id of this Shards.
        :type component_id: str
        """
        self._component_id = component_id

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
        if not isinstance(other, Shards):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
