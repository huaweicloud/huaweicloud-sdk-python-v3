# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmHistoryItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_id': 'str',
        'alarm_id': 'str',
        'name': 'str',
        'status': 'str',
        'type': 'str',
        'level': 'int',
        'begin_time': 'str',
        'metric': 'AlarmMetric',
        'condition': 'AlarmCondition',
        'additional_info': 'AdditionalInfo',
        'data_points': 'list[DataPointInfo]'
    }

    attribute_map = {
        'record_id': 'record_id',
        'alarm_id': 'alarm_id',
        'name': 'name',
        'status': 'status',
        'type': 'type',
        'level': 'level',
        'begin_time': 'begin_time',
        'metric': 'metric',
        'condition': 'condition',
        'additional_info': 'additional_info',
        'data_points': 'data_points'
    }

    def __init__(self, record_id=None, alarm_id=None, name=None, status=None, type=None, level=None, begin_time=None, metric=None, condition=None, additional_info=None, data_points=None):
        r"""AlarmHistoryItem

        The model defined in huaweicloud sdk

        :param record_id: 告警记录。
        :type record_id: str
        :param alarm_id: 告警规则ID。
        :type alarm_id: str
        :param name: 告警规则的名称。
        :type name: str
        :param status: 告警记录的状态，取值为ok，alarm，invalid； ok为正常，alarm为告警，invalid为已失效。
        :type status: str
        :param type: 告警规则类型 | ALL_INSTANCE为全部资源指标告警， RESOURCE_GROUP为资源分组指标告警， MULTI_INSTANCE为指定资源指标告警， EVENT.SYS为系统事件告警， EVENT.CUSTOM自定义事件告警， DNSHealthCheck为健康检查告警。
        :type type: str
        :param level: 告警记录的告警级别，值为1,2,3,4；1为紧急，2为重要，3为次要，4为提示。
        :type level: int
        :param begin_time: 产生时间,UTC时间。
        :type begin_time: str
        :param metric: 
        :type metric: :class:`huaweicloudsdkworkspace.v2.AlarmMetric`
        :param condition: 
        :type condition: :class:`huaweicloudsdkworkspace.v2.AlarmCondition`
        :param additional_info: 
        :type additional_info: :class:`huaweicloudsdkworkspace.v2.AdditionalInfo`
        :param data_points: 计算出该条告警记录的资源监控数据上报时间和监控数值。
        :type data_points: list[:class:`huaweicloudsdkworkspace.v2.DataPointInfo`]
        """
        
        

        self._record_id = None
        self._alarm_id = None
        self._name = None
        self._status = None
        self._type = None
        self._level = None
        self._begin_time = None
        self._metric = None
        self._condition = None
        self._additional_info = None
        self._data_points = None
        self.discriminator = None

        if record_id is not None:
            self.record_id = record_id
        if alarm_id is not None:
            self.alarm_id = alarm_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if level is not None:
            self.level = level
        if begin_time is not None:
            self.begin_time = begin_time
        if metric is not None:
            self.metric = metric
        if condition is not None:
            self.condition = condition
        if additional_info is not None:
            self.additional_info = additional_info
        if data_points is not None:
            self.data_points = data_points

    @property
    def record_id(self):
        r"""Gets the record_id of this AlarmHistoryItem.

        告警记录。

        :return: The record_id of this AlarmHistoryItem.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        r"""Sets the record_id of this AlarmHistoryItem.

        告警记录。

        :param record_id: The record_id of this AlarmHistoryItem.
        :type record_id: str
        """
        self._record_id = record_id

    @property
    def alarm_id(self):
        r"""Gets the alarm_id of this AlarmHistoryItem.

        告警规则ID。

        :return: The alarm_id of this AlarmHistoryItem.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        r"""Sets the alarm_id of this AlarmHistoryItem.

        告警规则ID。

        :param alarm_id: The alarm_id of this AlarmHistoryItem.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def name(self):
        r"""Gets the name of this AlarmHistoryItem.

        告警规则的名称。

        :return: The name of this AlarmHistoryItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AlarmHistoryItem.

        告警规则的名称。

        :param name: The name of this AlarmHistoryItem.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this AlarmHistoryItem.

        告警记录的状态，取值为ok，alarm，invalid； ok为正常，alarm为告警，invalid为已失效。

        :return: The status of this AlarmHistoryItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AlarmHistoryItem.

        告警记录的状态，取值为ok，alarm，invalid； ok为正常，alarm为告警，invalid为已失效。

        :param status: The status of this AlarmHistoryItem.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this AlarmHistoryItem.

        告警规则类型 | ALL_INSTANCE为全部资源指标告警， RESOURCE_GROUP为资源分组指标告警， MULTI_INSTANCE为指定资源指标告警， EVENT.SYS为系统事件告警， EVENT.CUSTOM自定义事件告警， DNSHealthCheck为健康检查告警。

        :return: The type of this AlarmHistoryItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AlarmHistoryItem.

        告警规则类型 | ALL_INSTANCE为全部资源指标告警， RESOURCE_GROUP为资源分组指标告警， MULTI_INSTANCE为指定资源指标告警， EVENT.SYS为系统事件告警， EVENT.CUSTOM自定义事件告警， DNSHealthCheck为健康检查告警。

        :param type: The type of this AlarmHistoryItem.
        :type type: str
        """
        self._type = type

    @property
    def level(self):
        r"""Gets the level of this AlarmHistoryItem.

        告警记录的告警级别，值为1,2,3,4；1为紧急，2为重要，3为次要，4为提示。

        :return: The level of this AlarmHistoryItem.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this AlarmHistoryItem.

        告警记录的告警级别，值为1,2,3,4；1为紧急，2为重要，3为次要，4为提示。

        :param level: The level of this AlarmHistoryItem.
        :type level: int
        """
        self._level = level

    @property
    def begin_time(self):
        r"""Gets the begin_time of this AlarmHistoryItem.

        产生时间,UTC时间。

        :return: The begin_time of this AlarmHistoryItem.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this AlarmHistoryItem.

        产生时间,UTC时间。

        :param begin_time: The begin_time of this AlarmHistoryItem.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def metric(self):
        r"""Gets the metric of this AlarmHistoryItem.

        :return: The metric of this AlarmHistoryItem.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AlarmMetric`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this AlarmHistoryItem.

        :param metric: The metric of this AlarmHistoryItem.
        :type metric: :class:`huaweicloudsdkworkspace.v2.AlarmMetric`
        """
        self._metric = metric

    @property
    def condition(self):
        r"""Gets the condition of this AlarmHistoryItem.

        :return: The condition of this AlarmHistoryItem.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AlarmCondition`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this AlarmHistoryItem.

        :param condition: The condition of this AlarmHistoryItem.
        :type condition: :class:`huaweicloudsdkworkspace.v2.AlarmCondition`
        """
        self._condition = condition

    @property
    def additional_info(self):
        r"""Gets the additional_info of this AlarmHistoryItem.

        :return: The additional_info of this AlarmHistoryItem.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AdditionalInfo`
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        r"""Sets the additional_info of this AlarmHistoryItem.

        :param additional_info: The additional_info of this AlarmHistoryItem.
        :type additional_info: :class:`huaweicloudsdkworkspace.v2.AdditionalInfo`
        """
        self._additional_info = additional_info

    @property
    def data_points(self):
        r"""Gets the data_points of this AlarmHistoryItem.

        计算出该条告警记录的资源监控数据上报时间和监控数值。

        :return: The data_points of this AlarmHistoryItem.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.DataPointInfo`]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        r"""Sets the data_points of this AlarmHistoryItem.

        计算出该条告警记录的资源监控数据上报时间和监控数值。

        :param data_points: The data_points of this AlarmHistoryItem.
        :type data_points: list[:class:`huaweicloudsdkworkspace.v2.DataPointInfo`]
        """
        self._data_points = data_points

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
        if not isinstance(other, AlarmHistoryItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
