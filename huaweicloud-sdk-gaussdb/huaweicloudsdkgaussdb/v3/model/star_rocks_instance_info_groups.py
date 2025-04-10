# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StarRocksInstanceInfoGroups:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'nodes': 'list[StarRocksInstanceInfoNodes]',
        'group_type_name': 'str',
        'group_node_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'nodes': 'nodes',
        'group_type_name': 'group_type_name',
        'group_node_type': 'group_node_type'
    }

    def __init__(self, id=None, name=None, nodes=None, group_type_name=None, group_node_type=None):
        r"""StarRocksInstanceInfoGroups

        The model defined in huaweicloud sdk

        :param id: 分组ID。
        :type id: str
        :param name: 分组名。
        :type name: str
        :param nodes: 实例节点。
        :type nodes: list[:class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoNodes`]
        :param group_type_name: 实例分组类型名。
        :type group_type_name: str
        :param group_node_type: 实例分组节点类型。
        :type group_node_type: str
        """
        
        

        self._id = None
        self._name = None
        self._nodes = None
        self._group_type_name = None
        self._group_node_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if nodes is not None:
            self.nodes = nodes
        if group_type_name is not None:
            self.group_type_name = group_type_name
        if group_node_type is not None:
            self.group_node_type = group_node_type

    @property
    def id(self):
        r"""Gets the id of this StarRocksInstanceInfoGroups.

        分组ID。

        :return: The id of this StarRocksInstanceInfoGroups.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StarRocksInstanceInfoGroups.

        分组ID。

        :param id: The id of this StarRocksInstanceInfoGroups.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this StarRocksInstanceInfoGroups.

        分组名。

        :return: The name of this StarRocksInstanceInfoGroups.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StarRocksInstanceInfoGroups.

        分组名。

        :param name: The name of this StarRocksInstanceInfoGroups.
        :type name: str
        """
        self._name = name

    @property
    def nodes(self):
        r"""Gets the nodes of this StarRocksInstanceInfoGroups.

        实例节点。

        :return: The nodes of this StarRocksInstanceInfoGroups.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoNodes`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this StarRocksInstanceInfoGroups.

        实例节点。

        :param nodes: The nodes of this StarRocksInstanceInfoGroups.
        :type nodes: list[:class:`huaweicloudsdkgaussdb.v3.StarRocksInstanceInfoNodes`]
        """
        self._nodes = nodes

    @property
    def group_type_name(self):
        r"""Gets the group_type_name of this StarRocksInstanceInfoGroups.

        实例分组类型名。

        :return: The group_type_name of this StarRocksInstanceInfoGroups.
        :rtype: str
        """
        return self._group_type_name

    @group_type_name.setter
    def group_type_name(self, group_type_name):
        r"""Sets the group_type_name of this StarRocksInstanceInfoGroups.

        实例分组类型名。

        :param group_type_name: The group_type_name of this StarRocksInstanceInfoGroups.
        :type group_type_name: str
        """
        self._group_type_name = group_type_name

    @property
    def group_node_type(self):
        r"""Gets the group_node_type of this StarRocksInstanceInfoGroups.

        实例分组节点类型。

        :return: The group_node_type of this StarRocksInstanceInfoGroups.
        :rtype: str
        """
        return self._group_node_type

    @group_node_type.setter
    def group_node_type(self, group_node_type):
        r"""Sets the group_node_type of this StarRocksInstanceInfoGroups.

        实例分组节点类型。

        :param group_node_type: The group_node_type of this StarRocksInstanceInfoGroups.
        :type group_node_type: str
        """
        self._group_node_type = group_node_type

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
        if not isinstance(other, StarRocksInstanceInfoGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
