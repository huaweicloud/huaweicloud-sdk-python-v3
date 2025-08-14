# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAntiVirusPaidTaskRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_name': 'str',
        'scan_type': 'str',
        'action': 'str',
        'host_ids': 'list[str]',
        'file_types': 'list[int]',
        'scan_dir': 'str',
        'ignore_dir': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'task_name': 'task_name',
        'scan_type': 'scan_type',
        'action': 'action',
        'host_ids': 'host_ids',
        'file_types': 'file_types',
        'scan_dir': 'scan_dir',
        'ignore_dir': 'ignore_dir',
        'task_id': 'task_id'
    }

    def __init__(self, task_name=None, scan_type=None, action=None, host_ids=None, file_types=None, scan_dir=None, ignore_dir=None, task_id=None):
        r"""CreateAntiVirusPaidTaskRequestInfo

        The model defined in huaweicloud sdk

        :param task_name: 任务名称
        :type task_name: str
        :param scan_type: 任务类型，包含如下:   - quick ：快速扫描   - full : 全盘扫描   - custom : 自定义扫描
        :type scan_type: str
        :param action: 处置动作，包含如下:   - auto：自动处置   - manual：人工处置
        :type action: str
        :param host_ids: 病毒查杀主机列表
        :type host_ids: list[str]
        :param file_types: 文件类型集合型，包含如下:   - 0 ：全部   - 1 : 可执行   - 2 : 压缩   - 3 : 脚本   - 4 : 文档   - 5 : 图片   - 6 : 音视频
        :type file_types: list[int]
        :param scan_dir: 扫描目录，多个用;分隔
        :type scan_dir: str
        :param ignore_dir: 排除目录，多个用;分隔
        :type ignore_dir: str
        :param task_id: 任务ID 创建病毒扫描任务时,task_id是null.重新扫描时，task_id不是null,是当前任务的ID
        :type task_id: str
        """
        
        

        self._task_name = None
        self._scan_type = None
        self._action = None
        self._host_ids = None
        self._file_types = None
        self._scan_dir = None
        self._ignore_dir = None
        self._task_id = None
        self.discriminator = None

        self.task_name = task_name
        self.scan_type = scan_type
        self.action = action
        self.host_ids = host_ids
        if file_types is not None:
            self.file_types = file_types
        if scan_dir is not None:
            self.scan_dir = scan_dir
        if ignore_dir is not None:
            self.ignore_dir = ignore_dir
        if task_id is not None:
            self.task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this CreateAntiVirusPaidTaskRequestInfo.

        任务名称

        :return: The task_name of this CreateAntiVirusPaidTaskRequestInfo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this CreateAntiVirusPaidTaskRequestInfo.

        任务名称

        :param task_name: The task_name of this CreateAntiVirusPaidTaskRequestInfo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def scan_type(self):
        r"""Gets the scan_type of this CreateAntiVirusPaidTaskRequestInfo.

        任务类型，包含如下:   - quick ：快速扫描   - full : 全盘扫描   - custom : 自定义扫描

        :return: The scan_type of this CreateAntiVirusPaidTaskRequestInfo.
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        r"""Sets the scan_type of this CreateAntiVirusPaidTaskRequestInfo.

        任务类型，包含如下:   - quick ：快速扫描   - full : 全盘扫描   - custom : 自定义扫描

        :param scan_type: The scan_type of this CreateAntiVirusPaidTaskRequestInfo.
        :type scan_type: str
        """
        self._scan_type = scan_type

    @property
    def action(self):
        r"""Gets the action of this CreateAntiVirusPaidTaskRequestInfo.

        处置动作，包含如下:   - auto：自动处置   - manual：人工处置

        :return: The action of this CreateAntiVirusPaidTaskRequestInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CreateAntiVirusPaidTaskRequestInfo.

        处置动作，包含如下:   - auto：自动处置   - manual：人工处置

        :param action: The action of this CreateAntiVirusPaidTaskRequestInfo.
        :type action: str
        """
        self._action = action

    @property
    def host_ids(self):
        r"""Gets the host_ids of this CreateAntiVirusPaidTaskRequestInfo.

        病毒查杀主机列表

        :return: The host_ids of this CreateAntiVirusPaidTaskRequestInfo.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this CreateAntiVirusPaidTaskRequestInfo.

        病毒查杀主机列表

        :param host_ids: The host_ids of this CreateAntiVirusPaidTaskRequestInfo.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

    @property
    def file_types(self):
        r"""Gets the file_types of this CreateAntiVirusPaidTaskRequestInfo.

        文件类型集合型，包含如下:   - 0 ：全部   - 1 : 可执行   - 2 : 压缩   - 3 : 脚本   - 4 : 文档   - 5 : 图片   - 6 : 音视频

        :return: The file_types of this CreateAntiVirusPaidTaskRequestInfo.
        :rtype: list[int]
        """
        return self._file_types

    @file_types.setter
    def file_types(self, file_types):
        r"""Sets the file_types of this CreateAntiVirusPaidTaskRequestInfo.

        文件类型集合型，包含如下:   - 0 ：全部   - 1 : 可执行   - 2 : 压缩   - 3 : 脚本   - 4 : 文档   - 5 : 图片   - 6 : 音视频

        :param file_types: The file_types of this CreateAntiVirusPaidTaskRequestInfo.
        :type file_types: list[int]
        """
        self._file_types = file_types

    @property
    def scan_dir(self):
        r"""Gets the scan_dir of this CreateAntiVirusPaidTaskRequestInfo.

        扫描目录，多个用;分隔

        :return: The scan_dir of this CreateAntiVirusPaidTaskRequestInfo.
        :rtype: str
        """
        return self._scan_dir

    @scan_dir.setter
    def scan_dir(self, scan_dir):
        r"""Sets the scan_dir of this CreateAntiVirusPaidTaskRequestInfo.

        扫描目录，多个用;分隔

        :param scan_dir: The scan_dir of this CreateAntiVirusPaidTaskRequestInfo.
        :type scan_dir: str
        """
        self._scan_dir = scan_dir

    @property
    def ignore_dir(self):
        r"""Gets the ignore_dir of this CreateAntiVirusPaidTaskRequestInfo.

        排除目录，多个用;分隔

        :return: The ignore_dir of this CreateAntiVirusPaidTaskRequestInfo.
        :rtype: str
        """
        return self._ignore_dir

    @ignore_dir.setter
    def ignore_dir(self, ignore_dir):
        r"""Sets the ignore_dir of this CreateAntiVirusPaidTaskRequestInfo.

        排除目录，多个用;分隔

        :param ignore_dir: The ignore_dir of this CreateAntiVirusPaidTaskRequestInfo.
        :type ignore_dir: str
        """
        self._ignore_dir = ignore_dir

    @property
    def task_id(self):
        r"""Gets the task_id of this CreateAntiVirusPaidTaskRequestInfo.

        任务ID 创建病毒扫描任务时,task_id是null.重新扫描时，task_id不是null,是当前任务的ID

        :return: The task_id of this CreateAntiVirusPaidTaskRequestInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this CreateAntiVirusPaidTaskRequestInfo.

        任务ID 创建病毒扫描任务时,task_id是null.重新扫描时，task_id不是null,是当前任务的ID

        :param task_id: The task_id of this CreateAntiVirusPaidTaskRequestInfo.
        :type task_id: str
        """
        self._task_id = task_id

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
        if not isinstance(other, CreateAntiVirusPaidTaskRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
