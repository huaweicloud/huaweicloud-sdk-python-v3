# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAntiVirusPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'start_type': 'str',
        'scan_period': 'str',
        'scan_period_date': 'int',
        'scan_time': 'int',
        'scan_hour': 'int',
        'scan_minute': 'int',
        'timezone_offset': 'int',
        'file_types': 'list[int]',
        'scan_dir': 'str',
        'ignore_dir': 'str',
        'action': 'str',
        'whether_paid_task': 'bool',
        'task_id': 'str',
        'host_ids': 'list[str]'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'start_type': 'start_type',
        'scan_period': 'scan_period',
        'scan_period_date': 'scan_period_date',
        'scan_time': 'scan_time',
        'scan_hour': 'scan_hour',
        'scan_minute': 'scan_minute',
        'timezone_offset': 'timezone_offset',
        'file_types': 'file_types',
        'scan_dir': 'scan_dir',
        'ignore_dir': 'ignore_dir',
        'action': 'action',
        'whether_paid_task': 'whether_paid_task',
        'task_id': 'task_id',
        'host_ids': 'host_ids'
    }

    def __init__(self, policy_name=None, start_type=None, scan_period=None, scan_period_date=None, scan_time=None, scan_hour=None, scan_minute=None, timezone_offset=None, file_types=None, scan_dir=None, ignore_dir=None, action=None, whether_paid_task=None, task_id=None, host_ids=None):
        r"""CreateAntiVirusPolicyRequestBody

        The model defined in huaweicloud sdk

        :param policy_name: 策略名称
        :type policy_name: str
        :param start_type: 启动类型，包含如下:   - now : 立即启动   - later : 稍后启动   - period : 周期启动
        :type start_type: str
        :param scan_period: 启动类型，包含如下:   - day ：每天   - week : 每周   - month : 每月
        :type scan_period: str
        :param scan_period_date: 扫描周期日期（1-28；扫描周期为week时，1-7代表周日至周六；扫描周期为month时，1-28代表每月1日到28日）
        :type scan_period_date: int
        :param scan_time: 扫描时间戳，毫秒（仅启动类型为later时有值）
        :type scan_time: int
        :param scan_hour: 扫描小时数（仅启动类型为period时有值）
        :type scan_hour: int
        :param scan_minute: 扫描分钟数（仅启动类型为period时有值）
        :type scan_minute: int
        :param timezone_offset: 时区偏移量（仅启动类型为period时有值，单位：分钟）
        :type timezone_offset: int
        :param file_types: 文件类型集合型，包含如下:   - 0 ：全部   - 1 : 可执行   - 2 : 压缩   - 3 : 脚本   - 4 : 文档   - 5 : 图片   - 6 : 音视频
        :type file_types: list[int]
        :param scan_dir: 扫描目录，多个用;分隔
        :type scan_dir: str
        :param ignore_dir: 排除目录，多个用;分隔
        :type ignore_dir: str
        :param action: 处置动作，包含如下:   - auto：自动处置   - manual：人工处置
        :type action: str
        :param whether_paid_task: 此次扫描任务是否付费
        :type whether_paid_task: bool
        :param task_id: 任务ID
        :type task_id: str
        :param host_ids: 策略管理主机列表
        :type host_ids: list[str]
        """
        
        

        self._policy_name = None
        self._start_type = None
        self._scan_period = None
        self._scan_period_date = None
        self._scan_time = None
        self._scan_hour = None
        self._scan_minute = None
        self._timezone_offset = None
        self._file_types = None
        self._scan_dir = None
        self._ignore_dir = None
        self._action = None
        self._whether_paid_task = None
        self._task_id = None
        self._host_ids = None
        self.discriminator = None

        self.policy_name = policy_name
        self.start_type = start_type
        if scan_period is not None:
            self.scan_period = scan_period
        if scan_period_date is not None:
            self.scan_period_date = scan_period_date
        if scan_time is not None:
            self.scan_time = scan_time
        if scan_hour is not None:
            self.scan_hour = scan_hour
        if scan_minute is not None:
            self.scan_minute = scan_minute
        if timezone_offset is not None:
            self.timezone_offset = timezone_offset
        self.file_types = file_types
        if scan_dir is not None:
            self.scan_dir = scan_dir
        if ignore_dir is not None:
            self.ignore_dir = ignore_dir
        self.action = action
        self.whether_paid_task = whether_paid_task
        if task_id is not None:
            self.task_id = task_id
        self.host_ids = host_ids

    @property
    def policy_name(self):
        r"""Gets the policy_name of this CreateAntiVirusPolicyRequestBody.

        策略名称

        :return: The policy_name of this CreateAntiVirusPolicyRequestBody.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this CreateAntiVirusPolicyRequestBody.

        策略名称

        :param policy_name: The policy_name of this CreateAntiVirusPolicyRequestBody.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def start_type(self):
        r"""Gets the start_type of this CreateAntiVirusPolicyRequestBody.

        启动类型，包含如下:   - now : 立即启动   - later : 稍后启动   - period : 周期启动

        :return: The start_type of this CreateAntiVirusPolicyRequestBody.
        :rtype: str
        """
        return self._start_type

    @start_type.setter
    def start_type(self, start_type):
        r"""Sets the start_type of this CreateAntiVirusPolicyRequestBody.

        启动类型，包含如下:   - now : 立即启动   - later : 稍后启动   - period : 周期启动

        :param start_type: The start_type of this CreateAntiVirusPolicyRequestBody.
        :type start_type: str
        """
        self._start_type = start_type

    @property
    def scan_period(self):
        r"""Gets the scan_period of this CreateAntiVirusPolicyRequestBody.

        启动类型，包含如下:   - day ：每天   - week : 每周   - month : 每月

        :return: The scan_period of this CreateAntiVirusPolicyRequestBody.
        :rtype: str
        """
        return self._scan_period

    @scan_period.setter
    def scan_period(self, scan_period):
        r"""Sets the scan_period of this CreateAntiVirusPolicyRequestBody.

        启动类型，包含如下:   - day ：每天   - week : 每周   - month : 每月

        :param scan_period: The scan_period of this CreateAntiVirusPolicyRequestBody.
        :type scan_period: str
        """
        self._scan_period = scan_period

    @property
    def scan_period_date(self):
        r"""Gets the scan_period_date of this CreateAntiVirusPolicyRequestBody.

        扫描周期日期（1-28；扫描周期为week时，1-7代表周日至周六；扫描周期为month时，1-28代表每月1日到28日）

        :return: The scan_period_date of this CreateAntiVirusPolicyRequestBody.
        :rtype: int
        """
        return self._scan_period_date

    @scan_period_date.setter
    def scan_period_date(self, scan_period_date):
        r"""Sets the scan_period_date of this CreateAntiVirusPolicyRequestBody.

        扫描周期日期（1-28；扫描周期为week时，1-7代表周日至周六；扫描周期为month时，1-28代表每月1日到28日）

        :param scan_period_date: The scan_period_date of this CreateAntiVirusPolicyRequestBody.
        :type scan_period_date: int
        """
        self._scan_period_date = scan_period_date

    @property
    def scan_time(self):
        r"""Gets the scan_time of this CreateAntiVirusPolicyRequestBody.

        扫描时间戳，毫秒（仅启动类型为later时有值）

        :return: The scan_time of this CreateAntiVirusPolicyRequestBody.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this CreateAntiVirusPolicyRequestBody.

        扫描时间戳，毫秒（仅启动类型为later时有值）

        :param scan_time: The scan_time of this CreateAntiVirusPolicyRequestBody.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def scan_hour(self):
        r"""Gets the scan_hour of this CreateAntiVirusPolicyRequestBody.

        扫描小时数（仅启动类型为period时有值）

        :return: The scan_hour of this CreateAntiVirusPolicyRequestBody.
        :rtype: int
        """
        return self._scan_hour

    @scan_hour.setter
    def scan_hour(self, scan_hour):
        r"""Sets the scan_hour of this CreateAntiVirusPolicyRequestBody.

        扫描小时数（仅启动类型为period时有值）

        :param scan_hour: The scan_hour of this CreateAntiVirusPolicyRequestBody.
        :type scan_hour: int
        """
        self._scan_hour = scan_hour

    @property
    def scan_minute(self):
        r"""Gets the scan_minute of this CreateAntiVirusPolicyRequestBody.

        扫描分钟数（仅启动类型为period时有值）

        :return: The scan_minute of this CreateAntiVirusPolicyRequestBody.
        :rtype: int
        """
        return self._scan_minute

    @scan_minute.setter
    def scan_minute(self, scan_minute):
        r"""Sets the scan_minute of this CreateAntiVirusPolicyRequestBody.

        扫描分钟数（仅启动类型为period时有值）

        :param scan_minute: The scan_minute of this CreateAntiVirusPolicyRequestBody.
        :type scan_minute: int
        """
        self._scan_minute = scan_minute

    @property
    def timezone_offset(self):
        r"""Gets the timezone_offset of this CreateAntiVirusPolicyRequestBody.

        时区偏移量（仅启动类型为period时有值，单位：分钟）

        :return: The timezone_offset of this CreateAntiVirusPolicyRequestBody.
        :rtype: int
        """
        return self._timezone_offset

    @timezone_offset.setter
    def timezone_offset(self, timezone_offset):
        r"""Sets the timezone_offset of this CreateAntiVirusPolicyRequestBody.

        时区偏移量（仅启动类型为period时有值，单位：分钟）

        :param timezone_offset: The timezone_offset of this CreateAntiVirusPolicyRequestBody.
        :type timezone_offset: int
        """
        self._timezone_offset = timezone_offset

    @property
    def file_types(self):
        r"""Gets the file_types of this CreateAntiVirusPolicyRequestBody.

        文件类型集合型，包含如下:   - 0 ：全部   - 1 : 可执行   - 2 : 压缩   - 3 : 脚本   - 4 : 文档   - 5 : 图片   - 6 : 音视频

        :return: The file_types of this CreateAntiVirusPolicyRequestBody.
        :rtype: list[int]
        """
        return self._file_types

    @file_types.setter
    def file_types(self, file_types):
        r"""Sets the file_types of this CreateAntiVirusPolicyRequestBody.

        文件类型集合型，包含如下:   - 0 ：全部   - 1 : 可执行   - 2 : 压缩   - 3 : 脚本   - 4 : 文档   - 5 : 图片   - 6 : 音视频

        :param file_types: The file_types of this CreateAntiVirusPolicyRequestBody.
        :type file_types: list[int]
        """
        self._file_types = file_types

    @property
    def scan_dir(self):
        r"""Gets the scan_dir of this CreateAntiVirusPolicyRequestBody.

        扫描目录，多个用;分隔

        :return: The scan_dir of this CreateAntiVirusPolicyRequestBody.
        :rtype: str
        """
        return self._scan_dir

    @scan_dir.setter
    def scan_dir(self, scan_dir):
        r"""Sets the scan_dir of this CreateAntiVirusPolicyRequestBody.

        扫描目录，多个用;分隔

        :param scan_dir: The scan_dir of this CreateAntiVirusPolicyRequestBody.
        :type scan_dir: str
        """
        self._scan_dir = scan_dir

    @property
    def ignore_dir(self):
        r"""Gets the ignore_dir of this CreateAntiVirusPolicyRequestBody.

        排除目录，多个用;分隔

        :return: The ignore_dir of this CreateAntiVirusPolicyRequestBody.
        :rtype: str
        """
        return self._ignore_dir

    @ignore_dir.setter
    def ignore_dir(self, ignore_dir):
        r"""Sets the ignore_dir of this CreateAntiVirusPolicyRequestBody.

        排除目录，多个用;分隔

        :param ignore_dir: The ignore_dir of this CreateAntiVirusPolicyRequestBody.
        :type ignore_dir: str
        """
        self._ignore_dir = ignore_dir

    @property
    def action(self):
        r"""Gets the action of this CreateAntiVirusPolicyRequestBody.

        处置动作，包含如下:   - auto：自动处置   - manual：人工处置

        :return: The action of this CreateAntiVirusPolicyRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CreateAntiVirusPolicyRequestBody.

        处置动作，包含如下:   - auto：自动处置   - manual：人工处置

        :param action: The action of this CreateAntiVirusPolicyRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def whether_paid_task(self):
        r"""Gets the whether_paid_task of this CreateAntiVirusPolicyRequestBody.

        此次扫描任务是否付费

        :return: The whether_paid_task of this CreateAntiVirusPolicyRequestBody.
        :rtype: bool
        """
        return self._whether_paid_task

    @whether_paid_task.setter
    def whether_paid_task(self, whether_paid_task):
        r"""Sets the whether_paid_task of this CreateAntiVirusPolicyRequestBody.

        此次扫描任务是否付费

        :param whether_paid_task: The whether_paid_task of this CreateAntiVirusPolicyRequestBody.
        :type whether_paid_task: bool
        """
        self._whether_paid_task = whether_paid_task

    @property
    def task_id(self):
        r"""Gets the task_id of this CreateAntiVirusPolicyRequestBody.

        任务ID

        :return: The task_id of this CreateAntiVirusPolicyRequestBody.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this CreateAntiVirusPolicyRequestBody.

        任务ID

        :param task_id: The task_id of this CreateAntiVirusPolicyRequestBody.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def host_ids(self):
        r"""Gets the host_ids of this CreateAntiVirusPolicyRequestBody.

        策略管理主机列表

        :return: The host_ids of this CreateAntiVirusPolicyRequestBody.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this CreateAntiVirusPolicyRequestBody.

        策略管理主机列表

        :param host_ids: The host_ids of this CreateAntiVirusPolicyRequestBody.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

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
        if not isinstance(other, CreateAntiVirusPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
