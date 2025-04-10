# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeNodesStartStopStatusBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_ids': 'list[str]',
        'action': 'str'
    }

    attribute_map = {
        'node_ids': 'node_ids',
        'action': 'action'
    }

    def __init__(self, node_ids=None, action=None):
        r"""ChangeNodesStartStopStatusBody

        The model defined in huaweicloud sdk

        :param node_ids: 实例需要启停的节点ID列表。未配置该参数时，默认启停实例全部节点。
        :type node_ids: list[str]
        :param action: 对实例节点的操作：  start：开启节点  stop：关闭节点 
        :type action: str
        """
        
        

        self._node_ids = None
        self._action = None
        self.discriminator = None

        if node_ids is not None:
            self.node_ids = node_ids
        if action is not None:
            self.action = action

    @property
    def node_ids(self):
        r"""Gets the node_ids of this ChangeNodesStartStopStatusBody.

        实例需要启停的节点ID列表。未配置该参数时，默认启停实例全部节点。

        :return: The node_ids of this ChangeNodesStartStopStatusBody.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        r"""Sets the node_ids of this ChangeNodesStartStopStatusBody.

        实例需要启停的节点ID列表。未配置该参数时，默认启停实例全部节点。

        :param node_ids: The node_ids of this ChangeNodesStartStopStatusBody.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    @property
    def action(self):
        r"""Gets the action of this ChangeNodesStartStopStatusBody.

        对实例节点的操作：  start：开启节点  stop：关闭节点 

        :return: The action of this ChangeNodesStartStopStatusBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ChangeNodesStartStopStatusBody.

        对实例节点的操作：  start：开启节点  stop：关闭节点 

        :param action: The action of this ChangeNodesStartStopStatusBody.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, ChangeNodesStartStopStatusBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
