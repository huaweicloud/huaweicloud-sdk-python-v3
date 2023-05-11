# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrgPeer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'node_count': 'int'
    }

    attribute_map = {
        'name': 'name',
        'node_count': 'node_count'
    }

    def __init__(self, name=None, node_count=None):
        """OrgPeer

        The model defined in huaweicloud sdk

        :param name: 组织名称
        :type name: str
        :param node_count: 组织节点数
        :type node_count: int
        """
        
        

        self._name = None
        self._node_count = None
        self.discriminator = None

        self.name = name
        self.node_count = node_count

    @property
    def name(self):
        """Gets the name of this OrgPeer.

        组织名称

        :return: The name of this OrgPeer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrgPeer.

        组织名称

        :param name: The name of this OrgPeer.
        :type name: str
        """
        self._name = name

    @property
    def node_count(self):
        """Gets the node_count of this OrgPeer.

        组织节点数

        :return: The node_count of this OrgPeer.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """Sets the node_count of this OrgPeer.

        组织节点数

        :param node_count: The node_count of this OrgPeer.
        :type node_count: int
        """
        self._node_count = node_count

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
        if not isinstance(other, OrgPeer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
