# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'namespace': 'str',
        'status': 'str',
        'region_id': 'str',
        'resource_id': 'str',
        'alarm_rule_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'namespace': 'namespace',
        'status': 'status',
        'region_id': 'region_id',
        'resource_id': 'resource_id',
        'alarm_rule_id': 'alarm_rule_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, domain_id=None, namespace=None, status=None, region_id=None, resource_id=None, alarm_rule_id=None, start_time=None, end_time=None, marker=None, limit=None):
        r"""ListAlarmsRequest

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param namespace: 告警命名空间，取值范围：SYS.CBR,SYS.RDS,SYS.GaussDB
        :type namespace: str
        :param status: 告警状态，取值范围：ok，alarm，invalid。
        :type status: str
        :param region_id: RegionID
        :type region_id: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param alarm_rule_id: 告警规则ID
        :type alarm_rule_id: str
        :param start_time: 查询范围起始时间，例如：2025-03-20T09:31:45Z。
        :type start_time: str
        :param end_time: 查询范围结束时间，例如：2025-03-21T09:31:45Z。
        :type end_time: str
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。
        :type marker: str
        :param limit: 单次查询的条数限制,取值范围(0,100]，默认值为10，用于限制结果数据条数。
        :type limit: int
        """
        
        

        self._domain_id = None
        self._namespace = None
        self._status = None
        self._region_id = None
        self._resource_id = None
        self._alarm_rule_id = None
        self._start_time = None
        self._end_time = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        self.domain_id = domain_id
        if namespace is not None:
            self.namespace = namespace
        if status is not None:
            self.status = status
        if region_id is not None:
            self.region_id = region_id
        if resource_id is not None:
            self.resource_id = resource_id
        if alarm_rule_id is not None:
            self.alarm_rule_id = alarm_rule_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListAlarmsRequest.

        账号ID

        :return: The domain_id of this ListAlarmsRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListAlarmsRequest.

        账号ID

        :param domain_id: The domain_id of this ListAlarmsRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def namespace(self):
        r"""Gets the namespace of this ListAlarmsRequest.

        告警命名空间，取值范围：SYS.CBR,SYS.RDS,SYS.GaussDB

        :return: The namespace of this ListAlarmsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListAlarmsRequest.

        告警命名空间，取值范围：SYS.CBR,SYS.RDS,SYS.GaussDB

        :param namespace: The namespace of this ListAlarmsRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def status(self):
        r"""Gets the status of this ListAlarmsRequest.

        告警状态，取值范围：ok，alarm，invalid。

        :return: The status of this ListAlarmsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAlarmsRequest.

        告警状态，取值范围：ok，alarm，invalid。

        :param status: The status of this ListAlarmsRequest.
        :type status: str
        """
        self._status = status

    @property
    def region_id(self):
        r"""Gets the region_id of this ListAlarmsRequest.

        RegionID

        :return: The region_id of this ListAlarmsRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListAlarmsRequest.

        RegionID

        :param region_id: The region_id of this ListAlarmsRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListAlarmsRequest.

        资源ID

        :return: The resource_id of this ListAlarmsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListAlarmsRequest.

        资源ID

        :param resource_id: The resource_id of this ListAlarmsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def alarm_rule_id(self):
        r"""Gets the alarm_rule_id of this ListAlarmsRequest.

        告警规则ID

        :return: The alarm_rule_id of this ListAlarmsRequest.
        :rtype: str
        """
        return self._alarm_rule_id

    @alarm_rule_id.setter
    def alarm_rule_id(self, alarm_rule_id):
        r"""Sets the alarm_rule_id of this ListAlarmsRequest.

        告警规则ID

        :param alarm_rule_id: The alarm_rule_id of this ListAlarmsRequest.
        :type alarm_rule_id: str
        """
        self._alarm_rule_id = alarm_rule_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListAlarmsRequest.

        查询范围起始时间，例如：2025-03-20T09:31:45Z。

        :return: The start_time of this ListAlarmsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListAlarmsRequest.

        查询范围起始时间，例如：2025-03-20T09:31:45Z。

        :param start_time: The start_time of this ListAlarmsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListAlarmsRequest.

        查询范围结束时间，例如：2025-03-21T09:31:45Z。

        :return: The end_time of this ListAlarmsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListAlarmsRequest.

        查询范围结束时间，例如：2025-03-21T09:31:45Z。

        :param end_time: The end_time of this ListAlarmsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def marker(self):
        r"""Gets the marker of this ListAlarmsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。

        :return: The marker of this ListAlarmsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAlarmsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。

        :param marker: The marker of this ListAlarmsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListAlarmsRequest.

        单次查询的条数限制,取值范围(0,100]，默认值为10，用于限制结果数据条数。

        :return: The limit of this ListAlarmsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAlarmsRequest.

        单次查询的条数限制,取值范围(0,100]，默认值为10，用于限制结果数据条数。

        :param limit: The limit of this ListAlarmsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAlarmsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
