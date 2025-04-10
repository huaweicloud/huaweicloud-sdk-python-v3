# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HangUpKillAllClientsRequestBody:

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
        'kill_all_nodes': 'bool'
    }

    attribute_map = {
        'node_id': 'node_id',
        'kill_all_nodes': 'kill_all_nodes'
    }

    def __init__(self, node_id=None, kill_all_nodes=None):
        r"""HangUpKillAllClientsRequestBody

        The model defined in huaweicloud sdk

        :param node_id: 指定要kill全部会话的节点ID，kill_all_nodes为false时必填
        :type node_id: str
        :param kill_all_nodes: true：Kill实例全部节点的会话 false: kill指定节点的全部会话
        :type kill_all_nodes: bool
        """
        
        

        self._node_id = None
        self._kill_all_nodes = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if kill_all_nodes is not None:
            self.kill_all_nodes = kill_all_nodes

    @property
    def node_id(self):
        r"""Gets the node_id of this HangUpKillAllClientsRequestBody.

        指定要kill全部会话的节点ID，kill_all_nodes为false时必填

        :return: The node_id of this HangUpKillAllClientsRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this HangUpKillAllClientsRequestBody.

        指定要kill全部会话的节点ID，kill_all_nodes为false时必填

        :param node_id: The node_id of this HangUpKillAllClientsRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def kill_all_nodes(self):
        r"""Gets the kill_all_nodes of this HangUpKillAllClientsRequestBody.

        true：Kill实例全部节点的会话 false: kill指定节点的全部会话

        :return: The kill_all_nodes of this HangUpKillAllClientsRequestBody.
        :rtype: bool
        """
        return self._kill_all_nodes

    @kill_all_nodes.setter
    def kill_all_nodes(self, kill_all_nodes):
        r"""Sets the kill_all_nodes of this HangUpKillAllClientsRequestBody.

        true：Kill实例全部节点的会话 false: kill指定节点的全部会话

        :param kill_all_nodes: The kill_all_nodes of this HangUpKillAllClientsRequestBody.
        :type kill_all_nodes: bool
        """
        self._kill_all_nodes = kill_all_nodes

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
        if not isinstance(other, HangUpKillAllClientsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
