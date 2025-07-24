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
        'offset': 'int',
        'limit': 'int',
        'event_level': 'str',
        'resource_id': 'str',
        '_from': 'str',
        'to': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'event_level': 'event_level',
        'resource_id': 'resource_id',
        '_from': 'from',
        'to': 'to'
    }

    def __init__(self, offset=None, limit=None, event_level=None, resource_id=None, _from=None, to=None):
        r"""ListEventsRequest

        The model defined in huaweicloud sdk

        :param offset: 分页游标
        :type offset: int
        :param limit: 分页大小
        :type limit: int
        :param event_level: 事件级别，值为critical为紧急，major为重要，minor为次要，info为提示
        :type event_level: str
        :param resource_id: 告警资源ID
        :type resource_id: str
        :param _from: 查询开始时间，格式为时间戳（毫秒），默认查询从当前时间起三十天内的数据
        :type _from: str
        :param to: 查询截止时间，格式为时间戳（毫秒），默认查询从当前时间起三十天内的数据
        :type to: str
        """
        
        

        self._offset = None
        self._limit = None
        self._event_level = None
        self._resource_id = None
        self.__from = None
        self._to = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if event_level is not None:
            self.event_level = event_level
        if resource_id is not None:
            self.resource_id = resource_id
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to

    @property
    def offset(self):
        r"""Gets the offset of this ListEventsRequest.

        分页游标

        :return: The offset of this ListEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEventsRequest.

        分页游标

        :param offset: The offset of this ListEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListEventsRequest.

        分页大小

        :return: The limit of this ListEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEventsRequest.

        分页大小

        :param limit: The limit of this ListEventsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def event_level(self):
        r"""Gets the event_level of this ListEventsRequest.

        事件级别，值为critical为紧急，major为重要，minor为次要，info为提示

        :return: The event_level of this ListEventsRequest.
        :rtype: str
        """
        return self._event_level

    @event_level.setter
    def event_level(self, event_level):
        r"""Sets the event_level of this ListEventsRequest.

        事件级别，值为critical为紧急，major为重要，minor为次要，info为提示

        :param event_level: The event_level of this ListEventsRequest.
        :type event_level: str
        """
        self._event_level = event_level

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListEventsRequest.

        告警资源ID

        :return: The resource_id of this ListEventsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListEventsRequest.

        告警资源ID

        :param resource_id: The resource_id of this ListEventsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def _from(self):
        r"""Gets the _from of this ListEventsRequest.

        查询开始时间，格式为时间戳（毫秒），默认查询从当前时间起三十天内的数据

        :return: The _from of this ListEventsRequest.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListEventsRequest.

        查询开始时间，格式为时间戳（毫秒），默认查询从当前时间起三十天内的数据

        :param _from: The _from of this ListEventsRequest.
        :type _from: str
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListEventsRequest.

        查询截止时间，格式为时间戳（毫秒），默认查询从当前时间起三十天内的数据

        :return: The to of this ListEventsRequest.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListEventsRequest.

        查询截止时间，格式为时间戳（毫秒），默认查询从当前时间起三十天内的数据

        :param to: The to of this ListEventsRequest.
        :type to: str
        """
        self._to = to

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
