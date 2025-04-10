# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGroupRequestBody:

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
        'type': 'str',
        'flavor_id': 'str',
        'nodes': 'list[NodeInfo]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'flavor_id': 'flavor_id',
        'nodes': 'nodes'
    }

    def __init__(self, name=None, type=None, flavor_id=None, nodes=None):
        r"""CreateGroupRequestBody

        The model defined in huaweicloud sdk

        :param name: 组名称
        :type name: str
        :param type: 组类型，type：rw读写、r只读
        :type type: str
        :param flavor_id: 节点规格ID。
        :type flavor_id: str
        :param nodes: 节点信息列表
        :type nodes: list[:class:`huaweicloudsdkddm.v1.NodeInfo`]
        """
        
        

        self._name = None
        self._type = None
        self._flavor_id = None
        self._nodes = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.flavor_id = flavor_id
        self.nodes = nodes

    @property
    def name(self):
        r"""Gets the name of this CreateGroupRequestBody.

        组名称

        :return: The name of this CreateGroupRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateGroupRequestBody.

        组名称

        :param name: The name of this CreateGroupRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this CreateGroupRequestBody.

        组类型，type：rw读写、r只读

        :return: The type of this CreateGroupRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateGroupRequestBody.

        组类型，type：rw读写、r只读

        :param type: The type of this CreateGroupRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this CreateGroupRequestBody.

        节点规格ID。

        :return: The flavor_id of this CreateGroupRequestBody.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this CreateGroupRequestBody.

        节点规格ID。

        :param flavor_id: The flavor_id of this CreateGroupRequestBody.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def nodes(self):
        r"""Gets the nodes of this CreateGroupRequestBody.

        节点信息列表

        :return: The nodes of this CreateGroupRequestBody.
        :rtype: list[:class:`huaweicloudsdkddm.v1.NodeInfo`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this CreateGroupRequestBody.

        节点信息列表

        :param nodes: The nodes of this CreateGroupRequestBody.
        :type nodes: list[:class:`huaweicloudsdkddm.v1.NodeInfo`]
        """
        self._nodes = nodes

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
        if not isinstance(other, CreateGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
