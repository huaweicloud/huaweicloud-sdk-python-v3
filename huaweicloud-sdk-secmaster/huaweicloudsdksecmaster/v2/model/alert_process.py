# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertProcess:

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
        'process_cmdline': 'str',
        'process_parent_name': 'str',
        'process_parent_path': 'str',
        'process_parent_pid': 'int',
        'process_parent_uid': 'int',
        'process_parent_cmdline': 'str',
        'process_child_name': 'str',
        'process_child_path': 'str',
        'process_child_pid': 'int',
        'process_child_uid': 'int',
        'process_child_cmdline': 'str',
        'process_launche_time': 'str',
        'process_terminate_time': 'str'
    }

    attribute_map = {
        'process_name': 'process_name',
        'process_path': 'process_path',
        'process_pid': 'process_pid',
        'process_uid': 'process_uid',
        'process_cmdline': 'process_cmdline',
        'process_parent_name': 'process_parent_name',
        'process_parent_path': 'process_parent_path',
        'process_parent_pid': 'process_parent_pid',
        'process_parent_uid': 'process_parent_uid',
        'process_parent_cmdline': 'process_parent_cmdline',
        'process_child_name': 'process_child_name',
        'process_child_path': 'process_child_path',
        'process_child_pid': 'process_child_pid',
        'process_child_uid': 'process_child_uid',
        'process_child_cmdline': 'process_child_cmdline',
        'process_launche_time': 'process_launche_time',
        'process_terminate_time': 'process_terminate_time'
    }

    def __init__(self, process_name=None, process_path=None, process_pid=None, process_uid=None, process_cmdline=None, process_parent_name=None, process_parent_path=None, process_parent_pid=None, process_parent_uid=None, process_parent_cmdline=None, process_child_name=None, process_child_path=None, process_child_pid=None, process_child_uid=None, process_child_cmdline=None, process_launche_time=None, process_terminate_time=None):
        """AlertProcess

        The model defined in huaweicloud sdk

        :param process_name: 进程名
        :type process_name: str
        :param process_path: 进程执行文件路径
        :type process_path: str
        :param process_pid: 进程id
        :type process_pid: int
        :param process_uid: 进程用户id
        :type process_uid: int
        :param process_cmdline: 进程命令行
        :type process_cmdline: str
        :param process_parent_name: 父进程名称
        :type process_parent_name: str
        :param process_parent_path: 父进程执行文件路径
        :type process_parent_path: str
        :param process_parent_pid: 父进程id
        :type process_parent_pid: int
        :param process_parent_uid: 父进程用户id
        :type process_parent_uid: int
        :param process_parent_cmdline: 父进程命令行
        :type process_parent_cmdline: str
        :param process_child_name: 子进程名称
        :type process_child_name: str
        :param process_child_path: 子进程执行文件路径
        :type process_child_path: str
        :param process_child_pid: 子进程id
        :type process_child_pid: int
        :param process_child_uid: 子进程用户id
        :type process_child_uid: int
        :param process_child_cmdline: 子进程命令行
        :type process_child_cmdline: str
        :param process_launche_time: 进程启动时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区
        :type process_launche_time: str
        :param process_terminate_time: 进程结束时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区
        :type process_terminate_time: str
        """
        
        

        self._process_name = None
        self._process_path = None
        self._process_pid = None
        self._process_uid = None
        self._process_cmdline = None
        self._process_parent_name = None
        self._process_parent_path = None
        self._process_parent_pid = None
        self._process_parent_uid = None
        self._process_parent_cmdline = None
        self._process_child_name = None
        self._process_child_path = None
        self._process_child_pid = None
        self._process_child_uid = None
        self._process_child_cmdline = None
        self._process_launche_time = None
        self._process_terminate_time = None
        self.discriminator = None

        if process_name is not None:
            self.process_name = process_name
        if process_path is not None:
            self.process_path = process_path
        if process_pid is not None:
            self.process_pid = process_pid
        if process_uid is not None:
            self.process_uid = process_uid
        if process_cmdline is not None:
            self.process_cmdline = process_cmdline
        if process_parent_name is not None:
            self.process_parent_name = process_parent_name
        if process_parent_path is not None:
            self.process_parent_path = process_parent_path
        if process_parent_pid is not None:
            self.process_parent_pid = process_parent_pid
        if process_parent_uid is not None:
            self.process_parent_uid = process_parent_uid
        if process_parent_cmdline is not None:
            self.process_parent_cmdline = process_parent_cmdline
        if process_child_name is not None:
            self.process_child_name = process_child_name
        if process_child_path is not None:
            self.process_child_path = process_child_path
        if process_child_pid is not None:
            self.process_child_pid = process_child_pid
        if process_child_uid is not None:
            self.process_child_uid = process_child_uid
        if process_child_cmdline is not None:
            self.process_child_cmdline = process_child_cmdline
        if process_launche_time is not None:
            self.process_launche_time = process_launche_time
        if process_terminate_time is not None:
            self.process_terminate_time = process_terminate_time

    @property
    def process_name(self):
        """Gets the process_name of this AlertProcess.

        进程名

        :return: The process_name of this AlertProcess.
        :rtype: str
        """
        return self._process_name

    @process_name.setter
    def process_name(self, process_name):
        """Sets the process_name of this AlertProcess.

        进程名

        :param process_name: The process_name of this AlertProcess.
        :type process_name: str
        """
        self._process_name = process_name

    @property
    def process_path(self):
        """Gets the process_path of this AlertProcess.

        进程执行文件路径

        :return: The process_path of this AlertProcess.
        :rtype: str
        """
        return self._process_path

    @process_path.setter
    def process_path(self, process_path):
        """Sets the process_path of this AlertProcess.

        进程执行文件路径

        :param process_path: The process_path of this AlertProcess.
        :type process_path: str
        """
        self._process_path = process_path

    @property
    def process_pid(self):
        """Gets the process_pid of this AlertProcess.

        进程id

        :return: The process_pid of this AlertProcess.
        :rtype: int
        """
        return self._process_pid

    @process_pid.setter
    def process_pid(self, process_pid):
        """Sets the process_pid of this AlertProcess.

        进程id

        :param process_pid: The process_pid of this AlertProcess.
        :type process_pid: int
        """
        self._process_pid = process_pid

    @property
    def process_uid(self):
        """Gets the process_uid of this AlertProcess.

        进程用户id

        :return: The process_uid of this AlertProcess.
        :rtype: int
        """
        return self._process_uid

    @process_uid.setter
    def process_uid(self, process_uid):
        """Sets the process_uid of this AlertProcess.

        进程用户id

        :param process_uid: The process_uid of this AlertProcess.
        :type process_uid: int
        """
        self._process_uid = process_uid

    @property
    def process_cmdline(self):
        """Gets the process_cmdline of this AlertProcess.

        进程命令行

        :return: The process_cmdline of this AlertProcess.
        :rtype: str
        """
        return self._process_cmdline

    @process_cmdline.setter
    def process_cmdline(self, process_cmdline):
        """Sets the process_cmdline of this AlertProcess.

        进程命令行

        :param process_cmdline: The process_cmdline of this AlertProcess.
        :type process_cmdline: str
        """
        self._process_cmdline = process_cmdline

    @property
    def process_parent_name(self):
        """Gets the process_parent_name of this AlertProcess.

        父进程名称

        :return: The process_parent_name of this AlertProcess.
        :rtype: str
        """
        return self._process_parent_name

    @process_parent_name.setter
    def process_parent_name(self, process_parent_name):
        """Sets the process_parent_name of this AlertProcess.

        父进程名称

        :param process_parent_name: The process_parent_name of this AlertProcess.
        :type process_parent_name: str
        """
        self._process_parent_name = process_parent_name

    @property
    def process_parent_path(self):
        """Gets the process_parent_path of this AlertProcess.

        父进程执行文件路径

        :return: The process_parent_path of this AlertProcess.
        :rtype: str
        """
        return self._process_parent_path

    @process_parent_path.setter
    def process_parent_path(self, process_parent_path):
        """Sets the process_parent_path of this AlertProcess.

        父进程执行文件路径

        :param process_parent_path: The process_parent_path of this AlertProcess.
        :type process_parent_path: str
        """
        self._process_parent_path = process_parent_path

    @property
    def process_parent_pid(self):
        """Gets the process_parent_pid of this AlertProcess.

        父进程id

        :return: The process_parent_pid of this AlertProcess.
        :rtype: int
        """
        return self._process_parent_pid

    @process_parent_pid.setter
    def process_parent_pid(self, process_parent_pid):
        """Sets the process_parent_pid of this AlertProcess.

        父进程id

        :param process_parent_pid: The process_parent_pid of this AlertProcess.
        :type process_parent_pid: int
        """
        self._process_parent_pid = process_parent_pid

    @property
    def process_parent_uid(self):
        """Gets the process_parent_uid of this AlertProcess.

        父进程用户id

        :return: The process_parent_uid of this AlertProcess.
        :rtype: int
        """
        return self._process_parent_uid

    @process_parent_uid.setter
    def process_parent_uid(self, process_parent_uid):
        """Sets the process_parent_uid of this AlertProcess.

        父进程用户id

        :param process_parent_uid: The process_parent_uid of this AlertProcess.
        :type process_parent_uid: int
        """
        self._process_parent_uid = process_parent_uid

    @property
    def process_parent_cmdline(self):
        """Gets the process_parent_cmdline of this AlertProcess.

        父进程命令行

        :return: The process_parent_cmdline of this AlertProcess.
        :rtype: str
        """
        return self._process_parent_cmdline

    @process_parent_cmdline.setter
    def process_parent_cmdline(self, process_parent_cmdline):
        """Sets the process_parent_cmdline of this AlertProcess.

        父进程命令行

        :param process_parent_cmdline: The process_parent_cmdline of this AlertProcess.
        :type process_parent_cmdline: str
        """
        self._process_parent_cmdline = process_parent_cmdline

    @property
    def process_child_name(self):
        """Gets the process_child_name of this AlertProcess.

        子进程名称

        :return: The process_child_name of this AlertProcess.
        :rtype: str
        """
        return self._process_child_name

    @process_child_name.setter
    def process_child_name(self, process_child_name):
        """Sets the process_child_name of this AlertProcess.

        子进程名称

        :param process_child_name: The process_child_name of this AlertProcess.
        :type process_child_name: str
        """
        self._process_child_name = process_child_name

    @property
    def process_child_path(self):
        """Gets the process_child_path of this AlertProcess.

        子进程执行文件路径

        :return: The process_child_path of this AlertProcess.
        :rtype: str
        """
        return self._process_child_path

    @process_child_path.setter
    def process_child_path(self, process_child_path):
        """Sets the process_child_path of this AlertProcess.

        子进程执行文件路径

        :param process_child_path: The process_child_path of this AlertProcess.
        :type process_child_path: str
        """
        self._process_child_path = process_child_path

    @property
    def process_child_pid(self):
        """Gets the process_child_pid of this AlertProcess.

        子进程id

        :return: The process_child_pid of this AlertProcess.
        :rtype: int
        """
        return self._process_child_pid

    @process_child_pid.setter
    def process_child_pid(self, process_child_pid):
        """Sets the process_child_pid of this AlertProcess.

        子进程id

        :param process_child_pid: The process_child_pid of this AlertProcess.
        :type process_child_pid: int
        """
        self._process_child_pid = process_child_pid

    @property
    def process_child_uid(self):
        """Gets the process_child_uid of this AlertProcess.

        子进程用户id

        :return: The process_child_uid of this AlertProcess.
        :rtype: int
        """
        return self._process_child_uid

    @process_child_uid.setter
    def process_child_uid(self, process_child_uid):
        """Sets the process_child_uid of this AlertProcess.

        子进程用户id

        :param process_child_uid: The process_child_uid of this AlertProcess.
        :type process_child_uid: int
        """
        self._process_child_uid = process_child_uid

    @property
    def process_child_cmdline(self):
        """Gets the process_child_cmdline of this AlertProcess.

        子进程命令行

        :return: The process_child_cmdline of this AlertProcess.
        :rtype: str
        """
        return self._process_child_cmdline

    @process_child_cmdline.setter
    def process_child_cmdline(self, process_child_cmdline):
        """Sets the process_child_cmdline of this AlertProcess.

        子进程命令行

        :param process_child_cmdline: The process_child_cmdline of this AlertProcess.
        :type process_child_cmdline: str
        """
        self._process_child_cmdline = process_child_cmdline

    @property
    def process_launche_time(self):
        """Gets the process_launche_time of this AlertProcess.

        进程启动时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :return: The process_launche_time of this AlertProcess.
        :rtype: str
        """
        return self._process_launche_time

    @process_launche_time.setter
    def process_launche_time(self, process_launche_time):
        """Sets the process_launche_time of this AlertProcess.

        进程启动时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :param process_launche_time: The process_launche_time of this AlertProcess.
        :type process_launche_time: str
        """
        self._process_launche_time = process_launche_time

    @property
    def process_terminate_time(self):
        """Gets the process_terminate_time of this AlertProcess.

        进程结束时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :return: The process_terminate_time of this AlertProcess.
        :rtype: str
        """
        return self._process_terminate_time

    @process_terminate_time.setter
    def process_terminate_time(self, process_terminate_time):
        """Sets the process_terminate_time of this AlertProcess.

        进程结束时间，格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。时区信息为事件发生时区，无法解析时区的时间，默认时区填东八区

        :param process_terminate_time: The process_terminate_time of this AlertProcess.
        :type process_terminate_time: str
        """
        self._process_terminate_time = process_terminate_time

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
        if not isinstance(other, AlertProcess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
