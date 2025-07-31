# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAntiVirusTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'task_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'last_days': 'int',
        'begin_time': 'str',
        'end_time': 'str',
        'task_status': 'str',
        'host_name': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'whether_paid_task': 'bool',
        'host_task_status': 'list[str]'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'task_name': 'task_name',
        'offset': 'offset',
        'limit': 'limit',
        'last_days': 'last_days',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'task_status': 'task_status',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'whether_paid_task': 'whether_paid_task',
        'host_task_status': 'host_task_status'
    }

    def __init__(self, enterprise_project_id=None, task_name=None, offset=None, limit=None, last_days=None, begin_time=None, end_time=None, task_status=None, host_name=None, private_ip=None, public_ip=None, whether_paid_task=None, host_task_status=None):
        r"""ListAntiVirusTaskRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param task_name: 任务名称
        :type task_name: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param last_days: 查询时间范围天数，与自定义查询时间begin_time，end_time互斥
        :type last_days: int
        :param begin_time: 自定义查询时间，与查询时间范围天数互斥，查询时间段的起始时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥
        :type begin_time: str
        :param end_time: 自定义时间，查询时间段的终止时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥
        :type end_time: str
        :param task_status: 任务状态，包含如下4种   - scanning ：扫描中   - cancel ：已取消   - fail ：扫描失败   - finish ：已完成
        :type task_status: str
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type host_name: str
        :param private_ip: **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type private_ip: str
        :param public_ip: 服务器公网IP
        :type public_ip: str
        :param whether_paid_task: 此次扫描任务是否付费
        :type whether_paid_task: bool
        :param host_task_status: 服务器扫描状态，包含如下4种   - scanning ：扫描中   - success ：扫描成功   - fail ：扫描失败   - cancel ：取消扫描
        :type host_task_status: list[str]
        """
        
        

        self._enterprise_project_id = None
        self._task_name = None
        self._offset = None
        self._limit = None
        self._last_days = None
        self._begin_time = None
        self._end_time = None
        self._task_status = None
        self._host_name = None
        self._private_ip = None
        self._public_ip = None
        self._whether_paid_task = None
        self._host_task_status = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if task_name is not None:
            self.task_name = task_name
        self.offset = offset
        self.limit = limit
        if last_days is not None:
            self.last_days = last_days
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if task_status is not None:
            self.task_status = task_status
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        self.whether_paid_task = whether_paid_task
        if host_task_status is not None:
            self.host_task_status = host_task_status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAntiVirusTaskRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListAntiVirusTaskRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAntiVirusTaskRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListAntiVirusTaskRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def task_name(self):
        r"""Gets the task_name of this ListAntiVirusTaskRequest.

        任务名称

        :return: The task_name of this ListAntiVirusTaskRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ListAntiVirusTaskRequest.

        任务名称

        :param task_name: The task_name of this ListAntiVirusTaskRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def offset(self):
        r"""Gets the offset of this ListAntiVirusTaskRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListAntiVirusTaskRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAntiVirusTaskRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListAntiVirusTaskRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAntiVirusTaskRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListAntiVirusTaskRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAntiVirusTaskRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListAntiVirusTaskRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def last_days(self):
        r"""Gets the last_days of this ListAntiVirusTaskRequest.

        查询时间范围天数，与自定义查询时间begin_time，end_time互斥

        :return: The last_days of this ListAntiVirusTaskRequest.
        :rtype: int
        """
        return self._last_days

    @last_days.setter
    def last_days(self, last_days):
        r"""Sets the last_days of this ListAntiVirusTaskRequest.

        查询时间范围天数，与自定义查询时间begin_time，end_time互斥

        :param last_days: The last_days of this ListAntiVirusTaskRequest.
        :type last_days: int
        """
        self._last_days = last_days

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListAntiVirusTaskRequest.

        自定义查询时间，与查询时间范围天数互斥，查询时间段的起始时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥

        :return: The begin_time of this ListAntiVirusTaskRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListAntiVirusTaskRequest.

        自定义查询时间，与查询时间范围天数互斥，查询时间段的起始时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥

        :param begin_time: The begin_time of this ListAntiVirusTaskRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListAntiVirusTaskRequest.

        自定义时间，查询时间段的终止时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥

        :return: The end_time of this ListAntiVirusTaskRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListAntiVirusTaskRequest.

        自定义时间，查询时间段的终止时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥

        :param end_time: The end_time of this ListAntiVirusTaskRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def task_status(self):
        r"""Gets the task_status of this ListAntiVirusTaskRequest.

        任务状态，包含如下4种   - scanning ：扫描中   - cancel ：已取消   - fail ：扫描失败   - finish ：已完成

        :return: The task_status of this ListAntiVirusTaskRequest.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this ListAntiVirusTaskRequest.

        任务状态，包含如下4种   - scanning ：扫描中   - cancel ：已取消   - fail ：扫描失败   - finish ：已完成

        :param task_status: The task_status of this ListAntiVirusTaskRequest.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def host_name(self):
        r"""Gets the host_name of this ListAntiVirusTaskRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The host_name of this ListAntiVirusTaskRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListAntiVirusTaskRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListAntiVirusTaskRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListAntiVirusTaskRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The private_ip of this ListAntiVirusTaskRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListAntiVirusTaskRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param private_ip: The private_ip of this ListAntiVirusTaskRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListAntiVirusTaskRequest.

        服务器公网IP

        :return: The public_ip of this ListAntiVirusTaskRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListAntiVirusTaskRequest.

        服务器公网IP

        :param public_ip: The public_ip of this ListAntiVirusTaskRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def whether_paid_task(self):
        r"""Gets the whether_paid_task of this ListAntiVirusTaskRequest.

        此次扫描任务是否付费

        :return: The whether_paid_task of this ListAntiVirusTaskRequest.
        :rtype: bool
        """
        return self._whether_paid_task

    @whether_paid_task.setter
    def whether_paid_task(self, whether_paid_task):
        r"""Sets the whether_paid_task of this ListAntiVirusTaskRequest.

        此次扫描任务是否付费

        :param whether_paid_task: The whether_paid_task of this ListAntiVirusTaskRequest.
        :type whether_paid_task: bool
        """
        self._whether_paid_task = whether_paid_task

    @property
    def host_task_status(self):
        r"""Gets the host_task_status of this ListAntiVirusTaskRequest.

        服务器扫描状态，包含如下4种   - scanning ：扫描中   - success ：扫描成功   - fail ：扫描失败   - cancel ：取消扫描

        :return: The host_task_status of this ListAntiVirusTaskRequest.
        :rtype: list[str]
        """
        return self._host_task_status

    @host_task_status.setter
    def host_task_status(self, host_task_status):
        r"""Sets the host_task_status of this ListAntiVirusTaskRequest.

        服务器扫描状态，包含如下4种   - scanning ：扫描中   - success ：扫描成功   - fail ：扫描失败   - cancel ：取消扫描

        :param host_task_status: The host_task_status of this ListAntiVirusTaskRequest.
        :type host_task_status: list[str]
        """
        self._host_task_status = host_task_status

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
        if not isinstance(other, ListAntiVirusTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
