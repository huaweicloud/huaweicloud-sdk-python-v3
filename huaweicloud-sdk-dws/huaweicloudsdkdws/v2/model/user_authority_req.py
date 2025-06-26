# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserAuthorityReq:

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
        'login': 'bool',
        'password': 'str',
        'system_admin': 'bool',
        'logical_cluster': 'str',
        'password_disable': 'bool',
        'create_role': 'bool',
        'create_db': 'bool',
        'inherit': 'bool',
        'conn_limit': 'int',
        'grant_members': 'list[str]',
        'grant_list': 'list[GrantAuthority]',
        'desc': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'login': 'login',
        'password': 'password',
        'system_admin': 'system_admin',
        'logical_cluster': 'logical_cluster',
        'password_disable': 'password_disable',
        'create_role': 'create_role',
        'create_db': 'create_db',
        'inherit': 'inherit',
        'conn_limit': 'conn_limit',
        'grant_members': 'grant_members',
        'grant_list': 'grant_list',
        'desc': 'desc'
    }

    def __init__(self, name=None, type=None, login=None, password=None, system_admin=None, logical_cluster=None, password_disable=None, create_role=None, create_db=None, inherit=None, conn_limit=None, grant_members=None, grant_list=None, desc=None):
        r"""UserAuthorityReq

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 用户名/角色名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type name: str
        :param type: **参数解释**： 类型。 **约束限制**： 不涉及。 **取值范围**： user：数据库用户。 role：数据库角色。 **默认取值**： 不涉及。
        :type type: str
        :param login: **参数解释**： 类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： false
        :type login: bool
        :param password: **参数解释**： 密码。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type password: str
        :param system_admin: **参数解释**： 是否是系统管理员。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type system_admin: bool
        :param logical_cluster: **参数解释**： 关联的逻辑集群名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type logical_cluster: str
        :param password_disable: **参数解释**： 是否允许密码登录。 **约束限制**： 不涉及。 **取值范围**： - true：允许密码登录 - false：不允许密码登录  **默认取值**： false
        :type password_disable: bool
        :param create_role: **参数解释**： 是否允许创建角色。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： false
        :type create_role: bool
        :param create_db: **参数解释**： 是否允许创建数据库。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： false
        :type create_db: bool
        :param inherit: **参数解释**： 是否允许继承权限。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： false
        :type inherit: bool
        :param conn_limit: **参数解释**： 连接数限制。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type conn_limit: int
        :param grant_members: **参数解释**： 授权对象信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type grant_members: list[str]
        :param grant_list: **参数解释**： 授权列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type grant_list: list[:class:`huaweicloudsdkdws.v2.GrantAuthority`]
        :param desc: **参数解释**： 描述信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type desc: str
        """
        
        

        self._name = None
        self._type = None
        self._login = None
        self._password = None
        self._system_admin = None
        self._logical_cluster = None
        self._password_disable = None
        self._create_role = None
        self._create_db = None
        self._inherit = None
        self._conn_limit = None
        self._grant_members = None
        self._grant_list = None
        self._desc = None
        self.discriminator = None

        self.name = name
        self.type = type
        if login is not None:
            self.login = login
        if password is not None:
            self.password = password
        if system_admin is not None:
            self.system_admin = system_admin
        if logical_cluster is not None:
            self.logical_cluster = logical_cluster
        if password_disable is not None:
            self.password_disable = password_disable
        if create_role is not None:
            self.create_role = create_role
        if create_db is not None:
            self.create_db = create_db
        if inherit is not None:
            self.inherit = inherit
        if conn_limit is not None:
            self.conn_limit = conn_limit
        if grant_members is not None:
            self.grant_members = grant_members
        if grant_list is not None:
            self.grant_list = grant_list
        if desc is not None:
            self.desc = desc

    @property
    def name(self):
        r"""Gets the name of this UserAuthorityReq.

        **参数解释**： 用户名/角色名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The name of this UserAuthorityReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UserAuthorityReq.

        **参数解释**： 用户名/角色名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param name: The name of this UserAuthorityReq.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this UserAuthorityReq.

        **参数解释**： 类型。 **约束限制**： 不涉及。 **取值范围**： user：数据库用户。 role：数据库角色。 **默认取值**： 不涉及。

        :return: The type of this UserAuthorityReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UserAuthorityReq.

        **参数解释**： 类型。 **约束限制**： 不涉及。 **取值范围**： user：数据库用户。 role：数据库角色。 **默认取值**： 不涉及。

        :param type: The type of this UserAuthorityReq.
        :type type: str
        """
        self._type = type

    @property
    def login(self):
        r"""Gets the login of this UserAuthorityReq.

        **参数解释**： 类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： false

        :return: The login of this UserAuthorityReq.
        :rtype: bool
        """
        return self._login

    @login.setter
    def login(self, login):
        r"""Sets the login of this UserAuthorityReq.

        **参数解释**： 类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： false

        :param login: The login of this UserAuthorityReq.
        :type login: bool
        """
        self._login = login

    @property
    def password(self):
        r"""Gets the password of this UserAuthorityReq.

        **参数解释**： 密码。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The password of this UserAuthorityReq.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this UserAuthorityReq.

        **参数解释**： 密码。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param password: The password of this UserAuthorityReq.
        :type password: str
        """
        self._password = password

    @property
    def system_admin(self):
        r"""Gets the system_admin of this UserAuthorityReq.

        **参数解释**： 是否是系统管理员。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The system_admin of this UserAuthorityReq.
        :rtype: bool
        """
        return self._system_admin

    @system_admin.setter
    def system_admin(self, system_admin):
        r"""Sets the system_admin of this UserAuthorityReq.

        **参数解释**： 是否是系统管理员。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param system_admin: The system_admin of this UserAuthorityReq.
        :type system_admin: bool
        """
        self._system_admin = system_admin

    @property
    def logical_cluster(self):
        r"""Gets the logical_cluster of this UserAuthorityReq.

        **参数解释**： 关联的逻辑集群名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The logical_cluster of this UserAuthorityReq.
        :rtype: str
        """
        return self._logical_cluster

    @logical_cluster.setter
    def logical_cluster(self, logical_cluster):
        r"""Sets the logical_cluster of this UserAuthorityReq.

        **参数解释**： 关联的逻辑集群名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param logical_cluster: The logical_cluster of this UserAuthorityReq.
        :type logical_cluster: str
        """
        self._logical_cluster = logical_cluster

    @property
    def password_disable(self):
        r"""Gets the password_disable of this UserAuthorityReq.

        **参数解释**： 是否允许密码登录。 **约束限制**： 不涉及。 **取值范围**： - true：允许密码登录 - false：不允许密码登录  **默认取值**： false

        :return: The password_disable of this UserAuthorityReq.
        :rtype: bool
        """
        return self._password_disable

    @password_disable.setter
    def password_disable(self, password_disable):
        r"""Sets the password_disable of this UserAuthorityReq.

        **参数解释**： 是否允许密码登录。 **约束限制**： 不涉及。 **取值范围**： - true：允许密码登录 - false：不允许密码登录  **默认取值**： false

        :param password_disable: The password_disable of this UserAuthorityReq.
        :type password_disable: bool
        """
        self._password_disable = password_disable

    @property
    def create_role(self):
        r"""Gets the create_role of this UserAuthorityReq.

        **参数解释**： 是否允许创建角色。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： false

        :return: The create_role of this UserAuthorityReq.
        :rtype: bool
        """
        return self._create_role

    @create_role.setter
    def create_role(self, create_role):
        r"""Sets the create_role of this UserAuthorityReq.

        **参数解释**： 是否允许创建角色。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： false

        :param create_role: The create_role of this UserAuthorityReq.
        :type create_role: bool
        """
        self._create_role = create_role

    @property
    def create_db(self):
        r"""Gets the create_db of this UserAuthorityReq.

        **参数解释**： 是否允许创建数据库。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： false

        :return: The create_db of this UserAuthorityReq.
        :rtype: bool
        """
        return self._create_db

    @create_db.setter
    def create_db(self, create_db):
        r"""Sets the create_db of this UserAuthorityReq.

        **参数解释**： 是否允许创建数据库。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： false

        :param create_db: The create_db of this UserAuthorityReq.
        :type create_db: bool
        """
        self._create_db = create_db

    @property
    def inherit(self):
        r"""Gets the inherit of this UserAuthorityReq.

        **参数解释**： 是否允许继承权限。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： false

        :return: The inherit of this UserAuthorityReq.
        :rtype: bool
        """
        return self._inherit

    @inherit.setter
    def inherit(self, inherit):
        r"""Sets the inherit of this UserAuthorityReq.

        **参数解释**： 是否允许继承权限。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： false

        :param inherit: The inherit of this UserAuthorityReq.
        :type inherit: bool
        """
        self._inherit = inherit

    @property
    def conn_limit(self):
        r"""Gets the conn_limit of this UserAuthorityReq.

        **参数解释**： 连接数限制。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The conn_limit of this UserAuthorityReq.
        :rtype: int
        """
        return self._conn_limit

    @conn_limit.setter
    def conn_limit(self, conn_limit):
        r"""Sets the conn_limit of this UserAuthorityReq.

        **参数解释**： 连接数限制。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param conn_limit: The conn_limit of this UserAuthorityReq.
        :type conn_limit: int
        """
        self._conn_limit = conn_limit

    @property
    def grant_members(self):
        r"""Gets the grant_members of this UserAuthorityReq.

        **参数解释**： 授权对象信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The grant_members of this UserAuthorityReq.
        :rtype: list[str]
        """
        return self._grant_members

    @grant_members.setter
    def grant_members(self, grant_members):
        r"""Sets the grant_members of this UserAuthorityReq.

        **参数解释**： 授权对象信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param grant_members: The grant_members of this UserAuthorityReq.
        :type grant_members: list[str]
        """
        self._grant_members = grant_members

    @property
    def grant_list(self):
        r"""Gets the grant_list of this UserAuthorityReq.

        **参数解释**： 授权列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The grant_list of this UserAuthorityReq.
        :rtype: list[:class:`huaweicloudsdkdws.v2.GrantAuthority`]
        """
        return self._grant_list

    @grant_list.setter
    def grant_list(self, grant_list):
        r"""Sets the grant_list of this UserAuthorityReq.

        **参数解释**： 授权列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param grant_list: The grant_list of this UserAuthorityReq.
        :type grant_list: list[:class:`huaweicloudsdkdws.v2.GrantAuthority`]
        """
        self._grant_list = grant_list

    @property
    def desc(self):
        r"""Gets the desc of this UserAuthorityReq.

        **参数解释**： 描述信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The desc of this UserAuthorityReq.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this UserAuthorityReq.

        **参数解释**： 描述信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param desc: The desc of this UserAuthorityReq.
        :type desc: str
        """
        self._desc = desc

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
        if not isinstance(other, UserAuthorityReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
