# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMetricOrEventAlarmRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'limit': 'str',
        'offset': 'str',
        'sort_by': 'str',
        'event_source': 'str',
        'event_severity': 'str',
        'alarm_rule_status': 'str',
        'alarm_rule_type': 'str',
        'prom_instance_id': 'str',
        'bind_notification_rule_id': 'str',
        'related_cce_clusters': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'limit': 'limit',
        'offset': 'offset',
        'sort_by': 'sort_by',
        'event_source': 'event_source',
        'event_severity': 'event_severity',
        'alarm_rule_status': 'alarm_rule_status',
        'alarm_rule_type': 'alarm_rule_type',
        'prom_instance_id': 'prom_instance_id',
        'bind_notification_rule_id': 'bind_notification_rule_id',
        'related_cce_clusters': 'related_cce_clusters',
        'enterprise_project_id': 'Enterprise-Project-Id'
    }

    def __init__(self, name=None, limit=None, offset=None, sort_by=None, event_source=None, event_severity=None, alarm_rule_status=None, alarm_rule_type=None, prom_instance_id=None, bind_notification_rule_id=None, related_cce_clusters=None, enterprise_project_id=None):
        r"""ListMetricOrEventAlarmRuleRequest

        The model defined in huaweicloud sdk

        :param name: 告警规则名称。
        :type name: str
        :param limit: 用于限制本次返回的结果数据条数。
        :type limit: str
        :param offset: 分页查询起始位置，为非负整数。
        :type offset: str
        :param sort_by: 根据告警规则名称或者告警创建时间排序。 - alarm_rule_name.asc - alarm_create_time.desc
        :type sort_by: str
        :param event_source: 事件告警规则事件来源。 - “RDS” - “EVS” - “CCE” - “LTS” - “AOM”
        :type event_source: str
        :param event_severity: 事件告警级别。 - “Critical\&quot; - “Major” - “Minor” - “Info”
        :type event_severity: str
        :param alarm_rule_status: 告警规则状态。 - “OK”：正常 - “alarm”：超限阈值 - “Effective”：生效中 - “Invalid”：停用中
        :type alarm_rule_status: str
        :param alarm_rule_type: 告警规则类型。 - “metric”：指标告警规则 - “event”：事件告警规则
        :type alarm_rule_type: str
        :param prom_instance_id: Prometheus实例id。
        :type prom_instance_id: str
        :param bind_notification_rule_id: 绑定的告警行动规则名称。
        :type bind_notification_rule_id: str
        :param related_cce_clusters: CCE集群id。
        :type related_cce_clusters: str
        :param enterprise_project_id: 企业项目id。  - 查询单个企业项目下实例，填写企业项目id。  - 查询所有企业项目下实例，填写“all_granted_eps”。
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._limit = None
        self._offset = None
        self._sort_by = None
        self._event_source = None
        self._event_severity = None
        self._alarm_rule_status = None
        self._alarm_rule_type = None
        self._prom_instance_id = None
        self._bind_notification_rule_id = None
        self._related_cce_clusters = None
        self._enterprise_project_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_by is not None:
            self.sort_by = sort_by
        if event_source is not None:
            self.event_source = event_source
        if event_severity is not None:
            self.event_severity = event_severity
        if alarm_rule_status is not None:
            self.alarm_rule_status = alarm_rule_status
        if alarm_rule_type is not None:
            self.alarm_rule_type = alarm_rule_type
        if prom_instance_id is not None:
            self.prom_instance_id = prom_instance_id
        if bind_notification_rule_id is not None:
            self.bind_notification_rule_id = bind_notification_rule_id
        if related_cce_clusters is not None:
            self.related_cce_clusters = related_cce_clusters
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        r"""Gets the name of this ListMetricOrEventAlarmRuleRequest.

        告警规则名称。

        :return: The name of this ListMetricOrEventAlarmRuleRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListMetricOrEventAlarmRuleRequest.

        告警规则名称。

        :param name: The name of this ListMetricOrEventAlarmRuleRequest.
        :type name: str
        """
        self._name = name

    @property
    def limit(self):
        r"""Gets the limit of this ListMetricOrEventAlarmRuleRequest.

        用于限制本次返回的结果数据条数。

        :return: The limit of this ListMetricOrEventAlarmRuleRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListMetricOrEventAlarmRuleRequest.

        用于限制本次返回的结果数据条数。

        :param limit: The limit of this ListMetricOrEventAlarmRuleRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListMetricOrEventAlarmRuleRequest.

        分页查询起始位置，为非负整数。

        :return: The offset of this ListMetricOrEventAlarmRuleRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListMetricOrEventAlarmRuleRequest.

        分页查询起始位置，为非负整数。

        :param offset: The offset of this ListMetricOrEventAlarmRuleRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListMetricOrEventAlarmRuleRequest.

        根据告警规则名称或者告警创建时间排序。 - alarm_rule_name.asc - alarm_create_time.desc

        :return: The sort_by of this ListMetricOrEventAlarmRuleRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListMetricOrEventAlarmRuleRequest.

        根据告警规则名称或者告警创建时间排序。 - alarm_rule_name.asc - alarm_create_time.desc

        :param sort_by: The sort_by of this ListMetricOrEventAlarmRuleRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def event_source(self):
        r"""Gets the event_source of this ListMetricOrEventAlarmRuleRequest.

        事件告警规则事件来源。 - “RDS” - “EVS” - “CCE” - “LTS” - “AOM”

        :return: The event_source of this ListMetricOrEventAlarmRuleRequest.
        :rtype: str
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        r"""Sets the event_source of this ListMetricOrEventAlarmRuleRequest.

        事件告警规则事件来源。 - “RDS” - “EVS” - “CCE” - “LTS” - “AOM”

        :param event_source: The event_source of this ListMetricOrEventAlarmRuleRequest.
        :type event_source: str
        """
        self._event_source = event_source

    @property
    def event_severity(self):
        r"""Gets the event_severity of this ListMetricOrEventAlarmRuleRequest.

        事件告警级别。 - “Critical\" - “Major” - “Minor” - “Info”

        :return: The event_severity of this ListMetricOrEventAlarmRuleRequest.
        :rtype: str
        """
        return self._event_severity

    @event_severity.setter
    def event_severity(self, event_severity):
        r"""Sets the event_severity of this ListMetricOrEventAlarmRuleRequest.

        事件告警级别。 - “Critical\" - “Major” - “Minor” - “Info”

        :param event_severity: The event_severity of this ListMetricOrEventAlarmRuleRequest.
        :type event_severity: str
        """
        self._event_severity = event_severity

    @property
    def alarm_rule_status(self):
        r"""Gets the alarm_rule_status of this ListMetricOrEventAlarmRuleRequest.

        告警规则状态。 - “OK”：正常 - “alarm”：超限阈值 - “Effective”：生效中 - “Invalid”：停用中

        :return: The alarm_rule_status of this ListMetricOrEventAlarmRuleRequest.
        :rtype: str
        """
        return self._alarm_rule_status

    @alarm_rule_status.setter
    def alarm_rule_status(self, alarm_rule_status):
        r"""Sets the alarm_rule_status of this ListMetricOrEventAlarmRuleRequest.

        告警规则状态。 - “OK”：正常 - “alarm”：超限阈值 - “Effective”：生效中 - “Invalid”：停用中

        :param alarm_rule_status: The alarm_rule_status of this ListMetricOrEventAlarmRuleRequest.
        :type alarm_rule_status: str
        """
        self._alarm_rule_status = alarm_rule_status

    @property
    def alarm_rule_type(self):
        r"""Gets the alarm_rule_type of this ListMetricOrEventAlarmRuleRequest.

        告警规则类型。 - “metric”：指标告警规则 - “event”：事件告警规则

        :return: The alarm_rule_type of this ListMetricOrEventAlarmRuleRequest.
        :rtype: str
        """
        return self._alarm_rule_type

    @alarm_rule_type.setter
    def alarm_rule_type(self, alarm_rule_type):
        r"""Sets the alarm_rule_type of this ListMetricOrEventAlarmRuleRequest.

        告警规则类型。 - “metric”：指标告警规则 - “event”：事件告警规则

        :param alarm_rule_type: The alarm_rule_type of this ListMetricOrEventAlarmRuleRequest.
        :type alarm_rule_type: str
        """
        self._alarm_rule_type = alarm_rule_type

    @property
    def prom_instance_id(self):
        r"""Gets the prom_instance_id of this ListMetricOrEventAlarmRuleRequest.

        Prometheus实例id。

        :return: The prom_instance_id of this ListMetricOrEventAlarmRuleRequest.
        :rtype: str
        """
        return self._prom_instance_id

    @prom_instance_id.setter
    def prom_instance_id(self, prom_instance_id):
        r"""Sets the prom_instance_id of this ListMetricOrEventAlarmRuleRequest.

        Prometheus实例id。

        :param prom_instance_id: The prom_instance_id of this ListMetricOrEventAlarmRuleRequest.
        :type prom_instance_id: str
        """
        self._prom_instance_id = prom_instance_id

    @property
    def bind_notification_rule_id(self):
        r"""Gets the bind_notification_rule_id of this ListMetricOrEventAlarmRuleRequest.

        绑定的告警行动规则名称。

        :return: The bind_notification_rule_id of this ListMetricOrEventAlarmRuleRequest.
        :rtype: str
        """
        return self._bind_notification_rule_id

    @bind_notification_rule_id.setter
    def bind_notification_rule_id(self, bind_notification_rule_id):
        r"""Sets the bind_notification_rule_id of this ListMetricOrEventAlarmRuleRequest.

        绑定的告警行动规则名称。

        :param bind_notification_rule_id: The bind_notification_rule_id of this ListMetricOrEventAlarmRuleRequest.
        :type bind_notification_rule_id: str
        """
        self._bind_notification_rule_id = bind_notification_rule_id

    @property
    def related_cce_clusters(self):
        r"""Gets the related_cce_clusters of this ListMetricOrEventAlarmRuleRequest.

        CCE集群id。

        :return: The related_cce_clusters of this ListMetricOrEventAlarmRuleRequest.
        :rtype: str
        """
        return self._related_cce_clusters

    @related_cce_clusters.setter
    def related_cce_clusters(self, related_cce_clusters):
        r"""Sets the related_cce_clusters of this ListMetricOrEventAlarmRuleRequest.

        CCE集群id。

        :param related_cce_clusters: The related_cce_clusters of this ListMetricOrEventAlarmRuleRequest.
        :type related_cce_clusters: str
        """
        self._related_cce_clusters = related_cce_clusters

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListMetricOrEventAlarmRuleRequest.

        企业项目id。  - 查询单个企业项目下实例，填写企业项目id。  - 查询所有企业项目下实例，填写“all_granted_eps”。

        :return: The enterprise_project_id of this ListMetricOrEventAlarmRuleRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListMetricOrEventAlarmRuleRequest.

        企业项目id。  - 查询单个企业项目下实例，填写企业项目id。  - 查询所有企业项目下实例，填写“all_granted_eps”。

        :param enterprise_project_id: The enterprise_project_id of this ListMetricOrEventAlarmRuleRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListMetricOrEventAlarmRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
