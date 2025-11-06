# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessForensicInfo:

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
        'process_gid': 'int',
        'process_egid': 'int',
        'process_euid': 'int',
        'process_username': 'str',
        'process_cmdline': 'str',
        'process_start_time': 'int',
        'process_file_hash': 'str',
        'ancestor_process_pid': 'int',
        'ancestor_process_cmdline': 'str',
        'ancestor_process_path': 'str',
        'session_id': 'int',
        'event_num': 'int',
        'type': 'str'
    }

    attribute_map = {
        'process_name': 'process_name',
        'process_path': 'process_path',
        'process_pid': 'process_pid',
        'process_uid': 'process_uid',
        'process_gid': 'process_gid',
        'process_egid': 'process_egid',
        'process_euid': 'process_euid',
        'process_username': 'process_username',
        'process_cmdline': 'process_cmdline',
        'process_start_time': 'process_start_time',
        'process_file_hash': 'process_file_hash',
        'ancestor_process_pid': 'ancestor_process_pid',
        'ancestor_process_cmdline': 'ancestor_process_cmdline',
        'ancestor_process_path': 'ancestor_process_path',
        'session_id': 'session_id',
        'event_num': 'event_num',
        'type': 'type'
    }

    def __init__(self, process_name=None, process_path=None, process_pid=None, process_uid=None, process_gid=None, process_egid=None, process_euid=None, process_username=None, process_cmdline=None, process_start_time=None, process_file_hash=None, ancestor_process_pid=None, ancestor_process_cmdline=None, ancestor_process_path=None, session_id=None, event_num=None, type=None):
        r"""ProcessForensicInfo

        The model defined in huaweicloud sdk

        :param process_name: **参数解释**： 进程名称 **取值范围**： 不涉及
        :type process_name: str
        :param process_path: **参数解释**： 进程文件路径 **取值范围**： 不涉及
        :type process_path: str
        :param process_pid: **参数解释**： 进程id **取值范围**： 不涉及
        :type process_pid: int
        :param process_uid: **参数解释**： 进程用户id **取值范围**： 不涉及
        :type process_uid: int
        :param process_gid: **参数解释**： 进程组id **取值范围**： 不涉及
        :type process_gid: int
        :param process_egid: **参数解释**： 进程有效组id **取值范围**： 不涉及
        :type process_egid: int
        :param process_euid: **参数解释**： 进程有效用户id **取值范围**： 不涉及
        :type process_euid: int
        :param process_username: **参数解释**： 运行进程的用户名 **取值范围**： 不涉及
        :type process_username: str
        :param process_cmdline: **参数解释**： 进程文件命令行 **取值范围**： 不涉及
        :type process_cmdline: str
        :param process_start_time: **参数解释**： 进程启动时间 **取值范围**： 不涉及
        :type process_start_time: int
        :param process_file_hash: **参数解释**： 进程文件hash **取值范围**： 不涉及
        :type process_file_hash: str
        :param ancestor_process_pid: **参数解释**： 祖父进程id **取值范围**： 不涉及
        :type ancestor_process_pid: int
        :param ancestor_process_cmdline: **参数解释**： 祖父进程命令行 **取值范围**： 不涉及
        :type ancestor_process_cmdline: str
        :param ancestor_process_path: **参数解释**： 祖父进程路径 **取值范围**： 不涉及
        :type ancestor_process_path: str
        :param session_id: **参数解释**： 会话id **取值范围**： 不涉及
        :type session_id: int
        :param event_num: **参数解释**： 威胁事件数 **取值范围**： 不涉及
        :type event_num: int
        :param type: **参数解释**： 节点类型 **取值范围**： - 0：进程 - 1：注册表 - 2：文件
        :type type: str
        """
        
        

        self._process_name = None
        self._process_path = None
        self._process_pid = None
        self._process_uid = None
        self._process_gid = None
        self._process_egid = None
        self._process_euid = None
        self._process_username = None
        self._process_cmdline = None
        self._process_start_time = None
        self._process_file_hash = None
        self._ancestor_process_pid = None
        self._ancestor_process_cmdline = None
        self._ancestor_process_path = None
        self._session_id = None
        self._event_num = None
        self._type = None
        self.discriminator = None

        if process_name is not None:
            self.process_name = process_name
        if process_path is not None:
            self.process_path = process_path
        if process_pid is not None:
            self.process_pid = process_pid
        if process_uid is not None:
            self.process_uid = process_uid
        if process_gid is not None:
            self.process_gid = process_gid
        if process_egid is not None:
            self.process_egid = process_egid
        if process_euid is not None:
            self.process_euid = process_euid
        if process_username is not None:
            self.process_username = process_username
        if process_cmdline is not None:
            self.process_cmdline = process_cmdline
        if process_start_time is not None:
            self.process_start_time = process_start_time
        if process_file_hash is not None:
            self.process_file_hash = process_file_hash
        if ancestor_process_pid is not None:
            self.ancestor_process_pid = ancestor_process_pid
        if ancestor_process_cmdline is not None:
            self.ancestor_process_cmdline = ancestor_process_cmdline
        if ancestor_process_path is not None:
            self.ancestor_process_path = ancestor_process_path
        if session_id is not None:
            self.session_id = session_id
        if event_num is not None:
            self.event_num = event_num
        if type is not None:
            self.type = type

    @property
    def process_name(self):
        r"""Gets the process_name of this ProcessForensicInfo.

        **参数解释**： 进程名称 **取值范围**： 不涉及

        :return: The process_name of this ProcessForensicInfo.
        :rtype: str
        """
        return self._process_name

    @process_name.setter
    def process_name(self, process_name):
        r"""Sets the process_name of this ProcessForensicInfo.

        **参数解释**： 进程名称 **取值范围**： 不涉及

        :param process_name: The process_name of this ProcessForensicInfo.
        :type process_name: str
        """
        self._process_name = process_name

    @property
    def process_path(self):
        r"""Gets the process_path of this ProcessForensicInfo.

        **参数解释**： 进程文件路径 **取值范围**： 不涉及

        :return: The process_path of this ProcessForensicInfo.
        :rtype: str
        """
        return self._process_path

    @process_path.setter
    def process_path(self, process_path):
        r"""Sets the process_path of this ProcessForensicInfo.

        **参数解释**： 进程文件路径 **取值范围**： 不涉及

        :param process_path: The process_path of this ProcessForensicInfo.
        :type process_path: str
        """
        self._process_path = process_path

    @property
    def process_pid(self):
        r"""Gets the process_pid of this ProcessForensicInfo.

        **参数解释**： 进程id **取值范围**： 不涉及

        :return: The process_pid of this ProcessForensicInfo.
        :rtype: int
        """
        return self._process_pid

    @process_pid.setter
    def process_pid(self, process_pid):
        r"""Sets the process_pid of this ProcessForensicInfo.

        **参数解释**： 进程id **取值范围**： 不涉及

        :param process_pid: The process_pid of this ProcessForensicInfo.
        :type process_pid: int
        """
        self._process_pid = process_pid

    @property
    def process_uid(self):
        r"""Gets the process_uid of this ProcessForensicInfo.

        **参数解释**： 进程用户id **取值范围**： 不涉及

        :return: The process_uid of this ProcessForensicInfo.
        :rtype: int
        """
        return self._process_uid

    @process_uid.setter
    def process_uid(self, process_uid):
        r"""Sets the process_uid of this ProcessForensicInfo.

        **参数解释**： 进程用户id **取值范围**： 不涉及

        :param process_uid: The process_uid of this ProcessForensicInfo.
        :type process_uid: int
        """
        self._process_uid = process_uid

    @property
    def process_gid(self):
        r"""Gets the process_gid of this ProcessForensicInfo.

        **参数解释**： 进程组id **取值范围**： 不涉及

        :return: The process_gid of this ProcessForensicInfo.
        :rtype: int
        """
        return self._process_gid

    @process_gid.setter
    def process_gid(self, process_gid):
        r"""Sets the process_gid of this ProcessForensicInfo.

        **参数解释**： 进程组id **取值范围**： 不涉及

        :param process_gid: The process_gid of this ProcessForensicInfo.
        :type process_gid: int
        """
        self._process_gid = process_gid

    @property
    def process_egid(self):
        r"""Gets the process_egid of this ProcessForensicInfo.

        **参数解释**： 进程有效组id **取值范围**： 不涉及

        :return: The process_egid of this ProcessForensicInfo.
        :rtype: int
        """
        return self._process_egid

    @process_egid.setter
    def process_egid(self, process_egid):
        r"""Sets the process_egid of this ProcessForensicInfo.

        **参数解释**： 进程有效组id **取值范围**： 不涉及

        :param process_egid: The process_egid of this ProcessForensicInfo.
        :type process_egid: int
        """
        self._process_egid = process_egid

    @property
    def process_euid(self):
        r"""Gets the process_euid of this ProcessForensicInfo.

        **参数解释**： 进程有效用户id **取值范围**： 不涉及

        :return: The process_euid of this ProcessForensicInfo.
        :rtype: int
        """
        return self._process_euid

    @process_euid.setter
    def process_euid(self, process_euid):
        r"""Sets the process_euid of this ProcessForensicInfo.

        **参数解释**： 进程有效用户id **取值范围**： 不涉及

        :param process_euid: The process_euid of this ProcessForensicInfo.
        :type process_euid: int
        """
        self._process_euid = process_euid

    @property
    def process_username(self):
        r"""Gets the process_username of this ProcessForensicInfo.

        **参数解释**： 运行进程的用户名 **取值范围**： 不涉及

        :return: The process_username of this ProcessForensicInfo.
        :rtype: str
        """
        return self._process_username

    @process_username.setter
    def process_username(self, process_username):
        r"""Sets the process_username of this ProcessForensicInfo.

        **参数解释**： 运行进程的用户名 **取值范围**： 不涉及

        :param process_username: The process_username of this ProcessForensicInfo.
        :type process_username: str
        """
        self._process_username = process_username

    @property
    def process_cmdline(self):
        r"""Gets the process_cmdline of this ProcessForensicInfo.

        **参数解释**： 进程文件命令行 **取值范围**： 不涉及

        :return: The process_cmdline of this ProcessForensicInfo.
        :rtype: str
        """
        return self._process_cmdline

    @process_cmdline.setter
    def process_cmdline(self, process_cmdline):
        r"""Sets the process_cmdline of this ProcessForensicInfo.

        **参数解释**： 进程文件命令行 **取值范围**： 不涉及

        :param process_cmdline: The process_cmdline of this ProcessForensicInfo.
        :type process_cmdline: str
        """
        self._process_cmdline = process_cmdline

    @property
    def process_start_time(self):
        r"""Gets the process_start_time of this ProcessForensicInfo.

        **参数解释**： 进程启动时间 **取值范围**： 不涉及

        :return: The process_start_time of this ProcessForensicInfo.
        :rtype: int
        """
        return self._process_start_time

    @process_start_time.setter
    def process_start_time(self, process_start_time):
        r"""Sets the process_start_time of this ProcessForensicInfo.

        **参数解释**： 进程启动时间 **取值范围**： 不涉及

        :param process_start_time: The process_start_time of this ProcessForensicInfo.
        :type process_start_time: int
        """
        self._process_start_time = process_start_time

    @property
    def process_file_hash(self):
        r"""Gets the process_file_hash of this ProcessForensicInfo.

        **参数解释**： 进程文件hash **取值范围**： 不涉及

        :return: The process_file_hash of this ProcessForensicInfo.
        :rtype: str
        """
        return self._process_file_hash

    @process_file_hash.setter
    def process_file_hash(self, process_file_hash):
        r"""Sets the process_file_hash of this ProcessForensicInfo.

        **参数解释**： 进程文件hash **取值范围**： 不涉及

        :param process_file_hash: The process_file_hash of this ProcessForensicInfo.
        :type process_file_hash: str
        """
        self._process_file_hash = process_file_hash

    @property
    def ancestor_process_pid(self):
        r"""Gets the ancestor_process_pid of this ProcessForensicInfo.

        **参数解释**： 祖父进程id **取值范围**： 不涉及

        :return: The ancestor_process_pid of this ProcessForensicInfo.
        :rtype: int
        """
        return self._ancestor_process_pid

    @ancestor_process_pid.setter
    def ancestor_process_pid(self, ancestor_process_pid):
        r"""Sets the ancestor_process_pid of this ProcessForensicInfo.

        **参数解释**： 祖父进程id **取值范围**： 不涉及

        :param ancestor_process_pid: The ancestor_process_pid of this ProcessForensicInfo.
        :type ancestor_process_pid: int
        """
        self._ancestor_process_pid = ancestor_process_pid

    @property
    def ancestor_process_cmdline(self):
        r"""Gets the ancestor_process_cmdline of this ProcessForensicInfo.

        **参数解释**： 祖父进程命令行 **取值范围**： 不涉及

        :return: The ancestor_process_cmdline of this ProcessForensicInfo.
        :rtype: str
        """
        return self._ancestor_process_cmdline

    @ancestor_process_cmdline.setter
    def ancestor_process_cmdline(self, ancestor_process_cmdline):
        r"""Sets the ancestor_process_cmdline of this ProcessForensicInfo.

        **参数解释**： 祖父进程命令行 **取值范围**： 不涉及

        :param ancestor_process_cmdline: The ancestor_process_cmdline of this ProcessForensicInfo.
        :type ancestor_process_cmdline: str
        """
        self._ancestor_process_cmdline = ancestor_process_cmdline

    @property
    def ancestor_process_path(self):
        r"""Gets the ancestor_process_path of this ProcessForensicInfo.

        **参数解释**： 祖父进程路径 **取值范围**： 不涉及

        :return: The ancestor_process_path of this ProcessForensicInfo.
        :rtype: str
        """
        return self._ancestor_process_path

    @ancestor_process_path.setter
    def ancestor_process_path(self, ancestor_process_path):
        r"""Sets the ancestor_process_path of this ProcessForensicInfo.

        **参数解释**： 祖父进程路径 **取值范围**： 不涉及

        :param ancestor_process_path: The ancestor_process_path of this ProcessForensicInfo.
        :type ancestor_process_path: str
        """
        self._ancestor_process_path = ancestor_process_path

    @property
    def session_id(self):
        r"""Gets the session_id of this ProcessForensicInfo.

        **参数解释**： 会话id **取值范围**： 不涉及

        :return: The session_id of this ProcessForensicInfo.
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this ProcessForensicInfo.

        **参数解释**： 会话id **取值范围**： 不涉及

        :param session_id: The session_id of this ProcessForensicInfo.
        :type session_id: int
        """
        self._session_id = session_id

    @property
    def event_num(self):
        r"""Gets the event_num of this ProcessForensicInfo.

        **参数解释**： 威胁事件数 **取值范围**： 不涉及

        :return: The event_num of this ProcessForensicInfo.
        :rtype: int
        """
        return self._event_num

    @event_num.setter
    def event_num(self, event_num):
        r"""Sets the event_num of this ProcessForensicInfo.

        **参数解释**： 威胁事件数 **取值范围**： 不涉及

        :param event_num: The event_num of this ProcessForensicInfo.
        :type event_num: int
        """
        self._event_num = event_num

    @property
    def type(self):
        r"""Gets the type of this ProcessForensicInfo.

        **参数解释**： 节点类型 **取值范围**： - 0：进程 - 1：注册表 - 2：文件

        :return: The type of this ProcessForensicInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ProcessForensicInfo.

        **参数解释**： 节点类型 **取值范围**： - 0：进程 - 1：注册表 - 2：文件

        :param type: The type of this ProcessForensicInfo.
        :type type: str
        """
        self._type = type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProcessForensicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
