# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStatisticsApiRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'mode': 'str',
        'roma_app_id': 'str',
        'api_id': 'str',
        'cycle': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'duration': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'mode': 'mode',
        'roma_app_id': 'roma_app_id',
        'api_id': 'api_id',
        'cycle': 'cycle',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'duration': 'duration'
    }

    def __init__(self, instance_id=None, mode=None, roma_app_id=None, api_id=None, cycle=None, start_time=None, end_time=None, duration=None):
        """ListStatisticsApiRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param mode: 查询模式，默认为INSTANCE * ALL：实例下所有调用应用，要求主帐号权限 * APP：指定集成应用 * API：指定API * INSTANCE：实例，默认值  注意：mode &#x3D; APP或ALL时，接口响应中不返回cycle，api_id，group_id，provider，register_time，status字段
        :type mode: str
        :param roma_app_id: 集成应用编号，查询模式为APP时必填
        :type roma_app_id: str
        :param api_id: API编号，查询模式为API时必填
        :type api_id: str
        :param cycle: 查询统计周期 * minute：分钟 * hour：小时 * day：天
        :type cycle: str
        :param start_time: 开始时间，格式：2020-06-18 10:00:01
        :type start_time: str
        :param end_time: 结束时间，格式：2020-06-18 23:00:00
        :type end_time: str
        :param duration: 统计时长格式：整数+单位（m、h），m：分钟，h：小时，可支持小时与分钟的组合。例如：1h或2h45m * 同时给定start_time和end_time优先查询[start_time, end_time] * start_time不存在，end_time和duration存在且合法，则查询区间为[end_time - duration, end_time] * start_time和end_time不存在，duration存在且合法，令end_time&#x3D;now，则查询区间为[end_time - duration, end_time] * start_time，end_time和duration都不存在，报错missing time range parameters。 * duration最长查询范围：小时最长支持72小时，分钟最长支持90分钟。
        :type duration: str
        """
        
        

        self._instance_id = None
        self._mode = None
        self._roma_app_id = None
        self._api_id = None
        self._cycle = None
        self._start_time = None
        self._end_time = None
        self._duration = None
        self.discriminator = None

        self.instance_id = instance_id
        if mode is not None:
            self.mode = mode
        if roma_app_id is not None:
            self.roma_app_id = roma_app_id
        if api_id is not None:
            self.api_id = api_id
        if cycle is not None:
            self.cycle = cycle
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if duration is not None:
            self.duration = duration

    @property
    def instance_id(self):
        """Gets the instance_id of this ListStatisticsApiRequest.

        实例ID

        :return: The instance_id of this ListStatisticsApiRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListStatisticsApiRequest.

        实例ID

        :param instance_id: The instance_id of this ListStatisticsApiRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def mode(self):
        """Gets the mode of this ListStatisticsApiRequest.

        查询模式，默认为INSTANCE * ALL：实例下所有调用应用，要求主帐号权限 * APP：指定集成应用 * API：指定API * INSTANCE：实例，默认值  注意：mode = APP或ALL时，接口响应中不返回cycle，api_id，group_id，provider，register_time，status字段

        :return: The mode of this ListStatisticsApiRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ListStatisticsApiRequest.

        查询模式，默认为INSTANCE * ALL：实例下所有调用应用，要求主帐号权限 * APP：指定集成应用 * API：指定API * INSTANCE：实例，默认值  注意：mode = APP或ALL时，接口响应中不返回cycle，api_id，group_id，provider，register_time，status字段

        :param mode: The mode of this ListStatisticsApiRequest.
        :type mode: str
        """
        self._mode = mode

    @property
    def roma_app_id(self):
        """Gets the roma_app_id of this ListStatisticsApiRequest.

        集成应用编号，查询模式为APP时必填

        :return: The roma_app_id of this ListStatisticsApiRequest.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        """Sets the roma_app_id of this ListStatisticsApiRequest.

        集成应用编号，查询模式为APP时必填

        :param roma_app_id: The roma_app_id of this ListStatisticsApiRequest.
        :type roma_app_id: str
        """
        self._roma_app_id = roma_app_id

    @property
    def api_id(self):
        """Gets the api_id of this ListStatisticsApiRequest.

        API编号，查询模式为API时必填

        :return: The api_id of this ListStatisticsApiRequest.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this ListStatisticsApiRequest.

        API编号，查询模式为API时必填

        :param api_id: The api_id of this ListStatisticsApiRequest.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def cycle(self):
        """Gets the cycle of this ListStatisticsApiRequest.

        查询统计周期 * minute：分钟 * hour：小时 * day：天

        :return: The cycle of this ListStatisticsApiRequest.
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this ListStatisticsApiRequest.

        查询统计周期 * minute：分钟 * hour：小时 * day：天

        :param cycle: The cycle of this ListStatisticsApiRequest.
        :type cycle: str
        """
        self._cycle = cycle

    @property
    def start_time(self):
        """Gets the start_time of this ListStatisticsApiRequest.

        开始时间，格式：2020-06-18 10:00:01

        :return: The start_time of this ListStatisticsApiRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListStatisticsApiRequest.

        开始时间，格式：2020-06-18 10:00:01

        :param start_time: The start_time of this ListStatisticsApiRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListStatisticsApiRequest.

        结束时间，格式：2020-06-18 23:00:00

        :return: The end_time of this ListStatisticsApiRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListStatisticsApiRequest.

        结束时间，格式：2020-06-18 23:00:00

        :param end_time: The end_time of this ListStatisticsApiRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def duration(self):
        """Gets the duration of this ListStatisticsApiRequest.

        统计时长格式：整数+单位（m、h），m：分钟，h：小时，可支持小时与分钟的组合。例如：1h或2h45m * 同时给定start_time和end_time优先查询[start_time, end_time] * start_time不存在，end_time和duration存在且合法，则查询区间为[end_time - duration, end_time] * start_time和end_time不存在，duration存在且合法，令end_time=now，则查询区间为[end_time - duration, end_time] * start_time，end_time和duration都不存在，报错missing time range parameters。 * duration最长查询范围：小时最长支持72小时，分钟最长支持90分钟。

        :return: The duration of this ListStatisticsApiRequest.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ListStatisticsApiRequest.

        统计时长格式：整数+单位（m、h），m：分钟，h：小时，可支持小时与分钟的组合。例如：1h或2h45m * 同时给定start_time和end_time优先查询[start_time, end_time] * start_time不存在，end_time和duration存在且合法，则查询区间为[end_time - duration, end_time] * start_time和end_time不存在，duration存在且合法，令end_time=now，则查询区间为[end_time - duration, end_time] * start_time，end_time和duration都不存在，报错missing time range parameters。 * duration最长查询范围：小时最长支持72小时，分钟最长支持90分钟。

        :param duration: The duration of this ListStatisticsApiRequest.
        :type duration: str
        """
        self._duration = duration

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
        if not isinstance(other, ListStatisticsApiRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
