# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventDetailResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'process_pid': 'int',
        'is_parent': 'bool',
        'file_hash': 'str',
        'file_path': 'str',
        'file_attr': 'str',
        'private_ip': 'str',
        'login_ip': 'str',
        'login_user_name': 'str',
        'keyword': 'str',
        'hash': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'process_pid': 'process_pid',
        'is_parent': 'is_parent',
        'file_hash': 'file_hash',
        'file_path': 'file_path',
        'file_attr': 'file_attr',
        'private_ip': 'private_ip',
        'login_ip': 'login_ip',
        'login_user_name': 'login_user_name',
        'keyword': 'keyword',
        'hash': 'hash'
    }

    def __init__(self, agent_id=None, process_pid=None, is_parent=None, file_hash=None, file_path=None, file_attr=None, private_ip=None, login_ip=None, login_user_name=None, keyword=None, hash=None):
        r"""EventDetailResponseInfo

        The model defined in huaweicloud sdk

        :param agent_id: **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type agent_id: str
        :param process_pid: **参数解释**： 进程ID **取值范围**： 最小值0，最大值2147483647 
        :type process_pid: int
        :param is_parent: **参数解释**： 是否是父进程 **取值范围**： - true：是父进程 - false：不是父进程 
        :type is_parent: bool
        :param file_hash: **参数解释**： 文件哈希 **取值范围**： 字符长度1-256位 
        :type file_hash: str
        :param file_path: **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 
        :type file_path: str
        :param file_attr: **参数解释**： 文件属性 **取值范围**： 字符长度1-256位 
        :type file_attr: str
        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param login_ip: **参数解释**： 登录源IP **取值范围**： 字符长度1-256位 
        :type login_ip: str
        :param login_user_name: **参数解释**： 登录用户名 **取值范围**： 字符长度1-256位 
        :type login_user_name: str
        :param keyword: 告警事件关键字，仅用于告警白名单
        :type keyword: str
        :param hash: 告警事件hash，仅用于告警白名单
        :type hash: str
        """
        
        

        self._agent_id = None
        self._process_pid = None
        self._is_parent = None
        self._file_hash = None
        self._file_path = None
        self._file_attr = None
        self._private_ip = None
        self._login_ip = None
        self._login_user_name = None
        self._keyword = None
        self._hash = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if process_pid is not None:
            self.process_pid = process_pid
        if is_parent is not None:
            self.is_parent = is_parent
        if file_hash is not None:
            self.file_hash = file_hash
        if file_path is not None:
            self.file_path = file_path
        if file_attr is not None:
            self.file_attr = file_attr
        if private_ip is not None:
            self.private_ip = private_ip
        if login_ip is not None:
            self.login_ip = login_ip
        if login_user_name is not None:
            self.login_user_name = login_user_name
        if keyword is not None:
            self.keyword = keyword
        if hash is not None:
            self.hash = hash

    @property
    def agent_id(self):
        r"""Gets the agent_id of this EventDetailResponseInfo.

        **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The agent_id of this EventDetailResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this EventDetailResponseInfo.

        **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param agent_id: The agent_id of this EventDetailResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def process_pid(self):
        r"""Gets the process_pid of this EventDetailResponseInfo.

        **参数解释**： 进程ID **取值范围**： 最小值0，最大值2147483647 

        :return: The process_pid of this EventDetailResponseInfo.
        :rtype: int
        """
        return self._process_pid

    @process_pid.setter
    def process_pid(self, process_pid):
        r"""Sets the process_pid of this EventDetailResponseInfo.

        **参数解释**： 进程ID **取值范围**： 最小值0，最大值2147483647 

        :param process_pid: The process_pid of this EventDetailResponseInfo.
        :type process_pid: int
        """
        self._process_pid = process_pid

    @property
    def is_parent(self):
        r"""Gets the is_parent of this EventDetailResponseInfo.

        **参数解释**： 是否是父进程 **取值范围**： - true：是父进程 - false：不是父进程 

        :return: The is_parent of this EventDetailResponseInfo.
        :rtype: bool
        """
        return self._is_parent

    @is_parent.setter
    def is_parent(self, is_parent):
        r"""Sets the is_parent of this EventDetailResponseInfo.

        **参数解释**： 是否是父进程 **取值范围**： - true：是父进程 - false：不是父进程 

        :param is_parent: The is_parent of this EventDetailResponseInfo.
        :type is_parent: bool
        """
        self._is_parent = is_parent

    @property
    def file_hash(self):
        r"""Gets the file_hash of this EventDetailResponseInfo.

        **参数解释**： 文件哈希 **取值范围**： 字符长度1-256位 

        :return: The file_hash of this EventDetailResponseInfo.
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        r"""Sets the file_hash of this EventDetailResponseInfo.

        **参数解释**： 文件哈希 **取值范围**： 字符长度1-256位 

        :param file_hash: The file_hash of this EventDetailResponseInfo.
        :type file_hash: str
        """
        self._file_hash = file_hash

    @property
    def file_path(self):
        r"""Gets the file_path of this EventDetailResponseInfo.

        **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 

        :return: The file_path of this EventDetailResponseInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this EventDetailResponseInfo.

        **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 

        :param file_path: The file_path of this EventDetailResponseInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_attr(self):
        r"""Gets the file_attr of this EventDetailResponseInfo.

        **参数解释**： 文件属性 **取值范围**： 字符长度1-256位 

        :return: The file_attr of this EventDetailResponseInfo.
        :rtype: str
        """
        return self._file_attr

    @file_attr.setter
    def file_attr(self, file_attr):
        r"""Sets the file_attr of this EventDetailResponseInfo.

        **参数解释**： 文件属性 **取值范围**： 字符长度1-256位 

        :param file_attr: The file_attr of this EventDetailResponseInfo.
        :type file_attr: str
        """
        self._file_attr = file_attr

    @property
    def private_ip(self):
        r"""Gets the private_ip of this EventDetailResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this EventDetailResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this EventDetailResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this EventDetailResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def login_ip(self):
        r"""Gets the login_ip of this EventDetailResponseInfo.

        **参数解释**： 登录源IP **取值范围**： 字符长度1-256位 

        :return: The login_ip of this EventDetailResponseInfo.
        :rtype: str
        """
        return self._login_ip

    @login_ip.setter
    def login_ip(self, login_ip):
        r"""Sets the login_ip of this EventDetailResponseInfo.

        **参数解释**： 登录源IP **取值范围**： 字符长度1-256位 

        :param login_ip: The login_ip of this EventDetailResponseInfo.
        :type login_ip: str
        """
        self._login_ip = login_ip

    @property
    def login_user_name(self):
        r"""Gets the login_user_name of this EventDetailResponseInfo.

        **参数解释**： 登录用户名 **取值范围**： 字符长度1-256位 

        :return: The login_user_name of this EventDetailResponseInfo.
        :rtype: str
        """
        return self._login_user_name

    @login_user_name.setter
    def login_user_name(self, login_user_name):
        r"""Sets the login_user_name of this EventDetailResponseInfo.

        **参数解释**： 登录用户名 **取值范围**： 字符长度1-256位 

        :param login_user_name: The login_user_name of this EventDetailResponseInfo.
        :type login_user_name: str
        """
        self._login_user_name = login_user_name

    @property
    def keyword(self):
        r"""Gets the keyword of this EventDetailResponseInfo.

        告警事件关键字，仅用于告警白名单

        :return: The keyword of this EventDetailResponseInfo.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this EventDetailResponseInfo.

        告警事件关键字，仅用于告警白名单

        :param keyword: The keyword of this EventDetailResponseInfo.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def hash(self):
        r"""Gets the hash of this EventDetailResponseInfo.

        告警事件hash，仅用于告警白名单

        :return: The hash of this EventDetailResponseInfo.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        r"""Sets the hash of this EventDetailResponseInfo.

        告警事件hash，仅用于告警白名单

        :param hash: The hash of this EventDetailResponseInfo.
        :type hash: str
        """
        self._hash = hash

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
        if not isinstance(other, EventDetailResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
