# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventsRequest:

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
        'region_id': 'str',
        'event_source': 'str',
        'event_level': 'str',
        'event_name': 'str',
        'resource_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'region_id': 'region_id',
        'event_source': 'event_source',
        'event_level': 'event_level',
        'event_name': 'event_name',
        'resource_id': 'resource_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, domain_id=None, region_id=None, event_source=None, event_level=None, event_name=None, resource_id=None, start_time=None, end_time=None, marker=None, limit=None):
        r"""ListEventsRequest

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param region_id: 区域ID
        :type region_id: str
        :param event_source: 事件源，取值范围：SYS.CBR,SYS.RDS,SYS.GaussDB
        :type event_source: str
        :param event_level: 事件等级，取值范围：Critical,Major,Minor,Info
        :type event_level: str
        :param event_name: 事件名称，长度范围4-64个字符。
        :type event_name: str
        :param resource_id: 资源ID，长度范围16-64个字符。
        :type resource_id: str
        :param start_time: 查询范围起始时间，例如：2025-03-20T09:31:45Z。
        :type start_time: str
        :param end_time: 查询范围结束时间，例如：2025-03-20T09:31:45Z。
        :type end_time: str
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。
        :type marker: str
        :param limit: 单次查询的条数限制,取值范围(0,100]，默认值为10，用于限制结果数据条数。
        :type limit: int
        """
        
        

        self._domain_id = None
        self._region_id = None
        self._event_source = None
        self._event_level = None
        self._event_name = None
        self._resource_id = None
        self._start_time = None
        self._end_time = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        self.domain_id = domain_id
        if region_id is not None:
            self.region_id = region_id
        if event_source is not None:
            self.event_source = event_source
        if event_level is not None:
            self.event_level = event_level
        if event_name is not None:
            self.event_name = event_name
        if resource_id is not None:
            self.resource_id = resource_id
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
        r"""Gets the domain_id of this ListEventsRequest.

        账号ID

        :return: The domain_id of this ListEventsRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListEventsRequest.

        账号ID

        :param domain_id: The domain_id of this ListEventsRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ListEventsRequest.

        区域ID

        :return: The region_id of this ListEventsRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListEventsRequest.

        区域ID

        :param region_id: The region_id of this ListEventsRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def event_source(self):
        r"""Gets the event_source of this ListEventsRequest.

        事件源，取值范围：SYS.CBR,SYS.RDS,SYS.GaussDB

        :return: The event_source of this ListEventsRequest.
        :rtype: str
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        r"""Sets the event_source of this ListEventsRequest.

        事件源，取值范围：SYS.CBR,SYS.RDS,SYS.GaussDB

        :param event_source: The event_source of this ListEventsRequest.
        :type event_source: str
        """
        self._event_source = event_source

    @property
    def event_level(self):
        r"""Gets the event_level of this ListEventsRequest.

        事件等级，取值范围：Critical,Major,Minor,Info

        :return: The event_level of this ListEventsRequest.
        :rtype: str
        """
        return self._event_level

    @event_level.setter
    def event_level(self, event_level):
        r"""Sets the event_level of this ListEventsRequest.

        事件等级，取值范围：Critical,Major,Minor,Info

        :param event_level: The event_level of this ListEventsRequest.
        :type event_level: str
        """
        self._event_level = event_level

    @property
    def event_name(self):
        r"""Gets the event_name of this ListEventsRequest.

        事件名称，长度范围4-64个字符。

        :return: The event_name of this ListEventsRequest.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this ListEventsRequest.

        事件名称，长度范围4-64个字符。

        :param event_name: The event_name of this ListEventsRequest.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListEventsRequest.

        资源ID，长度范围16-64个字符。

        :return: The resource_id of this ListEventsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListEventsRequest.

        资源ID，长度范围16-64个字符。

        :param resource_id: The resource_id of this ListEventsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListEventsRequest.

        查询范围起始时间，例如：2025-03-20T09:31:45Z。

        :return: The start_time of this ListEventsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListEventsRequest.

        查询范围起始时间，例如：2025-03-20T09:31:45Z。

        :param start_time: The start_time of this ListEventsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListEventsRequest.

        查询范围结束时间，例如：2025-03-20T09:31:45Z。

        :return: The end_time of this ListEventsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListEventsRequest.

        查询范围结束时间，例如：2025-03-20T09:31:45Z。

        :param end_time: The end_time of this ListEventsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def marker(self):
        r"""Gets the marker of this ListEventsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。

        :return: The marker of this ListEventsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListEventsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。

        :param marker: The marker of this ListEventsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListEventsRequest.

        单次查询的条数限制,取值范围(0,100]，默认值为10，用于限制结果数据条数。

        :return: The limit of this ListEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEventsRequest.

        单次查询的条数限制,取值范围(0,100]，默认值为10，用于限制结果数据条数。

        :param limit: The limit of this ListEventsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
