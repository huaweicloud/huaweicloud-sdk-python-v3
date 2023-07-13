# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserGroupInfo:

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
        'id': 'str',
        'create_time': 'str',
        'description': 'str',
        'user_quantity': 'int',
        'parent': 'UserGroupInfo',
        'realm_id': 'str',
        'platform_type': 'str',
        'group_dn': 'str',
        'domain': 'str',
        'sid': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'create_time': 'create_time',
        'description': 'description',
        'user_quantity': 'user_quantity',
        'parent': 'parent',
        'realm_id': 'realm_id',
        'platform_type': 'platform_type',
        'group_dn': 'group_dn',
        'domain': 'domain',
        'sid': 'sid'
    }

    def __init__(self, name=None, id=None, create_time=None, description=None, user_quantity=None, parent=None, realm_id=None, platform_type=None, group_dn=None, domain=None, sid=None):
        """UserGroupInfo

        The model defined in huaweicloud sdk

        :param name: 用户组名。
        :type name: str
        :param id: 用户组ID。
        :type id: str
        :param create_time: 用户组对应的创建时间，UTC时间：yyyy-MM-ddTHH:mm:ss.SSSZ。
        :type create_time: str
        :param description: 用户组描述。
        :type description: str
        :param user_quantity: 用户列表中用户数。
        :type user_quantity: int
        :param parent: 
        :type parent: :class:`huaweicloudsdkworkspace.v2.UserGroupInfo`
        :param realm_id: 用户组域Id。
        :type realm_id: str
        :param platform_type: 用户组类型。 * AD： AD域用户组 * LOCAL： 本地liteAs用户组
        :type platform_type: str
        :param group_dn: 用户组专有名。
        :type group_dn: str
        :param domain: 用户组域名。
        :type domain: str
        :param sid: 用户组sid。
        :type sid: str
        """
        
        

        self._name = None
        self._id = None
        self._create_time = None
        self._description = None
        self._user_quantity = None
        self._parent = None
        self._realm_id = None
        self._platform_type = None
        self._group_dn = None
        self._domain = None
        self._sid = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if user_quantity is not None:
            self.user_quantity = user_quantity
        if parent is not None:
            self.parent = parent
        if realm_id is not None:
            self.realm_id = realm_id
        if platform_type is not None:
            self.platform_type = platform_type
        if group_dn is not None:
            self.group_dn = group_dn
        if domain is not None:
            self.domain = domain
        if sid is not None:
            self.sid = sid

    @property
    def name(self):
        """Gets the name of this UserGroupInfo.

        用户组名。

        :return: The name of this UserGroupInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserGroupInfo.

        用户组名。

        :param name: The name of this UserGroupInfo.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this UserGroupInfo.

        用户组ID。

        :return: The id of this UserGroupInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserGroupInfo.

        用户组ID。

        :param id: The id of this UserGroupInfo.
        :type id: str
        """
        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this UserGroupInfo.

        用户组对应的创建时间，UTC时间：yyyy-MM-ddTHH:mm:ss.SSSZ。

        :return: The create_time of this UserGroupInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UserGroupInfo.

        用户组对应的创建时间，UTC时间：yyyy-MM-ddTHH:mm:ss.SSSZ。

        :param create_time: The create_time of this UserGroupInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this UserGroupInfo.

        用户组描述。

        :return: The description of this UserGroupInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserGroupInfo.

        用户组描述。

        :param description: The description of this UserGroupInfo.
        :type description: str
        """
        self._description = description

    @property
    def user_quantity(self):
        """Gets the user_quantity of this UserGroupInfo.

        用户列表中用户数。

        :return: The user_quantity of this UserGroupInfo.
        :rtype: int
        """
        return self._user_quantity

    @user_quantity.setter
    def user_quantity(self, user_quantity):
        """Sets the user_quantity of this UserGroupInfo.

        用户列表中用户数。

        :param user_quantity: The user_quantity of this UserGroupInfo.
        :type user_quantity: int
        """
        self._user_quantity = user_quantity

    @property
    def parent(self):
        """Gets the parent of this UserGroupInfo.

        :return: The parent of this UserGroupInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.UserGroupInfo`
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this UserGroupInfo.

        :param parent: The parent of this UserGroupInfo.
        :type parent: :class:`huaweicloudsdkworkspace.v2.UserGroupInfo`
        """
        self._parent = parent

    @property
    def realm_id(self):
        """Gets the realm_id of this UserGroupInfo.

        用户组域Id。

        :return: The realm_id of this UserGroupInfo.
        :rtype: str
        """
        return self._realm_id

    @realm_id.setter
    def realm_id(self, realm_id):
        """Sets the realm_id of this UserGroupInfo.

        用户组域Id。

        :param realm_id: The realm_id of this UserGroupInfo.
        :type realm_id: str
        """
        self._realm_id = realm_id

    @property
    def platform_type(self):
        """Gets the platform_type of this UserGroupInfo.

        用户组类型。 * AD： AD域用户组 * LOCAL： 本地liteAs用户组

        :return: The platform_type of this UserGroupInfo.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """Sets the platform_type of this UserGroupInfo.

        用户组类型。 * AD： AD域用户组 * LOCAL： 本地liteAs用户组

        :param platform_type: The platform_type of this UserGroupInfo.
        :type platform_type: str
        """
        self._platform_type = platform_type

    @property
    def group_dn(self):
        """Gets the group_dn of this UserGroupInfo.

        用户组专有名。

        :return: The group_dn of this UserGroupInfo.
        :rtype: str
        """
        return self._group_dn

    @group_dn.setter
    def group_dn(self, group_dn):
        """Sets the group_dn of this UserGroupInfo.

        用户组专有名。

        :param group_dn: The group_dn of this UserGroupInfo.
        :type group_dn: str
        """
        self._group_dn = group_dn

    @property
    def domain(self):
        """Gets the domain of this UserGroupInfo.

        用户组域名。

        :return: The domain of this UserGroupInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this UserGroupInfo.

        用户组域名。

        :param domain: The domain of this UserGroupInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def sid(self):
        """Gets the sid of this UserGroupInfo.

        用户组sid。

        :return: The sid of this UserGroupInfo.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this UserGroupInfo.

        用户组sid。

        :param sid: The sid of this UserGroupInfo.
        :type sid: str
        """
        self._sid = sid

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
        if not isinstance(other, UserGroupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
