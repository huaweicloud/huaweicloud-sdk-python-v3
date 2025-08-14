# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AntiVirusResultResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result_id': 'str',
        'malware_type': 'str',
        'malware_name': 'str',
        'severity': 'str',
        'task_id': 'str',
        'task_name': 'str',
        'file_info': 'ResultFileResponseInfo',
        'resource_info': 'ResultResourceResponseInfo',
        'event_type': 'int',
        'occur_time': 'int',
        'handle_status': 'str',
        'handle_method': 'str',
        'memo': 'str',
        'operate_accept_list': 'list[str]',
        'operate_detail_list': 'list[ResultDetailResponseInfo]',
        'isolate_tag': 'str'
    }

    attribute_map = {
        'result_id': 'result_id',
        'malware_type': 'malware_type',
        'malware_name': 'malware_name',
        'severity': 'severity',
        'task_id': 'task_id',
        'task_name': 'task_name',
        'file_info': 'file_info',
        'resource_info': 'resource_info',
        'event_type': 'event_type',
        'occur_time': 'occur_time',
        'handle_status': 'handle_status',
        'handle_method': 'handle_method',
        'memo': 'memo',
        'operate_accept_list': 'operate_accept_list',
        'operate_detail_list': 'operate_detail_list',
        'isolate_tag': 'isolate_tag'
    }

    def __init__(self, result_id=None, malware_type=None, malware_name=None, severity=None, task_id=None, task_name=None, file_info=None, resource_info=None, event_type=None, occur_time=None, handle_status=None, handle_method=None, memo=None, operate_accept_list=None, operate_detail_list=None, isolate_tag=None):
        r"""AntiVirusResultResponseInfo

        The model defined in huaweicloud sdk

        :param result_id: 病毒查杀结果ID
        :type result_id: str
        :param malware_type: 病毒类型
        :type malware_type: str
        :param malware_name: 病毒名称
        :type malware_name: str
        :param severity: 威胁等级，包含如下:   - Low：低危   - Medium：中危   - High：高危   - Critical：致命
        :type severity: str
        :param task_id: 任务ID
        :type task_id: str
        :param task_name: 任务名称
        :type task_name: str
        :param file_info: 
        :type file_info: :class:`huaweicloudsdkhss.v5.ResultFileResponseInfo`
        :param resource_info: 
        :type resource_info: :class:`huaweicloudsdkhss.v5.ResultResourceResponseInfo`
        :param event_type: 事件类型
        :type event_type: int
        :param occur_time: **参数解释**： 发生时间，毫秒 **取值范围**： 最小值0，最大值9223372036854775807 
        :type occur_time: int
        :param handle_status: **参数解释**： 处理状态 **取值范围**： - unhandled：未处理 - handled：已处理 
        :type handle_status: str
        :param handle_method: 处理方式，包含如下:   - mark_as_handled：手动处理   - ignore：忽略   - add_to_alarm_whitelist：加入告警白名单   - isolate_and_kill：隔离文件
        :type handle_method: str
        :param memo: 备注信息
        :type memo: str
        :param operate_accept_list: 支持的处理操作
        :type operate_accept_list: list[str]
        :param operate_detail_list: 操作详情信息列表（页面不展示）
        :type operate_detail_list: list[:class:`huaweicloudsdkhss.v5.ResultDetailResponseInfo`]
        :param isolate_tag: 自动隔离查杀标识
        :type isolate_tag: str
        """
        
        

        self._result_id = None
        self._malware_type = None
        self._malware_name = None
        self._severity = None
        self._task_id = None
        self._task_name = None
        self._file_info = None
        self._resource_info = None
        self._event_type = None
        self._occur_time = None
        self._handle_status = None
        self._handle_method = None
        self._memo = None
        self._operate_accept_list = None
        self._operate_detail_list = None
        self._isolate_tag = None
        self.discriminator = None

        if result_id is not None:
            self.result_id = result_id
        if malware_type is not None:
            self.malware_type = malware_type
        if malware_name is not None:
            self.malware_name = malware_name
        if severity is not None:
            self.severity = severity
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if file_info is not None:
            self.file_info = file_info
        if resource_info is not None:
            self.resource_info = resource_info
        if event_type is not None:
            self.event_type = event_type
        if occur_time is not None:
            self.occur_time = occur_time
        if handle_status is not None:
            self.handle_status = handle_status
        if handle_method is not None:
            self.handle_method = handle_method
        if memo is not None:
            self.memo = memo
        if operate_accept_list is not None:
            self.operate_accept_list = operate_accept_list
        if operate_detail_list is not None:
            self.operate_detail_list = operate_detail_list
        if isolate_tag is not None:
            self.isolate_tag = isolate_tag

    @property
    def result_id(self):
        r"""Gets the result_id of this AntiVirusResultResponseInfo.

        病毒查杀结果ID

        :return: The result_id of this AntiVirusResultResponseInfo.
        :rtype: str
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id):
        r"""Sets the result_id of this AntiVirusResultResponseInfo.

        病毒查杀结果ID

        :param result_id: The result_id of this AntiVirusResultResponseInfo.
        :type result_id: str
        """
        self._result_id = result_id

    @property
    def malware_type(self):
        r"""Gets the malware_type of this AntiVirusResultResponseInfo.

        病毒类型

        :return: The malware_type of this AntiVirusResultResponseInfo.
        :rtype: str
        """
        return self._malware_type

    @malware_type.setter
    def malware_type(self, malware_type):
        r"""Sets the malware_type of this AntiVirusResultResponseInfo.

        病毒类型

        :param malware_type: The malware_type of this AntiVirusResultResponseInfo.
        :type malware_type: str
        """
        self._malware_type = malware_type

    @property
    def malware_name(self):
        r"""Gets the malware_name of this AntiVirusResultResponseInfo.

        病毒名称

        :return: The malware_name of this AntiVirusResultResponseInfo.
        :rtype: str
        """
        return self._malware_name

    @malware_name.setter
    def malware_name(self, malware_name):
        r"""Sets the malware_name of this AntiVirusResultResponseInfo.

        病毒名称

        :param malware_name: The malware_name of this AntiVirusResultResponseInfo.
        :type malware_name: str
        """
        self._malware_name = malware_name

    @property
    def severity(self):
        r"""Gets the severity of this AntiVirusResultResponseInfo.

        威胁等级，包含如下:   - Low：低危   - Medium：中危   - High：高危   - Critical：致命

        :return: The severity of this AntiVirusResultResponseInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this AntiVirusResultResponseInfo.

        威胁等级，包含如下:   - Low：低危   - Medium：中危   - High：高危   - Critical：致命

        :param severity: The severity of this AntiVirusResultResponseInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def task_id(self):
        r"""Gets the task_id of this AntiVirusResultResponseInfo.

        任务ID

        :return: The task_id of this AntiVirusResultResponseInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this AntiVirusResultResponseInfo.

        任务ID

        :param task_id: The task_id of this AntiVirusResultResponseInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this AntiVirusResultResponseInfo.

        任务名称

        :return: The task_name of this AntiVirusResultResponseInfo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this AntiVirusResultResponseInfo.

        任务名称

        :param task_name: The task_name of this AntiVirusResultResponseInfo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def file_info(self):
        r"""Gets the file_info of this AntiVirusResultResponseInfo.

        :return: The file_info of this AntiVirusResultResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ResultFileResponseInfo`
        """
        return self._file_info

    @file_info.setter
    def file_info(self, file_info):
        r"""Sets the file_info of this AntiVirusResultResponseInfo.

        :param file_info: The file_info of this AntiVirusResultResponseInfo.
        :type file_info: :class:`huaweicloudsdkhss.v5.ResultFileResponseInfo`
        """
        self._file_info = file_info

    @property
    def resource_info(self):
        r"""Gets the resource_info of this AntiVirusResultResponseInfo.

        :return: The resource_info of this AntiVirusResultResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ResultResourceResponseInfo`
        """
        return self._resource_info

    @resource_info.setter
    def resource_info(self, resource_info):
        r"""Sets the resource_info of this AntiVirusResultResponseInfo.

        :param resource_info: The resource_info of this AntiVirusResultResponseInfo.
        :type resource_info: :class:`huaweicloudsdkhss.v5.ResultResourceResponseInfo`
        """
        self._resource_info = resource_info

    @property
    def event_type(self):
        r"""Gets the event_type of this AntiVirusResultResponseInfo.

        事件类型

        :return: The event_type of this AntiVirusResultResponseInfo.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this AntiVirusResultResponseInfo.

        事件类型

        :param event_type: The event_type of this AntiVirusResultResponseInfo.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def occur_time(self):
        r"""Gets the occur_time of this AntiVirusResultResponseInfo.

        **参数解释**： 发生时间，毫秒 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The occur_time of this AntiVirusResultResponseInfo.
        :rtype: int
        """
        return self._occur_time

    @occur_time.setter
    def occur_time(self, occur_time):
        r"""Sets the occur_time of this AntiVirusResultResponseInfo.

        **参数解释**： 发生时间，毫秒 **取值范围**： 最小值0，最大值9223372036854775807 

        :param occur_time: The occur_time of this AntiVirusResultResponseInfo.
        :type occur_time: int
        """
        self._occur_time = occur_time

    @property
    def handle_status(self):
        r"""Gets the handle_status of this AntiVirusResultResponseInfo.

        **参数解释**： 处理状态 **取值范围**： - unhandled：未处理 - handled：已处理 

        :return: The handle_status of this AntiVirusResultResponseInfo.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this AntiVirusResultResponseInfo.

        **参数解释**： 处理状态 **取值范围**： - unhandled：未处理 - handled：已处理 

        :param handle_status: The handle_status of this AntiVirusResultResponseInfo.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def handle_method(self):
        r"""Gets the handle_method of this AntiVirusResultResponseInfo.

        处理方式，包含如下:   - mark_as_handled：手动处理   - ignore：忽略   - add_to_alarm_whitelist：加入告警白名单   - isolate_and_kill：隔离文件

        :return: The handle_method of this AntiVirusResultResponseInfo.
        :rtype: str
        """
        return self._handle_method

    @handle_method.setter
    def handle_method(self, handle_method):
        r"""Sets the handle_method of this AntiVirusResultResponseInfo.

        处理方式，包含如下:   - mark_as_handled：手动处理   - ignore：忽略   - add_to_alarm_whitelist：加入告警白名单   - isolate_and_kill：隔离文件

        :param handle_method: The handle_method of this AntiVirusResultResponseInfo.
        :type handle_method: str
        """
        self._handle_method = handle_method

    @property
    def memo(self):
        r"""Gets the memo of this AntiVirusResultResponseInfo.

        备注信息

        :return: The memo of this AntiVirusResultResponseInfo.
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        r"""Sets the memo of this AntiVirusResultResponseInfo.

        备注信息

        :param memo: The memo of this AntiVirusResultResponseInfo.
        :type memo: str
        """
        self._memo = memo

    @property
    def operate_accept_list(self):
        r"""Gets the operate_accept_list of this AntiVirusResultResponseInfo.

        支持的处理操作

        :return: The operate_accept_list of this AntiVirusResultResponseInfo.
        :rtype: list[str]
        """
        return self._operate_accept_list

    @operate_accept_list.setter
    def operate_accept_list(self, operate_accept_list):
        r"""Sets the operate_accept_list of this AntiVirusResultResponseInfo.

        支持的处理操作

        :param operate_accept_list: The operate_accept_list of this AntiVirusResultResponseInfo.
        :type operate_accept_list: list[str]
        """
        self._operate_accept_list = operate_accept_list

    @property
    def operate_detail_list(self):
        r"""Gets the operate_detail_list of this AntiVirusResultResponseInfo.

        操作详情信息列表（页面不展示）

        :return: The operate_detail_list of this AntiVirusResultResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ResultDetailResponseInfo`]
        """
        return self._operate_detail_list

    @operate_detail_list.setter
    def operate_detail_list(self, operate_detail_list):
        r"""Sets the operate_detail_list of this AntiVirusResultResponseInfo.

        操作详情信息列表（页面不展示）

        :param operate_detail_list: The operate_detail_list of this AntiVirusResultResponseInfo.
        :type operate_detail_list: list[:class:`huaweicloudsdkhss.v5.ResultDetailResponseInfo`]
        """
        self._operate_detail_list = operate_detail_list

    @property
    def isolate_tag(self):
        r"""Gets the isolate_tag of this AntiVirusResultResponseInfo.

        自动隔离查杀标识

        :return: The isolate_tag of this AntiVirusResultResponseInfo.
        :rtype: str
        """
        return self._isolate_tag

    @isolate_tag.setter
    def isolate_tag(self, isolate_tag):
        r"""Sets the isolate_tag of this AntiVirusResultResponseInfo.

        自动隔离查杀标识

        :param isolate_tag: The isolate_tag of this AntiVirusResultResponseInfo.
        :type isolate_tag: str
        """
        self._isolate_tag = isolate_tag

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
        if not isinstance(other, AntiVirusResultResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
