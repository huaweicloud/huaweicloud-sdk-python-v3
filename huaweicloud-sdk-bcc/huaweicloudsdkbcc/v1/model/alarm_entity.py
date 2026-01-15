# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_record_id': 'str',
        'eps_id': 'str',
        'status': 'AlarmStatusEnum',
        'severity': 'str',
        'generate_time': 'str',
        'last_update_time': 'str',
        'duration': 'str',
        'alarm_type': 'AlarmTypeEnum',
        'namespace': 'AlarmNamespaceEnum',
        'abnormal_resource': 'str',
        'alarm_policy': 'str',
        'region_id': 'str',
        'alarm_rule_name': 'str',
        'alarm_rule_id': 'str',
        'alarm_datapoints': 'str',
        'metric': 'str',
        'condition': 'str',
        'alarm_actions': 'str',
        'ok_actions': 'str',
        'additional_info': 'str'
    }

    attribute_map = {
        'alarm_record_id': 'alarm_record_id',
        'eps_id': 'eps_id',
        'status': 'status',
        'severity': 'severity',
        'generate_time': 'generate_time',
        'last_update_time': 'last_update_time',
        'duration': 'duration',
        'alarm_type': 'alarm_type',
        'namespace': 'namespace',
        'abnormal_resource': 'abnormal_resource',
        'alarm_policy': 'alarm_policy',
        'region_id': 'region_id',
        'alarm_rule_name': 'alarm_rule_name',
        'alarm_rule_id': 'alarm_rule_id',
        'alarm_datapoints': 'alarm_datapoints',
        'metric': 'metric',
        'condition': 'condition',
        'alarm_actions': 'alarm_actions',
        'ok_actions': 'ok_actions',
        'additional_info': 'additional_info'
    }

    def __init__(self, alarm_record_id=None, eps_id=None, status=None, severity=None, generate_time=None, last_update_time=None, duration=None, alarm_type=None, namespace=None, abnormal_resource=None, alarm_policy=None, region_id=None, alarm_rule_name=None, alarm_rule_id=None, alarm_datapoints=None, metric=None, condition=None, alarm_actions=None, ok_actions=None, additional_info=None):
        r"""AlarmEntity

        The model defined in huaweicloud sdk

        :param alarm_record_id: 告警记录ID
        :type alarm_record_id: str
        :param eps_id: 企业项目ID
        :type eps_id: str
        :param status: 
        :type status: :class:`huaweicloudsdkbcc.v1.AlarmStatusEnum`
        :param severity: 告警级别,取值范围：1,2,3,4
        :type severity: str
        :param generate_time: 告警产生时间
        :type generate_time: str
        :param last_update_time: 最后更新时间
        :type last_update_time: str
        :param duration: 持续时长
        :type duration: str
        :param alarm_type: 
        :type alarm_type: :class:`huaweicloudsdkbcc.v1.AlarmTypeEnum`
        :param namespace: 
        :type namespace: :class:`huaweicloudsdkbcc.v1.AlarmNamespaceEnum`
        :param abnormal_resource: 异常资源数量
        :type abnormal_resource: str
        :param alarm_policy: 告警策略
        :type alarm_policy: str
        :param region_id: RegionID
        :type region_id: str
        :param alarm_rule_name: 告警规则名称
        :type alarm_rule_name: str
        :param alarm_rule_id: 告警规则ID
        :type alarm_rule_id: str
        :param alarm_datapoints: 计算出该条告警记录的资源监控数据上报时间和监控数值
        :type alarm_datapoints: str
        :param metric: 告警指标
        :type metric: str
        :param condition: 告警触发条件
        :type condition: str
        :param alarm_actions: 告警触发的动作
        :type alarm_actions: str
        :param ok_actions: 告警恢复触发的动作
        :type ok_actions: str
        :param additional_info: 告警记录额外字段
        :type additional_info: str
        """
        
        

        self._alarm_record_id = None
        self._eps_id = None
        self._status = None
        self._severity = None
        self._generate_time = None
        self._last_update_time = None
        self._duration = None
        self._alarm_type = None
        self._namespace = None
        self._abnormal_resource = None
        self._alarm_policy = None
        self._region_id = None
        self._alarm_rule_name = None
        self._alarm_rule_id = None
        self._alarm_datapoints = None
        self._metric = None
        self._condition = None
        self._alarm_actions = None
        self._ok_actions = None
        self._additional_info = None
        self.discriminator = None

        self.alarm_record_id = alarm_record_id
        if eps_id is not None:
            self.eps_id = eps_id
        if status is not None:
            self.status = status
        if severity is not None:
            self.severity = severity
        if generate_time is not None:
            self.generate_time = generate_time
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if duration is not None:
            self.duration = duration
        if alarm_type is not None:
            self.alarm_type = alarm_type
        if namespace is not None:
            self.namespace = namespace
        if abnormal_resource is not None:
            self.abnormal_resource = abnormal_resource
        if alarm_policy is not None:
            self.alarm_policy = alarm_policy
        if region_id is not None:
            self.region_id = region_id
        if alarm_rule_name is not None:
            self.alarm_rule_name = alarm_rule_name
        self.alarm_rule_id = alarm_rule_id
        if alarm_datapoints is not None:
            self.alarm_datapoints = alarm_datapoints
        if metric is not None:
            self.metric = metric
        if condition is not None:
            self.condition = condition
        if alarm_actions is not None:
            self.alarm_actions = alarm_actions
        if ok_actions is not None:
            self.ok_actions = ok_actions
        if additional_info is not None:
            self.additional_info = additional_info

    @property
    def alarm_record_id(self):
        r"""Gets the alarm_record_id of this AlarmEntity.

        告警记录ID

        :return: The alarm_record_id of this AlarmEntity.
        :rtype: str
        """
        return self._alarm_record_id

    @alarm_record_id.setter
    def alarm_record_id(self, alarm_record_id):
        r"""Sets the alarm_record_id of this AlarmEntity.

        告警记录ID

        :param alarm_record_id: The alarm_record_id of this AlarmEntity.
        :type alarm_record_id: str
        """
        self._alarm_record_id = alarm_record_id

    @property
    def eps_id(self):
        r"""Gets the eps_id of this AlarmEntity.

        企业项目ID

        :return: The eps_id of this AlarmEntity.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        r"""Sets the eps_id of this AlarmEntity.

        企业项目ID

        :param eps_id: The eps_id of this AlarmEntity.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def status(self):
        r"""Gets the status of this AlarmEntity.

        :return: The status of this AlarmEntity.
        :rtype: :class:`huaweicloudsdkbcc.v1.AlarmStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AlarmEntity.

        :param status: The status of this AlarmEntity.
        :type status: :class:`huaweicloudsdkbcc.v1.AlarmStatusEnum`
        """
        self._status = status

    @property
    def severity(self):
        r"""Gets the severity of this AlarmEntity.

        告警级别,取值范围：1,2,3,4

        :return: The severity of this AlarmEntity.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this AlarmEntity.

        告警级别,取值范围：1,2,3,4

        :param severity: The severity of this AlarmEntity.
        :type severity: str
        """
        self._severity = severity

    @property
    def generate_time(self):
        r"""Gets the generate_time of this AlarmEntity.

        告警产生时间

        :return: The generate_time of this AlarmEntity.
        :rtype: str
        """
        return self._generate_time

    @generate_time.setter
    def generate_time(self, generate_time):
        r"""Sets the generate_time of this AlarmEntity.

        告警产生时间

        :param generate_time: The generate_time of this AlarmEntity.
        :type generate_time: str
        """
        self._generate_time = generate_time

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this AlarmEntity.

        最后更新时间

        :return: The last_update_time of this AlarmEntity.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this AlarmEntity.

        最后更新时间

        :param last_update_time: The last_update_time of this AlarmEntity.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def duration(self):
        r"""Gets the duration of this AlarmEntity.

        持续时长

        :return: The duration of this AlarmEntity.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this AlarmEntity.

        持续时长

        :param duration: The duration of this AlarmEntity.
        :type duration: str
        """
        self._duration = duration

    @property
    def alarm_type(self):
        r"""Gets the alarm_type of this AlarmEntity.

        :return: The alarm_type of this AlarmEntity.
        :rtype: :class:`huaweicloudsdkbcc.v1.AlarmTypeEnum`
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        r"""Sets the alarm_type of this AlarmEntity.

        :param alarm_type: The alarm_type of this AlarmEntity.
        :type alarm_type: :class:`huaweicloudsdkbcc.v1.AlarmTypeEnum`
        """
        self._alarm_type = alarm_type

    @property
    def namespace(self):
        r"""Gets the namespace of this AlarmEntity.

        :return: The namespace of this AlarmEntity.
        :rtype: :class:`huaweicloudsdkbcc.v1.AlarmNamespaceEnum`
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this AlarmEntity.

        :param namespace: The namespace of this AlarmEntity.
        :type namespace: :class:`huaweicloudsdkbcc.v1.AlarmNamespaceEnum`
        """
        self._namespace = namespace

    @property
    def abnormal_resource(self):
        r"""Gets the abnormal_resource of this AlarmEntity.

        异常资源数量

        :return: The abnormal_resource of this AlarmEntity.
        :rtype: str
        """
        return self._abnormal_resource

    @abnormal_resource.setter
    def abnormal_resource(self, abnormal_resource):
        r"""Sets the abnormal_resource of this AlarmEntity.

        异常资源数量

        :param abnormal_resource: The abnormal_resource of this AlarmEntity.
        :type abnormal_resource: str
        """
        self._abnormal_resource = abnormal_resource

    @property
    def alarm_policy(self):
        r"""Gets the alarm_policy of this AlarmEntity.

        告警策略

        :return: The alarm_policy of this AlarmEntity.
        :rtype: str
        """
        return self._alarm_policy

    @alarm_policy.setter
    def alarm_policy(self, alarm_policy):
        r"""Sets the alarm_policy of this AlarmEntity.

        告警策略

        :param alarm_policy: The alarm_policy of this AlarmEntity.
        :type alarm_policy: str
        """
        self._alarm_policy = alarm_policy

    @property
    def region_id(self):
        r"""Gets the region_id of this AlarmEntity.

        RegionID

        :return: The region_id of this AlarmEntity.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this AlarmEntity.

        RegionID

        :param region_id: The region_id of this AlarmEntity.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def alarm_rule_name(self):
        r"""Gets the alarm_rule_name of this AlarmEntity.

        告警规则名称

        :return: The alarm_rule_name of this AlarmEntity.
        :rtype: str
        """
        return self._alarm_rule_name

    @alarm_rule_name.setter
    def alarm_rule_name(self, alarm_rule_name):
        r"""Sets the alarm_rule_name of this AlarmEntity.

        告警规则名称

        :param alarm_rule_name: The alarm_rule_name of this AlarmEntity.
        :type alarm_rule_name: str
        """
        self._alarm_rule_name = alarm_rule_name

    @property
    def alarm_rule_id(self):
        r"""Gets the alarm_rule_id of this AlarmEntity.

        告警规则ID

        :return: The alarm_rule_id of this AlarmEntity.
        :rtype: str
        """
        return self._alarm_rule_id

    @alarm_rule_id.setter
    def alarm_rule_id(self, alarm_rule_id):
        r"""Sets the alarm_rule_id of this AlarmEntity.

        告警规则ID

        :param alarm_rule_id: The alarm_rule_id of this AlarmEntity.
        :type alarm_rule_id: str
        """
        self._alarm_rule_id = alarm_rule_id

    @property
    def alarm_datapoints(self):
        r"""Gets the alarm_datapoints of this AlarmEntity.

        计算出该条告警记录的资源监控数据上报时间和监控数值

        :return: The alarm_datapoints of this AlarmEntity.
        :rtype: str
        """
        return self._alarm_datapoints

    @alarm_datapoints.setter
    def alarm_datapoints(self, alarm_datapoints):
        r"""Sets the alarm_datapoints of this AlarmEntity.

        计算出该条告警记录的资源监控数据上报时间和监控数值

        :param alarm_datapoints: The alarm_datapoints of this AlarmEntity.
        :type alarm_datapoints: str
        """
        self._alarm_datapoints = alarm_datapoints

    @property
    def metric(self):
        r"""Gets the metric of this AlarmEntity.

        告警指标

        :return: The metric of this AlarmEntity.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this AlarmEntity.

        告警指标

        :param metric: The metric of this AlarmEntity.
        :type metric: str
        """
        self._metric = metric

    @property
    def condition(self):
        r"""Gets the condition of this AlarmEntity.

        告警触发条件

        :return: The condition of this AlarmEntity.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this AlarmEntity.

        告警触发条件

        :param condition: The condition of this AlarmEntity.
        :type condition: str
        """
        self._condition = condition

    @property
    def alarm_actions(self):
        r"""Gets the alarm_actions of this AlarmEntity.

        告警触发的动作

        :return: The alarm_actions of this AlarmEntity.
        :rtype: str
        """
        return self._alarm_actions

    @alarm_actions.setter
    def alarm_actions(self, alarm_actions):
        r"""Sets the alarm_actions of this AlarmEntity.

        告警触发的动作

        :param alarm_actions: The alarm_actions of this AlarmEntity.
        :type alarm_actions: str
        """
        self._alarm_actions = alarm_actions

    @property
    def ok_actions(self):
        r"""Gets the ok_actions of this AlarmEntity.

        告警恢复触发的动作

        :return: The ok_actions of this AlarmEntity.
        :rtype: str
        """
        return self._ok_actions

    @ok_actions.setter
    def ok_actions(self, ok_actions):
        r"""Sets the ok_actions of this AlarmEntity.

        告警恢复触发的动作

        :param ok_actions: The ok_actions of this AlarmEntity.
        :type ok_actions: str
        """
        self._ok_actions = ok_actions

    @property
    def additional_info(self):
        r"""Gets the additional_info of this AlarmEntity.

        告警记录额外字段

        :return: The additional_info of this AlarmEntity.
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        r"""Sets the additional_info of this AlarmEntity.

        告警记录额外字段

        :param additional_info: The additional_info of this AlarmEntity.
        :type additional_info: str
        """
        self._additional_info = additional_info

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
        if not isinstance(other, AlarmEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
