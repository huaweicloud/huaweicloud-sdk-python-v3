# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebTamperEventResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_path': 'str',
        'event_description': 'str',
        'process_path': 'str',
        'process_cmd': 'str',
        'process_pid': 'int',
        'process_env': 'str',
        'web_app_name': 'str',
        'event_time': 'int',
        'host_info': 'WebTamperEventHostInfo',
        'container_info': 'WebTamperEventContainerInfo'
    }

    attribute_map = {
        'file_path': 'file_path',
        'event_description': 'event_description',
        'process_path': 'process_path',
        'process_cmd': 'process_cmd',
        'process_pid': 'process_pid',
        'process_env': 'process_env',
        'web_app_name': 'web_app_name',
        'event_time': 'event_time',
        'host_info': 'host_info',
        'container_info': 'container_info'
    }

    def __init__(self, file_path=None, event_description=None, process_path=None, process_cmd=None, process_pid=None, process_env=None, web_app_name=None, event_time=None, host_info=None, container_info=None):
        r"""WebTamperEventResponseInfo

        The model defined in huaweicloud sdk

        :param file_path: **参数解释**: 防护文件 **取值范围**: 字符长度0-256位 
        :type file_path: str
        :param event_description: **参数解释**: 事件描述 **取值范围**: 字符长度0-512位 
        :type event_description: str
        :param process_path: **参数解释**: 进程路径 **取值范围**: 字符长度0-256位 
        :type process_path: str
        :param process_cmd: **参数解释**: 进程命令行 **取值范围**: 字符长度0-256位 
        :type process_cmd: str
        :param process_pid: **参数解释**: 进程pid **取值范围**: 最小值0，最大值2147483647 
        :type process_pid: int
        :param process_env: **参数解释**: 进程环境，是指在容器内的进程或者宿主机的进程 **取值范围**: 字符长度0-32位 
        :type process_env: str
        :param web_app_name: **参数解释**: 网站应用名称 **取值范围**: 字符长度0-128位 
        :type web_app_name: str
        :param event_time: **参数解释**: 检测时间(ms) **取值范围**: 最小值0，最大值9223372036854775807 
        :type event_time: int
        :param host_info: 
        :type host_info: :class:`huaweicloudsdkhss.v5.WebTamperEventHostInfo`
        :param container_info: 
        :type container_info: :class:`huaweicloudsdkhss.v5.WebTamperEventContainerInfo`
        """
        
        

        self._file_path = None
        self._event_description = None
        self._process_path = None
        self._process_cmd = None
        self._process_pid = None
        self._process_env = None
        self._web_app_name = None
        self._event_time = None
        self._host_info = None
        self._container_info = None
        self.discriminator = None

        if file_path is not None:
            self.file_path = file_path
        if event_description is not None:
            self.event_description = event_description
        if process_path is not None:
            self.process_path = process_path
        if process_cmd is not None:
            self.process_cmd = process_cmd
        if process_pid is not None:
            self.process_pid = process_pid
        if process_env is not None:
            self.process_env = process_env
        if web_app_name is not None:
            self.web_app_name = web_app_name
        if event_time is not None:
            self.event_time = event_time
        if host_info is not None:
            self.host_info = host_info
        if container_info is not None:
            self.container_info = container_info

    @property
    def file_path(self):
        r"""Gets the file_path of this WebTamperEventResponseInfo.

        **参数解释**: 防护文件 **取值范围**: 字符长度0-256位 

        :return: The file_path of this WebTamperEventResponseInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this WebTamperEventResponseInfo.

        **参数解释**: 防护文件 **取值范围**: 字符长度0-256位 

        :param file_path: The file_path of this WebTamperEventResponseInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def event_description(self):
        r"""Gets the event_description of this WebTamperEventResponseInfo.

        **参数解释**: 事件描述 **取值范围**: 字符长度0-512位 

        :return: The event_description of this WebTamperEventResponseInfo.
        :rtype: str
        """
        return self._event_description

    @event_description.setter
    def event_description(self, event_description):
        r"""Sets the event_description of this WebTamperEventResponseInfo.

        **参数解释**: 事件描述 **取值范围**: 字符长度0-512位 

        :param event_description: The event_description of this WebTamperEventResponseInfo.
        :type event_description: str
        """
        self._event_description = event_description

    @property
    def process_path(self):
        r"""Gets the process_path of this WebTamperEventResponseInfo.

        **参数解释**: 进程路径 **取值范围**: 字符长度0-256位 

        :return: The process_path of this WebTamperEventResponseInfo.
        :rtype: str
        """
        return self._process_path

    @process_path.setter
    def process_path(self, process_path):
        r"""Sets the process_path of this WebTamperEventResponseInfo.

        **参数解释**: 进程路径 **取值范围**: 字符长度0-256位 

        :param process_path: The process_path of this WebTamperEventResponseInfo.
        :type process_path: str
        """
        self._process_path = process_path

    @property
    def process_cmd(self):
        r"""Gets the process_cmd of this WebTamperEventResponseInfo.

        **参数解释**: 进程命令行 **取值范围**: 字符长度0-256位 

        :return: The process_cmd of this WebTamperEventResponseInfo.
        :rtype: str
        """
        return self._process_cmd

    @process_cmd.setter
    def process_cmd(self, process_cmd):
        r"""Sets the process_cmd of this WebTamperEventResponseInfo.

        **参数解释**: 进程命令行 **取值范围**: 字符长度0-256位 

        :param process_cmd: The process_cmd of this WebTamperEventResponseInfo.
        :type process_cmd: str
        """
        self._process_cmd = process_cmd

    @property
    def process_pid(self):
        r"""Gets the process_pid of this WebTamperEventResponseInfo.

        **参数解释**: 进程pid **取值范围**: 最小值0，最大值2147483647 

        :return: The process_pid of this WebTamperEventResponseInfo.
        :rtype: int
        """
        return self._process_pid

    @process_pid.setter
    def process_pid(self, process_pid):
        r"""Sets the process_pid of this WebTamperEventResponseInfo.

        **参数解释**: 进程pid **取值范围**: 最小值0，最大值2147483647 

        :param process_pid: The process_pid of this WebTamperEventResponseInfo.
        :type process_pid: int
        """
        self._process_pid = process_pid

    @property
    def process_env(self):
        r"""Gets the process_env of this WebTamperEventResponseInfo.

        **参数解释**: 进程环境，是指在容器内的进程或者宿主机的进程 **取值范围**: 字符长度0-32位 

        :return: The process_env of this WebTamperEventResponseInfo.
        :rtype: str
        """
        return self._process_env

    @process_env.setter
    def process_env(self, process_env):
        r"""Sets the process_env of this WebTamperEventResponseInfo.

        **参数解释**: 进程环境，是指在容器内的进程或者宿主机的进程 **取值范围**: 字符长度0-32位 

        :param process_env: The process_env of this WebTamperEventResponseInfo.
        :type process_env: str
        """
        self._process_env = process_env

    @property
    def web_app_name(self):
        r"""Gets the web_app_name of this WebTamperEventResponseInfo.

        **参数解释**: 网站应用名称 **取值范围**: 字符长度0-128位 

        :return: The web_app_name of this WebTamperEventResponseInfo.
        :rtype: str
        """
        return self._web_app_name

    @web_app_name.setter
    def web_app_name(self, web_app_name):
        r"""Sets the web_app_name of this WebTamperEventResponseInfo.

        **参数解释**: 网站应用名称 **取值范围**: 字符长度0-128位 

        :param web_app_name: The web_app_name of this WebTamperEventResponseInfo.
        :type web_app_name: str
        """
        self._web_app_name = web_app_name

    @property
    def event_time(self):
        r"""Gets the event_time of this WebTamperEventResponseInfo.

        **参数解释**: 检测时间(ms) **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The event_time of this WebTamperEventResponseInfo.
        :rtype: int
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        r"""Sets the event_time of this WebTamperEventResponseInfo.

        **参数解释**: 检测时间(ms) **取值范围**: 最小值0，最大值9223372036854775807 

        :param event_time: The event_time of this WebTamperEventResponseInfo.
        :type event_time: int
        """
        self._event_time = event_time

    @property
    def host_info(self):
        r"""Gets the host_info of this WebTamperEventResponseInfo.

        :return: The host_info of this WebTamperEventResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.WebTamperEventHostInfo`
        """
        return self._host_info

    @host_info.setter
    def host_info(self, host_info):
        r"""Sets the host_info of this WebTamperEventResponseInfo.

        :param host_info: The host_info of this WebTamperEventResponseInfo.
        :type host_info: :class:`huaweicloudsdkhss.v5.WebTamperEventHostInfo`
        """
        self._host_info = host_info

    @property
    def container_info(self):
        r"""Gets the container_info of this WebTamperEventResponseInfo.

        :return: The container_info of this WebTamperEventResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.WebTamperEventContainerInfo`
        """
        return self._container_info

    @container_info.setter
    def container_info(self, container_info):
        r"""Sets the container_info of this WebTamperEventResponseInfo.

        :param container_info: The container_info of this WebTamperEventResponseInfo.
        :type container_info: :class:`huaweicloudsdkhss.v5.WebTamperEventContainerInfo`
        """
        self._container_info = container_info

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
        if not isinstance(other, WebTamperEventResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
