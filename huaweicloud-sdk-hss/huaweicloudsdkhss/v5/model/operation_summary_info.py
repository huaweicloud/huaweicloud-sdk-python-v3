# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperationSummaryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hss_visit_days': 'int',
        'workload_beat_rate': 'float',
        'user_name': 'str',
        'current_month_start': 'int',
        'current_month_end': 'int',
        'handled_security_event_num': 'int',
        'total_workload_beat_rate': 'float',
        'title': 'str',
        'report_id': 'str',
        'current_month': 'int',
        'work': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'hss_visit_days': 'hss_visit_days',
        'workload_beat_rate': 'workload_beat_rate',
        'user_name': 'user_name',
        'current_month_start': 'current_month_start',
        'current_month_end': 'current_month_end',
        'handled_security_event_num': 'handled_security_event_num',
        'total_workload_beat_rate': 'total_workload_beat_rate',
        'title': 'title',
        'report_id': 'report_id',
        'current_month': 'current_month',
        'work': 'work',
        'create_time': 'create_time'
    }

    def __init__(self, hss_visit_days=None, workload_beat_rate=None, user_name=None, current_month_start=None, current_month_end=None, handled_security_event_num=None, total_workload_beat_rate=None, title=None, report_id=None, current_month=None, work=None, create_time=None):
        r"""OperationSummaryInfo

        The model defined in huaweicloud sdk

        :param hss_visit_days: **参数解释**: 用户访问HSS天数 **取值范围**: 最小值0，最大值365 
        :type hss_visit_days: int
        :param workload_beat_rate: **参数解释**: 某个工作超过的用户百分比（目前只有漏洞或告警，哪个打败的用户占比高，显示哪个） **取值范围**: 最小值0，最大值1 
        :type workload_beat_rate: float
        :param user_name: **参数解释**: 用户名 **取值范围**: 字符长度0-128位 
        :type user_name: str
        :param current_month_start: **参数解释**: 当前月初时间戳 **取值范围**: 最小值0，最大值9223372036854775807 
        :type current_month_start: int
        :param current_month_end: **参数解释**: 当前月末时间戳 **取值范围**: 最小值0，最大值9223372036854775807 
        :type current_month_end: int
        :param handled_security_event_num: **参数解释**: 处置的安全事件条数 **取值范围**: 最小值0，最大值2147483647 
        :type handled_security_event_num: int
        :param total_workload_beat_rate: **参数解释**: 工作量打败的用户百分比 **取值范围**: 最小值0，最大值1 
        :type total_workload_beat_rate: float
        :param title: **参数解释**:  称号 **取值范围**: -vul-fix-master: 补洞大师。 -vul-fix-expert: 漏洞修复小能手。 -baseline-handle: 风险配置处置高手。 -malware-file: 防病毒先锋。 -ransomware-event: 防勒索达人。 -web-tamper-event: 网站守卫。 
        :type title: str
        :param report_id: **参数解释**: 时间字符串 **取值范围**: 字符长度0-32位 
        :type report_id: str
        :param current_month: **参数解释**: 当前月份 **取值范围**: 最小值1，最大值12 
        :type current_month: int
        :param work: **参数解释**: 工作（哪个打败的用户占比高，显示哪个) **取值范围**: -vul-fix: 漏洞修复 -baseline-handle: 基线处置 -event-handle: 处置入侵事件 
        :type work: str
        :param create_time: **参数解释**: 报告生成时间戳 **取值范围**: 最小值0，最大值9223372036854775807 
        :type create_time: int
        """
        
        

        self._hss_visit_days = None
        self._workload_beat_rate = None
        self._user_name = None
        self._current_month_start = None
        self._current_month_end = None
        self._handled_security_event_num = None
        self._total_workload_beat_rate = None
        self._title = None
        self._report_id = None
        self._current_month = None
        self._work = None
        self._create_time = None
        self.discriminator = None

        if hss_visit_days is not None:
            self.hss_visit_days = hss_visit_days
        if workload_beat_rate is not None:
            self.workload_beat_rate = workload_beat_rate
        if user_name is not None:
            self.user_name = user_name
        if current_month_start is not None:
            self.current_month_start = current_month_start
        if current_month_end is not None:
            self.current_month_end = current_month_end
        if handled_security_event_num is not None:
            self.handled_security_event_num = handled_security_event_num
        if total_workload_beat_rate is not None:
            self.total_workload_beat_rate = total_workload_beat_rate
        if title is not None:
            self.title = title
        if report_id is not None:
            self.report_id = report_id
        if current_month is not None:
            self.current_month = current_month
        if work is not None:
            self.work = work
        if create_time is not None:
            self.create_time = create_time

    @property
    def hss_visit_days(self):
        r"""Gets the hss_visit_days of this OperationSummaryInfo.

        **参数解释**: 用户访问HSS天数 **取值范围**: 最小值0，最大值365 

        :return: The hss_visit_days of this OperationSummaryInfo.
        :rtype: int
        """
        return self._hss_visit_days

    @hss_visit_days.setter
    def hss_visit_days(self, hss_visit_days):
        r"""Sets the hss_visit_days of this OperationSummaryInfo.

        **参数解释**: 用户访问HSS天数 **取值范围**: 最小值0，最大值365 

        :param hss_visit_days: The hss_visit_days of this OperationSummaryInfo.
        :type hss_visit_days: int
        """
        self._hss_visit_days = hss_visit_days

    @property
    def workload_beat_rate(self):
        r"""Gets the workload_beat_rate of this OperationSummaryInfo.

        **参数解释**: 某个工作超过的用户百分比（目前只有漏洞或告警，哪个打败的用户占比高，显示哪个） **取值范围**: 最小值0，最大值1 

        :return: The workload_beat_rate of this OperationSummaryInfo.
        :rtype: float
        """
        return self._workload_beat_rate

    @workload_beat_rate.setter
    def workload_beat_rate(self, workload_beat_rate):
        r"""Sets the workload_beat_rate of this OperationSummaryInfo.

        **参数解释**: 某个工作超过的用户百分比（目前只有漏洞或告警，哪个打败的用户占比高，显示哪个） **取值范围**: 最小值0，最大值1 

        :param workload_beat_rate: The workload_beat_rate of this OperationSummaryInfo.
        :type workload_beat_rate: float
        """
        self._workload_beat_rate = workload_beat_rate

    @property
    def user_name(self):
        r"""Gets the user_name of this OperationSummaryInfo.

        **参数解释**: 用户名 **取值范围**: 字符长度0-128位 

        :return: The user_name of this OperationSummaryInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this OperationSummaryInfo.

        **参数解释**: 用户名 **取值范围**: 字符长度0-128位 

        :param user_name: The user_name of this OperationSummaryInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def current_month_start(self):
        r"""Gets the current_month_start of this OperationSummaryInfo.

        **参数解释**: 当前月初时间戳 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The current_month_start of this OperationSummaryInfo.
        :rtype: int
        """
        return self._current_month_start

    @current_month_start.setter
    def current_month_start(self, current_month_start):
        r"""Sets the current_month_start of this OperationSummaryInfo.

        **参数解释**: 当前月初时间戳 **取值范围**: 最小值0，最大值9223372036854775807 

        :param current_month_start: The current_month_start of this OperationSummaryInfo.
        :type current_month_start: int
        """
        self._current_month_start = current_month_start

    @property
    def current_month_end(self):
        r"""Gets the current_month_end of this OperationSummaryInfo.

        **参数解释**: 当前月末时间戳 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The current_month_end of this OperationSummaryInfo.
        :rtype: int
        """
        return self._current_month_end

    @current_month_end.setter
    def current_month_end(self, current_month_end):
        r"""Sets the current_month_end of this OperationSummaryInfo.

        **参数解释**: 当前月末时间戳 **取值范围**: 最小值0，最大值9223372036854775807 

        :param current_month_end: The current_month_end of this OperationSummaryInfo.
        :type current_month_end: int
        """
        self._current_month_end = current_month_end

    @property
    def handled_security_event_num(self):
        r"""Gets the handled_security_event_num of this OperationSummaryInfo.

        **参数解释**: 处置的安全事件条数 **取值范围**: 最小值0，最大值2147483647 

        :return: The handled_security_event_num of this OperationSummaryInfo.
        :rtype: int
        """
        return self._handled_security_event_num

    @handled_security_event_num.setter
    def handled_security_event_num(self, handled_security_event_num):
        r"""Sets the handled_security_event_num of this OperationSummaryInfo.

        **参数解释**: 处置的安全事件条数 **取值范围**: 最小值0，最大值2147483647 

        :param handled_security_event_num: The handled_security_event_num of this OperationSummaryInfo.
        :type handled_security_event_num: int
        """
        self._handled_security_event_num = handled_security_event_num

    @property
    def total_workload_beat_rate(self):
        r"""Gets the total_workload_beat_rate of this OperationSummaryInfo.

        **参数解释**: 工作量打败的用户百分比 **取值范围**: 最小值0，最大值1 

        :return: The total_workload_beat_rate of this OperationSummaryInfo.
        :rtype: float
        """
        return self._total_workload_beat_rate

    @total_workload_beat_rate.setter
    def total_workload_beat_rate(self, total_workload_beat_rate):
        r"""Sets the total_workload_beat_rate of this OperationSummaryInfo.

        **参数解释**: 工作量打败的用户百分比 **取值范围**: 最小值0，最大值1 

        :param total_workload_beat_rate: The total_workload_beat_rate of this OperationSummaryInfo.
        :type total_workload_beat_rate: float
        """
        self._total_workload_beat_rate = total_workload_beat_rate

    @property
    def title(self):
        r"""Gets the title of this OperationSummaryInfo.

        **参数解释**:  称号 **取值范围**: -vul-fix-master: 补洞大师。 -vul-fix-expert: 漏洞修复小能手。 -baseline-handle: 风险配置处置高手。 -malware-file: 防病毒先锋。 -ransomware-event: 防勒索达人。 -web-tamper-event: 网站守卫。 

        :return: The title of this OperationSummaryInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this OperationSummaryInfo.

        **参数解释**:  称号 **取值范围**: -vul-fix-master: 补洞大师。 -vul-fix-expert: 漏洞修复小能手。 -baseline-handle: 风险配置处置高手。 -malware-file: 防病毒先锋。 -ransomware-event: 防勒索达人。 -web-tamper-event: 网站守卫。 

        :param title: The title of this OperationSummaryInfo.
        :type title: str
        """
        self._title = title

    @property
    def report_id(self):
        r"""Gets the report_id of this OperationSummaryInfo.

        **参数解释**: 时间字符串 **取值范围**: 字符长度0-32位 

        :return: The report_id of this OperationSummaryInfo.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this OperationSummaryInfo.

        **参数解释**: 时间字符串 **取值范围**: 字符长度0-32位 

        :param report_id: The report_id of this OperationSummaryInfo.
        :type report_id: str
        """
        self._report_id = report_id

    @property
    def current_month(self):
        r"""Gets the current_month of this OperationSummaryInfo.

        **参数解释**: 当前月份 **取值范围**: 最小值1，最大值12 

        :return: The current_month of this OperationSummaryInfo.
        :rtype: int
        """
        return self._current_month

    @current_month.setter
    def current_month(self, current_month):
        r"""Sets the current_month of this OperationSummaryInfo.

        **参数解释**: 当前月份 **取值范围**: 最小值1，最大值12 

        :param current_month: The current_month of this OperationSummaryInfo.
        :type current_month: int
        """
        self._current_month = current_month

    @property
    def work(self):
        r"""Gets the work of this OperationSummaryInfo.

        **参数解释**: 工作（哪个打败的用户占比高，显示哪个) **取值范围**: -vul-fix: 漏洞修复 -baseline-handle: 基线处置 -event-handle: 处置入侵事件 

        :return: The work of this OperationSummaryInfo.
        :rtype: str
        """
        return self._work

    @work.setter
    def work(self, work):
        r"""Sets the work of this OperationSummaryInfo.

        **参数解释**: 工作（哪个打败的用户占比高，显示哪个) **取值范围**: -vul-fix: 漏洞修复 -baseline-handle: 基线处置 -event-handle: 处置入侵事件 

        :param work: The work of this OperationSummaryInfo.
        :type work: str
        """
        self._work = work

    @property
    def create_time(self):
        r"""Gets the create_time of this OperationSummaryInfo.

        **参数解释**: 报告生成时间戳 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The create_time of this OperationSummaryInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this OperationSummaryInfo.

        **参数解释**: 报告生成时间戳 **取值范围**: 最小值0，最大值9223372036854775807 

        :param create_time: The create_time of this OperationSummaryInfo.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, OperationSummaryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
