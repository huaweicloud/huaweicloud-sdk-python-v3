# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClientInfo:

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
        'addr': 'str',
        'fd': 'str',
        'name': 'str',
        'cmd': 'str',
        'age': 'int',
        'idle': 'int',
        'db': 'str',
        'flags': 'str',
        'sub': 'int',
        'psub': 'int',
        'multi': 'int',
        'qbuf': 'int',
        'qbuf_free': 'int',
        'obl': 'int',
        'oll': 'int',
        'omem': 'int',
        'events': 'str',
        'network': 'str',
        'peer': 'str',
        'user': 'str'
    }

    attribute_map = {
        'id': 'id',
        'addr': 'addr',
        'fd': 'fd',
        'name': 'name',
        'cmd': 'cmd',
        'age': 'age',
        'idle': 'idle',
        'db': 'db',
        'flags': 'flags',
        'sub': 'sub',
        'psub': 'psub',
        'multi': 'multi',
        'qbuf': 'qbuf',
        'qbuf_free': 'qbuf_free',
        'obl': 'obl',
        'oll': 'oll',
        'omem': 'omem',
        'events': 'events',
        'network': 'network',
        'peer': 'peer',
        'user': 'user'
    }

    def __init__(self, id=None, addr=None, fd=None, name=None, cmd=None, age=None, idle=None, db=None, flags=None, sub=None, psub=None, multi=None, qbuf=None, qbuf_free=None, obl=None, oll=None, omem=None, events=None, network=None, peer=None, user=None):
        r"""ClientInfo

        The model defined in huaweicloud sdk

        :param id: 客户端ID
        :type id: str
        :param addr: 客户端的地址和端口
        :type addr: str
        :param fd: 套接字所使用的文件描述符。
        :type fd: str
        :param name: 客户端的名称
        :type name: str
        :param cmd: 最近一次执行的命令
        :type cmd: str
        :param age: 已连接时长（单位：秒）
        :type age: int
        :param idle: 空闲时长（单位：秒）
        :type idle: int
        :param db: 该客户端正在使用的数据库 ID
        :type db: str
        :param flags: 客户端标志
        :type flags: str
        :param sub: 已订阅频道的数量
        :type sub: int
        :param psub: 已订阅模式的数量
        :type psub: int
        :param multi: 在事务中被执行的命令数量
        :type multi: int
        :param qbuf: 查询缓冲区的长度（单位为字节， 0 表示没有分配查询缓冲区）
        :type qbuf: int
        :param qbuf_free: 查询缓冲区剩余空间的长度（单位为字节， 0 表示没有剩余空间）
        :type qbuf_free: int
        :param obl: 输出缓冲区的长度（单位为字节， 0 表示没有分配输出缓冲区）
        :type obl: int
        :param oll: 输出列表包含的对象数量（当输出缓冲区没有剩余空间时，命令回复会以字符串对象的形式被入队到这个队列里）
        :type oll: int
        :param omem: 输出缓冲区和输出列表占用的内存总量
        :type omem: int
        :param events: 文件描述符事件
        :type events: str
        :param network: 客户端所使用的网络类型。
        :type network: str
        :param peer: 单机，主备和cluster实例地址和端口。
        :type peer: str
        :param user: 客户端用户。
        :type user: str
        """
        
        

        self._id = None
        self._addr = None
        self._fd = None
        self._name = None
        self._cmd = None
        self._age = None
        self._idle = None
        self._db = None
        self._flags = None
        self._sub = None
        self._psub = None
        self._multi = None
        self._qbuf = None
        self._qbuf_free = None
        self._obl = None
        self._oll = None
        self._omem = None
        self._events = None
        self._network = None
        self._peer = None
        self._user = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if addr is not None:
            self.addr = addr
        if fd is not None:
            self.fd = fd
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
        if flags is not None:
            self.flags = flags
        if sub is not None:
            self.sub = sub
        if psub is not None:
            self.psub = psub
        if multi is not None:
            self.multi = multi
        if qbuf is not None:
            self.qbuf = qbuf
        if qbuf_free is not None:
            self.qbuf_free = qbuf_free
        if obl is not None:
            self.obl = obl
        if oll is not None:
            self.oll = oll
        if omem is not None:
            self.omem = omem
        if events is not None:
            self.events = events
        if network is not None:
            self.network = network
        if peer is not None:
            self.peer = peer
        if user is not None:
            self.user = user

    @property
    def id(self):
        r"""Gets the id of this ClientInfo.

        客户端ID

        :return: The id of this ClientInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ClientInfo.

        客户端ID

        :param id: The id of this ClientInfo.
        :type id: str
        """
        self._id = id

    @property
    def addr(self):
        r"""Gets the addr of this ClientInfo.

        客户端的地址和端口

        :return: The addr of this ClientInfo.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        r"""Sets the addr of this ClientInfo.

        客户端的地址和端口

        :param addr: The addr of this ClientInfo.
        :type addr: str
        """
        self._addr = addr

    @property
    def fd(self):
        r"""Gets the fd of this ClientInfo.

        套接字所使用的文件描述符。

        :return: The fd of this ClientInfo.
        :rtype: str
        """
        return self._fd

    @fd.setter
    def fd(self, fd):
        r"""Sets the fd of this ClientInfo.

        套接字所使用的文件描述符。

        :param fd: The fd of this ClientInfo.
        :type fd: str
        """
        self._fd = fd

    @property
    def name(self):
        r"""Gets the name of this ClientInfo.

        客户端的名称

        :return: The name of this ClientInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ClientInfo.

        客户端的名称

        :param name: The name of this ClientInfo.
        :type name: str
        """
        self._name = name

    @property
    def cmd(self):
        r"""Gets the cmd of this ClientInfo.

        最近一次执行的命令

        :return: The cmd of this ClientInfo.
        :rtype: str
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        r"""Sets the cmd of this ClientInfo.

        最近一次执行的命令

        :param cmd: The cmd of this ClientInfo.
        :type cmd: str
        """
        self._cmd = cmd

    @property
    def age(self):
        r"""Gets the age of this ClientInfo.

        已连接时长（单位：秒）

        :return: The age of this ClientInfo.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        r"""Sets the age of this ClientInfo.

        已连接时长（单位：秒）

        :param age: The age of this ClientInfo.
        :type age: int
        """
        self._age = age

    @property
    def idle(self):
        r"""Gets the idle of this ClientInfo.

        空闲时长（单位：秒）

        :return: The idle of this ClientInfo.
        :rtype: int
        """
        return self._idle

    @idle.setter
    def idle(self, idle):
        r"""Sets the idle of this ClientInfo.

        空闲时长（单位：秒）

        :param idle: The idle of this ClientInfo.
        :type idle: int
        """
        self._idle = idle

    @property
    def db(self):
        r"""Gets the db of this ClientInfo.

        该客户端正在使用的数据库 ID

        :return: The db of this ClientInfo.
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        r"""Sets the db of this ClientInfo.

        该客户端正在使用的数据库 ID

        :param db: The db of this ClientInfo.
        :type db: str
        """
        self._db = db

    @property
    def flags(self):
        r"""Gets the flags of this ClientInfo.

        客户端标志

        :return: The flags of this ClientInfo.
        :rtype: str
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        r"""Sets the flags of this ClientInfo.

        客户端标志

        :param flags: The flags of this ClientInfo.
        :type flags: str
        """
        self._flags = flags

    @property
    def sub(self):
        r"""Gets the sub of this ClientInfo.

        已订阅频道的数量

        :return: The sub of this ClientInfo.
        :rtype: int
        """
        return self._sub

    @sub.setter
    def sub(self, sub):
        r"""Sets the sub of this ClientInfo.

        已订阅频道的数量

        :param sub: The sub of this ClientInfo.
        :type sub: int
        """
        self._sub = sub

    @property
    def psub(self):
        r"""Gets the psub of this ClientInfo.

        已订阅模式的数量

        :return: The psub of this ClientInfo.
        :rtype: int
        """
        return self._psub

    @psub.setter
    def psub(self, psub):
        r"""Sets the psub of this ClientInfo.

        已订阅模式的数量

        :param psub: The psub of this ClientInfo.
        :type psub: int
        """
        self._psub = psub

    @property
    def multi(self):
        r"""Gets the multi of this ClientInfo.

        在事务中被执行的命令数量

        :return: The multi of this ClientInfo.
        :rtype: int
        """
        return self._multi

    @multi.setter
    def multi(self, multi):
        r"""Sets the multi of this ClientInfo.

        在事务中被执行的命令数量

        :param multi: The multi of this ClientInfo.
        :type multi: int
        """
        self._multi = multi

    @property
    def qbuf(self):
        r"""Gets the qbuf of this ClientInfo.

        查询缓冲区的长度（单位为字节， 0 表示没有分配查询缓冲区）

        :return: The qbuf of this ClientInfo.
        :rtype: int
        """
        return self._qbuf

    @qbuf.setter
    def qbuf(self, qbuf):
        r"""Sets the qbuf of this ClientInfo.

        查询缓冲区的长度（单位为字节， 0 表示没有分配查询缓冲区）

        :param qbuf: The qbuf of this ClientInfo.
        :type qbuf: int
        """
        self._qbuf = qbuf

    @property
    def qbuf_free(self):
        r"""Gets the qbuf_free of this ClientInfo.

        查询缓冲区剩余空间的长度（单位为字节， 0 表示没有剩余空间）

        :return: The qbuf_free of this ClientInfo.
        :rtype: int
        """
        return self._qbuf_free

    @qbuf_free.setter
    def qbuf_free(self, qbuf_free):
        r"""Sets the qbuf_free of this ClientInfo.

        查询缓冲区剩余空间的长度（单位为字节， 0 表示没有剩余空间）

        :param qbuf_free: The qbuf_free of this ClientInfo.
        :type qbuf_free: int
        """
        self._qbuf_free = qbuf_free

    @property
    def obl(self):
        r"""Gets the obl of this ClientInfo.

        输出缓冲区的长度（单位为字节， 0 表示没有分配输出缓冲区）

        :return: The obl of this ClientInfo.
        :rtype: int
        """
        return self._obl

    @obl.setter
    def obl(self, obl):
        r"""Sets the obl of this ClientInfo.

        输出缓冲区的长度（单位为字节， 0 表示没有分配输出缓冲区）

        :param obl: The obl of this ClientInfo.
        :type obl: int
        """
        self._obl = obl

    @property
    def oll(self):
        r"""Gets the oll of this ClientInfo.

        输出列表包含的对象数量（当输出缓冲区没有剩余空间时，命令回复会以字符串对象的形式被入队到这个队列里）

        :return: The oll of this ClientInfo.
        :rtype: int
        """
        return self._oll

    @oll.setter
    def oll(self, oll):
        r"""Sets the oll of this ClientInfo.

        输出列表包含的对象数量（当输出缓冲区没有剩余空间时，命令回复会以字符串对象的形式被入队到这个队列里）

        :param oll: The oll of this ClientInfo.
        :type oll: int
        """
        self._oll = oll

    @property
    def omem(self):
        r"""Gets the omem of this ClientInfo.

        输出缓冲区和输出列表占用的内存总量

        :return: The omem of this ClientInfo.
        :rtype: int
        """
        return self._omem

    @omem.setter
    def omem(self, omem):
        r"""Sets the omem of this ClientInfo.

        输出缓冲区和输出列表占用的内存总量

        :param omem: The omem of this ClientInfo.
        :type omem: int
        """
        self._omem = omem

    @property
    def events(self):
        r"""Gets the events of this ClientInfo.

        文件描述符事件

        :return: The events of this ClientInfo.
        :rtype: str
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this ClientInfo.

        文件描述符事件

        :param events: The events of this ClientInfo.
        :type events: str
        """
        self._events = events

    @property
    def network(self):
        r"""Gets the network of this ClientInfo.

        客户端所使用的网络类型。

        :return: The network of this ClientInfo.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        r"""Sets the network of this ClientInfo.

        客户端所使用的网络类型。

        :param network: The network of this ClientInfo.
        :type network: str
        """
        self._network = network

    @property
    def peer(self):
        r"""Gets the peer of this ClientInfo.

        单机，主备和cluster实例地址和端口。

        :return: The peer of this ClientInfo.
        :rtype: str
        """
        return self._peer

    @peer.setter
    def peer(self, peer):
        r"""Sets the peer of this ClientInfo.

        单机，主备和cluster实例地址和端口。

        :param peer: The peer of this ClientInfo.
        :type peer: str
        """
        self._peer = peer

    @property
    def user(self):
        r"""Gets the user of this ClientInfo.

        客户端用户。

        :return: The user of this ClientInfo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this ClientInfo.

        客户端用户。

        :param user: The user of this ClientInfo.
        :type user: str
        """
        self._user = user

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
        if not isinstance(other, ClientInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
