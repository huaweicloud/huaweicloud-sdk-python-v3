# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChInstancesInfoRsponseInstanceGroups:

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
        'group_type_name': 'str',
        'nodes': 'list[ClickHouseNodeInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'group_type_name': 'group_type_name',
        'nodes': 'nodes'
    }

    def __init__(self, id=None, name=None, group_type_name=None, nodes=None):
        """ChInstancesInfoRsponseInstanceGroups

        The model defined in huaweicloud sdk

        :param id: 分组ID。
        :type id: str
        :param name: 分组名。
        :type name: str
        :param group_type_name: 实例分组类型名，现在只支持clickhouse。
        :type group_type_name: str
        :param nodes: 实例节点信息。
        :type nodes: list[:class:`huaweicloudsdkgaussdb.v3.ClickHouseNodeInfo`]
        """
        
        

        self._id = None
        self._name = None
        self._group_type_name = None
        self._nodes = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.group_type_name = group_type_name
        self.nodes = nodes

    @property
    def id(self):
        """Gets the id of this ChInstancesInfoRsponseInstanceGroups.

        分组ID。

        :return: The id of this ChInstancesInfoRsponseInstanceGroups.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChInstancesInfoRsponseInstanceGroups.

        分组ID。

        :param id: The id of this ChInstancesInfoRsponseInstanceGroups.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ChInstancesInfoRsponseInstanceGroups.

        分组名。

        :return: The name of this ChInstancesInfoRsponseInstanceGroups.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChInstancesInfoRsponseInstanceGroups.

        分组名。

        :param name: The name of this ChInstancesInfoRsponseInstanceGroups.
        :type name: str
        """
        self._name = name

    @property
    def group_type_name(self):
        """Gets the group_type_name of this ChInstancesInfoRsponseInstanceGroups.

        实例分组类型名，现在只支持clickhouse。

        :return: The group_type_name of this ChInstancesInfoRsponseInstanceGroups.
        :rtype: str
        """
        return self._group_type_name

    @group_type_name.setter
    def group_type_name(self, group_type_name):
        """Sets the group_type_name of this ChInstancesInfoRsponseInstanceGroups.

        实例分组类型名，现在只支持clickhouse。

        :param group_type_name: The group_type_name of this ChInstancesInfoRsponseInstanceGroups.
        :type group_type_name: str
        """
        self._group_type_name = group_type_name

    @property
    def nodes(self):
        """Gets the nodes of this ChInstancesInfoRsponseInstanceGroups.

        实例节点信息。

        :return: The nodes of this ChInstancesInfoRsponseInstanceGroups.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ClickHouseNodeInfo`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ChInstancesInfoRsponseInstanceGroups.

        实例节点信息。

        :param nodes: The nodes of this ChInstancesInfoRsponseInstanceGroups.
        :type nodes: list[:class:`huaweicloudsdkgaussdb.v3.ClickHouseNodeInfo`]
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
        if not isinstance(other, ChInstancesInfoRsponseInstanceGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
