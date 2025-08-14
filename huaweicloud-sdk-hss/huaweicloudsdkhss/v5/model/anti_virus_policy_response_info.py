# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AntiVirusPolicyResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'policy_name': 'str',
        'start_type': 'str',
        'scan_period': 'str',
        'scan_period_date': 'int',
        'scan_time': 'int',
        'scan_hour': 'int',
        'scan_minute': 'int',
        'next_start_time': 'int',
        'scan_dir': 'str',
        'ignore_dir': 'str',
        'action': 'str',
        'invalidate': 'bool',
        'host_num': 'int',
        'host_info_list': 'list[AntiVirusPolicyHostResponseInfo]',
        'whether_paid_task': 'bool',
        'file_type_list': 'list[int]'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'start_type': 'start_type',
        'scan_period': 'scan_period',
        'scan_period_date': 'scan_period_date',
        'scan_time': 'scan_time',
        'scan_hour': 'scan_hour',
        'scan_minute': 'scan_minute',
        'next_start_time': 'next_start_time',
        'scan_dir': 'scan_dir',
        'ignore_dir': 'ignore_dir',
        'action': 'action',
        'invalidate': 'invalidate',
        'host_num': 'host_num',
        'host_info_list': 'host_info_list',
        'whether_paid_task': 'whether_paid_task',
        'file_type_list': 'file_type_list'
    }

    def __init__(self, policy_id=None, policy_name=None, start_type=None, scan_period=None, scan_period_date=None, scan_time=None, scan_hour=None, scan_minute=None, next_start_time=None, scan_dir=None, ignore_dir=None, action=None, invalidate=None, host_num=None, host_info_list=None, whether_paid_task=None, file_type_list=None):
        r"""AntiVirusPolicyResponseInfo

        The model defined in huaweicloud sdk

        :param policy_id: 策略ID
        :type policy_id: str
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
        :param next_start_time: 下次启动时间，毫秒
        :type next_start_time: int
        :param scan_dir: 扫描目录，多个用;分隔
        :type scan_dir: str
        :param ignore_dir: 排除目录，多个用;分隔
        :type ignore_dir: str
        :param action: 处置动作，包含如下:   - auto：自动处置   - manual：人工处置
        :type action: str
        :param invalidate: 失效，包含如下:   - true ：是   - fasle ：否
        :type invalidate: bool
        :param host_num: **参数解释**: 影响主机数量 **取值范围**: 最小值0，最大值2147483647 
        :type host_num: int
        :param host_info_list: 主机信息
        :type host_info_list: list[:class:`huaweicloudsdkhss.v5.AntiVirusPolicyHostResponseInfo`]
        :param whether_paid_task: 此次扫描任务是否付费
        :type whether_paid_task: bool
        :param file_type_list: 文件类型集合型
        :type file_type_list: list[int]
        """
        
        

        self._policy_id = None
        self._policy_name = None
        self._start_type = None
        self._scan_period = None
        self._scan_period_date = None
        self._scan_time = None
        self._scan_hour = None
        self._scan_minute = None
        self._next_start_time = None
        self._scan_dir = None
        self._ignore_dir = None
        self._action = None
        self._invalidate = None
        self._host_num = None
        self._host_info_list = None
        self._whether_paid_task = None
        self._file_type_list = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if start_type is not None:
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
        if next_start_time is not None:
            self.next_start_time = next_start_time
        if scan_dir is not None:
            self.scan_dir = scan_dir
        if ignore_dir is not None:
            self.ignore_dir = ignore_dir
        if action is not None:
            self.action = action
        if invalidate is not None:
            self.invalidate = invalidate
        if host_num is not None:
            self.host_num = host_num
        if host_info_list is not None:
            self.host_info_list = host_info_list
        if whether_paid_task is not None:
            self.whether_paid_task = whether_paid_task
        if file_type_list is not None:
            self.file_type_list = file_type_list

    @property
    def policy_id(self):
        r"""Gets the policy_id of this AntiVirusPolicyResponseInfo.

        策略ID

        :return: The policy_id of this AntiVirusPolicyResponseInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this AntiVirusPolicyResponseInfo.

        策略ID

        :param policy_id: The policy_id of this AntiVirusPolicyResponseInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this AntiVirusPolicyResponseInfo.

        策略名称

        :return: The policy_name of this AntiVirusPolicyResponseInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this AntiVirusPolicyResponseInfo.

        策略名称

        :param policy_name: The policy_name of this AntiVirusPolicyResponseInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def start_type(self):
        r"""Gets the start_type of this AntiVirusPolicyResponseInfo.

        启动类型，包含如下:   - now : 立即启动   - later : 稍后启动   - period : 周期启动

        :return: The start_type of this AntiVirusPolicyResponseInfo.
        :rtype: str
        """
        return self._start_type

    @start_type.setter
    def start_type(self, start_type):
        r"""Sets the start_type of this AntiVirusPolicyResponseInfo.

        启动类型，包含如下:   - now : 立即启动   - later : 稍后启动   - period : 周期启动

        :param start_type: The start_type of this AntiVirusPolicyResponseInfo.
        :type start_type: str
        """
        self._start_type = start_type

    @property
    def scan_period(self):
        r"""Gets the scan_period of this AntiVirusPolicyResponseInfo.

        启动类型，包含如下:   - day ：每天   - week : 每周   - month : 每月

        :return: The scan_period of this AntiVirusPolicyResponseInfo.
        :rtype: str
        """
        return self._scan_period

    @scan_period.setter
    def scan_period(self, scan_period):
        r"""Sets the scan_period of this AntiVirusPolicyResponseInfo.

        启动类型，包含如下:   - day ：每天   - week : 每周   - month : 每月

        :param scan_period: The scan_period of this AntiVirusPolicyResponseInfo.
        :type scan_period: str
        """
        self._scan_period = scan_period

    @property
    def scan_period_date(self):
        r"""Gets the scan_period_date of this AntiVirusPolicyResponseInfo.

        扫描周期日期（1-28；扫描周期为week时，1-7代表周日至周六；扫描周期为month时，1-28代表每月1日到28日）

        :return: The scan_period_date of this AntiVirusPolicyResponseInfo.
        :rtype: int
        """
        return self._scan_period_date

    @scan_period_date.setter
    def scan_period_date(self, scan_period_date):
        r"""Sets the scan_period_date of this AntiVirusPolicyResponseInfo.

        扫描周期日期（1-28；扫描周期为week时，1-7代表周日至周六；扫描周期为month时，1-28代表每月1日到28日）

        :param scan_period_date: The scan_period_date of this AntiVirusPolicyResponseInfo.
        :type scan_period_date: int
        """
        self._scan_period_date = scan_period_date

    @property
    def scan_time(self):
        r"""Gets the scan_time of this AntiVirusPolicyResponseInfo.

        扫描时间戳，毫秒（仅启动类型为later时有值）

        :return: The scan_time of this AntiVirusPolicyResponseInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this AntiVirusPolicyResponseInfo.

        扫描时间戳，毫秒（仅启动类型为later时有值）

        :param scan_time: The scan_time of this AntiVirusPolicyResponseInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def scan_hour(self):
        r"""Gets the scan_hour of this AntiVirusPolicyResponseInfo.

        扫描小时数（仅启动类型为period时有值）

        :return: The scan_hour of this AntiVirusPolicyResponseInfo.
        :rtype: int
        """
        return self._scan_hour

    @scan_hour.setter
    def scan_hour(self, scan_hour):
        r"""Sets the scan_hour of this AntiVirusPolicyResponseInfo.

        扫描小时数（仅启动类型为period时有值）

        :param scan_hour: The scan_hour of this AntiVirusPolicyResponseInfo.
        :type scan_hour: int
        """
        self._scan_hour = scan_hour

    @property
    def scan_minute(self):
        r"""Gets the scan_minute of this AntiVirusPolicyResponseInfo.

        扫描分钟数（仅启动类型为period时有值）

        :return: The scan_minute of this AntiVirusPolicyResponseInfo.
        :rtype: int
        """
        return self._scan_minute

    @scan_minute.setter
    def scan_minute(self, scan_minute):
        r"""Sets the scan_minute of this AntiVirusPolicyResponseInfo.

        扫描分钟数（仅启动类型为period时有值）

        :param scan_minute: The scan_minute of this AntiVirusPolicyResponseInfo.
        :type scan_minute: int
        """
        self._scan_minute = scan_minute

    @property
    def next_start_time(self):
        r"""Gets the next_start_time of this AntiVirusPolicyResponseInfo.

        下次启动时间，毫秒

        :return: The next_start_time of this AntiVirusPolicyResponseInfo.
        :rtype: int
        """
        return self._next_start_time

    @next_start_time.setter
    def next_start_time(self, next_start_time):
        r"""Sets the next_start_time of this AntiVirusPolicyResponseInfo.

        下次启动时间，毫秒

        :param next_start_time: The next_start_time of this AntiVirusPolicyResponseInfo.
        :type next_start_time: int
        """
        self._next_start_time = next_start_time

    @property
    def scan_dir(self):
        r"""Gets the scan_dir of this AntiVirusPolicyResponseInfo.

        扫描目录，多个用;分隔

        :return: The scan_dir of this AntiVirusPolicyResponseInfo.
        :rtype: str
        """
        return self._scan_dir

    @scan_dir.setter
    def scan_dir(self, scan_dir):
        r"""Sets the scan_dir of this AntiVirusPolicyResponseInfo.

        扫描目录，多个用;分隔

        :param scan_dir: The scan_dir of this AntiVirusPolicyResponseInfo.
        :type scan_dir: str
        """
        self._scan_dir = scan_dir

    @property
    def ignore_dir(self):
        r"""Gets the ignore_dir of this AntiVirusPolicyResponseInfo.

        排除目录，多个用;分隔

        :return: The ignore_dir of this AntiVirusPolicyResponseInfo.
        :rtype: str
        """
        return self._ignore_dir

    @ignore_dir.setter
    def ignore_dir(self, ignore_dir):
        r"""Sets the ignore_dir of this AntiVirusPolicyResponseInfo.

        排除目录，多个用;分隔

        :param ignore_dir: The ignore_dir of this AntiVirusPolicyResponseInfo.
        :type ignore_dir: str
        """
        self._ignore_dir = ignore_dir

    @property
    def action(self):
        r"""Gets the action of this AntiVirusPolicyResponseInfo.

        处置动作，包含如下:   - auto：自动处置   - manual：人工处置

        :return: The action of this AntiVirusPolicyResponseInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this AntiVirusPolicyResponseInfo.

        处置动作，包含如下:   - auto：自动处置   - manual：人工处置

        :param action: The action of this AntiVirusPolicyResponseInfo.
        :type action: str
        """
        self._action = action

    @property
    def invalidate(self):
        r"""Gets the invalidate of this AntiVirusPolicyResponseInfo.

        失效，包含如下:   - true ：是   - fasle ：否

        :return: The invalidate of this AntiVirusPolicyResponseInfo.
        :rtype: bool
        """
        return self._invalidate

    @invalidate.setter
    def invalidate(self, invalidate):
        r"""Sets the invalidate of this AntiVirusPolicyResponseInfo.

        失效，包含如下:   - true ：是   - fasle ：否

        :param invalidate: The invalidate of this AntiVirusPolicyResponseInfo.
        :type invalidate: bool
        """
        self._invalidate = invalidate

    @property
    def host_num(self):
        r"""Gets the host_num of this AntiVirusPolicyResponseInfo.

        **参数解释**: 影响主机数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The host_num of this AntiVirusPolicyResponseInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this AntiVirusPolicyResponseInfo.

        **参数解释**: 影响主机数量 **取值范围**: 最小值0，最大值2147483647 

        :param host_num: The host_num of this AntiVirusPolicyResponseInfo.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def host_info_list(self):
        r"""Gets the host_info_list of this AntiVirusPolicyResponseInfo.

        主机信息

        :return: The host_info_list of this AntiVirusPolicyResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AntiVirusPolicyHostResponseInfo`]
        """
        return self._host_info_list

    @host_info_list.setter
    def host_info_list(self, host_info_list):
        r"""Sets the host_info_list of this AntiVirusPolicyResponseInfo.

        主机信息

        :param host_info_list: The host_info_list of this AntiVirusPolicyResponseInfo.
        :type host_info_list: list[:class:`huaweicloudsdkhss.v5.AntiVirusPolicyHostResponseInfo`]
        """
        self._host_info_list = host_info_list

    @property
    def whether_paid_task(self):
        r"""Gets the whether_paid_task of this AntiVirusPolicyResponseInfo.

        此次扫描任务是否付费

        :return: The whether_paid_task of this AntiVirusPolicyResponseInfo.
        :rtype: bool
        """
        return self._whether_paid_task

    @whether_paid_task.setter
    def whether_paid_task(self, whether_paid_task):
        r"""Sets the whether_paid_task of this AntiVirusPolicyResponseInfo.

        此次扫描任务是否付费

        :param whether_paid_task: The whether_paid_task of this AntiVirusPolicyResponseInfo.
        :type whether_paid_task: bool
        """
        self._whether_paid_task = whether_paid_task

    @property
    def file_type_list(self):
        r"""Gets the file_type_list of this AntiVirusPolicyResponseInfo.

        文件类型集合型

        :return: The file_type_list of this AntiVirusPolicyResponseInfo.
        :rtype: list[int]
        """
        return self._file_type_list

    @file_type_list.setter
    def file_type_list(self, file_type_list):
        r"""Sets the file_type_list of this AntiVirusPolicyResponseInfo.

        文件类型集合型

        :param file_type_list: The file_type_list of this AntiVirusPolicyResponseInfo.
        :type file_type_list: list[int]
        """
        self._file_type_list = file_type_list

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
        if not isinstance(other, AntiVirusPolicyResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
