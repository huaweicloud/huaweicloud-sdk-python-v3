# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RouteTable:

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
        'description': 'str',
        'is_default_association': 'bool',
        'is_default_propagation': 'bool',
        'state': 'str',
        'tags': 'list[Tag]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'is_default_association': 'is_default_association',
        'is_default_propagation': 'is_default_propagation',
        'state': 'state',
        'tags': 'tags',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, description=None, is_default_association=None, is_default_propagation=None, state=None, tags=None, created_at=None, updated_at=None):
        """RouteTable

        The model defined in huaweicloud sdk

        :param id: 路由表的id
        :type id: str
        :param name: 路由表名字
        :type name: str
        :param description: 描述信息
        :type description: str
        :param is_default_association: 是否为默认关联的路由表
        :type is_default_association: bool
        :param is_default_propagation: 是否为默认传递路由表
        :type is_default_propagation: bool
        :param state: 路由表状态，支持的状态有pending | available | deleting | deleted | failed
        :type state: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdker.v3.Tag`]
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._is_default_association = None
        self._is_default_propagation = None
        self._state = None
        self._tags = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.is_default_association = is_default_association
        self.is_default_propagation = is_default_propagation
        self.state = state
        if tags is not None:
            self.tags = tags
        self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this RouteTable.

        路由表的id

        :return: The id of this RouteTable.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RouteTable.

        路由表的id

        :param id: The id of this RouteTable.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this RouteTable.

        路由表名字

        :return: The name of this RouteTable.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RouteTable.

        路由表名字

        :param name: The name of this RouteTable.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this RouteTable.

        描述信息

        :return: The description of this RouteTable.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RouteTable.

        描述信息

        :param description: The description of this RouteTable.
        :type description: str
        """
        self._description = description

    @property
    def is_default_association(self):
        """Gets the is_default_association of this RouteTable.

        是否为默认关联的路由表

        :return: The is_default_association of this RouteTable.
        :rtype: bool
        """
        return self._is_default_association

    @is_default_association.setter
    def is_default_association(self, is_default_association):
        """Sets the is_default_association of this RouteTable.

        是否为默认关联的路由表

        :param is_default_association: The is_default_association of this RouteTable.
        :type is_default_association: bool
        """
        self._is_default_association = is_default_association

    @property
    def is_default_propagation(self):
        """Gets the is_default_propagation of this RouteTable.

        是否为默认传递路由表

        :return: The is_default_propagation of this RouteTable.
        :rtype: bool
        """
        return self._is_default_propagation

    @is_default_propagation.setter
    def is_default_propagation(self, is_default_propagation):
        """Sets the is_default_propagation of this RouteTable.

        是否为默认传递路由表

        :param is_default_propagation: The is_default_propagation of this RouteTable.
        :type is_default_propagation: bool
        """
        self._is_default_propagation = is_default_propagation

    @property
    def state(self):
        """Gets the state of this RouteTable.

        路由表状态，支持的状态有pending | available | deleting | deleted | failed

        :return: The state of this RouteTable.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RouteTable.

        路由表状态，支持的状态有pending | available | deleting | deleted | failed

        :param state: The state of this RouteTable.
        :type state: str
        """
        self._state = state

    @property
    def tags(self):
        """Gets the tags of this RouteTable.

        标签

        :return: The tags of this RouteTable.
        :rtype: list[:class:`huaweicloudsdker.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RouteTable.

        标签

        :param tags: The tags of this RouteTable.
        :type tags: list[:class:`huaweicloudsdker.v3.Tag`]
        """
        self._tags = tags

    @property
    def created_at(self):
        """Gets the created_at of this RouteTable.

        创建时间

        :return: The created_at of this RouteTable.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RouteTable.

        创建时间

        :param created_at: The created_at of this RouteTable.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this RouteTable.

        更新时间

        :return: The updated_at of this RouteTable.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RouteTable.

        更新时间

        :param updated_at: The updated_at of this RouteTable.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, RouteTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
