# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceNodesInfoInstanceNodes:

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
        'role': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'role': 'role',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, role=None, status=None, type=None):
        r"""InstanceNodesInfoInstanceNodes

        The model defined in huaweicloud sdk

        :param id: 节点ID
        :type id: str
        :param name: 节点名
        :type name: str
        :param role: 节点角色
        :type role: str
        :param status: 节点状态
        :type status: str
        :param type: 节点类型
        :type type: str
        """
        
        

        self._id = None
        self._name = None
        self._role = None
        self._status = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if role is not None:
            self.role = role
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def id(self):
        r"""Gets the id of this InstanceNodesInfoInstanceNodes.

        节点ID

        :return: The id of this InstanceNodesInfoInstanceNodes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InstanceNodesInfoInstanceNodes.

        节点ID

        :param id: The id of this InstanceNodesInfoInstanceNodes.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this InstanceNodesInfoInstanceNodes.

        节点名

        :return: The name of this InstanceNodesInfoInstanceNodes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InstanceNodesInfoInstanceNodes.

        节点名

        :param name: The name of this InstanceNodesInfoInstanceNodes.
        :type name: str
        """
        self._name = name

    @property
    def role(self):
        r"""Gets the role of this InstanceNodesInfoInstanceNodes.

        节点角色

        :return: The role of this InstanceNodesInfoInstanceNodes.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this InstanceNodesInfoInstanceNodes.

        节点角色

        :param role: The role of this InstanceNodesInfoInstanceNodes.
        :type role: str
        """
        self._role = role

    @property
    def status(self):
        r"""Gets the status of this InstanceNodesInfoInstanceNodes.

        节点状态

        :return: The status of this InstanceNodesInfoInstanceNodes.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InstanceNodesInfoInstanceNodes.

        节点状态

        :param status: The status of this InstanceNodesInfoInstanceNodes.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this InstanceNodesInfoInstanceNodes.

        节点类型

        :return: The type of this InstanceNodesInfoInstanceNodes.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this InstanceNodesInfoInstanceNodes.

        节点类型

        :param type: The type of this InstanceNodesInfoInstanceNodes.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, InstanceNodesInfoInstanceNodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
