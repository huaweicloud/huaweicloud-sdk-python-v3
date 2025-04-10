# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNodeSessionsResultSessions:

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
        'cmd': 'str',
        'age': 'str',
        'idle': 'str',
        'db': 'str',
        'addr': 'str',
        'fd': 'str',
        'sub': 'str',
        'psub': 'str',
        'multi': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'cmd': 'cmd',
        'age': 'age',
        'idle': 'idle',
        'db': 'db',
        'addr': 'addr',
        'fd': 'fd',
        'sub': 'sub',
        'psub': 'psub',
        'multi': 'multi'
    }

    def __init__(self, id=None, name=None, cmd=None, age=None, idle=None, db=None, addr=None, fd=None, sub=None, psub=None, multi=None):
        r"""ListNodeSessionsResultSessions

        The model defined in huaweicloud sdk

        :param id: 会话ID。
        :type id: str
        :param name: 连接名。
        :type name: str
        :param cmd: 最近一次执行的命令。
        :type cmd: str
        :param age: 以秒计算的已连接时长。
        :type age: str
        :param idle: 以秒计算的空闲时长。
        :type idle: str
        :param db: 该客户端正在使用的数据库ID。
        :type db: str
        :param addr: 客户端的地址和端口。
        :type addr: str
        :param fd: 套接字所使用的文件描述符。
        :type fd: str
        :param sub: 已订阅频道的数量。
        :type sub: str
        :param psub: 已订阅模式的数量。
        :type psub: str
        :param multi: 在事务中被执行的命令数量。
        :type multi: str
        """
        
        

        self._id = None
        self._name = None
        self._cmd = None
        self._age = None
        self._idle = None
        self._db = None
        self._addr = None
        self._fd = None
        self._sub = None
        self._psub = None
        self._multi = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if cmd is not None:
            self.cmd = cmd
        if age is not None:
            self.age = age
        if idle is not None:
            self.idle = idle
        if db is not None:
            self.db = db
        if addr is not None:
            self.addr = addr
        if fd is not None:
            self.fd = fd
        if sub is not None:
            self.sub = sub
        if psub is not None:
            self.psub = psub
        if multi is not None:
            self.multi = multi

    @property
    def id(self):
        r"""Gets the id of this ListNodeSessionsResultSessions.

        会话ID。

        :return: The id of this ListNodeSessionsResultSessions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListNodeSessionsResultSessions.

        会话ID。

        :param id: The id of this ListNodeSessionsResultSessions.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListNodeSessionsResultSessions.

        连接名。

        :return: The name of this ListNodeSessionsResultSessions.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListNodeSessionsResultSessions.

        连接名。

        :param name: The name of this ListNodeSessionsResultSessions.
        :type name: str
        """
        self._name = name

    @property
    def cmd(self):
        r"""Gets the cmd of this ListNodeSessionsResultSessions.

        最近一次执行的命令。

        :return: The cmd of this ListNodeSessionsResultSessions.
        :rtype: str
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        r"""Sets the cmd of this ListNodeSessionsResultSessions.

        最近一次执行的命令。

        :param cmd: The cmd of this ListNodeSessionsResultSessions.
        :type cmd: str
        """
        self._cmd = cmd

    @property
    def age(self):
        r"""Gets the age of this ListNodeSessionsResultSessions.

        以秒计算的已连接时长。

        :return: The age of this ListNodeSessionsResultSessions.
        :rtype: str
        """
        return self._age

    @age.setter
    def age(self, age):
        r"""Sets the age of this ListNodeSessionsResultSessions.

        以秒计算的已连接时长。

        :param age: The age of this ListNodeSessionsResultSessions.
        :type age: str
        """
        self._age = age

    @property
    def idle(self):
        r"""Gets the idle of this ListNodeSessionsResultSessions.

        以秒计算的空闲时长。

        :return: The idle of this ListNodeSessionsResultSessions.
        :rtype: str
        """
        return self._idle

    @idle.setter
    def idle(self, idle):
        r"""Sets the idle of this ListNodeSessionsResultSessions.

        以秒计算的空闲时长。

        :param idle: The idle of this ListNodeSessionsResultSessions.
        :type idle: str
        """
        self._idle = idle

    @property
    def db(self):
        r"""Gets the db of this ListNodeSessionsResultSessions.

        该客户端正在使用的数据库ID。

        :return: The db of this ListNodeSessionsResultSessions.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this ListNodeSessionsResultSessions.

        该客户端正在使用的数据库ID。

        :param db: The db of this ListNodeSessionsResultSessions.
        :type db: str
        """
        self._db = db

    @property
    def addr(self):
        r"""Gets the addr of this ListNodeSessionsResultSessions.

        客户端的地址和端口。

        :return: The addr of this ListNodeSessionsResultSessions.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        r"""Sets the addr of this ListNodeSessionsResultSessions.

        客户端的地址和端口。

        :param addr: The addr of this ListNodeSessionsResultSessions.
        :type addr: str
        """
        self._addr = addr

    @property
    def fd(self):
        r"""Gets the fd of this ListNodeSessionsResultSessions.

        套接字所使用的文件描述符。

        :return: The fd of this ListNodeSessionsResultSessions.
        :rtype: str
        """
        return self._fd

    @fd.setter
    def fd(self, fd):
        r"""Sets the fd of this ListNodeSessionsResultSessions.

        套接字所使用的文件描述符。

        :param fd: The fd of this ListNodeSessionsResultSessions.
        :type fd: str
        """
        self._fd = fd

    @property
    def sub(self):
        r"""Gets the sub of this ListNodeSessionsResultSessions.

        已订阅频道的数量。

        :return: The sub of this ListNodeSessionsResultSessions.
        :rtype: str
        """
        return self._sub

    @sub.setter
    def sub(self, sub):
        r"""Sets the sub of this ListNodeSessionsResultSessions.

        已订阅频道的数量。

        :param sub: The sub of this ListNodeSessionsResultSessions.
        :type sub: str
        """
        self._sub = sub

    @property
    def psub(self):
        r"""Gets the psub of this ListNodeSessionsResultSessions.

        已订阅模式的数量。

        :return: The psub of this ListNodeSessionsResultSessions.
        :rtype: str
        """
        return self._psub

    @psub.setter
    def psub(self, psub):
        r"""Sets the psub of this ListNodeSessionsResultSessions.

        已订阅模式的数量。

        :param psub: The psub of this ListNodeSessionsResultSessions.
        :type psub: str
        """
        self._psub = psub

    @property
    def multi(self):
        r"""Gets the multi of this ListNodeSessionsResultSessions.

        在事务中被执行的命令数量。

        :return: The multi of this ListNodeSessionsResultSessions.
        :rtype: str
        """
        return self._multi

    @multi.setter
    def multi(self, multi):
        r"""Sets the multi of this ListNodeSessionsResultSessions.

        在事务中被执行的命令数量。

        :param multi: The multi of this ListNodeSessionsResultSessions.
        :type multi: str
        """
        self._multi = multi

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
        if not isinstance(other, ListNodeSessionsResultSessions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
