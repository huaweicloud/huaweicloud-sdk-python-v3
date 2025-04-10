# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EmChildNodeV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'relation_id': 'str',
        'id': 'str',
        'name': 'str',
        'child_nodes': 'list[EmChildNodeV2]'
    }

    attribute_map = {
        'relation_id': 'relation_id',
        'id': 'id',
        'name': 'name',
        'child_nodes': 'child_nodes'
    }

    def __init__(self, relation_id=None, id=None, name=None, child_nodes=None):
        r"""EmChildNodeV2

        The model defined in huaweicloud sdk

        :param relation_id: 实体关系ID。
        :type relation_id: str
        :param id: 节点ID（即组织单元的Party ID）。
        :type id: str
        :param name: 节点名称。
        :type name: str
        :param child_nodes: 子节点列表。
        :type child_nodes: list[:class:`huaweicloudsdkbss.v2.EmChildNodeV2`]
        """
        
        

        self._relation_id = None
        self._id = None
        self._name = None
        self._child_nodes = None
        self.discriminator = None

        if relation_id is not None:
            self.relation_id = relation_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if child_nodes is not None:
            self.child_nodes = child_nodes

    @property
    def relation_id(self):
        r"""Gets the relation_id of this EmChildNodeV2.

        实体关系ID。

        :return: The relation_id of this EmChildNodeV2.
        :rtype: str
        """
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        r"""Sets the relation_id of this EmChildNodeV2.

        实体关系ID。

        :param relation_id: The relation_id of this EmChildNodeV2.
        :type relation_id: str
        """
        self._relation_id = relation_id

    @property
    def id(self):
        r"""Gets the id of this EmChildNodeV2.

        节点ID（即组织单元的Party ID）。

        :return: The id of this EmChildNodeV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EmChildNodeV2.

        节点ID（即组织单元的Party ID）。

        :param id: The id of this EmChildNodeV2.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this EmChildNodeV2.

        节点名称。

        :return: The name of this EmChildNodeV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EmChildNodeV2.

        节点名称。

        :param name: The name of this EmChildNodeV2.
        :type name: str
        """
        self._name = name

    @property
    def child_nodes(self):
        r"""Gets the child_nodes of this EmChildNodeV2.

        子节点列表。

        :return: The child_nodes of this EmChildNodeV2.
        :rtype: list[:class:`huaweicloudsdkbss.v2.EmChildNodeV2`]
        """
        return self._child_nodes

    @child_nodes.setter
    def child_nodes(self, child_nodes):
        r"""Sets the child_nodes of this EmChildNodeV2.

        子节点列表。

        :param child_nodes: The child_nodes of this EmChildNodeV2.
        :type child_nodes: list[:class:`huaweicloudsdkbss.v2.EmChildNodeV2`]
        """
        self._child_nodes = child_nodes

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
        if not isinstance(other, EmChildNodeV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
