# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopoNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_type': 'str',
        'node_name': 'str',
        'node_id': 'str',
        'env_id': 'int'
    }

    attribute_map = {
        'node_type': 'node_type',
        'node_name': 'node_name',
        'node_id': 'node_id',
        'env_id': 'env_id'
    }

    def __init__(self, node_type=None, node_name=None, node_id=None, env_id=None):
        """TopoNode

        The model defined in huaweicloud sdk

        :param node_type: 节点类型。
        :type node_type: str
        :param node_name: 节点名称。
        :type node_name: str
        :param node_id: 节点id。
        :type node_id: str
        :param env_id: 环境id。
        :type env_id: int
        """
        
        

        self._node_type = None
        self._node_name = None
        self._node_id = None
        self._env_id = None
        self.discriminator = None

        if node_type is not None:
            self.node_type = node_type
        if node_name is not None:
            self.node_name = node_name
        if node_id is not None:
            self.node_id = node_id
        if env_id is not None:
            self.env_id = env_id

    @property
    def node_type(self):
        """Gets the node_type of this TopoNode.

        节点类型。

        :return: The node_type of this TopoNode.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this TopoNode.

        节点类型。

        :param node_type: The node_type of this TopoNode.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def node_name(self):
        """Gets the node_name of this TopoNode.

        节点名称。

        :return: The node_name of this TopoNode.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this TopoNode.

        节点名称。

        :param node_name: The node_name of this TopoNode.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def node_id(self):
        """Gets the node_id of this TopoNode.

        节点id。

        :return: The node_id of this TopoNode.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this TopoNode.

        节点id。

        :param node_id: The node_id of this TopoNode.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def env_id(self):
        """Gets the env_id of this TopoNode.

        环境id。

        :return: The env_id of this TopoNode.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this TopoNode.

        环境id。

        :param env_id: The env_id of this TopoNode.
        :type env_id: int
        """
        self._env_id = env_id

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
        if not isinstance(other, TopoNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
