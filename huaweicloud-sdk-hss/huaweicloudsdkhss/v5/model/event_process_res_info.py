# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventProcessResInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'process_name': 'str',
        'process_path': 'str',
        'process_pid': 'int',
        'process_uid': 'int',
        'process_username': 'str',
        'process_cmdline': 'str',
        'process_filename': 'str',
        'process_start_time': 'int',
        'process_gid': 'int',
        'process_egid': 'int',
        'process_euid': 'int',
        'parent_process_name': 'str',
        'parent_process_path': 'str',
        'parent_process_pid': 'int',
        'parent_process_uid': 'int',
        'parent_process_cmdline': 'str',
        'parent_process_filename': 'str',
        'parent_process_start_time': 'int',
        'parent_process_gid': 'int',
        'parent_process_egid': 'int',
        'parent_process_euid': 'int',
        'child_process_name': 'str',
        'child_process_path': 'str',
        'child_process_pid': 'int',
        'child_process_uid': 'int',
        'child_process_cmdline': 'str',
        'child_process_filename': 'str',
        'child_process_start_time': 'int',
        'child_process_gid': 'int',
        'child_process_egid': 'int',
        'child_process_euid': 'int',
        'virt_cmd': 'str',
        'virt_process_name': 'str',
        'escape_mode': 'str',
        'escape_cmd': 'str',
        'process_hash': 'str',
        'mode': 'str',
        'rule': 'int',
        'score': 'int',
        'process_file_hash': 'str',
        'parent_process_file_hash': 'str',
        'ancestor_process_pid': 'int',
        'ancestor_process_cmdline': 'str',
        'ancestor_process_path': 'str',
        'operate_type': 'int',
        'session_id': 'int'
    }

    attribute_map = {
        'process_name': 'process_name',
        'process_path': 'process_path',
        'process_pid': 'process_pid',
        'process_uid': 'process_uid',
        'process_username': 'process_username',
        'process_cmdline': 'process_cmdline',
        'process_filename': 'process_filename',
        'process_start_time': 'process_start_time',
        'process_gid': 'process_gid',
        'process_egid': 'process_egid',
        'process_euid': 'process_euid',
        'parent_process_name': 'parent_process_name',
        'parent_process_path': 'parent_process_path',
        'parent_process_pid': 'parent_process_pid',
        'parent_process_uid': 'parent_process_uid',
        'parent_process_cmdline': 'parent_process_cmdline',
        'parent_process_filename': 'parent_process_filename',
        'parent_process_start_time': 'parent_process_start_time',
        'parent_process_gid': 'parent_process_gid',
        'parent_process_egid': 'parent_process_egid',
        'parent_process_euid': 'parent_process_euid',
        'child_process_name': 'child_process_name',
        'child_process_path': 'child_process_path',
        'child_process_pid': 'child_process_pid',
        'child_process_uid': 'child_process_uid',
        'child_process_cmdline': 'child_process_cmdline',
        'child_process_filename': 'child_process_filename',
        'child_process_start_time': 'child_process_start_time',
        'child_process_gid': 'child_process_gid',
        'child_process_egid': 'child_process_egid',
        'child_process_euid': 'child_process_euid',
        'virt_cmd': 'virt_cmd',
        'virt_process_name': 'virt_process_name',
        'escape_mode': 'escape_mode',
        'escape_cmd': 'escape_cmd',
        'process_hash': 'process_hash',
        'mode': 'mode',
        'rule': 'rule',
        'score': 'score',
        'process_file_hash': 'process_file_hash',
        'parent_process_file_hash': 'parent_process_file_hash',
        'ancestor_process_pid': 'ancestor_process_pid',
        'ancestor_process_cmdline': 'ancestor_process_cmdline',
        'ancestor_process_path': 'ancestor_process_path',
        'operate_type': 'operate_type',
        'session_id': 'session_id'
    }

    def __init__(self, process_name=None, process_path=None, process_pid=None, process_uid=None, process_username=None, process_cmdline=None, process_filename=None, process_start_time=None, process_gid=None, process_egid=None, process_euid=None, parent_process_name=None, parent_process_path=None, parent_process_pid=None, parent_process_uid=None, parent_process_cmdline=None, parent_process_filename=None, parent_process_start_time=None, parent_process_gid=None, parent_process_egid=None, parent_process_euid=None, child_process_name=None, child_process_path=None, child_process_pid=None, child_process_uid=None, child_process_cmdline=None, child_process_filename=None, child_process_start_time=None, child_process_gid=None, child_process_egid=None, child_process_euid=None, virt_cmd=None, virt_process_name=None, escape_mode=None, escape_cmd=None, process_hash=None, mode=None, rule=None, score=None, process_file_hash=None, parent_process_file_hash=None, ancestor_process_pid=None, ancestor_process_cmdline=None, ancestor_process_path=None, operate_type=None, session_id=None):
        r"""EventProcessResInfo

        The model defined in huaweicloud sdk

        :param process_name: **参数解释**： 进程名称 **取值范围**： 字符长度1-128位 
        :type process_name: str
        :param process_path: **参数解释**： 进程路径 **取值范围**： 字符长度1-256位 
        :type process_path: str
        :param process_pid: **参数解释**： 进程ID **取值范围**： 最小值0，最大值2147483647 
        :type process_pid: int
        :param process_uid: **参数解释**： 进程名称 **取值范围**： 最小值0，最大值2147483647 
        :type process_uid: int
        :param process_username: **参数解释**： 运行进程的用户名 **取值范围**： 字符长度1-128位 
        :type process_username: str
        :param process_cmdline: **参数解释**： 进程命令行 **约束限制**： 不涉及 
        :type process_cmdline: str
        :param process_filename: **参数解释**： 进程文件名 **取值范围**： 字符长度1-64位 
        :type process_filename: str
        :param process_start_time: **参数解释**: 进程启动时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type process_start_time: int
        :param process_gid: **参数解释**: 进程组ID **取值范围**: 最小值0，最大值2147483647 
        :type process_gid: int
        :param process_egid: **参数解释**: 进程有效组ID **取值范围**: 最小值0，最大值2147483647 
        :type process_egid: int
        :param process_euid: **参数解释**: 进程有效用户ID **取值范围**: 最小值0，最大值9223372036854775807 
        :type process_euid: int
        :param parent_process_name: **参数解释**： 父进程名称 **取值范围**： 字符长度1-64位 
        :type parent_process_name: str
        :param parent_process_path: **参数解释**： 父进程文件路径 **取值范围**： 字符长度1-64位 
        :type parent_process_path: str
        :param parent_process_pid: **参数解释**: 父进程id **取值范围**: 最小值0，最大值2147483647 
        :type parent_process_pid: int
        :param parent_process_uid: **参数解释**: 父进程用户id **取值范围**: 最小值0，最大值2147483647 
        :type parent_process_uid: int
        :param parent_process_cmdline: **参数解释**： 父进程文件命令行 **取值范围**： 字符长度1-64位 
        :type parent_process_cmdline: str
        :param parent_process_filename: **参数解释**： 父进程文件名 **取值范围**： 字符长度1-64位 
        :type parent_process_filename: str
        :param parent_process_start_time: **参数解释**: 父进程启动时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type parent_process_start_time: int
        :param parent_process_gid: **参数解释**: 父进程组ID **取值范围**: 最小值0，最大值2147483647 
        :type parent_process_gid: int
        :param parent_process_egid: **参数解释**: 父进程有效组ID **取值范围**: 最小值0，最大值2147483647 
        :type parent_process_egid: int
        :param parent_process_euid: **参数解释**: 父进程有效用户ID **取值范围**: 最小值0，最大值2147483647 
        :type parent_process_euid: int
        :param child_process_name: **参数解释**： 子进程名称 **取值范围**： 字符长度1-64位 
        :type child_process_name: str
        :param child_process_path: **参数解释**： 子进程文件路径 **取值范围**： 字符长度1-64位 
        :type child_process_path: str
        :param child_process_pid: **参数解释**: 子进程id **取值范围**: 最小值0，最大值2147483647 
        :type child_process_pid: int
        :param child_process_uid: **参数解释**: 子进程用户id **取值范围**: 最小值0，最大值2147483647 
        :type child_process_uid: int
        :param child_process_cmdline: **参数解释**： 子进程文件命令行 **取值范围**： 字符长度1-64位 
        :type child_process_cmdline: str
        :param child_process_filename: **参数解释**： 子进程文件名 **取值范围**： 字符长度1-64位 
        :type child_process_filename: str
        :param child_process_start_time: **参数解释**: 子进程启动时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type child_process_start_time: int
        :param child_process_gid: **参数解释**: 子进程组ID **取值范围**: 最小值0，最大值2147483647 
        :type child_process_gid: int
        :param child_process_egid: **参数解释**: 子进程有效组ID **取值范围**: 最小值0，最大值2147483647 
        :type child_process_egid: int
        :param child_process_euid: **参数解释**: 子进程有效用户ID **取值范围**: 最小值0，最大值2147483647 
        :type child_process_euid: int
        :param virt_cmd: **参数解释**： 虚拟化命令 **取值范围**： 字符长度1-64位 
        :type virt_cmd: str
        :param virt_process_name: **参数解释**： 虚拟化进程名称 **取值范围**： 字符长度1-64位 
        :type virt_process_name: str
        :param escape_mode: **参数解释**： 逃逸方式 **取值范围**： 字符长度1-64位 
        :type escape_mode: str
        :param escape_cmd: **参数解释**： 逃逸后执行的命令 **取值范围**： 字符长度1-128位 
        :type escape_cmd: str
        :param process_hash: **参数解释**： 进程启动文件hash **取值范围**： 字符长度1-64位 
        :type process_hash: str
        :param mode: **参数解释**： 文件属性 **取值范围**： 字符长度1-64位 
        :type mode: str
        :param rule: **参数解释**： 规则 **取值范围**： 字符长度1-64位 
        :type rule: int
        :param score: **参数解释**： 分数 **取值范围**： 字符长度1-64位 
        :type score: int
        :param process_file_hash: **参数解释**： 进程文件hash **取值范围**： 字符长度1-64位 
        :type process_file_hash: str
        :param parent_process_file_hash: **参数解释**： 父进程文件hash **取值范围**： 字符长度1-64位 
        :type parent_process_file_hash: str
        :param ancestor_process_pid: **参数解释**: 祖父进程id **取值范围**: 最小值1，最大值2147483647 
        :type ancestor_process_pid: int
        :param ancestor_process_cmdline: **参数解释**： 祖父进程命令行 **取值范围**： 字符长度1-64位 
        :type ancestor_process_cmdline: str
        :param ancestor_process_path: **参数解释**： 祖父进程路径 **取值范围**： 字符长度1-64位 
        :type ancestor_process_path: str
        :param operate_type: **参数解释**: 操作类型 **取值范围**: 最小值1，最大值2147483647 
        :type operate_type: int
        :param session_id: **参数解释**: 会话id **取值范围**: 最小值1，最大值2147483647 
        :type session_id: int
        """
        
        

        self._process_name = None
        self._process_path = None
        self._process_pid = None
        self._process_uid = None
        self._process_username = None
        self._process_cmdline = None
        self._process_filename = None
        self._process_start_time = None
        self._process_gid = None
        self._process_egid = None
        self._process_euid = None
        self._parent_process_name = None
        self._parent_process_path = None
        self._parent_process_pid = None
        self._parent_process_uid = None
        self._parent_process_cmdline = None
        self._parent_process_filename = None
        self._parent_process_start_time = None
        self._parent_process_gid = None
        self._parent_process_egid = None
        self._parent_process_euid = None
        self._child_process_name = None
        self._child_process_path = None
        self._child_process_pid = None
        self._child_process_uid = None
        self._child_process_cmdline = None
        self._child_process_filename = None
        self._child_process_start_time = None
        self._child_process_gid = None
        self._child_process_egid = None
        self._child_process_euid = None
        self._virt_cmd = None
        self._virt_process_name = None
        self._escape_mode = None
        self._escape_cmd = None
        self._process_hash = None
        self._mode = None
        self._rule = None
        self._score = None
        self._process_file_hash = None
        self._parent_process_file_hash = None
        self._ancestor_process_pid = None
        self._ancestor_process_cmdline = None
        self._ancestor_process_path = None
        self._operate_type = None
        self._session_id = None
        self.discriminator = None

        if process_name is not None:
            self.process_name = process_name
        if process_path is not None:
            self.process_path = process_path
        if process_pid is not None:
            self.process_pid = process_pid
        if process_uid is not None:
            self.process_uid = process_uid
        if process_username is not None:
            self.process_username = process_username
        if process_cmdline is not None:
            self.process_cmdline = process_cmdline
        if process_filename is not None:
            self.process_filename = process_filename
        if process_start_time is not None:
            self.process_start_time = process_start_time
        if process_gid is not None:
            self.process_gid = process_gid
        if process_egid is not None:
            self.process_egid = process_egid
        if process_euid is not None:
            self.process_euid = process_euid
        if parent_process_name is not None:
            self.parent_process_name = parent_process_name
        if parent_process_path is not None:
            self.parent_process_path = parent_process_path
        if parent_process_pid is not None:
            self.parent_process_pid = parent_process_pid
        if parent_process_uid is not None:
            self.parent_process_uid = parent_process_uid
        if parent_process_cmdline is not None:
            self.parent_process_cmdline = parent_process_cmdline
        if parent_process_filename is not None:
            self.parent_process_filename = parent_process_filename
        if parent_process_start_time is not None:
            self.parent_process_start_time = parent_process_start_time
        if parent_process_gid is not None:
            self.parent_process_gid = parent_process_gid
        if parent_process_egid is not None:
            self.parent_process_egid = parent_process_egid
        if parent_process_euid is not None:
            self.parent_process_euid = parent_process_euid
        if child_process_name is not None:
            self.child_process_name = child_process_name
        if child_process_path is not None:
            self.child_process_path = child_process_path
        if child_process_pid is not None:
            self.child_process_pid = child_process_pid
        if child_process_uid is not None:
            self.child_process_uid = child_process_uid
        if child_process_cmdline is not None:
            self.child_process_cmdline = child_process_cmdline
        if child_process_filename is not None:
            self.child_process_filename = child_process_filename
        if child_process_start_time is not None:
            self.child_process_start_time = child_process_start_time
        if child_process_gid is not None:
            self.child_process_gid = child_process_gid
        if child_process_egid is not None:
            self.child_process_egid = child_process_egid
        if child_process_euid is not None:
            self.child_process_euid = child_process_euid
        if virt_cmd is not None:
            self.virt_cmd = virt_cmd
        if virt_process_name is not None:
            self.virt_process_name = virt_process_name
        if escape_mode is not None:
            self.escape_mode = escape_mode
        if escape_cmd is not None:
            self.escape_cmd = escape_cmd
        if process_hash is not None:
            self.process_hash = process_hash
        if mode is not None:
            self.mode = mode
        if rule is not None:
            self.rule = rule
        if score is not None:
            self.score = score
        if process_file_hash is not None:
            self.process_file_hash = process_file_hash
        if parent_process_file_hash is not None:
            self.parent_process_file_hash = parent_process_file_hash
        if ancestor_process_pid is not None:
            self.ancestor_process_pid = ancestor_process_pid
        if ancestor_process_cmdline is not None:
            self.ancestor_process_cmdline = ancestor_process_cmdline
        if ancestor_process_path is not None:
            self.ancestor_process_path = ancestor_process_path
        if operate_type is not None:
            self.operate_type = operate_type
        if session_id is not None:
            self.session_id = session_id

    @property
    def process_name(self):
        r"""Gets the process_name of this EventProcessResInfo.

        **参数解释**： 进程名称 **取值范围**： 字符长度1-128位 

        :return: The process_name of this EventProcessResInfo.
        :rtype: str
        """
        return self._process_name

    @process_name.setter
    def process_name(self, process_name):
        r"""Sets the process_name of this EventProcessResInfo.

        **参数解释**： 进程名称 **取值范围**： 字符长度1-128位 

        :param process_name: The process_name of this EventProcessResInfo.
        :type process_name: str
        """
        self._process_name = process_name

    @property
    def process_path(self):
        r"""Gets the process_path of this EventProcessResInfo.

        **参数解释**： 进程路径 **取值范围**： 字符长度1-256位 

        :return: The process_path of this EventProcessResInfo.
        :rtype: str
        """
        return self._process_path

    @process_path.setter
    def process_path(self, process_path):
        r"""Sets the process_path of this EventProcessResInfo.

        **参数解释**： 进程路径 **取值范围**： 字符长度1-256位 

        :param process_path: The process_path of this EventProcessResInfo.
        :type process_path: str
        """
        self._process_path = process_path

    @property
    def process_pid(self):
        r"""Gets the process_pid of this EventProcessResInfo.

        **参数解释**： 进程ID **取值范围**： 最小值0，最大值2147483647 

        :return: The process_pid of this EventProcessResInfo.
        :rtype: int
        """
        return self._process_pid

    @process_pid.setter
    def process_pid(self, process_pid):
        r"""Sets the process_pid of this EventProcessResInfo.

        **参数解释**： 进程ID **取值范围**： 最小值0，最大值2147483647 

        :param process_pid: The process_pid of this EventProcessResInfo.
        :type process_pid: int
        """
        self._process_pid = process_pid

    @property
    def process_uid(self):
        r"""Gets the process_uid of this EventProcessResInfo.

        **参数解释**： 进程名称 **取值范围**： 最小值0，最大值2147483647 

        :return: The process_uid of this EventProcessResInfo.
        :rtype: int
        """
        return self._process_uid

    @process_uid.setter
    def process_uid(self, process_uid):
        r"""Sets the process_uid of this EventProcessResInfo.

        **参数解释**： 进程名称 **取值范围**： 最小值0，最大值2147483647 

        :param process_uid: The process_uid of this EventProcessResInfo.
        :type process_uid: int
        """
        self._process_uid = process_uid

    @property
    def process_username(self):
        r"""Gets the process_username of this EventProcessResInfo.

        **参数解释**： 运行进程的用户名 **取值范围**： 字符长度1-128位 

        :return: The process_username of this EventProcessResInfo.
        :rtype: str
        """
        return self._process_username

    @process_username.setter
    def process_username(self, process_username):
        r"""Sets the process_username of this EventProcessResInfo.

        **参数解释**： 运行进程的用户名 **取值范围**： 字符长度1-128位 

        :param process_username: The process_username of this EventProcessResInfo.
        :type process_username: str
        """
        self._process_username = process_username

    @property
    def process_cmdline(self):
        r"""Gets the process_cmdline of this EventProcessResInfo.

        **参数解释**： 进程命令行 **约束限制**： 不涉及 

        :return: The process_cmdline of this EventProcessResInfo.
        :rtype: str
        """
        return self._process_cmdline

    @process_cmdline.setter
    def process_cmdline(self, process_cmdline):
        r"""Sets the process_cmdline of this EventProcessResInfo.

        **参数解释**： 进程命令行 **约束限制**： 不涉及 

        :param process_cmdline: The process_cmdline of this EventProcessResInfo.
        :type process_cmdline: str
        """
        self._process_cmdline = process_cmdline

    @property
    def process_filename(self):
        r"""Gets the process_filename of this EventProcessResInfo.

        **参数解释**： 进程文件名 **取值范围**： 字符长度1-64位 

        :return: The process_filename of this EventProcessResInfo.
        :rtype: str
        """
        return self._process_filename

    @process_filename.setter
    def process_filename(self, process_filename):
        r"""Sets the process_filename of this EventProcessResInfo.

        **参数解释**： 进程文件名 **取值范围**： 字符长度1-64位 

        :param process_filename: The process_filename of this EventProcessResInfo.
        :type process_filename: str
        """
        self._process_filename = process_filename

    @property
    def process_start_time(self):
        r"""Gets the process_start_time of this EventProcessResInfo.

        **参数解释**: 进程启动时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The process_start_time of this EventProcessResInfo.
        :rtype: int
        """
        return self._process_start_time

    @process_start_time.setter
    def process_start_time(self, process_start_time):
        r"""Sets the process_start_time of this EventProcessResInfo.

        **参数解释**: 进程启动时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param process_start_time: The process_start_time of this EventProcessResInfo.
        :type process_start_time: int
        """
        self._process_start_time = process_start_time

    @property
    def process_gid(self):
        r"""Gets the process_gid of this EventProcessResInfo.

        **参数解释**: 进程组ID **取值范围**: 最小值0，最大值2147483647 

        :return: The process_gid of this EventProcessResInfo.
        :rtype: int
        """
        return self._process_gid

    @process_gid.setter
    def process_gid(self, process_gid):
        r"""Sets the process_gid of this EventProcessResInfo.

        **参数解释**: 进程组ID **取值范围**: 最小值0，最大值2147483647 

        :param process_gid: The process_gid of this EventProcessResInfo.
        :type process_gid: int
        """
        self._process_gid = process_gid

    @property
    def process_egid(self):
        r"""Gets the process_egid of this EventProcessResInfo.

        **参数解释**: 进程有效组ID **取值范围**: 最小值0，最大值2147483647 

        :return: The process_egid of this EventProcessResInfo.
        :rtype: int
        """
        return self._process_egid

    @process_egid.setter
    def process_egid(self, process_egid):
        r"""Sets the process_egid of this EventProcessResInfo.

        **参数解释**: 进程有效组ID **取值范围**: 最小值0，最大值2147483647 

        :param process_egid: The process_egid of this EventProcessResInfo.
        :type process_egid: int
        """
        self._process_egid = process_egid

    @property
    def process_euid(self):
        r"""Gets the process_euid of this EventProcessResInfo.

        **参数解释**: 进程有效用户ID **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The process_euid of this EventProcessResInfo.
        :rtype: int
        """
        return self._process_euid

    @process_euid.setter
    def process_euid(self, process_euid):
        r"""Sets the process_euid of this EventProcessResInfo.

        **参数解释**: 进程有效用户ID **取值范围**: 最小值0，最大值9223372036854775807 

        :param process_euid: The process_euid of this EventProcessResInfo.
        :type process_euid: int
        """
        self._process_euid = process_euid

    @property
    def parent_process_name(self):
        r"""Gets the parent_process_name of this EventProcessResInfo.

        **参数解释**： 父进程名称 **取值范围**： 字符长度1-64位 

        :return: The parent_process_name of this EventProcessResInfo.
        :rtype: str
        """
        return self._parent_process_name

    @parent_process_name.setter
    def parent_process_name(self, parent_process_name):
        r"""Sets the parent_process_name of this EventProcessResInfo.

        **参数解释**： 父进程名称 **取值范围**： 字符长度1-64位 

        :param parent_process_name: The parent_process_name of this EventProcessResInfo.
        :type parent_process_name: str
        """
        self._parent_process_name = parent_process_name

    @property
    def parent_process_path(self):
        r"""Gets the parent_process_path of this EventProcessResInfo.

        **参数解释**： 父进程文件路径 **取值范围**： 字符长度1-64位 

        :return: The parent_process_path of this EventProcessResInfo.
        :rtype: str
        """
        return self._parent_process_path

    @parent_process_path.setter
    def parent_process_path(self, parent_process_path):
        r"""Sets the parent_process_path of this EventProcessResInfo.

        **参数解释**： 父进程文件路径 **取值范围**： 字符长度1-64位 

        :param parent_process_path: The parent_process_path of this EventProcessResInfo.
        :type parent_process_path: str
        """
        self._parent_process_path = parent_process_path

    @property
    def parent_process_pid(self):
        r"""Gets the parent_process_pid of this EventProcessResInfo.

        **参数解释**: 父进程id **取值范围**: 最小值0，最大值2147483647 

        :return: The parent_process_pid of this EventProcessResInfo.
        :rtype: int
        """
        return self._parent_process_pid

    @parent_process_pid.setter
    def parent_process_pid(self, parent_process_pid):
        r"""Sets the parent_process_pid of this EventProcessResInfo.

        **参数解释**: 父进程id **取值范围**: 最小值0，最大值2147483647 

        :param parent_process_pid: The parent_process_pid of this EventProcessResInfo.
        :type parent_process_pid: int
        """
        self._parent_process_pid = parent_process_pid

    @property
    def parent_process_uid(self):
        r"""Gets the parent_process_uid of this EventProcessResInfo.

        **参数解释**: 父进程用户id **取值范围**: 最小值0，最大值2147483647 

        :return: The parent_process_uid of this EventProcessResInfo.
        :rtype: int
        """
        return self._parent_process_uid

    @parent_process_uid.setter
    def parent_process_uid(self, parent_process_uid):
        r"""Sets the parent_process_uid of this EventProcessResInfo.

        **参数解释**: 父进程用户id **取值范围**: 最小值0，最大值2147483647 

        :param parent_process_uid: The parent_process_uid of this EventProcessResInfo.
        :type parent_process_uid: int
        """
        self._parent_process_uid = parent_process_uid

    @property
    def parent_process_cmdline(self):
        r"""Gets the parent_process_cmdline of this EventProcessResInfo.

        **参数解释**： 父进程文件命令行 **取值范围**： 字符长度1-64位 

        :return: The parent_process_cmdline of this EventProcessResInfo.
        :rtype: str
        """
        return self._parent_process_cmdline

    @parent_process_cmdline.setter
    def parent_process_cmdline(self, parent_process_cmdline):
        r"""Sets the parent_process_cmdline of this EventProcessResInfo.

        **参数解释**： 父进程文件命令行 **取值范围**： 字符长度1-64位 

        :param parent_process_cmdline: The parent_process_cmdline of this EventProcessResInfo.
        :type parent_process_cmdline: str
        """
        self._parent_process_cmdline = parent_process_cmdline

    @property
    def parent_process_filename(self):
        r"""Gets the parent_process_filename of this EventProcessResInfo.

        **参数解释**： 父进程文件名 **取值范围**： 字符长度1-64位 

        :return: The parent_process_filename of this EventProcessResInfo.
        :rtype: str
        """
        return self._parent_process_filename

    @parent_process_filename.setter
    def parent_process_filename(self, parent_process_filename):
        r"""Sets the parent_process_filename of this EventProcessResInfo.

        **参数解释**： 父进程文件名 **取值范围**： 字符长度1-64位 

        :param parent_process_filename: The parent_process_filename of this EventProcessResInfo.
        :type parent_process_filename: str
        """
        self._parent_process_filename = parent_process_filename

    @property
    def parent_process_start_time(self):
        r"""Gets the parent_process_start_time of this EventProcessResInfo.

        **参数解释**: 父进程启动时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The parent_process_start_time of this EventProcessResInfo.
        :rtype: int
        """
        return self._parent_process_start_time

    @parent_process_start_time.setter
    def parent_process_start_time(self, parent_process_start_time):
        r"""Sets the parent_process_start_time of this EventProcessResInfo.

        **参数解释**: 父进程启动时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param parent_process_start_time: The parent_process_start_time of this EventProcessResInfo.
        :type parent_process_start_time: int
        """
        self._parent_process_start_time = parent_process_start_time

    @property
    def parent_process_gid(self):
        r"""Gets the parent_process_gid of this EventProcessResInfo.

        **参数解释**: 父进程组ID **取值范围**: 最小值0，最大值2147483647 

        :return: The parent_process_gid of this EventProcessResInfo.
        :rtype: int
        """
        return self._parent_process_gid

    @parent_process_gid.setter
    def parent_process_gid(self, parent_process_gid):
        r"""Sets the parent_process_gid of this EventProcessResInfo.

        **参数解释**: 父进程组ID **取值范围**: 最小值0，最大值2147483647 

        :param parent_process_gid: The parent_process_gid of this EventProcessResInfo.
        :type parent_process_gid: int
        """
        self._parent_process_gid = parent_process_gid

    @property
    def parent_process_egid(self):
        r"""Gets the parent_process_egid of this EventProcessResInfo.

        **参数解释**: 父进程有效组ID **取值范围**: 最小值0，最大值2147483647 

        :return: The parent_process_egid of this EventProcessResInfo.
        :rtype: int
        """
        return self._parent_process_egid

    @parent_process_egid.setter
    def parent_process_egid(self, parent_process_egid):
        r"""Sets the parent_process_egid of this EventProcessResInfo.

        **参数解释**: 父进程有效组ID **取值范围**: 最小值0，最大值2147483647 

        :param parent_process_egid: The parent_process_egid of this EventProcessResInfo.
        :type parent_process_egid: int
        """
        self._parent_process_egid = parent_process_egid

    @property
    def parent_process_euid(self):
        r"""Gets the parent_process_euid of this EventProcessResInfo.

        **参数解释**: 父进程有效用户ID **取值范围**: 最小值0，最大值2147483647 

        :return: The parent_process_euid of this EventProcessResInfo.
        :rtype: int
        """
        return self._parent_process_euid

    @parent_process_euid.setter
    def parent_process_euid(self, parent_process_euid):
        r"""Sets the parent_process_euid of this EventProcessResInfo.

        **参数解释**: 父进程有效用户ID **取值范围**: 最小值0，最大值2147483647 

        :param parent_process_euid: The parent_process_euid of this EventProcessResInfo.
        :type parent_process_euid: int
        """
        self._parent_process_euid = parent_process_euid

    @property
    def child_process_name(self):
        r"""Gets the child_process_name of this EventProcessResInfo.

        **参数解释**： 子进程名称 **取值范围**： 字符长度1-64位 

        :return: The child_process_name of this EventProcessResInfo.
        :rtype: str
        """
        return self._child_process_name

    @child_process_name.setter
    def child_process_name(self, child_process_name):
        r"""Sets the child_process_name of this EventProcessResInfo.

        **参数解释**： 子进程名称 **取值范围**： 字符长度1-64位 

        :param child_process_name: The child_process_name of this EventProcessResInfo.
        :type child_process_name: str
        """
        self._child_process_name = child_process_name

    @property
    def child_process_path(self):
        r"""Gets the child_process_path of this EventProcessResInfo.

        **参数解释**： 子进程文件路径 **取值范围**： 字符长度1-64位 

        :return: The child_process_path of this EventProcessResInfo.
        :rtype: str
        """
        return self._child_process_path

    @child_process_path.setter
    def child_process_path(self, child_process_path):
        r"""Sets the child_process_path of this EventProcessResInfo.

        **参数解释**： 子进程文件路径 **取值范围**： 字符长度1-64位 

        :param child_process_path: The child_process_path of this EventProcessResInfo.
        :type child_process_path: str
        """
        self._child_process_path = child_process_path

    @property
    def child_process_pid(self):
        r"""Gets the child_process_pid of this EventProcessResInfo.

        **参数解释**: 子进程id **取值范围**: 最小值0，最大值2147483647 

        :return: The child_process_pid of this EventProcessResInfo.
        :rtype: int
        """
        return self._child_process_pid

    @child_process_pid.setter
    def child_process_pid(self, child_process_pid):
        r"""Sets the child_process_pid of this EventProcessResInfo.

        **参数解释**: 子进程id **取值范围**: 最小值0，最大值2147483647 

        :param child_process_pid: The child_process_pid of this EventProcessResInfo.
        :type child_process_pid: int
        """
        self._child_process_pid = child_process_pid

    @property
    def child_process_uid(self):
        r"""Gets the child_process_uid of this EventProcessResInfo.

        **参数解释**: 子进程用户id **取值范围**: 最小值0，最大值2147483647 

        :return: The child_process_uid of this EventProcessResInfo.
        :rtype: int
        """
        return self._child_process_uid

    @child_process_uid.setter
    def child_process_uid(self, child_process_uid):
        r"""Sets the child_process_uid of this EventProcessResInfo.

        **参数解释**: 子进程用户id **取值范围**: 最小值0，最大值2147483647 

        :param child_process_uid: The child_process_uid of this EventProcessResInfo.
        :type child_process_uid: int
        """
        self._child_process_uid = child_process_uid

    @property
    def child_process_cmdline(self):
        r"""Gets the child_process_cmdline of this EventProcessResInfo.

        **参数解释**： 子进程文件命令行 **取值范围**： 字符长度1-64位 

        :return: The child_process_cmdline of this EventProcessResInfo.
        :rtype: str
        """
        return self._child_process_cmdline

    @child_process_cmdline.setter
    def child_process_cmdline(self, child_process_cmdline):
        r"""Sets the child_process_cmdline of this EventProcessResInfo.

        **参数解释**： 子进程文件命令行 **取值范围**： 字符长度1-64位 

        :param child_process_cmdline: The child_process_cmdline of this EventProcessResInfo.
        :type child_process_cmdline: str
        """
        self._child_process_cmdline = child_process_cmdline

    @property
    def child_process_filename(self):
        r"""Gets the child_process_filename of this EventProcessResInfo.

        **参数解释**： 子进程文件名 **取值范围**： 字符长度1-64位 

        :return: The child_process_filename of this EventProcessResInfo.
        :rtype: str
        """
        return self._child_process_filename

    @child_process_filename.setter
    def child_process_filename(self, child_process_filename):
        r"""Sets the child_process_filename of this EventProcessResInfo.

        **参数解释**： 子进程文件名 **取值范围**： 字符长度1-64位 

        :param child_process_filename: The child_process_filename of this EventProcessResInfo.
        :type child_process_filename: str
        """
        self._child_process_filename = child_process_filename

    @property
    def child_process_start_time(self):
        r"""Gets the child_process_start_time of this EventProcessResInfo.

        **参数解释**: 子进程启动时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The child_process_start_time of this EventProcessResInfo.
        :rtype: int
        """
        return self._child_process_start_time

    @child_process_start_time.setter
    def child_process_start_time(self, child_process_start_time):
        r"""Sets the child_process_start_time of this EventProcessResInfo.

        **参数解释**: 子进程启动时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param child_process_start_time: The child_process_start_time of this EventProcessResInfo.
        :type child_process_start_time: int
        """
        self._child_process_start_time = child_process_start_time

    @property
    def child_process_gid(self):
        r"""Gets the child_process_gid of this EventProcessResInfo.

        **参数解释**: 子进程组ID **取值范围**: 最小值0，最大值2147483647 

        :return: The child_process_gid of this EventProcessResInfo.
        :rtype: int
        """
        return self._child_process_gid

    @child_process_gid.setter
    def child_process_gid(self, child_process_gid):
        r"""Sets the child_process_gid of this EventProcessResInfo.

        **参数解释**: 子进程组ID **取值范围**: 最小值0，最大值2147483647 

        :param child_process_gid: The child_process_gid of this EventProcessResInfo.
        :type child_process_gid: int
        """
        self._child_process_gid = child_process_gid

    @property
    def child_process_egid(self):
        r"""Gets the child_process_egid of this EventProcessResInfo.

        **参数解释**: 子进程有效组ID **取值范围**: 最小值0，最大值2147483647 

        :return: The child_process_egid of this EventProcessResInfo.
        :rtype: int
        """
        return self._child_process_egid

    @child_process_egid.setter
    def child_process_egid(self, child_process_egid):
        r"""Sets the child_process_egid of this EventProcessResInfo.

        **参数解释**: 子进程有效组ID **取值范围**: 最小值0，最大值2147483647 

        :param child_process_egid: The child_process_egid of this EventProcessResInfo.
        :type child_process_egid: int
        """
        self._child_process_egid = child_process_egid

    @property
    def child_process_euid(self):
        r"""Gets the child_process_euid of this EventProcessResInfo.

        **参数解释**: 子进程有效用户ID **取值范围**: 最小值0，最大值2147483647 

        :return: The child_process_euid of this EventProcessResInfo.
        :rtype: int
        """
        return self._child_process_euid

    @child_process_euid.setter
    def child_process_euid(self, child_process_euid):
        r"""Sets the child_process_euid of this EventProcessResInfo.

        **参数解释**: 子进程有效用户ID **取值范围**: 最小值0，最大值2147483647 

        :param child_process_euid: The child_process_euid of this EventProcessResInfo.
        :type child_process_euid: int
        """
        self._child_process_euid = child_process_euid

    @property
    def virt_cmd(self):
        r"""Gets the virt_cmd of this EventProcessResInfo.

        **参数解释**： 虚拟化命令 **取值范围**： 字符长度1-64位 

        :return: The virt_cmd of this EventProcessResInfo.
        :rtype: str
        """
        return self._virt_cmd

    @virt_cmd.setter
    def virt_cmd(self, virt_cmd):
        r"""Sets the virt_cmd of this EventProcessResInfo.

        **参数解释**： 虚拟化命令 **取值范围**： 字符长度1-64位 

        :param virt_cmd: The virt_cmd of this EventProcessResInfo.
        :type virt_cmd: str
        """
        self._virt_cmd = virt_cmd

    @property
    def virt_process_name(self):
        r"""Gets the virt_process_name of this EventProcessResInfo.

        **参数解释**： 虚拟化进程名称 **取值范围**： 字符长度1-64位 

        :return: The virt_process_name of this EventProcessResInfo.
        :rtype: str
        """
        return self._virt_process_name

    @virt_process_name.setter
    def virt_process_name(self, virt_process_name):
        r"""Sets the virt_process_name of this EventProcessResInfo.

        **参数解释**： 虚拟化进程名称 **取值范围**： 字符长度1-64位 

        :param virt_process_name: The virt_process_name of this EventProcessResInfo.
        :type virt_process_name: str
        """
        self._virt_process_name = virt_process_name

    @property
    def escape_mode(self):
        r"""Gets the escape_mode of this EventProcessResInfo.

        **参数解释**： 逃逸方式 **取值范围**： 字符长度1-64位 

        :return: The escape_mode of this EventProcessResInfo.
        :rtype: str
        """
        return self._escape_mode

    @escape_mode.setter
    def escape_mode(self, escape_mode):
        r"""Sets the escape_mode of this EventProcessResInfo.

        **参数解释**： 逃逸方式 **取值范围**： 字符长度1-64位 

        :param escape_mode: The escape_mode of this EventProcessResInfo.
        :type escape_mode: str
        """
        self._escape_mode = escape_mode

    @property
    def escape_cmd(self):
        r"""Gets the escape_cmd of this EventProcessResInfo.

        **参数解释**： 逃逸后执行的命令 **取值范围**： 字符长度1-128位 

        :return: The escape_cmd of this EventProcessResInfo.
        :rtype: str
        """
        return self._escape_cmd

    @escape_cmd.setter
    def escape_cmd(self, escape_cmd):
        r"""Sets the escape_cmd of this EventProcessResInfo.

        **参数解释**： 逃逸后执行的命令 **取值范围**： 字符长度1-128位 

        :param escape_cmd: The escape_cmd of this EventProcessResInfo.
        :type escape_cmd: str
        """
        self._escape_cmd = escape_cmd

    @property
    def process_hash(self):
        r"""Gets the process_hash of this EventProcessResInfo.

        **参数解释**： 进程启动文件hash **取值范围**： 字符长度1-64位 

        :return: The process_hash of this EventProcessResInfo.
        :rtype: str
        """
        return self._process_hash

    @process_hash.setter
    def process_hash(self, process_hash):
        r"""Sets the process_hash of this EventProcessResInfo.

        **参数解释**： 进程启动文件hash **取值范围**： 字符长度1-64位 

        :param process_hash: The process_hash of this EventProcessResInfo.
        :type process_hash: str
        """
        self._process_hash = process_hash

    @property
    def mode(self):
        r"""Gets the mode of this EventProcessResInfo.

        **参数解释**： 文件属性 **取值范围**： 字符长度1-64位 

        :return: The mode of this EventProcessResInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this EventProcessResInfo.

        **参数解释**： 文件属性 **取值范围**： 字符长度1-64位 

        :param mode: The mode of this EventProcessResInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def rule(self):
        r"""Gets the rule of this EventProcessResInfo.

        **参数解释**： 规则 **取值范围**： 字符长度1-64位 

        :return: The rule of this EventProcessResInfo.
        :rtype: int
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this EventProcessResInfo.

        **参数解释**： 规则 **取值范围**： 字符长度1-64位 

        :param rule: The rule of this EventProcessResInfo.
        :type rule: int
        """
        self._rule = rule

    @property
    def score(self):
        r"""Gets the score of this EventProcessResInfo.

        **参数解释**： 分数 **取值范围**： 字符长度1-64位 

        :return: The score of this EventProcessResInfo.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this EventProcessResInfo.

        **参数解释**： 分数 **取值范围**： 字符长度1-64位 

        :param score: The score of this EventProcessResInfo.
        :type score: int
        """
        self._score = score

    @property
    def process_file_hash(self):
        r"""Gets the process_file_hash of this EventProcessResInfo.

        **参数解释**： 进程文件hash **取值范围**： 字符长度1-64位 

        :return: The process_file_hash of this EventProcessResInfo.
        :rtype: str
        """
        return self._process_file_hash

    @process_file_hash.setter
    def process_file_hash(self, process_file_hash):
        r"""Sets the process_file_hash of this EventProcessResInfo.

        **参数解释**： 进程文件hash **取值范围**： 字符长度1-64位 

        :param process_file_hash: The process_file_hash of this EventProcessResInfo.
        :type process_file_hash: str
        """
        self._process_file_hash = process_file_hash

    @property
    def parent_process_file_hash(self):
        r"""Gets the parent_process_file_hash of this EventProcessResInfo.

        **参数解释**： 父进程文件hash **取值范围**： 字符长度1-64位 

        :return: The parent_process_file_hash of this EventProcessResInfo.
        :rtype: str
        """
        return self._parent_process_file_hash

    @parent_process_file_hash.setter
    def parent_process_file_hash(self, parent_process_file_hash):
        r"""Sets the parent_process_file_hash of this EventProcessResInfo.

        **参数解释**： 父进程文件hash **取值范围**： 字符长度1-64位 

        :param parent_process_file_hash: The parent_process_file_hash of this EventProcessResInfo.
        :type parent_process_file_hash: str
        """
        self._parent_process_file_hash = parent_process_file_hash

    @property
    def ancestor_process_pid(self):
        r"""Gets the ancestor_process_pid of this EventProcessResInfo.

        **参数解释**: 祖父进程id **取值范围**: 最小值1，最大值2147483647 

        :return: The ancestor_process_pid of this EventProcessResInfo.
        :rtype: int
        """
        return self._ancestor_process_pid

    @ancestor_process_pid.setter
    def ancestor_process_pid(self, ancestor_process_pid):
        r"""Sets the ancestor_process_pid of this EventProcessResInfo.

        **参数解释**: 祖父进程id **取值范围**: 最小值1，最大值2147483647 

        :param ancestor_process_pid: The ancestor_process_pid of this EventProcessResInfo.
        :type ancestor_process_pid: int
        """
        self._ancestor_process_pid = ancestor_process_pid

    @property
    def ancestor_process_cmdline(self):
        r"""Gets the ancestor_process_cmdline of this EventProcessResInfo.

        **参数解释**： 祖父进程命令行 **取值范围**： 字符长度1-64位 

        :return: The ancestor_process_cmdline of this EventProcessResInfo.
        :rtype: str
        """
        return self._ancestor_process_cmdline

    @ancestor_process_cmdline.setter
    def ancestor_process_cmdline(self, ancestor_process_cmdline):
        r"""Sets the ancestor_process_cmdline of this EventProcessResInfo.

        **参数解释**： 祖父进程命令行 **取值范围**： 字符长度1-64位 

        :param ancestor_process_cmdline: The ancestor_process_cmdline of this EventProcessResInfo.
        :type ancestor_process_cmdline: str
        """
        self._ancestor_process_cmdline = ancestor_process_cmdline

    @property
    def ancestor_process_path(self):
        r"""Gets the ancestor_process_path of this EventProcessResInfo.

        **参数解释**： 祖父进程路径 **取值范围**： 字符长度1-64位 

        :return: The ancestor_process_path of this EventProcessResInfo.
        :rtype: str
        """
        return self._ancestor_process_path

    @ancestor_process_path.setter
    def ancestor_process_path(self, ancestor_process_path):
        r"""Sets the ancestor_process_path of this EventProcessResInfo.

        **参数解释**： 祖父进程路径 **取值范围**： 字符长度1-64位 

        :param ancestor_process_path: The ancestor_process_path of this EventProcessResInfo.
        :type ancestor_process_path: str
        """
        self._ancestor_process_path = ancestor_process_path

    @property
    def operate_type(self):
        r"""Gets the operate_type of this EventProcessResInfo.

        **参数解释**: 操作类型 **取值范围**: 最小值1，最大值2147483647 

        :return: The operate_type of this EventProcessResInfo.
        :rtype: int
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this EventProcessResInfo.

        **参数解释**: 操作类型 **取值范围**: 最小值1，最大值2147483647 

        :param operate_type: The operate_type of this EventProcessResInfo.
        :type operate_type: int
        """
        self._operate_type = operate_type

    @property
    def session_id(self):
        r"""Gets the session_id of this EventProcessResInfo.

        **参数解释**: 会话id **取值范围**: 最小值1，最大值2147483647 

        :return: The session_id of this EventProcessResInfo.
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this EventProcessResInfo.

        **参数解释**: 会话id **取值范围**: 最小值1，最大值2147483647 

        :param session_id: The session_id of this EventProcessResInfo.
        :type session_id: int
        """
        self._session_id = session_id

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
        if not isinstance(other, EventProcessResInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
