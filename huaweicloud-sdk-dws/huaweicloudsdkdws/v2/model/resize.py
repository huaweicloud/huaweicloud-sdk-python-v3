# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Resize:

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
        'number_of_node': 'int'
    }

    attribute_map = {
        'node_type': 'node_type',
        'number_of_node': 'number_of_node'
    }

    def __init__(self, node_type=None, number_of_node=None):
        """Resize

        The model defined in huaweicloud sdk

        :param node_type: 调整大小目标规格
        :type node_type: str
        :param number_of_node: 调整大小目标节点数
        :type number_of_node: int
        """
        
        

        self._node_type = None
        self._number_of_node = None
        self.discriminator = None

        self.node_type = node_type
        self.number_of_node = number_of_node

    @property
    def node_type(self):
        """Gets the node_type of this Resize.

        调整大小目标规格

        :return: The node_type of this Resize.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this Resize.

        调整大小目标规格

        :param node_type: The node_type of this Resize.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def number_of_node(self):
        """Gets the number_of_node of this Resize.

        调整大小目标节点数

        :return: The number_of_node of this Resize.
        :rtype: int
        """
        return self._number_of_node

    @number_of_node.setter
    def number_of_node(self, number_of_node):
        """Sets the number_of_node of this Resize.

        调整大小目标节点数

        :param number_of_node: The number_of_node of this Resize.
        :type number_of_node: int
        """
        self._number_of_node = number_of_node

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
        if not isinstance(other, Resize):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
