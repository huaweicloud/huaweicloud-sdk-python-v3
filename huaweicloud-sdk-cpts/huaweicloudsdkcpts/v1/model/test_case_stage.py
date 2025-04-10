# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCaseStage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate_mode': 'int',
        'name': 'str',
        'time': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'issue_num': 'int',
        'count': 'int',
        'pressure_mode': 'int',
        'tps_value': 'int',
        'current_user_num': 'int',
        'current_tps': 'int',
        'voltage_regulating_mode': 'int',
        'maximum': 'int',
        'minimum': 'int',
        'loop_count': 'int',
        'max_duration': 'int',
        'ramp_up': 'int',
        'peak_load_kpis': 'StageKpiItems',
        'step_duration': 'int',
        'step_size': 'int'
    }

    attribute_map = {
        'operate_mode': 'operate_mode',
        'name': 'name',
        'time': 'time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'issue_num': 'issue_num',
        'count': 'count',
        'pressure_mode': 'pressure_mode',
        'tps_value': 'tps_value',
        'current_user_num': 'current_user_num',
        'current_tps': 'current_tps',
        'voltage_regulating_mode': 'voltage_regulating_mode',
        'maximum': 'maximum',
        'minimum': 'minimum',
        'loop_count': 'loop_count',
        'max_duration': 'max_duration',
        'ramp_up': 'ramp_up',
        'peak_load_kpis': 'peak_load_kpis',
        'step_duration': 'step_duration',
        'step_size': 'step_size'
    }

    def __init__(self, operate_mode=None, name=None, time=None, start_time=None, end_time=None, issue_num=None, count=None, pressure_mode=None, tps_value=None, current_user_num=None, current_tps=None, voltage_regulating_mode=None, maximum=None, minimum=None, loop_count=None, max_duration=None, ramp_up=None, peak_load_kpis=None, step_duration=None, step_size=None):
        r"""TestCaseStage

        The model defined in huaweicloud sdk

        :param operate_mode: 压力阶段模式，0：时长模式；1：次数模式
        :type operate_mode: int
        :param name: 阶段名称
        :type name: str
        :param time: 压测时长（单位：秒）
        :type time: int
        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        :param issue_num: 最大并发数
        :type issue_num: int
        :param count: 次数模式发送总次数
        :type count: int
        :param pressure_mode: 压力模式，0：并发模式；1：TPS模式；2：摸高模式；3：浪涌并发模式；4：浪涌TPS模式；5：震荡并发模式；6：震荡TPS模式；7：智能摸高模式
        :type pressure_mode: int
        :param tps_value: TPS模式下TPS值
        :type tps_value: int
        :param current_user_num: 起始并发数
        :type current_user_num: int
        :param current_tps: 起始tps值
        :type current_tps: int
        :param voltage_regulating_mode: 调压模式，0：自动调压模式；1：手动调压模式
        :type voltage_regulating_mode: int
        :param maximum: 浪涌/浪涌模式下最大并发数
        :type maximum: int
        :param minimum: 浪涌/浪涌模式下最小并发数
        :type minimum: int
        :param loop_count: 震荡/浪涌次数
        :type loop_count: int
        :param max_duration: 浪涌模式下峰值持续时间
        :type max_duration: int
        :param ramp_up: 摸高模式下爬坡时长（单位：秒）
        :type ramp_up: int
        :param peak_load_kpis: 
        :type peak_load_kpis: :class:`huaweicloudsdkcpts.v1.StageKpiItems`
        :param step_duration: 智能摸高模式下单步执行时长
        :type step_duration: int
        :param step_size: 智能摸高模式下递增并发数
        :type step_size: int
        """
        
        

        self._operate_mode = None
        self._name = None
        self._time = None
        self._start_time = None
        self._end_time = None
        self._issue_num = None
        self._count = None
        self._pressure_mode = None
        self._tps_value = None
        self._current_user_num = None
        self._current_tps = None
        self._voltage_regulating_mode = None
        self._maximum = None
        self._minimum = None
        self._loop_count = None
        self._max_duration = None
        self._ramp_up = None
        self._peak_load_kpis = None
        self._step_duration = None
        self._step_size = None
        self.discriminator = None

        if operate_mode is not None:
            self.operate_mode = operate_mode
        if name is not None:
            self.name = name
        if time is not None:
            self.time = time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if issue_num is not None:
            self.issue_num = issue_num
        if count is not None:
            self.count = count
        if pressure_mode is not None:
            self.pressure_mode = pressure_mode
        if tps_value is not None:
            self.tps_value = tps_value
        if current_user_num is not None:
            self.current_user_num = current_user_num
        if current_tps is not None:
            self.current_tps = current_tps
        if voltage_regulating_mode is not None:
            self.voltage_regulating_mode = voltage_regulating_mode
        if maximum is not None:
            self.maximum = maximum
        if minimum is not None:
            self.minimum = minimum
        if loop_count is not None:
            self.loop_count = loop_count
        if max_duration is not None:
            self.max_duration = max_duration
        if ramp_up is not None:
            self.ramp_up = ramp_up
        if peak_load_kpis is not None:
            self.peak_load_kpis = peak_load_kpis
        if step_duration is not None:
            self.step_duration = step_duration
        if step_size is not None:
            self.step_size = step_size

    @property
    def operate_mode(self):
        r"""Gets the operate_mode of this TestCaseStage.

        压力阶段模式，0：时长模式；1：次数模式

        :return: The operate_mode of this TestCaseStage.
        :rtype: int
        """
        return self._operate_mode

    @operate_mode.setter
    def operate_mode(self, operate_mode):
        r"""Sets the operate_mode of this TestCaseStage.

        压力阶段模式，0：时长模式；1：次数模式

        :param operate_mode: The operate_mode of this TestCaseStage.
        :type operate_mode: int
        """
        self._operate_mode = operate_mode

    @property
    def name(self):
        r"""Gets the name of this TestCaseStage.

        阶段名称

        :return: The name of this TestCaseStage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TestCaseStage.

        阶段名称

        :param name: The name of this TestCaseStage.
        :type name: str
        """
        self._name = name

    @property
    def time(self):
        r"""Gets the time of this TestCaseStage.

        压测时长（单位：秒）

        :return: The time of this TestCaseStage.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this TestCaseStage.

        压测时长（单位：秒）

        :param time: The time of this TestCaseStage.
        :type time: int
        """
        self._time = time

    @property
    def start_time(self):
        r"""Gets the start_time of this TestCaseStage.

        开始时间

        :return: The start_time of this TestCaseStage.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TestCaseStage.

        开始时间

        :param start_time: The start_time of this TestCaseStage.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this TestCaseStage.

        结束时间

        :return: The end_time of this TestCaseStage.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this TestCaseStage.

        结束时间

        :param end_time: The end_time of this TestCaseStage.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def issue_num(self):
        r"""Gets the issue_num of this TestCaseStage.

        最大并发数

        :return: The issue_num of this TestCaseStage.
        :rtype: int
        """
        return self._issue_num

    @issue_num.setter
    def issue_num(self, issue_num):
        r"""Sets the issue_num of this TestCaseStage.

        最大并发数

        :param issue_num: The issue_num of this TestCaseStage.
        :type issue_num: int
        """
        self._issue_num = issue_num

    @property
    def count(self):
        r"""Gets the count of this TestCaseStage.

        次数模式发送总次数

        :return: The count of this TestCaseStage.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this TestCaseStage.

        次数模式发送总次数

        :param count: The count of this TestCaseStage.
        :type count: int
        """
        self._count = count

    @property
    def pressure_mode(self):
        r"""Gets the pressure_mode of this TestCaseStage.

        压力模式，0：并发模式；1：TPS模式；2：摸高模式；3：浪涌并发模式；4：浪涌TPS模式；5：震荡并发模式；6：震荡TPS模式；7：智能摸高模式

        :return: The pressure_mode of this TestCaseStage.
        :rtype: int
        """
        return self._pressure_mode

    @pressure_mode.setter
    def pressure_mode(self, pressure_mode):
        r"""Sets the pressure_mode of this TestCaseStage.

        压力模式，0：并发模式；1：TPS模式；2：摸高模式；3：浪涌并发模式；4：浪涌TPS模式；5：震荡并发模式；6：震荡TPS模式；7：智能摸高模式

        :param pressure_mode: The pressure_mode of this TestCaseStage.
        :type pressure_mode: int
        """
        self._pressure_mode = pressure_mode

    @property
    def tps_value(self):
        r"""Gets the tps_value of this TestCaseStage.

        TPS模式下TPS值

        :return: The tps_value of this TestCaseStage.
        :rtype: int
        """
        return self._tps_value

    @tps_value.setter
    def tps_value(self, tps_value):
        r"""Sets the tps_value of this TestCaseStage.

        TPS模式下TPS值

        :param tps_value: The tps_value of this TestCaseStage.
        :type tps_value: int
        """
        self._tps_value = tps_value

    @property
    def current_user_num(self):
        r"""Gets the current_user_num of this TestCaseStage.

        起始并发数

        :return: The current_user_num of this TestCaseStage.
        :rtype: int
        """
        return self._current_user_num

    @current_user_num.setter
    def current_user_num(self, current_user_num):
        r"""Sets the current_user_num of this TestCaseStage.

        起始并发数

        :param current_user_num: The current_user_num of this TestCaseStage.
        :type current_user_num: int
        """
        self._current_user_num = current_user_num

    @property
    def current_tps(self):
        r"""Gets the current_tps of this TestCaseStage.

        起始tps值

        :return: The current_tps of this TestCaseStage.
        :rtype: int
        """
        return self._current_tps

    @current_tps.setter
    def current_tps(self, current_tps):
        r"""Sets the current_tps of this TestCaseStage.

        起始tps值

        :param current_tps: The current_tps of this TestCaseStage.
        :type current_tps: int
        """
        self._current_tps = current_tps

    @property
    def voltage_regulating_mode(self):
        r"""Gets the voltage_regulating_mode of this TestCaseStage.

        调压模式，0：自动调压模式；1：手动调压模式

        :return: The voltage_regulating_mode of this TestCaseStage.
        :rtype: int
        """
        return self._voltage_regulating_mode

    @voltage_regulating_mode.setter
    def voltage_regulating_mode(self, voltage_regulating_mode):
        r"""Sets the voltage_regulating_mode of this TestCaseStage.

        调压模式，0：自动调压模式；1：手动调压模式

        :param voltage_regulating_mode: The voltage_regulating_mode of this TestCaseStage.
        :type voltage_regulating_mode: int
        """
        self._voltage_regulating_mode = voltage_regulating_mode

    @property
    def maximum(self):
        r"""Gets the maximum of this TestCaseStage.

        浪涌/浪涌模式下最大并发数

        :return: The maximum of this TestCaseStage.
        :rtype: int
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        r"""Sets the maximum of this TestCaseStage.

        浪涌/浪涌模式下最大并发数

        :param maximum: The maximum of this TestCaseStage.
        :type maximum: int
        """
        self._maximum = maximum

    @property
    def minimum(self):
        r"""Gets the minimum of this TestCaseStage.

        浪涌/浪涌模式下最小并发数

        :return: The minimum of this TestCaseStage.
        :rtype: int
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        r"""Sets the minimum of this TestCaseStage.

        浪涌/浪涌模式下最小并发数

        :param minimum: The minimum of this TestCaseStage.
        :type minimum: int
        """
        self._minimum = minimum

    @property
    def loop_count(self):
        r"""Gets the loop_count of this TestCaseStage.

        震荡/浪涌次数

        :return: The loop_count of this TestCaseStage.
        :rtype: int
        """
        return self._loop_count

    @loop_count.setter
    def loop_count(self, loop_count):
        r"""Sets the loop_count of this TestCaseStage.

        震荡/浪涌次数

        :param loop_count: The loop_count of this TestCaseStage.
        :type loop_count: int
        """
        self._loop_count = loop_count

    @property
    def max_duration(self):
        r"""Gets the max_duration of this TestCaseStage.

        浪涌模式下峰值持续时间

        :return: The max_duration of this TestCaseStage.
        :rtype: int
        """
        return self._max_duration

    @max_duration.setter
    def max_duration(self, max_duration):
        r"""Sets the max_duration of this TestCaseStage.

        浪涌模式下峰值持续时间

        :param max_duration: The max_duration of this TestCaseStage.
        :type max_duration: int
        """
        self._max_duration = max_duration

    @property
    def ramp_up(self):
        r"""Gets the ramp_up of this TestCaseStage.

        摸高模式下爬坡时长（单位：秒）

        :return: The ramp_up of this TestCaseStage.
        :rtype: int
        """
        return self._ramp_up

    @ramp_up.setter
    def ramp_up(self, ramp_up):
        r"""Sets the ramp_up of this TestCaseStage.

        摸高模式下爬坡时长（单位：秒）

        :param ramp_up: The ramp_up of this TestCaseStage.
        :type ramp_up: int
        """
        self._ramp_up = ramp_up

    @property
    def peak_load_kpis(self):
        r"""Gets the peak_load_kpis of this TestCaseStage.

        :return: The peak_load_kpis of this TestCaseStage.
        :rtype: :class:`huaweicloudsdkcpts.v1.StageKpiItems`
        """
        return self._peak_load_kpis

    @peak_load_kpis.setter
    def peak_load_kpis(self, peak_load_kpis):
        r"""Sets the peak_load_kpis of this TestCaseStage.

        :param peak_load_kpis: The peak_load_kpis of this TestCaseStage.
        :type peak_load_kpis: :class:`huaweicloudsdkcpts.v1.StageKpiItems`
        """
        self._peak_load_kpis = peak_load_kpis

    @property
    def step_duration(self):
        r"""Gets the step_duration of this TestCaseStage.

        智能摸高模式下单步执行时长

        :return: The step_duration of this TestCaseStage.
        :rtype: int
        """
        return self._step_duration

    @step_duration.setter
    def step_duration(self, step_duration):
        r"""Sets the step_duration of this TestCaseStage.

        智能摸高模式下单步执行时长

        :param step_duration: The step_duration of this TestCaseStage.
        :type step_duration: int
        """
        self._step_duration = step_duration

    @property
    def step_size(self):
        r"""Gets the step_size of this TestCaseStage.

        智能摸高模式下递增并发数

        :return: The step_size of this TestCaseStage.
        :rtype: int
        """
        return self._step_size

    @step_size.setter
    def step_size(self, step_size):
        r"""Sets the step_size of this TestCaseStage.

        智能摸高模式下递增并发数

        :param step_size: The step_size of this TestCaseStage.
        :type step_size: int
        """
        self._step_size = step_size

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
        if not isinstance(other, TestCaseStage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
