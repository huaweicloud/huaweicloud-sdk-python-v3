# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpnUser:

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
        'user_group_id': 'str',
        'user_group_name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'static_ip': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'user_group_id': 'user_group_id',
        'user_group_name': 'user_group_name',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'static_ip': 'static_ip'
    }

    def __init__(self, id=None, name=None, description=None, user_group_id=None, user_group_name=None, created_at=None, updated_at=None, static_ip=None):
        r"""VpnUser

        The model defined in huaweicloud sdk

        :param id: 用户ID
        :type id: str
        :param name: 用户名称
        :type name: str
        :param description: 用户描述
        :type description: str
        :param user_group_id: 所属用户组ID
        :type user_group_id: str
        :param user_group_name: 所属用户组名称
        :type user_group_name: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param static_ip: 静态客户端IP地址，disable表示随机分配客户端IP
        :type static_ip: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._user_group_id = None
        self._user_group_name = None
        self._created_at = None
        self._updated_at = None
        self._static_ip = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if user_group_id is not None:
            self.user_group_id = user_group_id
        if user_group_name is not None:
            self.user_group_name = user_group_name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if static_ip is not None:
            self.static_ip = static_ip

    @property
    def id(self):
        r"""Gets the id of this VpnUser.

        用户ID

        :return: The id of this VpnUser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VpnUser.

        用户ID

        :param id: The id of this VpnUser.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this VpnUser.

        用户名称

        :return: The name of this VpnUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this VpnUser.

        用户名称

        :param name: The name of this VpnUser.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this VpnUser.

        用户描述

        :return: The description of this VpnUser.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this VpnUser.

        用户描述

        :param description: The description of this VpnUser.
        :type description: str
        """
        self._description = description

    @property
    def user_group_id(self):
        r"""Gets the user_group_id of this VpnUser.

        所属用户组ID

        :return: The user_group_id of this VpnUser.
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        r"""Sets the user_group_id of this VpnUser.

        所属用户组ID

        :param user_group_id: The user_group_id of this VpnUser.
        :type user_group_id: str
        """
        self._user_group_id = user_group_id

    @property
    def user_group_name(self):
        r"""Gets the user_group_name of this VpnUser.

        所属用户组名称

        :return: The user_group_name of this VpnUser.
        :rtype: str
        """
        return self._user_group_name

    @user_group_name.setter
    def user_group_name(self, user_group_name):
        r"""Sets the user_group_name of this VpnUser.

        所属用户组名称

        :param user_group_name: The user_group_name of this VpnUser.
        :type user_group_name: str
        """
        self._user_group_name = user_group_name

    @property
    def created_at(self):
        r"""Gets the created_at of this VpnUser.

        创建时间

        :return: The created_at of this VpnUser.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this VpnUser.

        创建时间

        :param created_at: The created_at of this VpnUser.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this VpnUser.

        更新时间

        :return: The updated_at of this VpnUser.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this VpnUser.

        更新时间

        :param updated_at: The updated_at of this VpnUser.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def static_ip(self):
        r"""Gets the static_ip of this VpnUser.

        静态客户端IP地址，disable表示随机分配客户端IP

        :return: The static_ip of this VpnUser.
        :rtype: str
        """
        return self._static_ip

    @static_ip.setter
    def static_ip(self, static_ip):
        r"""Sets the static_ip of this VpnUser.

        静态客户端IP地址，disable表示随机分配客户端IP

        :param static_ip: The static_ip of this VpnUser.
        :type static_ip: str
        """
        self._static_ip = static_ip

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
        if not isinstance(other, VpnUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
