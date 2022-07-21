# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventProcessResponseInfo:

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
        'process_hash': 'str'
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
        'process_hash': 'process_hash'
    }

    def __init__(self, process_name=None, process_path=None, process_pid=None, process_uid=None, process_username=None, process_cmdline=None, process_filename=None, process_start_time=None, process_gid=None, process_egid=None, process_euid=None, parent_process_name=None, parent_process_path=None, parent_process_pid=None, parent_process_uid=None, parent_process_cmdline=None, parent_process_filename=None, parent_process_start_time=None, parent_process_gid=None, parent_process_egid=None, parent_process_euid=None, child_process_name=None, child_process_path=None, child_process_pid=None, child_process_uid=None, child_process_cmdline=None, child_process_filename=None, child_process_start_time=None, child_process_gid=None, child_process_egid=None, child_process_euid=None, virt_cmd=None, virt_process_name=None, escape_mode=None, escape_cmd=None, process_hash=None):
        """EventProcessResponseInfo

        The model defined in huaweicloud sdk

        :param process_name: 进程名称
        :type process_name: str
        :param process_path: 进程文件路径
        :type process_path: str
        :param process_pid: 进程id
        :type process_pid: int
        :param process_uid: 进程用户id
        :type process_uid: int
        :param process_username: 运行进程的用户名
        :type process_username: str
        :param process_cmdline: 进程文件命令行
        :type process_cmdline: str
        :param process_filename: 进程文件名
        :type process_filename: str
        :param process_start_time: 进程启动时间
        :type process_start_time: int
        :param process_gid: 进程组ID
        :type process_gid: int
        :param process_egid: 进程有效组ID
        :type process_egid: int
        :param process_euid: 进程有效用户ID
        :type process_euid: int
        :param parent_process_name: 父进程名称
        :type parent_process_name: str
        :param parent_process_path: 父进程文件路径
        :type parent_process_path: str
        :param parent_process_pid: 父进程id
        :type parent_process_pid: int
        :param parent_process_uid: 父进程用户id
        :type parent_process_uid: int
        :param parent_process_cmdline: 父进程文件命令行
        :type parent_process_cmdline: str
        :param parent_process_filename: 父进程文件名
        :type parent_process_filename: str
        :param parent_process_start_time: 父进程启动时间
        :type parent_process_start_time: int
        :param parent_process_gid: 父进程组ID
        :type parent_process_gid: int
        :param parent_process_egid: 父进程有效组ID
        :type parent_process_egid: int
        :param parent_process_euid: 父进程有效用户ID
        :type parent_process_euid: int
        :param child_process_name: 子进程名称
        :type child_process_name: str
        :param child_process_path: 子进程文件路径
        :type child_process_path: str
        :param child_process_pid: 子进程id
        :type child_process_pid: int
        :param child_process_uid: 子进程用户id
        :type child_process_uid: int
        :param child_process_cmdline: 子进程文件命令行
        :type child_process_cmdline: str
        :param child_process_filename: 子进程文件名
        :type child_process_filename: str
        :param child_process_start_time: 子进程启动时间
        :type child_process_start_time: int
        :param child_process_gid: 子进程组ID
        :type child_process_gid: int
        :param child_process_egid: 子进程有效组ID
        :type child_process_egid: int
        :param child_process_euid: 子进程有效用户ID
        :type child_process_euid: int
        :param virt_cmd: 虚拟化命令
        :type virt_cmd: str
        :param virt_process_name: 虚拟化进程名称
        :type virt_process_name: str
        :param escape_mode: 逃逸方式
        :type escape_mode: str
        :param escape_cmd: 逃逸后后执行的命令
        :type escape_cmd: str
        :param process_hash: 进程启动文件hash
        :type process_hash: str
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

    @property
    def process_name(self):
        """Gets the process_name of this EventProcessResponseInfo.

        进程名称

        :return: The process_name of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._process_name

    @process_name.setter
    def process_name(self, process_name):
        """Sets the process_name of this EventProcessResponseInfo.

        进程名称

        :param process_name: The process_name of this EventProcessResponseInfo.
        :type process_name: str
        """
        self._process_name = process_name

    @property
    def process_path(self):
        """Gets the process_path of this EventProcessResponseInfo.

        进程文件路径

        :return: The process_path of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._process_path

    @process_path.setter
    def process_path(self, process_path):
        """Sets the process_path of this EventProcessResponseInfo.

        进程文件路径

        :param process_path: The process_path of this EventProcessResponseInfo.
        :type process_path: str
        """
        self._process_path = process_path

    @property
    def process_pid(self):
        """Gets the process_pid of this EventProcessResponseInfo.

        进程id

        :return: The process_pid of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._process_pid

    @process_pid.setter
    def process_pid(self, process_pid):
        """Sets the process_pid of this EventProcessResponseInfo.

        进程id

        :param process_pid: The process_pid of this EventProcessResponseInfo.
        :type process_pid: int
        """
        self._process_pid = process_pid

    @property
    def process_uid(self):
        """Gets the process_uid of this EventProcessResponseInfo.

        进程用户id

        :return: The process_uid of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._process_uid

    @process_uid.setter
    def process_uid(self, process_uid):
        """Sets the process_uid of this EventProcessResponseInfo.

        进程用户id

        :param process_uid: The process_uid of this EventProcessResponseInfo.
        :type process_uid: int
        """
        self._process_uid = process_uid

    @property
    def process_username(self):
        """Gets the process_username of this EventProcessResponseInfo.

        运行进程的用户名

        :return: The process_username of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._process_username

    @process_username.setter
    def process_username(self, process_username):
        """Sets the process_username of this EventProcessResponseInfo.

        运行进程的用户名

        :param process_username: The process_username of this EventProcessResponseInfo.
        :type process_username: str
        """
        self._process_username = process_username

    @property
    def process_cmdline(self):
        """Gets the process_cmdline of this EventProcessResponseInfo.

        进程文件命令行

        :return: The process_cmdline of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._process_cmdline

    @process_cmdline.setter
    def process_cmdline(self, process_cmdline):
        """Sets the process_cmdline of this EventProcessResponseInfo.

        进程文件命令行

        :param process_cmdline: The process_cmdline of this EventProcessResponseInfo.
        :type process_cmdline: str
        """
        self._process_cmdline = process_cmdline

    @property
    def process_filename(self):
        """Gets the process_filename of this EventProcessResponseInfo.

        进程文件名

        :return: The process_filename of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._process_filename

    @process_filename.setter
    def process_filename(self, process_filename):
        """Sets the process_filename of this EventProcessResponseInfo.

        进程文件名

        :param process_filename: The process_filename of this EventProcessResponseInfo.
        :type process_filename: str
        """
        self._process_filename = process_filename

    @property
    def process_start_time(self):
        """Gets the process_start_time of this EventProcessResponseInfo.

        进程启动时间

        :return: The process_start_time of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._process_start_time

    @process_start_time.setter
    def process_start_time(self, process_start_time):
        """Sets the process_start_time of this EventProcessResponseInfo.

        进程启动时间

        :param process_start_time: The process_start_time of this EventProcessResponseInfo.
        :type process_start_time: int
        """
        self._process_start_time = process_start_time

    @property
    def process_gid(self):
        """Gets the process_gid of this EventProcessResponseInfo.

        进程组ID

        :return: The process_gid of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._process_gid

    @process_gid.setter
    def process_gid(self, process_gid):
        """Sets the process_gid of this EventProcessResponseInfo.

        进程组ID

        :param process_gid: The process_gid of this EventProcessResponseInfo.
        :type process_gid: int
        """
        self._process_gid = process_gid

    @property
    def process_egid(self):
        """Gets the process_egid of this EventProcessResponseInfo.

        进程有效组ID

        :return: The process_egid of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._process_egid

    @process_egid.setter
    def process_egid(self, process_egid):
        """Sets the process_egid of this EventProcessResponseInfo.

        进程有效组ID

        :param process_egid: The process_egid of this EventProcessResponseInfo.
        :type process_egid: int
        """
        self._process_egid = process_egid

    @property
    def process_euid(self):
        """Gets the process_euid of this EventProcessResponseInfo.

        进程有效用户ID

        :return: The process_euid of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._process_euid

    @process_euid.setter
    def process_euid(self, process_euid):
        """Sets the process_euid of this EventProcessResponseInfo.

        进程有效用户ID

        :param process_euid: The process_euid of this EventProcessResponseInfo.
        :type process_euid: int
        """
        self._process_euid = process_euid

    @property
    def parent_process_name(self):
        """Gets the parent_process_name of this EventProcessResponseInfo.

        父进程名称

        :return: The parent_process_name of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._parent_process_name

    @parent_process_name.setter
    def parent_process_name(self, parent_process_name):
        """Sets the parent_process_name of this EventProcessResponseInfo.

        父进程名称

        :param parent_process_name: The parent_process_name of this EventProcessResponseInfo.
        :type parent_process_name: str
        """
        self._parent_process_name = parent_process_name

    @property
    def parent_process_path(self):
        """Gets the parent_process_path of this EventProcessResponseInfo.

        父进程文件路径

        :return: The parent_process_path of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._parent_process_path

    @parent_process_path.setter
    def parent_process_path(self, parent_process_path):
        """Sets the parent_process_path of this EventProcessResponseInfo.

        父进程文件路径

        :param parent_process_path: The parent_process_path of this EventProcessResponseInfo.
        :type parent_process_path: str
        """
        self._parent_process_path = parent_process_path

    @property
    def parent_process_pid(self):
        """Gets the parent_process_pid of this EventProcessResponseInfo.

        父进程id

        :return: The parent_process_pid of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._parent_process_pid

    @parent_process_pid.setter
    def parent_process_pid(self, parent_process_pid):
        """Sets the parent_process_pid of this EventProcessResponseInfo.

        父进程id

        :param parent_process_pid: The parent_process_pid of this EventProcessResponseInfo.
        :type parent_process_pid: int
        """
        self._parent_process_pid = parent_process_pid

    @property
    def parent_process_uid(self):
        """Gets the parent_process_uid of this EventProcessResponseInfo.

        父进程用户id

        :return: The parent_process_uid of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._parent_process_uid

    @parent_process_uid.setter
    def parent_process_uid(self, parent_process_uid):
        """Sets the parent_process_uid of this EventProcessResponseInfo.

        父进程用户id

        :param parent_process_uid: The parent_process_uid of this EventProcessResponseInfo.
        :type parent_process_uid: int
        """
        self._parent_process_uid = parent_process_uid

    @property
    def parent_process_cmdline(self):
        """Gets the parent_process_cmdline of this EventProcessResponseInfo.

        父进程文件命令行

        :return: The parent_process_cmdline of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._parent_process_cmdline

    @parent_process_cmdline.setter
    def parent_process_cmdline(self, parent_process_cmdline):
        """Sets the parent_process_cmdline of this EventProcessResponseInfo.

        父进程文件命令行

        :param parent_process_cmdline: The parent_process_cmdline of this EventProcessResponseInfo.
        :type parent_process_cmdline: str
        """
        self._parent_process_cmdline = parent_process_cmdline

    @property
    def parent_process_filename(self):
        """Gets the parent_process_filename of this EventProcessResponseInfo.

        父进程文件名

        :return: The parent_process_filename of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._parent_process_filename

    @parent_process_filename.setter
    def parent_process_filename(self, parent_process_filename):
        """Sets the parent_process_filename of this EventProcessResponseInfo.

        父进程文件名

        :param parent_process_filename: The parent_process_filename of this EventProcessResponseInfo.
        :type parent_process_filename: str
        """
        self._parent_process_filename = parent_process_filename

    @property
    def parent_process_start_time(self):
        """Gets the parent_process_start_time of this EventProcessResponseInfo.

        父进程启动时间

        :return: The parent_process_start_time of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._parent_process_start_time

    @parent_process_start_time.setter
    def parent_process_start_time(self, parent_process_start_time):
        """Sets the parent_process_start_time of this EventProcessResponseInfo.

        父进程启动时间

        :param parent_process_start_time: The parent_process_start_time of this EventProcessResponseInfo.
        :type parent_process_start_time: int
        """
        self._parent_process_start_time = parent_process_start_time

    @property
    def parent_process_gid(self):
        """Gets the parent_process_gid of this EventProcessResponseInfo.

        父进程组ID

        :return: The parent_process_gid of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._parent_process_gid

    @parent_process_gid.setter
    def parent_process_gid(self, parent_process_gid):
        """Sets the parent_process_gid of this EventProcessResponseInfo.

        父进程组ID

        :param parent_process_gid: The parent_process_gid of this EventProcessResponseInfo.
        :type parent_process_gid: int
        """
        self._parent_process_gid = parent_process_gid

    @property
    def parent_process_egid(self):
        """Gets the parent_process_egid of this EventProcessResponseInfo.

        父进程有效组ID

        :return: The parent_process_egid of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._parent_process_egid

    @parent_process_egid.setter
    def parent_process_egid(self, parent_process_egid):
        """Sets the parent_process_egid of this EventProcessResponseInfo.

        父进程有效组ID

        :param parent_process_egid: The parent_process_egid of this EventProcessResponseInfo.
        :type parent_process_egid: int
        """
        self._parent_process_egid = parent_process_egid

    @property
    def parent_process_euid(self):
        """Gets the parent_process_euid of this EventProcessResponseInfo.

        父进程有效用户ID

        :return: The parent_process_euid of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._parent_process_euid

    @parent_process_euid.setter
    def parent_process_euid(self, parent_process_euid):
        """Sets the parent_process_euid of this EventProcessResponseInfo.

        父进程有效用户ID

        :param parent_process_euid: The parent_process_euid of this EventProcessResponseInfo.
        :type parent_process_euid: int
        """
        self._parent_process_euid = parent_process_euid

    @property
    def child_process_name(self):
        """Gets the child_process_name of this EventProcessResponseInfo.

        子进程名称

        :return: The child_process_name of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._child_process_name

    @child_process_name.setter
    def child_process_name(self, child_process_name):
        """Sets the child_process_name of this EventProcessResponseInfo.

        子进程名称

        :param child_process_name: The child_process_name of this EventProcessResponseInfo.
        :type child_process_name: str
        """
        self._child_process_name = child_process_name

    @property
    def child_process_path(self):
        """Gets the child_process_path of this EventProcessResponseInfo.

        子进程文件路径

        :return: The child_process_path of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._child_process_path

    @child_process_path.setter
    def child_process_path(self, child_process_path):
        """Sets the child_process_path of this EventProcessResponseInfo.

        子进程文件路径

        :param child_process_path: The child_process_path of this EventProcessResponseInfo.
        :type child_process_path: str
        """
        self._child_process_path = child_process_path

    @property
    def child_process_pid(self):
        """Gets the child_process_pid of this EventProcessResponseInfo.

        子进程id

        :return: The child_process_pid of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._child_process_pid

    @child_process_pid.setter
    def child_process_pid(self, child_process_pid):
        """Sets the child_process_pid of this EventProcessResponseInfo.

        子进程id

        :param child_process_pid: The child_process_pid of this EventProcessResponseInfo.
        :type child_process_pid: int
        """
        self._child_process_pid = child_process_pid

    @property
    def child_process_uid(self):
        """Gets the child_process_uid of this EventProcessResponseInfo.

        子进程用户id

        :return: The child_process_uid of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._child_process_uid

    @child_process_uid.setter
    def child_process_uid(self, child_process_uid):
        """Sets the child_process_uid of this EventProcessResponseInfo.

        子进程用户id

        :param child_process_uid: The child_process_uid of this EventProcessResponseInfo.
        :type child_process_uid: int
        """
        self._child_process_uid = child_process_uid

    @property
    def child_process_cmdline(self):
        """Gets the child_process_cmdline of this EventProcessResponseInfo.

        子进程文件命令行

        :return: The child_process_cmdline of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._child_process_cmdline

    @child_process_cmdline.setter
    def child_process_cmdline(self, child_process_cmdline):
        """Sets the child_process_cmdline of this EventProcessResponseInfo.

        子进程文件命令行

        :param child_process_cmdline: The child_process_cmdline of this EventProcessResponseInfo.
        :type child_process_cmdline: str
        """
        self._child_process_cmdline = child_process_cmdline

    @property
    def child_process_filename(self):
        """Gets the child_process_filename of this EventProcessResponseInfo.

        子进程文件名

        :return: The child_process_filename of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._child_process_filename

    @child_process_filename.setter
    def child_process_filename(self, child_process_filename):
        """Sets the child_process_filename of this EventProcessResponseInfo.

        子进程文件名

        :param child_process_filename: The child_process_filename of this EventProcessResponseInfo.
        :type child_process_filename: str
        """
        self._child_process_filename = child_process_filename

    @property
    def child_process_start_time(self):
        """Gets the child_process_start_time of this EventProcessResponseInfo.

        子进程启动时间

        :return: The child_process_start_time of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._child_process_start_time

    @child_process_start_time.setter
    def child_process_start_time(self, child_process_start_time):
        """Sets the child_process_start_time of this EventProcessResponseInfo.

        子进程启动时间

        :param child_process_start_time: The child_process_start_time of this EventProcessResponseInfo.
        :type child_process_start_time: int
        """
        self._child_process_start_time = child_process_start_time

    @property
    def child_process_gid(self):
        """Gets the child_process_gid of this EventProcessResponseInfo.

        子进程组ID

        :return: The child_process_gid of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._child_process_gid

    @child_process_gid.setter
    def child_process_gid(self, child_process_gid):
        """Sets the child_process_gid of this EventProcessResponseInfo.

        子进程组ID

        :param child_process_gid: The child_process_gid of this EventProcessResponseInfo.
        :type child_process_gid: int
        """
        self._child_process_gid = child_process_gid

    @property
    def child_process_egid(self):
        """Gets the child_process_egid of this EventProcessResponseInfo.

        子进程有效组ID

        :return: The child_process_egid of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._child_process_egid

    @child_process_egid.setter
    def child_process_egid(self, child_process_egid):
        """Sets the child_process_egid of this EventProcessResponseInfo.

        子进程有效组ID

        :param child_process_egid: The child_process_egid of this EventProcessResponseInfo.
        :type child_process_egid: int
        """
        self._child_process_egid = child_process_egid

    @property
    def child_process_euid(self):
        """Gets the child_process_euid of this EventProcessResponseInfo.

        子进程有效用户ID

        :return: The child_process_euid of this EventProcessResponseInfo.
        :rtype: int
        """
        return self._child_process_euid

    @child_process_euid.setter
    def child_process_euid(self, child_process_euid):
        """Sets the child_process_euid of this EventProcessResponseInfo.

        子进程有效用户ID

        :param child_process_euid: The child_process_euid of this EventProcessResponseInfo.
        :type child_process_euid: int
        """
        self._child_process_euid = child_process_euid

    @property
    def virt_cmd(self):
        """Gets the virt_cmd of this EventProcessResponseInfo.

        虚拟化命令

        :return: The virt_cmd of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._virt_cmd

    @virt_cmd.setter
    def virt_cmd(self, virt_cmd):
        """Sets the virt_cmd of this EventProcessResponseInfo.

        虚拟化命令

        :param virt_cmd: The virt_cmd of this EventProcessResponseInfo.
        :type virt_cmd: str
        """
        self._virt_cmd = virt_cmd

    @property
    def virt_process_name(self):
        """Gets the virt_process_name of this EventProcessResponseInfo.

        虚拟化进程名称

        :return: The virt_process_name of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._virt_process_name

    @virt_process_name.setter
    def virt_process_name(self, virt_process_name):
        """Sets the virt_process_name of this EventProcessResponseInfo.

        虚拟化进程名称

        :param virt_process_name: The virt_process_name of this EventProcessResponseInfo.
        :type virt_process_name: str
        """
        self._virt_process_name = virt_process_name

    @property
    def escape_mode(self):
        """Gets the escape_mode of this EventProcessResponseInfo.

        逃逸方式

        :return: The escape_mode of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._escape_mode

    @escape_mode.setter
    def escape_mode(self, escape_mode):
        """Sets the escape_mode of this EventProcessResponseInfo.

        逃逸方式

        :param escape_mode: The escape_mode of this EventProcessResponseInfo.
        :type escape_mode: str
        """
        self._escape_mode = escape_mode

    @property
    def escape_cmd(self):
        """Gets the escape_cmd of this EventProcessResponseInfo.

        逃逸后后执行的命令

        :return: The escape_cmd of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._escape_cmd

    @escape_cmd.setter
    def escape_cmd(self, escape_cmd):
        """Sets the escape_cmd of this EventProcessResponseInfo.

        逃逸后后执行的命令

        :param escape_cmd: The escape_cmd of this EventProcessResponseInfo.
        :type escape_cmd: str
        """
        self._escape_cmd = escape_cmd

    @property
    def process_hash(self):
        """Gets the process_hash of this EventProcessResponseInfo.

        进程启动文件hash

        :return: The process_hash of this EventProcessResponseInfo.
        :rtype: str
        """
        return self._process_hash

    @process_hash.setter
    def process_hash(self, process_hash):
        """Sets the process_hash of this EventProcessResponseInfo.

        进程启动文件hash

        :param process_hash: The process_hash of this EventProcessResponseInfo.
        :type process_hash: str
        """
        self._process_hash = process_hash

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
        if not isinstance(other, EventProcessResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
