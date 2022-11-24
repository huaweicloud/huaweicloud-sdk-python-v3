# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TraceTopologyNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'int',
        'node_name': 'str',
        'hint': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'node_name': 'node_name',
        'hint': 'hint'
    }

    def __init__(self, node_id=None, node_name=None, hint=None):
        """TraceTopologyNode

        The model defined in huaweicloud sdk

        :param node_id: 节点id。
        :type node_id: int
        :param node_name: 节点名称。
        :type node_name: str
        :param hint: 节点提示字段。
        :type hint: str
        """
        
        

        self._node_id = None
        self._node_name = None
        self._hint = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name
        if hint is not None:
            self.hint = hint

    @property
    def node_id(self):
        """Gets the node_id of this TraceTopologyNode.

        节点id。

        :return: The node_id of this TraceTopologyNode.
        :rtype: int
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this TraceTopologyNode.

        节点id。

        :param node_id: The node_id of this TraceTopologyNode.
        :type node_id: int
        """
        self._node_id = node_id

    @property
    def node_name(self):
        """Gets the node_name of this TraceTopologyNode.

        节点名称。

        :return: The node_name of this TraceTopologyNode.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this TraceTopologyNode.

        节点名称。

        :param node_name: The node_name of this TraceTopologyNode.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def hint(self):
        """Gets the hint of this TraceTopologyNode.

        节点提示字段。

        :return: The hint of this TraceTopologyNode.
        :rtype: str
        """
        return self._hint

    @hint.setter
    def hint(self, hint):
        """Sets the hint of this TraceTopologyNode.

        节点提示字段。

        :param hint: The hint of this TraceTopologyNode.
        :type hint: str
        """
        self._hint = hint

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
        if not isinstance(other, TraceTopologyNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
