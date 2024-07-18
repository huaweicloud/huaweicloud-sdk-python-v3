# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpnAccessPolicy:

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
        'user_group_id': 'str',
        'user_group_name': 'str',
        'description': 'str',
        'dest_ip_cidrs': 'list[str]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'user_group_id': 'user_group_id',
        'user_group_name': 'user_group_name',
        'description': 'description',
        'dest_ip_cidrs': 'dest_ip_cidrs',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, user_group_id=None, user_group_name=None, description=None, dest_ip_cidrs=None, created_at=None, updated_at=None):
        """VpnAccessPolicy

        The model defined in huaweicloud sdk

        :param id: 访问策略ID
        :type id: str
        :param name: 访问策略名称
        :type name: str
        :param user_group_id: 关联用户组ID
        :type user_group_id: str
        :param user_group_name: 关联用户组名称
        :type user_group_name: str
        :param description: 访问策略描述
        :type description: str
        :param dest_ip_cidrs: 目的IP网段列表
        :type dest_ip_cidrs: list[str]
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._user_group_id = None
        self._user_group_name = None
        self._description = None
        self._dest_ip_cidrs = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if user_group_id is not None:
            self.user_group_id = user_group_id
        if user_group_name is not None:
            self.user_group_name = user_group_name
        if description is not None:
            self.description = description
        if dest_ip_cidrs is not None:
            self.dest_ip_cidrs = dest_ip_cidrs
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this VpnAccessPolicy.

        访问策略ID

        :return: The id of this VpnAccessPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VpnAccessPolicy.

        访问策略ID

        :param id: The id of this VpnAccessPolicy.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this VpnAccessPolicy.

        访问策略名称

        :return: The name of this VpnAccessPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VpnAccessPolicy.

        访问策略名称

        :param name: The name of this VpnAccessPolicy.
        :type name: str
        """
        self._name = name

    @property
    def user_group_id(self):
        """Gets the user_group_id of this VpnAccessPolicy.

        关联用户组ID

        :return: The user_group_id of this VpnAccessPolicy.
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """Sets the user_group_id of this VpnAccessPolicy.

        关联用户组ID

        :param user_group_id: The user_group_id of this VpnAccessPolicy.
        :type user_group_id: str
        """
        self._user_group_id = user_group_id

    @property
    def user_group_name(self):
        """Gets the user_group_name of this VpnAccessPolicy.

        关联用户组名称

        :return: The user_group_name of this VpnAccessPolicy.
        :rtype: str
        """
        return self._user_group_name

    @user_group_name.setter
    def user_group_name(self, user_group_name):
        """Sets the user_group_name of this VpnAccessPolicy.

        关联用户组名称

        :param user_group_name: The user_group_name of this VpnAccessPolicy.
        :type user_group_name: str
        """
        self._user_group_name = user_group_name

    @property
    def description(self):
        """Gets the description of this VpnAccessPolicy.

        访问策略描述

        :return: The description of this VpnAccessPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VpnAccessPolicy.

        访问策略描述

        :param description: The description of this VpnAccessPolicy.
        :type description: str
        """
        self._description = description

    @property
    def dest_ip_cidrs(self):
        """Gets the dest_ip_cidrs of this VpnAccessPolicy.

        目的IP网段列表

        :return: The dest_ip_cidrs of this VpnAccessPolicy.
        :rtype: list[str]
        """
        return self._dest_ip_cidrs

    @dest_ip_cidrs.setter
    def dest_ip_cidrs(self, dest_ip_cidrs):
        """Sets the dest_ip_cidrs of this VpnAccessPolicy.

        目的IP网段列表

        :param dest_ip_cidrs: The dest_ip_cidrs of this VpnAccessPolicy.
        :type dest_ip_cidrs: list[str]
        """
        self._dest_ip_cidrs = dest_ip_cidrs

    @property
    def created_at(self):
        """Gets the created_at of this VpnAccessPolicy.

        创建时间

        :return: The created_at of this VpnAccessPolicy.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VpnAccessPolicy.

        创建时间

        :param created_at: The created_at of this VpnAccessPolicy.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this VpnAccessPolicy.

        更新时间

        :return: The updated_at of this VpnAccessPolicy.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this VpnAccessPolicy.

        更新时间

        :param updated_at: The updated_at of this VpnAccessPolicy.
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
        if not isinstance(other, VpnAccessPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
