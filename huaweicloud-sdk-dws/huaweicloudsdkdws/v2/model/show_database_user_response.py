# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDatabaseUserResponse(SdkResponse):

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
        'login': 'bool',
        'createrole': 'bool',
        'createdb': 'bool',
        'systemadmin': 'bool',
        'auditadmin': 'bool',
        'inherit': 'bool',
        'useft': 'bool',
        'conn_limit': 'int',
        'replication': 'bool',
        'valid_begin': 'int',
        'valid_until': 'int',
        'lock': 'bool',
        'desc': 'str',
        'user_type': 'str',
        'logical_cluster': 'str'
    }

    attribute_map = {
        'name': 'name',
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
        'lock': 'lock',
        'desc': 'desc',
        'user_type': 'user_type',
        'logical_cluster': 'logical_cluster'
    }

    def __init__(self, name=None, login=None, createrole=None, createdb=None, systemadmin=None, auditadmin=None, inherit=None, useft=None, conn_limit=None, replication=None, valid_begin=None, valid_until=None, lock=None, desc=None, user_type=None, logical_cluster=None):
        """ShowDatabaseUserResponse

        The model defined in huaweicloud sdk

        :param name: 用户名称
        :type name: str
        :param login: 是否可以登陆
        :type login: bool
        :param createrole: 创建角色权限
        :type createrole: bool
        :param createdb: 创建数据库权限
        :type createdb: bool
        :param systemadmin: 系统管理员
        :type systemadmin: bool
        :param auditadmin: 审计管理员
        :type auditadmin: bool
        :param inherit: 继承所在组权限
        :type inherit: bool
        :param useft: 访问外表权限
        :type useft: bool
        :param conn_limit: 连接数限制
        :type conn_limit: int
        :param replication: 是否允许流复制
        :type replication: bool
        :param valid_begin: 角色生效时间
        :type valid_begin: int
        :param valid_until: 角色过期时间
        :type valid_until: int
        :param lock: 是否锁定
        :type lock: bool
        :param desc: 描述
        :type desc: str
        :param user_type: 用户类型
        :type user_type: str
        :param logical_cluster: 所属逻辑集群
        :type logical_cluster: str
        """
        
        super(ShowDatabaseUserResponse, self).__init__()

        self._name = None
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
        self._desc = None
        self._user_type = None
        self._logical_cluster = None
        self.discriminator = None

        if name is not None:
            self.name = name
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
        if desc is not None:
            self.desc = desc
        if user_type is not None:
            self.user_type = user_type
        if logical_cluster is not None:
            self.logical_cluster = logical_cluster

    @property
    def name(self):
        """Gets the name of this ShowDatabaseUserResponse.

        用户名称

        :return: The name of this ShowDatabaseUserResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowDatabaseUserResponse.

        用户名称

        :param name: The name of this ShowDatabaseUserResponse.
        :type name: str
        """
        self._name = name

    @property
    def login(self):
        """Gets the login of this ShowDatabaseUserResponse.

        是否可以登陆

        :return: The login of this ShowDatabaseUserResponse.
        :rtype: bool
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this ShowDatabaseUserResponse.

        是否可以登陆

        :param login: The login of this ShowDatabaseUserResponse.
        :type login: bool
        """
        self._login = login

    @property
    def createrole(self):
        """Gets the createrole of this ShowDatabaseUserResponse.

        创建角色权限

        :return: The createrole of this ShowDatabaseUserResponse.
        :rtype: bool
        """
        return self._createrole

    @createrole.setter
    def createrole(self, createrole):
        """Sets the createrole of this ShowDatabaseUserResponse.

        创建角色权限

        :param createrole: The createrole of this ShowDatabaseUserResponse.
        :type createrole: bool
        """
        self._createrole = createrole

    @property
    def createdb(self):
        """Gets the createdb of this ShowDatabaseUserResponse.

        创建数据库权限

        :return: The createdb of this ShowDatabaseUserResponse.
        :rtype: bool
        """
        return self._createdb

    @createdb.setter
    def createdb(self, createdb):
        """Sets the createdb of this ShowDatabaseUserResponse.

        创建数据库权限

        :param createdb: The createdb of this ShowDatabaseUserResponse.
        :type createdb: bool
        """
        self._createdb = createdb

    @property
    def systemadmin(self):
        """Gets the systemadmin of this ShowDatabaseUserResponse.

        系统管理员

        :return: The systemadmin of this ShowDatabaseUserResponse.
        :rtype: bool
        """
        return self._systemadmin

    @systemadmin.setter
    def systemadmin(self, systemadmin):
        """Sets the systemadmin of this ShowDatabaseUserResponse.

        系统管理员

        :param systemadmin: The systemadmin of this ShowDatabaseUserResponse.
        :type systemadmin: bool
        """
        self._systemadmin = systemadmin

    @property
    def auditadmin(self):
        """Gets the auditadmin of this ShowDatabaseUserResponse.

        审计管理员

        :return: The auditadmin of this ShowDatabaseUserResponse.
        :rtype: bool
        """
        return self._auditadmin

    @auditadmin.setter
    def auditadmin(self, auditadmin):
        """Sets the auditadmin of this ShowDatabaseUserResponse.

        审计管理员

        :param auditadmin: The auditadmin of this ShowDatabaseUserResponse.
        :type auditadmin: bool
        """
        self._auditadmin = auditadmin

    @property
    def inherit(self):
        """Gets the inherit of this ShowDatabaseUserResponse.

        继承所在组权限

        :return: The inherit of this ShowDatabaseUserResponse.
        :rtype: bool
        """
        return self._inherit

    @inherit.setter
    def inherit(self, inherit):
        """Sets the inherit of this ShowDatabaseUserResponse.

        继承所在组权限

        :param inherit: The inherit of this ShowDatabaseUserResponse.
        :type inherit: bool
        """
        self._inherit = inherit

    @property
    def useft(self):
        """Gets the useft of this ShowDatabaseUserResponse.

        访问外表权限

        :return: The useft of this ShowDatabaseUserResponse.
        :rtype: bool
        """
        return self._useft

    @useft.setter
    def useft(self, useft):
        """Sets the useft of this ShowDatabaseUserResponse.

        访问外表权限

        :param useft: The useft of this ShowDatabaseUserResponse.
        :type useft: bool
        """
        self._useft = useft

    @property
    def conn_limit(self):
        """Gets the conn_limit of this ShowDatabaseUserResponse.

        连接数限制

        :return: The conn_limit of this ShowDatabaseUserResponse.
        :rtype: int
        """
        return self._conn_limit

    @conn_limit.setter
    def conn_limit(self, conn_limit):
        """Sets the conn_limit of this ShowDatabaseUserResponse.

        连接数限制

        :param conn_limit: The conn_limit of this ShowDatabaseUserResponse.
        :type conn_limit: int
        """
        self._conn_limit = conn_limit

    @property
    def replication(self):
        """Gets the replication of this ShowDatabaseUserResponse.

        是否允许流复制

        :return: The replication of this ShowDatabaseUserResponse.
        :rtype: bool
        """
        return self._replication

    @replication.setter
    def replication(self, replication):
        """Sets the replication of this ShowDatabaseUserResponse.

        是否允许流复制

        :param replication: The replication of this ShowDatabaseUserResponse.
        :type replication: bool
        """
        self._replication = replication

    @property
    def valid_begin(self):
        """Gets the valid_begin of this ShowDatabaseUserResponse.

        角色生效时间

        :return: The valid_begin of this ShowDatabaseUserResponse.
        :rtype: int
        """
        return self._valid_begin

    @valid_begin.setter
    def valid_begin(self, valid_begin):
        """Sets the valid_begin of this ShowDatabaseUserResponse.

        角色生效时间

        :param valid_begin: The valid_begin of this ShowDatabaseUserResponse.
        :type valid_begin: int
        """
        self._valid_begin = valid_begin

    @property
    def valid_until(self):
        """Gets the valid_until of this ShowDatabaseUserResponse.

        角色过期时间

        :return: The valid_until of this ShowDatabaseUserResponse.
        :rtype: int
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """Sets the valid_until of this ShowDatabaseUserResponse.

        角色过期时间

        :param valid_until: The valid_until of this ShowDatabaseUserResponse.
        :type valid_until: int
        """
        self._valid_until = valid_until

    @property
    def lock(self):
        """Gets the lock of this ShowDatabaseUserResponse.

        是否锁定

        :return: The lock of this ShowDatabaseUserResponse.
        :rtype: bool
        """
        return self._lock

    @lock.setter
    def lock(self, lock):
        """Sets the lock of this ShowDatabaseUserResponse.

        是否锁定

        :param lock: The lock of this ShowDatabaseUserResponse.
        :type lock: bool
        """
        self._lock = lock

    @property
    def desc(self):
        """Gets the desc of this ShowDatabaseUserResponse.

        描述

        :return: The desc of this ShowDatabaseUserResponse.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this ShowDatabaseUserResponse.

        描述

        :param desc: The desc of this ShowDatabaseUserResponse.
        :type desc: str
        """
        self._desc = desc

    @property
    def user_type(self):
        """Gets the user_type of this ShowDatabaseUserResponse.

        用户类型

        :return: The user_type of this ShowDatabaseUserResponse.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this ShowDatabaseUserResponse.

        用户类型

        :param user_type: The user_type of this ShowDatabaseUserResponse.
        :type user_type: str
        """
        self._user_type = user_type

    @property
    def logical_cluster(self):
        """Gets the logical_cluster of this ShowDatabaseUserResponse.

        所属逻辑集群

        :return: The logical_cluster of this ShowDatabaseUserResponse.
        :rtype: str
        """
        return self._logical_cluster

    @logical_cluster.setter
    def logical_cluster(self, logical_cluster):
        """Sets the logical_cluster of this ShowDatabaseUserResponse.

        所属逻辑集群

        :param logical_cluster: The logical_cluster of this ShowDatabaseUserResponse.
        :type logical_cluster: str
        """
        self._logical_cluster = logical_cluster

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
        if not isinstance(other, ShowDatabaseUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
