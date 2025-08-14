# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AntiVirusTaskResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_name': 'str',
        'scan_type': 'str',
        'start_type': 'str',
        'action': 'str',
        'start_time': 'int',
        'task_status': 'str',
        'host_num': 'int',
        'success_host_num': 'int',
        'fail_host_num': 'int',
        'cancel_host_num': 'int',
        'host_info_list': 'list[AntiVirusTaskHostResponseInfo]',
        'rescan': 'bool',
        'whether_paid_task': 'bool'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'scan_type': 'scan_type',
        'start_type': 'start_type',
        'action': 'action',
        'start_time': 'start_time',
        'task_status': 'task_status',
        'host_num': 'host_num',
        'success_host_num': 'success_host_num',
        'fail_host_num': 'fail_host_num',
        'cancel_host_num': 'cancel_host_num',
        'host_info_list': 'host_info_list',
        'rescan': 'rescan',
        'whether_paid_task': 'whether_paid_task'
    }

    def __init__(self, task_id=None, task_name=None, scan_type=None, start_type=None, action=None, start_time=None, task_status=None, host_num=None, success_host_num=None, fail_host_num=None, cancel_host_num=None, host_info_list=None, rescan=None, whether_paid_task=None):
        r"""AntiVirusTaskResponseInfo

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param task_name: 任务名称
        :type task_name: str
        :param scan_type: 任务类型，包含如下:   - quick ：快速扫描   - full : 全盘扫描   - custom : 自定义扫描
        :type scan_type: str
        :param start_type: 启动类型，包含如下:   - now : 立即启动   - later : 稍后启动   - period : 周期启动
        :type start_type: str
        :param action: 处置动作，包含如下:   - auto：自动处置   - manual：人工处置
        :type action: str
        :param start_time: 启动时间，毫秒
        :type start_time: int
        :param task_status: 任务状态，包含如下2种   - scanning ：扫描中   - finish ：扫描完成
        :type task_status: str
        :param host_num: 关联服务器数
        :type host_num: int
        :param success_host_num: 扫描成功服务器数
        :type success_host_num: int
        :param fail_host_num: 扫描失败服务器数
        :type fail_host_num: int
        :param cancel_host_num: 已取消服务器数
        :type cancel_host_num: int
        :param host_info_list: 主机信息
        :type host_info_list: list[:class:`huaweicloudsdkhss.v5.AntiVirusTaskHostResponseInfo`]
        :param rescan: 是否需要重新扫描
        :type rescan: bool
        :param whether_paid_task: 此次扫描任务是否付费
        :type whether_paid_task: bool
        """
        
        

        self._task_id = None
        self._task_name = None
        self._scan_type = None
        self._start_type = None
        self._action = None
        self._start_time = None
        self._task_status = None
        self._host_num = None
        self._success_host_num = None
        self._fail_host_num = None
        self._cancel_host_num = None
        self._host_info_list = None
        self._rescan = None
        self._whether_paid_task = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if scan_type is not None:
            self.scan_type = scan_type
        if start_type is not None:
            self.start_type = start_type
        if action is not None:
            self.action = action
        if start_time is not None:
            self.start_time = start_time
        if task_status is not None:
            self.task_status = task_status
        if host_num is not None:
            self.host_num = host_num
        if success_host_num is not None:
            self.success_host_num = success_host_num
        if fail_host_num is not None:
            self.fail_host_num = fail_host_num
        if cancel_host_num is not None:
            self.cancel_host_num = cancel_host_num
        if host_info_list is not None:
            self.host_info_list = host_info_list
        if rescan is not None:
            self.rescan = rescan
        if whether_paid_task is not None:
            self.whether_paid_task = whether_paid_task

    @property
    def task_id(self):
        r"""Gets the task_id of this AntiVirusTaskResponseInfo.

        任务ID

        :return: The task_id of this AntiVirusTaskResponseInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this AntiVirusTaskResponseInfo.

        任务ID

        :param task_id: The task_id of this AntiVirusTaskResponseInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this AntiVirusTaskResponseInfo.

        任务名称

        :return: The task_name of this AntiVirusTaskResponseInfo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this AntiVirusTaskResponseInfo.

        任务名称

        :param task_name: The task_name of this AntiVirusTaskResponseInfo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def scan_type(self):
        r"""Gets the scan_type of this AntiVirusTaskResponseInfo.

        任务类型，包含如下:   - quick ：快速扫描   - full : 全盘扫描   - custom : 自定义扫描

        :return: The scan_type of this AntiVirusTaskResponseInfo.
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        r"""Sets the scan_type of this AntiVirusTaskResponseInfo.

        任务类型，包含如下:   - quick ：快速扫描   - full : 全盘扫描   - custom : 自定义扫描

        :param scan_type: The scan_type of this AntiVirusTaskResponseInfo.
        :type scan_type: str
        """
        self._scan_type = scan_type

    @property
    def start_type(self):
        r"""Gets the start_type of this AntiVirusTaskResponseInfo.

        启动类型，包含如下:   - now : 立即启动   - later : 稍后启动   - period : 周期启动

        :return: The start_type of this AntiVirusTaskResponseInfo.
        :rtype: str
        """
        return self._start_type

    @start_type.setter
    def start_type(self, start_type):
        r"""Sets the start_type of this AntiVirusTaskResponseInfo.

        启动类型，包含如下:   - now : 立即启动   - later : 稍后启动   - period : 周期启动

        :param start_type: The start_type of this AntiVirusTaskResponseInfo.
        :type start_type: str
        """
        self._start_type = start_type

    @property
    def action(self):
        r"""Gets the action of this AntiVirusTaskResponseInfo.

        处置动作，包含如下:   - auto：自动处置   - manual：人工处置

        :return: The action of this AntiVirusTaskResponseInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this AntiVirusTaskResponseInfo.

        处置动作，包含如下:   - auto：自动处置   - manual：人工处置

        :param action: The action of this AntiVirusTaskResponseInfo.
        :type action: str
        """
        self._action = action

    @property
    def start_time(self):
        r"""Gets the start_time of this AntiVirusTaskResponseInfo.

        启动时间，毫秒

        :return: The start_time of this AntiVirusTaskResponseInfo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this AntiVirusTaskResponseInfo.

        启动时间，毫秒

        :param start_time: The start_time of this AntiVirusTaskResponseInfo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def task_status(self):
        r"""Gets the task_status of this AntiVirusTaskResponseInfo.

        任务状态，包含如下2种   - scanning ：扫描中   - finish ：扫描完成

        :return: The task_status of this AntiVirusTaskResponseInfo.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this AntiVirusTaskResponseInfo.

        任务状态，包含如下2种   - scanning ：扫描中   - finish ：扫描完成

        :param task_status: The task_status of this AntiVirusTaskResponseInfo.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def host_num(self):
        r"""Gets the host_num of this AntiVirusTaskResponseInfo.

        关联服务器数

        :return: The host_num of this AntiVirusTaskResponseInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this AntiVirusTaskResponseInfo.

        关联服务器数

        :param host_num: The host_num of this AntiVirusTaskResponseInfo.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def success_host_num(self):
        r"""Gets the success_host_num of this AntiVirusTaskResponseInfo.

        扫描成功服务器数

        :return: The success_host_num of this AntiVirusTaskResponseInfo.
        :rtype: int
        """
        return self._success_host_num

    @success_host_num.setter
    def success_host_num(self, success_host_num):
        r"""Sets the success_host_num of this AntiVirusTaskResponseInfo.

        扫描成功服务器数

        :param success_host_num: The success_host_num of this AntiVirusTaskResponseInfo.
        :type success_host_num: int
        """
        self._success_host_num = success_host_num

    @property
    def fail_host_num(self):
        r"""Gets the fail_host_num of this AntiVirusTaskResponseInfo.

        扫描失败服务器数

        :return: The fail_host_num of this AntiVirusTaskResponseInfo.
        :rtype: int
        """
        return self._fail_host_num

    @fail_host_num.setter
    def fail_host_num(self, fail_host_num):
        r"""Sets the fail_host_num of this AntiVirusTaskResponseInfo.

        扫描失败服务器数

        :param fail_host_num: The fail_host_num of this AntiVirusTaskResponseInfo.
        :type fail_host_num: int
        """
        self._fail_host_num = fail_host_num

    @property
    def cancel_host_num(self):
        r"""Gets the cancel_host_num of this AntiVirusTaskResponseInfo.

        已取消服务器数

        :return: The cancel_host_num of this AntiVirusTaskResponseInfo.
        :rtype: int
        """
        return self._cancel_host_num

    @cancel_host_num.setter
    def cancel_host_num(self, cancel_host_num):
        r"""Sets the cancel_host_num of this AntiVirusTaskResponseInfo.

        已取消服务器数

        :param cancel_host_num: The cancel_host_num of this AntiVirusTaskResponseInfo.
        :type cancel_host_num: int
        """
        self._cancel_host_num = cancel_host_num

    @property
    def host_info_list(self):
        r"""Gets the host_info_list of this AntiVirusTaskResponseInfo.

        主机信息

        :return: The host_info_list of this AntiVirusTaskResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AntiVirusTaskHostResponseInfo`]
        """
        return self._host_info_list

    @host_info_list.setter
    def host_info_list(self, host_info_list):
        r"""Sets the host_info_list of this AntiVirusTaskResponseInfo.

        主机信息

        :param host_info_list: The host_info_list of this AntiVirusTaskResponseInfo.
        :type host_info_list: list[:class:`huaweicloudsdkhss.v5.AntiVirusTaskHostResponseInfo`]
        """
        self._host_info_list = host_info_list

    @property
    def rescan(self):
        r"""Gets the rescan of this AntiVirusTaskResponseInfo.

        是否需要重新扫描

        :return: The rescan of this AntiVirusTaskResponseInfo.
        :rtype: bool
        """
        return self._rescan

    @rescan.setter
    def rescan(self, rescan):
        r"""Sets the rescan of this AntiVirusTaskResponseInfo.

        是否需要重新扫描

        :param rescan: The rescan of this AntiVirusTaskResponseInfo.
        :type rescan: bool
        """
        self._rescan = rescan

    @property
    def whether_paid_task(self):
        r"""Gets the whether_paid_task of this AntiVirusTaskResponseInfo.

        此次扫描任务是否付费

        :return: The whether_paid_task of this AntiVirusTaskResponseInfo.
        :rtype: bool
        """
        return self._whether_paid_task

    @whether_paid_task.setter
    def whether_paid_task(self, whether_paid_task):
        r"""Sets the whether_paid_task of this AntiVirusTaskResponseInfo.

        此次扫描任务是否付费

        :param whether_paid_task: The whether_paid_task of this AntiVirusTaskResponseInfo.
        :type whether_paid_task: bool
        """
        self._whether_paid_task = whether_paid_task

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
        if not isinstance(other, AntiVirusTaskResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
