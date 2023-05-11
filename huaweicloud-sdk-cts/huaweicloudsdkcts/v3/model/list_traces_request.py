# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTracesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trace_type': 'str',
        'limit': 'int',
        '_from': 'int',
        'next': 'str',
        'to': 'int',
        'tracker_name': 'str',
        'service_type': 'str',
        'user': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'trace_id': 'str',
        'trace_name': 'str',
        'trace_rating': 'str'
    }

    attribute_map = {
        'trace_type': 'trace_type',
        'limit': 'limit',
        '_from': 'from',
        'next': 'next',
        'to': 'to',
        'tracker_name': 'tracker_name',
        'service_type': 'service_type',
        'user': 'user',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'trace_id': 'trace_id',
        'trace_name': 'trace_name',
        'trace_rating': 'trace_rating'
    }

    def __init__(self, trace_type=None, limit=None, _from=None, next=None, to=None, tracker_name=None, service_type=None, user=None, resource_id=None, resource_name=None, resource_type=None, trace_id=None, trace_name=None, trace_rating=None):
        """ListTracesRequest

        The model defined in huaweicloud sdk

        :param trace_type: 标识审计事件类型。 目前支持管理类事件（system）和数据类事件（data）。 默认值为\&quot;system\&quot;。
        :type trace_type: str
        :param limit: 标示查询事件列表中限定返回的事件条数。不传时默认10条，最大值200条。
        :type limit: int
        :param _from: 标识查询事件列表的起始时间戳（timestamp，为标准UTC时间，毫秒级，13位数字，不包括传入时间）默认为上一小时的时间戳。查询条件from与to配套使用。
        :type _from: int
        :param next: 取值为响应中中marker的值，用于标识查询事件的起始时间（自此条事件的记录时间起，向更早时间查询）。 可以与“from”、“to”结合使用。 最终的查询条件取两组时间条件的交集。
        :type next: str
        :param to: 标识查询事件列表的结束时间戳（timestamp，为标准UTC时间，毫秒级，13位数字，不包括传入时间）默认为当前时间戳。查询条件to与from配套使用。
        :type to: int
        :param tracker_name: 当\&quot;trace_type\&quot;字段值为\&quot;system\&quot;时，该字段值默认为\&quot;system\&quot;。 当\&quot;trace_type\&quot;字段值为\&quot;data\&quot;时，该字段值可以传入数据类追踪器名称，达到筛选某个数据类追踪器下的数据事件目的。
        :type tracker_name: str
        :param service_type: 标识查询事件列表对应的云服务类型。必须为已对接CTS的云服务的英文缩写，且服务类型一般为大写字母。 当\&quot;trace_type\&quot;字段值为\&quot;system\&quot;时，该字段筛选有效\&quot;。 已对接的云服务列表参见《云审计服务用户指南》“支持的服务”章节。
        :type service_type: str
        :param user: 标识特定用户名称，用以查询该用户下的所有事件。 当\&quot;trace_type\&quot;字段值为\&quot;system\&quot;时，该字段筛选有效\&quot;。
        :type user: str
        :param resource_id: 标示查询事件列表对应的云服务资源ID。 当\&quot;trace_type\&quot;字段值为\&quot;system\&quot;时，该字段筛选有效\&quot;。
        :type resource_id: str
        :param resource_name: 标示查询事件列表对应的的资源名称。 当\&quot;trace_type\&quot;字段值为\&quot;system\&quot;时，该字段筛选有效\&quot;。 说明：该字段可能包含大写字母。
        :type resource_name: str
        :param resource_type: 标示查询事件列表对应的资源类型。 当\&quot;trace_type\&quot;字段值为\&quot;system\&quot;时，该字段筛选有效\&quot;。
        :type resource_type: str
        :param trace_id: 标示某一条事件的事件ID。当传入这个查询条件时，其他查询条件自动不生效。 当\&quot;trace_type\&quot;字段值为\&quot;system\&quot;时，该字段筛选有效\&quot;。
        :type trace_id: str
        :param trace_name: 标示查询事件列表对应的事件名称。 当\&quot;trace_type\&quot;字段值为\&quot;system\&quot;时，该字段筛选有效\&quot;。 说明：该字段可能包含大写字母。
        :type trace_name: str
        :param trace_rating: 标示查询事件列表对应的事件等级目前有三种：正常(normal), 警告(warning),事故(incident)。 当\&quot;trace_type\&quot;字段值为\&quot;system\&quot;时，该字段筛选有效\&quot;。
        :type trace_rating: str
        """
        
        

        self._trace_type = None
        self._limit = None
        self.__from = None
        self._next = None
        self._to = None
        self._tracker_name = None
        self._service_type = None
        self._user = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._trace_id = None
        self._trace_name = None
        self._trace_rating = None
        self.discriminator = None

        self.trace_type = trace_type
        if limit is not None:
            self.limit = limit
        if _from is not None:
            self._from = _from
        if next is not None:
            self.next = next
        if to is not None:
            self.to = to
        if tracker_name is not None:
            self.tracker_name = tracker_name
        if service_type is not None:
            self.service_type = service_type
        if user is not None:
            self.user = user
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if trace_id is not None:
            self.trace_id = trace_id
        if trace_name is not None:
            self.trace_name = trace_name
        if trace_rating is not None:
            self.trace_rating = trace_rating

    @property
    def trace_type(self):
        """Gets the trace_type of this ListTracesRequest.

        标识审计事件类型。 目前支持管理类事件（system）和数据类事件（data）。 默认值为\"system\"。

        :return: The trace_type of this ListTracesRequest.
        :rtype: str
        """
        return self._trace_type

    @trace_type.setter
    def trace_type(self, trace_type):
        """Sets the trace_type of this ListTracesRequest.

        标识审计事件类型。 目前支持管理类事件（system）和数据类事件（data）。 默认值为\"system\"。

        :param trace_type: The trace_type of this ListTracesRequest.
        :type trace_type: str
        """
        self._trace_type = trace_type

    @property
    def limit(self):
        """Gets the limit of this ListTracesRequest.

        标示查询事件列表中限定返回的事件条数。不传时默认10条，最大值200条。

        :return: The limit of this ListTracesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTracesRequest.

        标示查询事件列表中限定返回的事件条数。不传时默认10条，最大值200条。

        :param limit: The limit of this ListTracesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def _from(self):
        """Gets the _from of this ListTracesRequest.

        标识查询事件列表的起始时间戳（timestamp，为标准UTC时间，毫秒级，13位数字，不包括传入时间）默认为上一小时的时间戳。查询条件from与to配套使用。

        :return: The _from of this ListTracesRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ListTracesRequest.

        标识查询事件列表的起始时间戳（timestamp，为标准UTC时间，毫秒级，13位数字，不包括传入时间）默认为上一小时的时间戳。查询条件from与to配套使用。

        :param _from: The _from of this ListTracesRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def next(self):
        """Gets the next of this ListTracesRequest.

        取值为响应中中marker的值，用于标识查询事件的起始时间（自此条事件的记录时间起，向更早时间查询）。 可以与“from”、“to”结合使用。 最终的查询条件取两组时间条件的交集。

        :return: The next of this ListTracesRequest.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this ListTracesRequest.

        取值为响应中中marker的值，用于标识查询事件的起始时间（自此条事件的记录时间起，向更早时间查询）。 可以与“from”、“to”结合使用。 最终的查询条件取两组时间条件的交集。

        :param next: The next of this ListTracesRequest.
        :type next: str
        """
        self._next = next

    @property
    def to(self):
        """Gets the to of this ListTracesRequest.

        标识查询事件列表的结束时间戳（timestamp，为标准UTC时间，毫秒级，13位数字，不包括传入时间）默认为当前时间戳。查询条件to与from配套使用。

        :return: The to of this ListTracesRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ListTracesRequest.

        标识查询事件列表的结束时间戳（timestamp，为标准UTC时间，毫秒级，13位数字，不包括传入时间）默认为当前时间戳。查询条件to与from配套使用。

        :param to: The to of this ListTracesRequest.
        :type to: int
        """
        self._to = to

    @property
    def tracker_name(self):
        """Gets the tracker_name of this ListTracesRequest.

        当\"trace_type\"字段值为\"system\"时，该字段值默认为\"system\"。 当\"trace_type\"字段值为\"data\"时，该字段值可以传入数据类追踪器名称，达到筛选某个数据类追踪器下的数据事件目的。

        :return: The tracker_name of this ListTracesRequest.
        :rtype: str
        """
        return self._tracker_name

    @tracker_name.setter
    def tracker_name(self, tracker_name):
        """Sets the tracker_name of this ListTracesRequest.

        当\"trace_type\"字段值为\"system\"时，该字段值默认为\"system\"。 当\"trace_type\"字段值为\"data\"时，该字段值可以传入数据类追踪器名称，达到筛选某个数据类追踪器下的数据事件目的。

        :param tracker_name: The tracker_name of this ListTracesRequest.
        :type tracker_name: str
        """
        self._tracker_name = tracker_name

    @property
    def service_type(self):
        """Gets the service_type of this ListTracesRequest.

        标识查询事件列表对应的云服务类型。必须为已对接CTS的云服务的英文缩写，且服务类型一般为大写字母。 当\"trace_type\"字段值为\"system\"时，该字段筛选有效\"。 已对接的云服务列表参见《云审计服务用户指南》“支持的服务”章节。

        :return: The service_type of this ListTracesRequest.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this ListTracesRequest.

        标识查询事件列表对应的云服务类型。必须为已对接CTS的云服务的英文缩写，且服务类型一般为大写字母。 当\"trace_type\"字段值为\"system\"时，该字段筛选有效\"。 已对接的云服务列表参见《云审计服务用户指南》“支持的服务”章节。

        :param service_type: The service_type of this ListTracesRequest.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def user(self):
        """Gets the user of this ListTracesRequest.

        标识特定用户名称，用以查询该用户下的所有事件。 当\"trace_type\"字段值为\"system\"时，该字段筛选有效\"。

        :return: The user of this ListTracesRequest.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ListTracesRequest.

        标识特定用户名称，用以查询该用户下的所有事件。 当\"trace_type\"字段值为\"system\"时，该字段筛选有效\"。

        :param user: The user of this ListTracesRequest.
        :type user: str
        """
        self._user = user

    @property
    def resource_id(self):
        """Gets the resource_id of this ListTracesRequest.

        标示查询事件列表对应的云服务资源ID。 当\"trace_type\"字段值为\"system\"时，该字段筛选有效\"。

        :return: The resource_id of this ListTracesRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListTracesRequest.

        标示查询事件列表对应的云服务资源ID。 当\"trace_type\"字段值为\"system\"时，该字段筛选有效\"。

        :param resource_id: The resource_id of this ListTracesRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this ListTracesRequest.

        标示查询事件列表对应的的资源名称。 当\"trace_type\"字段值为\"system\"时，该字段筛选有效\"。 说明：该字段可能包含大写字母。

        :return: The resource_name of this ListTracesRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ListTracesRequest.

        标示查询事件列表对应的的资源名称。 当\"trace_type\"字段值为\"system\"时，该字段筛选有效\"。 说明：该字段可能包含大写字母。

        :param resource_name: The resource_name of this ListTracesRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """Gets the resource_type of this ListTracesRequest.

        标示查询事件列表对应的资源类型。 当\"trace_type\"字段值为\"system\"时，该字段筛选有效\"。

        :return: The resource_type of this ListTracesRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListTracesRequest.

        标示查询事件列表对应的资源类型。 当\"trace_type\"字段值为\"system\"时，该字段筛选有效\"。

        :param resource_type: The resource_type of this ListTracesRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def trace_id(self):
        """Gets the trace_id of this ListTracesRequest.

        标示某一条事件的事件ID。当传入这个查询条件时，其他查询条件自动不生效。 当\"trace_type\"字段值为\"system\"时，该字段筛选有效\"。

        :return: The trace_id of this ListTracesRequest.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this ListTracesRequest.

        标示某一条事件的事件ID。当传入这个查询条件时，其他查询条件自动不生效。 当\"trace_type\"字段值为\"system\"时，该字段筛选有效\"。

        :param trace_id: The trace_id of this ListTracesRequest.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def trace_name(self):
        """Gets the trace_name of this ListTracesRequest.

        标示查询事件列表对应的事件名称。 当\"trace_type\"字段值为\"system\"时，该字段筛选有效\"。 说明：该字段可能包含大写字母。

        :return: The trace_name of this ListTracesRequest.
        :rtype: str
        """
        return self._trace_name

    @trace_name.setter
    def trace_name(self, trace_name):
        """Sets the trace_name of this ListTracesRequest.

        标示查询事件列表对应的事件名称。 当\"trace_type\"字段值为\"system\"时，该字段筛选有效\"。 说明：该字段可能包含大写字母。

        :param trace_name: The trace_name of this ListTracesRequest.
        :type trace_name: str
        """
        self._trace_name = trace_name

    @property
    def trace_rating(self):
        """Gets the trace_rating of this ListTracesRequest.

        标示查询事件列表对应的事件等级目前有三种：正常(normal), 警告(warning),事故(incident)。 当\"trace_type\"字段值为\"system\"时，该字段筛选有效\"。

        :return: The trace_rating of this ListTracesRequest.
        :rtype: str
        """
        return self._trace_rating

    @trace_rating.setter
    def trace_rating(self, trace_rating):
        """Sets the trace_rating of this ListTracesRequest.

        标示查询事件列表对应的事件等级目前有三种：正常(normal), 警告(warning),事故(incident)。 当\"trace_type\"字段值为\"system\"时，该字段筛选有效\"。

        :param trace_rating: The trace_rating of this ListTracesRequest.
        :type trace_rating: str
        """
        self._trace_rating = trace_rating

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
        if not isinstance(other, ListTracesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
