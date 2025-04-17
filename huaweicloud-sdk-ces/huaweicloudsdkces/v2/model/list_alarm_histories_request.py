# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmHistoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_id': 'list[str]',
        'record_id': 'str',
        'name': 'str',
        'status': 'list[str]',
        'level': 'int',
        'namespace': 'str',
        'resource_id': 'str',
        '_from': 'str',
        'to': 'str',
        'alarm_type': 'str',
        'create_time_from': 'str',
        'create_time_to': 'str',
        'offset': 'int',
        'limit': 'int',
        'order_by': 'str'
    }

    attribute_map = {
        'alarm_id': 'alarm_id',
        'record_id': 'record_id',
        'name': 'name',
        'status': 'status',
        'level': 'level',
        'namespace': 'namespace',
        'resource_id': 'resource_id',
        '_from': 'from',
        'to': 'to',
        'alarm_type': 'alarm_type',
        'create_time_from': 'create_time_from',
        'create_time_to': 'create_time_to',
        'offset': 'offset',
        'limit': 'limit',
        'order_by': 'order_by'
    }

    def __init__(self, alarm_id=None, record_id=None, name=None, status=None, level=None, namespace=None, resource_id=None, _from=None, to=None, alarm_type=None, create_time_from=None, create_time_to=None, offset=None, limit=None, order_by=None):
        r"""ListAlarmHistoriesRequest

        The model defined in huaweicloud sdk

        :param alarm_id: 告警ID,以al开头，后跟22位由字母或数字组成的字符串
        :type alarm_id: list[str]
        :param record_id: 告警记录ID,以ah开头，后跟22位由字母或数字组成的字符串
        :type record_id: str
        :param name: 告警规则名称
        :type name: str
        :param status: 告警规则状态, ok为正常，alarm为告警，invalid为已失效
        :type status: list[str]
        :param level: 告警级别, 1为紧急，2为重要，3为次要，4为提示
        :type level: int
        :param namespace: 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”
        :type namespace: str
        :param resource_id: 告警资源ID，多维度情况按字母升序排列并使用逗号分隔
        :type resource_id: str
        :param _from: 查询告警记录的起始更新时间，例如：2022-02-10T10:05:46+08:00
        :type _from: str
        :param to: 查询告警记录的截止更新时间，例如：2022-02-10T10:05:47+08:00
        :type to: str
        :param alarm_type: 告警类型，event：查询事件类型告警，metric：查询指标类型告警
        :type alarm_type: str
        :param create_time_from: 查询告警记录的起始创建时间，例如：2022-02-10T10:05:46+08:00
        :type create_time_from: str
        :param create_time_to: 查询告警记录的截止创建时间，例如：2022-02-10T10:05:47+08:00
        :type create_time_to: str
        :param offset: 分页偏移量
        :type offset: int
        :param limit: 分页大小
        :type limit: int
        :param order_by: 按关键字排序, 默认为update_time, {first_alarm_time: 告警产生时间, update_time: 更新时间, alarm_level: 告警级别, record_id：表记录主键} 
        :type order_by: str
        """
        
        

        self._alarm_id = None
        self._record_id = None
        self._name = None
        self._status = None
        self._level = None
        self._namespace = None
        self._resource_id = None
        self.__from = None
        self._to = None
        self._alarm_type = None
        self._create_time_from = None
        self._create_time_to = None
        self._offset = None
        self._limit = None
        self._order_by = None
        self.discriminator = None

        if alarm_id is not None:
            self.alarm_id = alarm_id
        if record_id is not None:
            self.record_id = record_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if level is not None:
            self.level = level
        if namespace is not None:
            self.namespace = namespace
        if resource_id is not None:
            self.resource_id = resource_id
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if alarm_type is not None:
            self.alarm_type = alarm_type
        if create_time_from is not None:
            self.create_time_from = create_time_from
        if create_time_to is not None:
            self.create_time_to = create_time_to
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order_by is not None:
            self.order_by = order_by

    @property
    def alarm_id(self):
        r"""Gets the alarm_id of this ListAlarmHistoriesRequest.

        告警ID,以al开头，后跟22位由字母或数字组成的字符串

        :return: The alarm_id of this ListAlarmHistoriesRequest.
        :rtype: list[str]
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        r"""Sets the alarm_id of this ListAlarmHistoriesRequest.

        告警ID,以al开头，后跟22位由字母或数字组成的字符串

        :param alarm_id: The alarm_id of this ListAlarmHistoriesRequest.
        :type alarm_id: list[str]
        """
        self._alarm_id = alarm_id

    @property
    def record_id(self):
        r"""Gets the record_id of this ListAlarmHistoriesRequest.

        告警记录ID,以ah开头，后跟22位由字母或数字组成的字符串

        :return: The record_id of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        r"""Sets the record_id of this ListAlarmHistoriesRequest.

        告警记录ID,以ah开头，后跟22位由字母或数字组成的字符串

        :param record_id: The record_id of this ListAlarmHistoriesRequest.
        :type record_id: str
        """
        self._record_id = record_id

    @property
    def name(self):
        r"""Gets the name of this ListAlarmHistoriesRequest.

        告警规则名称

        :return: The name of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListAlarmHistoriesRequest.

        告警规则名称

        :param name: The name of this ListAlarmHistoriesRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListAlarmHistoriesRequest.

        告警规则状态, ok为正常，alarm为告警，invalid为已失效

        :return: The status of this ListAlarmHistoriesRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAlarmHistoriesRequest.

        告警规则状态, ok为正常，alarm为告警，invalid为已失效

        :param status: The status of this ListAlarmHistoriesRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def level(self):
        r"""Gets the level of this ListAlarmHistoriesRequest.

        告警级别, 1为紧急，2为重要，3为次要，4为提示

        :return: The level of this ListAlarmHistoriesRequest.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ListAlarmHistoriesRequest.

        告警级别, 1为紧急，2为重要，3为次要，4为提示

        :param level: The level of this ListAlarmHistoriesRequest.
        :type level: int
        """
        self._level = level

    @property
    def namespace(self):
        r"""Gets the namespace of this ListAlarmHistoriesRequest.

        查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”

        :return: The namespace of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListAlarmHistoriesRequest.

        查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”

        :param namespace: The namespace of this ListAlarmHistoriesRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListAlarmHistoriesRequest.

        告警资源ID，多维度情况按字母升序排列并使用逗号分隔

        :return: The resource_id of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListAlarmHistoriesRequest.

        告警资源ID，多维度情况按字母升序排列并使用逗号分隔

        :param resource_id: The resource_id of this ListAlarmHistoriesRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def _from(self):
        r"""Gets the _from of this ListAlarmHistoriesRequest.

        查询告警记录的起始更新时间，例如：2022-02-10T10:05:46+08:00

        :return: The _from of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListAlarmHistoriesRequest.

        查询告警记录的起始更新时间，例如：2022-02-10T10:05:46+08:00

        :param _from: The _from of this ListAlarmHistoriesRequest.
        :type _from: str
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListAlarmHistoriesRequest.

        查询告警记录的截止更新时间，例如：2022-02-10T10:05:47+08:00

        :return: The to of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListAlarmHistoriesRequest.

        查询告警记录的截止更新时间，例如：2022-02-10T10:05:47+08:00

        :param to: The to of this ListAlarmHistoriesRequest.
        :type to: str
        """
        self._to = to

    @property
    def alarm_type(self):
        r"""Gets the alarm_type of this ListAlarmHistoriesRequest.

        告警类型，event：查询事件类型告警，metric：查询指标类型告警

        :return: The alarm_type of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        r"""Sets the alarm_type of this ListAlarmHistoriesRequest.

        告警类型，event：查询事件类型告警，metric：查询指标类型告警

        :param alarm_type: The alarm_type of this ListAlarmHistoriesRequest.
        :type alarm_type: str
        """
        self._alarm_type = alarm_type

    @property
    def create_time_from(self):
        r"""Gets the create_time_from of this ListAlarmHistoriesRequest.

        查询告警记录的起始创建时间，例如：2022-02-10T10:05:46+08:00

        :return: The create_time_from of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._create_time_from

    @create_time_from.setter
    def create_time_from(self, create_time_from):
        r"""Sets the create_time_from of this ListAlarmHistoriesRequest.

        查询告警记录的起始创建时间，例如：2022-02-10T10:05:46+08:00

        :param create_time_from: The create_time_from of this ListAlarmHistoriesRequest.
        :type create_time_from: str
        """
        self._create_time_from = create_time_from

    @property
    def create_time_to(self):
        r"""Gets the create_time_to of this ListAlarmHistoriesRequest.

        查询告警记录的截止创建时间，例如：2022-02-10T10:05:47+08:00

        :return: The create_time_to of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._create_time_to

    @create_time_to.setter
    def create_time_to(self, create_time_to):
        r"""Sets the create_time_to of this ListAlarmHistoriesRequest.

        查询告警记录的截止创建时间，例如：2022-02-10T10:05:47+08:00

        :param create_time_to: The create_time_to of this ListAlarmHistoriesRequest.
        :type create_time_to: str
        """
        self._create_time_to = create_time_to

    @property
    def offset(self):
        r"""Gets the offset of this ListAlarmHistoriesRequest.

        分页偏移量

        :return: The offset of this ListAlarmHistoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAlarmHistoriesRequest.

        分页偏移量

        :param offset: The offset of this ListAlarmHistoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAlarmHistoriesRequest.

        分页大小

        :return: The limit of this ListAlarmHistoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAlarmHistoriesRequest.

        分页大小

        :param limit: The limit of this ListAlarmHistoriesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order_by(self):
        r"""Gets the order_by of this ListAlarmHistoriesRequest.

        按关键字排序, 默认为update_time, {first_alarm_time: 告警产生时间, update_time: 更新时间, alarm_level: 告警级别, record_id：表记录主键} 

        :return: The order_by of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListAlarmHistoriesRequest.

        按关键字排序, 默认为update_time, {first_alarm_time: 告警产生时间, update_time: 更新时间, alarm_level: 告警级别, record_id：表记录主键} 

        :param order_by: The order_by of this ListAlarmHistoriesRequest.
        :type order_by: str
        """
        self._order_by = order_by

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
        if not isinstance(other, ListAlarmHistoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
