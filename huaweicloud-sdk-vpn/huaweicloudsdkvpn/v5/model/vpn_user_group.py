# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpnUserGroup:

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
        'type': 'str',
        'user_number': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'user_number': 'user_number',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, description=None, type=None, user_number=None, created_at=None, updated_at=None):
        """VpnUserGroup

        The model defined in huaweicloud sdk

        :param id: 用户组ID
        :type id: str
        :param name: 用户组名称
        :type name: str
        :param description: 用户组描述
        :type description: str
        :param type: 用户组类型
        :type type: str
        :param user_number: 用户数量
        :type user_number: int
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._type = None
        self._user_number = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if user_number is not None:
            self.user_number = user_number
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this VpnUserGroup.

        用户组ID

        :return: The id of this VpnUserGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VpnUserGroup.

        用户组ID

        :param id: The id of this VpnUserGroup.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this VpnUserGroup.

        用户组名称

        :return: The name of this VpnUserGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VpnUserGroup.

        用户组名称

        :param name: The name of this VpnUserGroup.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this VpnUserGroup.

        用户组描述

        :return: The description of this VpnUserGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VpnUserGroup.

        用户组描述

        :param description: The description of this VpnUserGroup.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this VpnUserGroup.

        用户组类型

        :return: The type of this VpnUserGroup.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VpnUserGroup.

        用户组类型

        :param type: The type of this VpnUserGroup.
        :type type: str
        """
        self._type = type

    @property
    def user_number(self):
        """Gets the user_number of this VpnUserGroup.

        用户数量

        :return: The user_number of this VpnUserGroup.
        :rtype: int
        """
        return self._user_number

    @user_number.setter
    def user_number(self, user_number):
        """Sets the user_number of this VpnUserGroup.

        用户数量

        :param user_number: The user_number of this VpnUserGroup.
        :type user_number: int
        """
        self._user_number = user_number

    @property
    def created_at(self):
        """Gets the created_at of this VpnUserGroup.

        创建时间

        :return: The created_at of this VpnUserGroup.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VpnUserGroup.

        创建时间

        :param created_at: The created_at of this VpnUserGroup.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this VpnUserGroup.

        更新时间

        :return: The updated_at of this VpnUserGroup.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this VpnUserGroup.

        更新时间

        :param updated_at: The updated_at of this VpnUserGroup.
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
        if not isinstance(other, VpnUserGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
