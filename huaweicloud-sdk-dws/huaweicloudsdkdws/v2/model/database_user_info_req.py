# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseUserInfoReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'login': 'bool',
        'createrole': 'bool',
        'createdb': 'bool',
        'systemadmin': 'bool',
        'auditadmin': 'bool',
        'inherit': 'bool',
        'useft': 'bool',
        'conn_limit': 'int',
        'replication': 'bool',
        'valid_begin': 'str',
        'valid_until': 'str',
        'lock': 'bool'
    }

    attribute_map = {
        'login': 'login',
        'createrole': 'createrole',
        'createdb': 'createdb',
        'systemadmin': 'systemadmin',
        'auditadmin': 'auditadmin',
        'inherit': 'inherit',
        'useft': 'useft',
        'conn_limit': 'conn_limit',
        'replication': 'replication',
        'valid_begin': 'valid_begin',
        'valid_until': 'valid_until',
        'lock': 'lock'
    }

    def __init__(self, login=None, createrole=None, createdb=None, systemadmin=None, auditadmin=None, inherit=None, useft=None, conn_limit=None, replication=None, valid_begin=None, valid_until=None, lock=None):
        r"""DatabaseUserInfoReq

        The model defined in huaweicloud sdk

        :param login: **参数解释**： 是否可以登录。 **取值范围**： 不涉及。
        :type login: bool
        :param createrole: **参数解释**： 创建角色权限。 **取值范围**： 不涉及。
        :type createrole: bool
        :param createdb: **参数解释**： 创建数据库权限。 **取值范围**： 不涉及。
        :type createdb: bool
        :param systemadmin: **参数解释**： 系统管理员。 **取值范围**： 不涉及。
        :type systemadmin: bool
        :param auditadmin: **参数解释**： 审计管理员。 **取值范围**： 不涉及。
        :type auditadmin: bool
        :param inherit: **参数解释**： 继承所在组权限。 **取值范围**： 不涉及。
        :type inherit: bool
        :param useft: **参数解释**： 访问外表权限。 **取值范围**： 不涉及。
        :type useft: bool
        :param conn_limit: **参数解释**： 连接数限制。 **取值范围**： 不涉及。
        :type conn_limit: int
        :param replication: **参数解释**： 是否允许流复制。 **取值范围**： 不涉及。
        :type replication: bool
        :param valid_begin: **参数解释**： 角色生效时间。格式：yyyy-MM-ddTHH:mm:ssZ。 **取值范围**： 不涉及。
        :type valid_begin: str
        :param valid_until: **参数解释**： 角色过期时间。格式：yyyy-MM-ddTHH:mm:ssZ。 **取值范围**： 不涉及。
        :type valid_until: str
        :param lock: **参数解释**： 是否锁定。 **取值范围**： 不涉及。
        :type lock: bool
        """
        
        

        self._login = None
        self._createrole = None
        self._createdb = None
        self._systemadmin = None
        self._auditadmin = None
        self._inherit = None
        self._useft = None
        self._conn_limit = None
        self._replication = None
        self._valid_begin = None
        self._valid_until = None
        self._lock = None
        self.discriminator = None

        if login is not None:
            self.login = login
        if createrole is not None:
            self.createrole = createrole
        if createdb is not None:
            self.createdb = createdb
        if systemadmin is not None:
            self.systemadmin = systemadmin
        if auditadmin is not None:
            self.auditadmin = auditadmin
        if inherit is not None:
            self.inherit = inherit
        if useft is not None:
            self.useft = useft
        if conn_limit is not None:
            self.conn_limit = conn_limit
        if replication is not None:
            self.replication = replication
        if valid_begin is not None:
            self.valid_begin = valid_begin
        if valid_until is not None:
            self.valid_until = valid_until
        if lock is not None:
            self.lock = lock

    @property
    def login(self):
        r"""Gets the login of this DatabaseUserInfoReq.

        **参数解释**： 是否可以登录。 **取值范围**： 不涉及。

        :return: The login of this DatabaseUserInfoReq.
        :rtype: bool
        """
        return self._login

    @login.setter
    def login(self, login):
        r"""Sets the login of this DatabaseUserInfoReq.

        **参数解释**： 是否可以登录。 **取值范围**： 不涉及。

        :param login: The login of this DatabaseUserInfoReq.
        :type login: bool
        """
        self._login = login

    @property
    def createrole(self):
        r"""Gets the createrole of this DatabaseUserInfoReq.

        **参数解释**： 创建角色权限。 **取值范围**： 不涉及。

        :return: The createrole of this DatabaseUserInfoReq.
        :rtype: bool
        """
        return self._createrole

    @createrole.setter
    def createrole(self, createrole):
        r"""Sets the createrole of this DatabaseUserInfoReq.

        **参数解释**： 创建角色权限。 **取值范围**： 不涉及。

        :param createrole: The createrole of this DatabaseUserInfoReq.
        :type createrole: bool
        """
        self._createrole = createrole

    @property
    def createdb(self):
        r"""Gets the createdb of this DatabaseUserInfoReq.

        **参数解释**： 创建数据库权限。 **取值范围**： 不涉及。

        :return: The createdb of this DatabaseUserInfoReq.
        :rtype: bool
        """
        return self._createdb

    @createdb.setter
    def createdb(self, createdb):
        r"""Sets the createdb of this DatabaseUserInfoReq.

        **参数解释**： 创建数据库权限。 **取值范围**： 不涉及。

        :param createdb: The createdb of this DatabaseUserInfoReq.
        :type createdb: bool
        """
        self._createdb = createdb

    @property
    def systemadmin(self):
        r"""Gets the systemadmin of this DatabaseUserInfoReq.

        **参数解释**： 系统管理员。 **取值范围**： 不涉及。

        :return: The systemadmin of this DatabaseUserInfoReq.
        :rtype: bool
        """
        return self._systemadmin

    @systemadmin.setter
    def systemadmin(self, systemadmin):
        r"""Sets the systemadmin of this DatabaseUserInfoReq.

        **参数解释**： 系统管理员。 **取值范围**： 不涉及。

        :param systemadmin: The systemadmin of this DatabaseUserInfoReq.
        :type systemadmin: bool
        """
        self._systemadmin = systemadmin

    @property
    def auditadmin(self):
        r"""Gets the auditadmin of this DatabaseUserInfoReq.

        **参数解释**： 审计管理员。 **取值范围**： 不涉及。

        :return: The auditadmin of this DatabaseUserInfoReq.
        :rtype: bool
        """
        return self._auditadmin

    @auditadmin.setter
    def auditadmin(self, auditadmin):
        r"""Sets the auditadmin of this DatabaseUserInfoReq.

        **参数解释**： 审计管理员。 **取值范围**： 不涉及。

        :param auditadmin: The auditadmin of this DatabaseUserInfoReq.
        :type auditadmin: bool
        """
        self._auditadmin = auditadmin

    @property
    def inherit(self):
        r"""Gets the inherit of this DatabaseUserInfoReq.

        **参数解释**： 继承所在组权限。 **取值范围**： 不涉及。

        :return: The inherit of this DatabaseUserInfoReq.
        :rtype: bool
        """
        return self._inherit

    @inherit.setter
    def inherit(self, inherit):
        r"""Sets the inherit of this DatabaseUserInfoReq.

        **参数解释**： 继承所在组权限。 **取值范围**： 不涉及。

        :param inherit: The inherit of this DatabaseUserInfoReq.
        :type inherit: bool
        """
        self._inherit = inherit

    @property
    def useft(self):
        r"""Gets the useft of this DatabaseUserInfoReq.

        **参数解释**： 访问外表权限。 **取值范围**： 不涉及。

        :return: The useft of this DatabaseUserInfoReq.
        :rtype: bool
        """
        return self._useft

    @useft.setter
    def useft(self, useft):
        r"""Sets the useft of this DatabaseUserInfoReq.

        **参数解释**： 访问外表权限。 **取值范围**： 不涉及。

        :param useft: The useft of this DatabaseUserInfoReq.
        :type useft: bool
        """
        self._useft = useft

    @property
    def conn_limit(self):
        r"""Gets the conn_limit of this DatabaseUserInfoReq.

        **参数解释**： 连接数限制。 **取值范围**： 不涉及。

        :return: The conn_limit of this DatabaseUserInfoReq.
        :rtype: int
        """
        return self._conn_limit

    @conn_limit.setter
    def conn_limit(self, conn_limit):
        r"""Sets the conn_limit of this DatabaseUserInfoReq.

        **参数解释**： 连接数限制。 **取值范围**： 不涉及。

        :param conn_limit: The conn_limit of this DatabaseUserInfoReq.
        :type conn_limit: int
        """
        self._conn_limit = conn_limit

    @property
    def replication(self):
        r"""Gets the replication of this DatabaseUserInfoReq.

        **参数解释**： 是否允许流复制。 **取值范围**： 不涉及。

        :return: The replication of this DatabaseUserInfoReq.
        :rtype: bool
        """
        return self._replication

    @replication.setter
    def replication(self, replication):
        r"""Sets the replication of this DatabaseUserInfoReq.

        **参数解释**： 是否允许流复制。 **取值范围**： 不涉及。

        :param replication: The replication of this DatabaseUserInfoReq.
        :type replication: bool
        """
        self._replication = replication

    @property
    def valid_begin(self):
        r"""Gets the valid_begin of this DatabaseUserInfoReq.

        **参数解释**： 角色生效时间。格式：yyyy-MM-ddTHH:mm:ssZ。 **取值范围**： 不涉及。

        :return: The valid_begin of this DatabaseUserInfoReq.
        :rtype: str
        """
        return self._valid_begin

    @valid_begin.setter
    def valid_begin(self, valid_begin):
        r"""Sets the valid_begin of this DatabaseUserInfoReq.

        **参数解释**： 角色生效时间。格式：yyyy-MM-ddTHH:mm:ssZ。 **取值范围**： 不涉及。

        :param valid_begin: The valid_begin of this DatabaseUserInfoReq.
        :type valid_begin: str
        """
        self._valid_begin = valid_begin

    @property
    def valid_until(self):
        r"""Gets the valid_until of this DatabaseUserInfoReq.

        **参数解释**： 角色过期时间。格式：yyyy-MM-ddTHH:mm:ssZ。 **取值范围**： 不涉及。

        :return: The valid_until of this DatabaseUserInfoReq.
        :rtype: str
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        r"""Sets the valid_until of this DatabaseUserInfoReq.

        **参数解释**： 角色过期时间。格式：yyyy-MM-ddTHH:mm:ssZ。 **取值范围**： 不涉及。

        :param valid_until: The valid_until of this DatabaseUserInfoReq.
        :type valid_until: str
        """
        self._valid_until = valid_until

    @property
    def lock(self):
        r"""Gets the lock of this DatabaseUserInfoReq.

        **参数解释**： 是否锁定。 **取值范围**： 不涉及。

        :return: The lock of this DatabaseUserInfoReq.
        :rtype: bool
        """
        return self._lock

    @lock.setter
    def lock(self, lock):
        r"""Sets the lock of this DatabaseUserInfoReq.

        **参数解释**： 是否锁定。 **取值范围**： 不涉及。

        :param lock: The lock of this DatabaseUserInfoReq.
        :type lock: bool
        """
        self._lock = lock

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
        if not isinstance(other, DatabaseUserInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
