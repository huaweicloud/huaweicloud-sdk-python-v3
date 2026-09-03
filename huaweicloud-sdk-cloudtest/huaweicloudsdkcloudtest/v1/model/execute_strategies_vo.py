# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteStrategiesVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'advanced_config': 'AdvancedConfig',
        'daily_report_enable': 'str',
        'execute_model': 'str',
        'execute_period_begin': 'str',
        'execute_period_end': 'str',
        'execute_start_time': 'int',
        'execution_time': 'list[ExecutionTime]',
        'executor_option': 'dict(str, object)',
        'executor_parameters': 'dict(str, object)',
        'failed_retry_times': 'int',
        'interval_in_seconds': 'int',
        'ip_key': 'str',
        'location_ids': 'list[str]',
        'operate_notice': 'OperateNotice',
        'pbi': 'str',
        'protocol_test': 'ProtocolTestVo',
        'repeat_times': 'int',
        'service_name_cbg': 'str',
        'service_scope_cbg': 'str',
        'service_version_cbg': 'str',
        'test_node_server': 'str',
        'timeout_mil_sec': 'int',
        'timer_expression': 'str',
        'token': 'str'
    }

    attribute_map = {
        'advanced_config': 'advancedConfig',
        'daily_report_enable': 'dailyReportEnable',
        'execute_model': 'executeModel',
        'execute_period_begin': 'executePeriodBegin',
        'execute_period_end': 'executePeriodEnd',
        'execute_start_time': 'executeStartTime',
        'execution_time': 'executionTime',
        'executor_option': 'executorOption',
        'executor_parameters': 'executorParameters',
        'failed_retry_times': 'failedRetryTimes',
        'interval_in_seconds': 'intervalInSeconds',
        'ip_key': 'ipKey',
        'location_ids': 'location_ids',
        'operate_notice': 'operateNotice',
        'pbi': 'pbi',
        'protocol_test': 'protocol_test',
        'repeat_times': 'repeatTimes',
        'service_name_cbg': 'serviceNameCBG',
        'service_scope_cbg': 'serviceScopeCBG',
        'service_version_cbg': 'serviceVersionCBG',
        'test_node_server': 'testNodeServer',
        'timeout_mil_sec': 'timeoutMilSec',
        'timer_expression': 'timerExpression',
        'token': 'token'
    }

    def __init__(self, advanced_config=None, daily_report_enable=None, execute_model=None, execute_period_begin=None, execute_period_end=None, execute_start_time=None, execution_time=None, executor_option=None, executor_parameters=None, failed_retry_times=None, interval_in_seconds=None, ip_key=None, location_ids=None, operate_notice=None, pbi=None, protocol_test=None, repeat_times=None, service_name_cbg=None, service_scope_cbg=None, service_version_cbg=None, test_node_server=None, timeout_mil_sec=None, timer_expression=None, token=None):
        r"""ExecuteStrategiesVo

        The model defined in huaweicloud sdk

        :param advanced_config: 
        :type advanced_config: :class:`huaweicloudsdkcloudtest.v1.AdvancedConfig`
        :param daily_report_enable: 日报 0 关闭 1开启
        :type daily_report_enable: str
        :param execute_model: 执行顺序 串行 1 并行 2 
        :type execute_model: str
        :param execute_period_begin: 执行区间，开始时间
        :type execute_period_begin: str
        :param execute_period_end: 执行区间，开始时间
        :type execute_period_end: str
        :param execute_start_time: 执行模式 立即执行 0，延后执行: 延后执行时间
        :type execute_start_time: int
        :param execution_time: 任务执行时间段 -- 重新启用，任务采用多段时间区间执行，quartz需要用这个参数
        :type execution_time: list[:class:`huaweicloudsdkcloudtest.v1.ExecutionTime`]
        :param executor_option: 目前无用字段
        :type executor_option: dict(str, object)
        :param executor_parameters: deployTest修改properties使用，字段不固定。小网拨测使用该字段修改properties中的ip
        :type executor_parameters: dict(str, object)
        :param failed_retry_times: 失败重试次数
        :type failed_retry_times: int
        :param interval_in_seconds: 执行间隔
        :type interval_in_seconds: int
        :param ip_key: deployTest使用
        :type ip_key: str
        :param location_ids: 执行区域
        :type location_ids: list[str]
        :param operate_notice: 
        :type operate_notice: :class:`huaweicloudsdkcloudtest.v1.OperateNotice`
        :param pbi: deployTest使用
        :type pbi: str
        :param protocol_test: 
        :type protocol_test: :class:`huaweicloudsdkcloudtest.v1.ProtocolTestVo`
        :param repeat_times: 重试次数，冒烟测试使用
        :type repeat_times: int
        :param service_name_cbg: deployTest使用
        :type service_name_cbg: str
        :param service_scope_cbg: deployTest使用
        :type service_scope_cbg: str
        :param service_version_cbg: deployTest使用
        :type service_version_cbg: str
        :param test_node_server: 不再使用
        :type test_node_server: str
        :param timeout_mil_sec: 超时时间
        :type timeout_mil_sec: int
        :param timer_expression: 执行时间表达式
        :type timer_expression: str
        :param token: deployTest使用
        :type token: str
        """
        
        

        self._advanced_config = None
        self._daily_report_enable = None
        self._execute_model = None
        self._execute_period_begin = None
        self._execute_period_end = None
        self._execute_start_time = None
        self._execution_time = None
        self._executor_option = None
        self._executor_parameters = None
        self._failed_retry_times = None
        self._interval_in_seconds = None
        self._ip_key = None
        self._location_ids = None
        self._operate_notice = None
        self._pbi = None
        self._protocol_test = None
        self._repeat_times = None
        self._service_name_cbg = None
        self._service_scope_cbg = None
        self._service_version_cbg = None
        self._test_node_server = None
        self._timeout_mil_sec = None
        self._timer_expression = None
        self._token = None
        self.discriminator = None

        if advanced_config is not None:
            self.advanced_config = advanced_config
        if daily_report_enable is not None:
            self.daily_report_enable = daily_report_enable
        if execute_model is not None:
            self.execute_model = execute_model
        if execute_period_begin is not None:
            self.execute_period_begin = execute_period_begin
        if execute_period_end is not None:
            self.execute_period_end = execute_period_end
        if execute_start_time is not None:
            self.execute_start_time = execute_start_time
        if execution_time is not None:
            self.execution_time = execution_time
        if executor_option is not None:
            self.executor_option = executor_option
        if executor_parameters is not None:
            self.executor_parameters = executor_parameters
        if failed_retry_times is not None:
            self.failed_retry_times = failed_retry_times
        if interval_in_seconds is not None:
            self.interval_in_seconds = interval_in_seconds
        if ip_key is not None:
            self.ip_key = ip_key
        if location_ids is not None:
            self.location_ids = location_ids
        if operate_notice is not None:
            self.operate_notice = operate_notice
        if pbi is not None:
            self.pbi = pbi
        if protocol_test is not None:
            self.protocol_test = protocol_test
        if repeat_times is not None:
            self.repeat_times = repeat_times
        if service_name_cbg is not None:
            self.service_name_cbg = service_name_cbg
        if service_scope_cbg is not None:
            self.service_scope_cbg = service_scope_cbg
        if service_version_cbg is not None:
            self.service_version_cbg = service_version_cbg
        if test_node_server is not None:
            self.test_node_server = test_node_server
        if timeout_mil_sec is not None:
            self.timeout_mil_sec = timeout_mil_sec
        if timer_expression is not None:
            self.timer_expression = timer_expression
        if token is not None:
            self.token = token

    @property
    def advanced_config(self):
        r"""Gets the advanced_config of this ExecuteStrategiesVo.

        :return: The advanced_config of this ExecuteStrategiesVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AdvancedConfig`
        """
        return self._advanced_config

    @advanced_config.setter
    def advanced_config(self, advanced_config):
        r"""Sets the advanced_config of this ExecuteStrategiesVo.

        :param advanced_config: The advanced_config of this ExecuteStrategiesVo.
        :type advanced_config: :class:`huaweicloudsdkcloudtest.v1.AdvancedConfig`
        """
        self._advanced_config = advanced_config

    @property
    def daily_report_enable(self):
        r"""Gets the daily_report_enable of this ExecuteStrategiesVo.

        日报 0 关闭 1开启

        :return: The daily_report_enable of this ExecuteStrategiesVo.
        :rtype: str
        """
        return self._daily_report_enable

    @daily_report_enable.setter
    def daily_report_enable(self, daily_report_enable):
        r"""Sets the daily_report_enable of this ExecuteStrategiesVo.

        日报 0 关闭 1开启

        :param daily_report_enable: The daily_report_enable of this ExecuteStrategiesVo.
        :type daily_report_enable: str
        """
        self._daily_report_enable = daily_report_enable

    @property
    def execute_model(self):
        r"""Gets the execute_model of this ExecuteStrategiesVo.

        执行顺序 串行 1 并行 2 

        :return: The execute_model of this ExecuteStrategiesVo.
        :rtype: str
        """
        return self._execute_model

    @execute_model.setter
    def execute_model(self, execute_model):
        r"""Sets the execute_model of this ExecuteStrategiesVo.

        执行顺序 串行 1 并行 2 

        :param execute_model: The execute_model of this ExecuteStrategiesVo.
        :type execute_model: str
        """
        self._execute_model = execute_model

    @property
    def execute_period_begin(self):
        r"""Gets the execute_period_begin of this ExecuteStrategiesVo.

        执行区间，开始时间

        :return: The execute_period_begin of this ExecuteStrategiesVo.
        :rtype: str
        """
        return self._execute_period_begin

    @execute_period_begin.setter
    def execute_period_begin(self, execute_period_begin):
        r"""Sets the execute_period_begin of this ExecuteStrategiesVo.

        执行区间，开始时间

        :param execute_period_begin: The execute_period_begin of this ExecuteStrategiesVo.
        :type execute_period_begin: str
        """
        self._execute_period_begin = execute_period_begin

    @property
    def execute_period_end(self):
        r"""Gets the execute_period_end of this ExecuteStrategiesVo.

        执行区间，开始时间

        :return: The execute_period_end of this ExecuteStrategiesVo.
        :rtype: str
        """
        return self._execute_period_end

    @execute_period_end.setter
    def execute_period_end(self, execute_period_end):
        r"""Sets the execute_period_end of this ExecuteStrategiesVo.

        执行区间，开始时间

        :param execute_period_end: The execute_period_end of this ExecuteStrategiesVo.
        :type execute_period_end: str
        """
        self._execute_period_end = execute_period_end

    @property
    def execute_start_time(self):
        r"""Gets the execute_start_time of this ExecuteStrategiesVo.

        执行模式 立即执行 0，延后执行: 延后执行时间

        :return: The execute_start_time of this ExecuteStrategiesVo.
        :rtype: int
        """
        return self._execute_start_time

    @execute_start_time.setter
    def execute_start_time(self, execute_start_time):
        r"""Sets the execute_start_time of this ExecuteStrategiesVo.

        执行模式 立即执行 0，延后执行: 延后执行时间

        :param execute_start_time: The execute_start_time of this ExecuteStrategiesVo.
        :type execute_start_time: int
        """
        self._execute_start_time = execute_start_time

    @property
    def execution_time(self):
        r"""Gets the execution_time of this ExecuteStrategiesVo.

        任务执行时间段 -- 重新启用，任务采用多段时间区间执行，quartz需要用这个参数

        :return: The execution_time of this ExecuteStrategiesVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.ExecutionTime`]
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        r"""Sets the execution_time of this ExecuteStrategiesVo.

        任务执行时间段 -- 重新启用，任务采用多段时间区间执行，quartz需要用这个参数

        :param execution_time: The execution_time of this ExecuteStrategiesVo.
        :type execution_time: list[:class:`huaweicloudsdkcloudtest.v1.ExecutionTime`]
        """
        self._execution_time = execution_time

    @property
    def executor_option(self):
        r"""Gets the executor_option of this ExecuteStrategiesVo.

        目前无用字段

        :return: The executor_option of this ExecuteStrategiesVo.
        :rtype: dict(str, object)
        """
        return self._executor_option

    @executor_option.setter
    def executor_option(self, executor_option):
        r"""Sets the executor_option of this ExecuteStrategiesVo.

        目前无用字段

        :param executor_option: The executor_option of this ExecuteStrategiesVo.
        :type executor_option: dict(str, object)
        """
        self._executor_option = executor_option

    @property
    def executor_parameters(self):
        r"""Gets the executor_parameters of this ExecuteStrategiesVo.

        deployTest修改properties使用，字段不固定。小网拨测使用该字段修改properties中的ip

        :return: The executor_parameters of this ExecuteStrategiesVo.
        :rtype: dict(str, object)
        """
        return self._executor_parameters

    @executor_parameters.setter
    def executor_parameters(self, executor_parameters):
        r"""Sets the executor_parameters of this ExecuteStrategiesVo.

        deployTest修改properties使用，字段不固定。小网拨测使用该字段修改properties中的ip

        :param executor_parameters: The executor_parameters of this ExecuteStrategiesVo.
        :type executor_parameters: dict(str, object)
        """
        self._executor_parameters = executor_parameters

    @property
    def failed_retry_times(self):
        r"""Gets the failed_retry_times of this ExecuteStrategiesVo.

        失败重试次数

        :return: The failed_retry_times of this ExecuteStrategiesVo.
        :rtype: int
        """
        return self._failed_retry_times

    @failed_retry_times.setter
    def failed_retry_times(self, failed_retry_times):
        r"""Sets the failed_retry_times of this ExecuteStrategiesVo.

        失败重试次数

        :param failed_retry_times: The failed_retry_times of this ExecuteStrategiesVo.
        :type failed_retry_times: int
        """
        self._failed_retry_times = failed_retry_times

    @property
    def interval_in_seconds(self):
        r"""Gets the interval_in_seconds of this ExecuteStrategiesVo.

        执行间隔

        :return: The interval_in_seconds of this ExecuteStrategiesVo.
        :rtype: int
        """
        return self._interval_in_seconds

    @interval_in_seconds.setter
    def interval_in_seconds(self, interval_in_seconds):
        r"""Sets the interval_in_seconds of this ExecuteStrategiesVo.

        执行间隔

        :param interval_in_seconds: The interval_in_seconds of this ExecuteStrategiesVo.
        :type interval_in_seconds: int
        """
        self._interval_in_seconds = interval_in_seconds

    @property
    def ip_key(self):
        r"""Gets the ip_key of this ExecuteStrategiesVo.

        deployTest使用

        :return: The ip_key of this ExecuteStrategiesVo.
        :rtype: str
        """
        return self._ip_key

    @ip_key.setter
    def ip_key(self, ip_key):
        r"""Sets the ip_key of this ExecuteStrategiesVo.

        deployTest使用

        :param ip_key: The ip_key of this ExecuteStrategiesVo.
        :type ip_key: str
        """
        self._ip_key = ip_key

    @property
    def location_ids(self):
        r"""Gets the location_ids of this ExecuteStrategiesVo.

        执行区域

        :return: The location_ids of this ExecuteStrategiesVo.
        :rtype: list[str]
        """
        return self._location_ids

    @location_ids.setter
    def location_ids(self, location_ids):
        r"""Sets the location_ids of this ExecuteStrategiesVo.

        执行区域

        :param location_ids: The location_ids of this ExecuteStrategiesVo.
        :type location_ids: list[str]
        """
        self._location_ids = location_ids

    @property
    def operate_notice(self):
        r"""Gets the operate_notice of this ExecuteStrategiesVo.

        :return: The operate_notice of this ExecuteStrategiesVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.OperateNotice`
        """
        return self._operate_notice

    @operate_notice.setter
    def operate_notice(self, operate_notice):
        r"""Sets the operate_notice of this ExecuteStrategiesVo.

        :param operate_notice: The operate_notice of this ExecuteStrategiesVo.
        :type operate_notice: :class:`huaweicloudsdkcloudtest.v1.OperateNotice`
        """
        self._operate_notice = operate_notice

    @property
    def pbi(self):
        r"""Gets the pbi of this ExecuteStrategiesVo.

        deployTest使用

        :return: The pbi of this ExecuteStrategiesVo.
        :rtype: str
        """
        return self._pbi

    @pbi.setter
    def pbi(self, pbi):
        r"""Sets the pbi of this ExecuteStrategiesVo.

        deployTest使用

        :param pbi: The pbi of this ExecuteStrategiesVo.
        :type pbi: str
        """
        self._pbi = pbi

    @property
    def protocol_test(self):
        r"""Gets the protocol_test of this ExecuteStrategiesVo.

        :return: The protocol_test of this ExecuteStrategiesVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ProtocolTestVo`
        """
        return self._protocol_test

    @protocol_test.setter
    def protocol_test(self, protocol_test):
        r"""Sets the protocol_test of this ExecuteStrategiesVo.

        :param protocol_test: The protocol_test of this ExecuteStrategiesVo.
        :type protocol_test: :class:`huaweicloudsdkcloudtest.v1.ProtocolTestVo`
        """
        self._protocol_test = protocol_test

    @property
    def repeat_times(self):
        r"""Gets the repeat_times of this ExecuteStrategiesVo.

        重试次数，冒烟测试使用

        :return: The repeat_times of this ExecuteStrategiesVo.
        :rtype: int
        """
        return self._repeat_times

    @repeat_times.setter
    def repeat_times(self, repeat_times):
        r"""Sets the repeat_times of this ExecuteStrategiesVo.

        重试次数，冒烟测试使用

        :param repeat_times: The repeat_times of this ExecuteStrategiesVo.
        :type repeat_times: int
        """
        self._repeat_times = repeat_times

    @property
    def service_name_cbg(self):
        r"""Gets the service_name_cbg of this ExecuteStrategiesVo.

        deployTest使用

        :return: The service_name_cbg of this ExecuteStrategiesVo.
        :rtype: str
        """
        return self._service_name_cbg

    @service_name_cbg.setter
    def service_name_cbg(self, service_name_cbg):
        r"""Sets the service_name_cbg of this ExecuteStrategiesVo.

        deployTest使用

        :param service_name_cbg: The service_name_cbg of this ExecuteStrategiesVo.
        :type service_name_cbg: str
        """
        self._service_name_cbg = service_name_cbg

    @property
    def service_scope_cbg(self):
        r"""Gets the service_scope_cbg of this ExecuteStrategiesVo.

        deployTest使用

        :return: The service_scope_cbg of this ExecuteStrategiesVo.
        :rtype: str
        """
        return self._service_scope_cbg

    @service_scope_cbg.setter
    def service_scope_cbg(self, service_scope_cbg):
        r"""Sets the service_scope_cbg of this ExecuteStrategiesVo.

        deployTest使用

        :param service_scope_cbg: The service_scope_cbg of this ExecuteStrategiesVo.
        :type service_scope_cbg: str
        """
        self._service_scope_cbg = service_scope_cbg

    @property
    def service_version_cbg(self):
        r"""Gets the service_version_cbg of this ExecuteStrategiesVo.

        deployTest使用

        :return: The service_version_cbg of this ExecuteStrategiesVo.
        :rtype: str
        """
        return self._service_version_cbg

    @service_version_cbg.setter
    def service_version_cbg(self, service_version_cbg):
        r"""Sets the service_version_cbg of this ExecuteStrategiesVo.

        deployTest使用

        :param service_version_cbg: The service_version_cbg of this ExecuteStrategiesVo.
        :type service_version_cbg: str
        """
        self._service_version_cbg = service_version_cbg

    @property
    def test_node_server(self):
        r"""Gets the test_node_server of this ExecuteStrategiesVo.

        不再使用

        :return: The test_node_server of this ExecuteStrategiesVo.
        :rtype: str
        """
        return self._test_node_server

    @test_node_server.setter
    def test_node_server(self, test_node_server):
        r"""Sets the test_node_server of this ExecuteStrategiesVo.

        不再使用

        :param test_node_server: The test_node_server of this ExecuteStrategiesVo.
        :type test_node_server: str
        """
        self._test_node_server = test_node_server

    @property
    def timeout_mil_sec(self):
        r"""Gets the timeout_mil_sec of this ExecuteStrategiesVo.

        超时时间

        :return: The timeout_mil_sec of this ExecuteStrategiesVo.
        :rtype: int
        """
        return self._timeout_mil_sec

    @timeout_mil_sec.setter
    def timeout_mil_sec(self, timeout_mil_sec):
        r"""Sets the timeout_mil_sec of this ExecuteStrategiesVo.

        超时时间

        :param timeout_mil_sec: The timeout_mil_sec of this ExecuteStrategiesVo.
        :type timeout_mil_sec: int
        """
        self._timeout_mil_sec = timeout_mil_sec

    @property
    def timer_expression(self):
        r"""Gets the timer_expression of this ExecuteStrategiesVo.

        执行时间表达式

        :return: The timer_expression of this ExecuteStrategiesVo.
        :rtype: str
        """
        return self._timer_expression

    @timer_expression.setter
    def timer_expression(self, timer_expression):
        r"""Sets the timer_expression of this ExecuteStrategiesVo.

        执行时间表达式

        :param timer_expression: The timer_expression of this ExecuteStrategiesVo.
        :type timer_expression: str
        """
        self._timer_expression = timer_expression

    @property
    def token(self):
        r"""Gets the token of this ExecuteStrategiesVo.

        deployTest使用

        :return: The token of this ExecuteStrategiesVo.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this ExecuteStrategiesVo.

        deployTest使用

        :param token: The token of this ExecuteStrategiesVo.
        :type token: str
        """
        self._token = token

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
        if not isinstance(other, ExecuteStrategiesVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
