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
        'event_type': 'str',
        'sub_event_type': 'str',
        'event_name': 'str',
        '_from': 'int',
        'to': 'int',
        'start': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'event_type': 'event_type',
        'sub_event_type': 'sub_event_type',
        'event_name': 'event_name',
        '_from': 'from',
        'to': 'to',
        'start': 'start',
        'limit': 'limit'
    }

    def __init__(self, event_type=None, sub_event_type=None, event_name=None, _from=None, to=None, start=None, limit=None):
        r"""ListEventsRequest

        The model defined in huaweicloud sdk

        :param event_type: 事件类型，值为EVENT.SYS或EVENT.CUSTOM，EVENT.SYS表示系统事件，EVENT.CUSTOM表示自定义事件。
        :type event_type: str
        :param sub_event_type: 事件子类, 枚举类型：SUB_EVENT.OPS 运维事件, SUB_EVENT.PLAN 计划事件，SUB_EVENT.CUSTOM 自定义事件
        :type sub_event_type: str
        :param event_name: 事件名称，值为系统产生的事件名称，或用户自定义上报的事件名称。
        :type event_name: str
        :param _from: 查询数据起始时间，UNIX时间戳，单位毫秒；例如：1605952700911。
        :type _from: int
        :param to: 查询数据截止时间UNIX时间戳，单位毫秒。from必须小于to，例如：1606557500911。
        :type to: int
        :param start: 分页起始值，类型为integer，默认值为0。
        :type start: int
        :param limit: 单次查询的条数限制，取值范围(0,100]，默认值为100，用于限制结果数据条数。
        :type limit: int
        """
        
        

        self._event_type = None
        self._sub_event_type = None
        self._event_name = None
        self.__from = None
        self._to = None
        self._start = None
        self._limit = None
        self.discriminator = None

        if event_type is not None:
            self.event_type = event_type
        if sub_event_type is not None:
            self.sub_event_type = sub_event_type
        if event_name is not None:
            self.event_name = event_name
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit

    @property
    def event_type(self):
        r"""Gets the event_type of this ListEventsRequest.

        事件类型，值为EVENT.SYS或EVENT.CUSTOM，EVENT.SYS表示系统事件，EVENT.CUSTOM表示自定义事件。

        :return: The event_type of this ListEventsRequest.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ListEventsRequest.

        事件类型，值为EVENT.SYS或EVENT.CUSTOM，EVENT.SYS表示系统事件，EVENT.CUSTOM表示自定义事件。

        :param event_type: The event_type of this ListEventsRequest.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def sub_event_type(self):
        r"""Gets the sub_event_type of this ListEventsRequest.

        事件子类, 枚举类型：SUB_EVENT.OPS 运维事件, SUB_EVENT.PLAN 计划事件，SUB_EVENT.CUSTOM 自定义事件

        :return: The sub_event_type of this ListEventsRequest.
        :rtype: str
        """
        return self._sub_event_type

    @sub_event_type.setter
    def sub_event_type(self, sub_event_type):
        r"""Sets the sub_event_type of this ListEventsRequest.

        事件子类, 枚举类型：SUB_EVENT.OPS 运维事件, SUB_EVENT.PLAN 计划事件，SUB_EVENT.CUSTOM 自定义事件

        :param sub_event_type: The sub_event_type of this ListEventsRequest.
        :type sub_event_type: str
        """
        self._sub_event_type = sub_event_type

    @property
    def event_name(self):
        r"""Gets the event_name of this ListEventsRequest.

        事件名称，值为系统产生的事件名称，或用户自定义上报的事件名称。

        :return: The event_name of this ListEventsRequest.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this ListEventsRequest.

        事件名称，值为系统产生的事件名称，或用户自定义上报的事件名称。

        :param event_name: The event_name of this ListEventsRequest.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def _from(self):
        r"""Gets the _from of this ListEventsRequest.

        查询数据起始时间，UNIX时间戳，单位毫秒；例如：1605952700911。

        :return: The _from of this ListEventsRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListEventsRequest.

        查询数据起始时间，UNIX时间戳，单位毫秒；例如：1605952700911。

        :param _from: The _from of this ListEventsRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListEventsRequest.

        查询数据截止时间UNIX时间戳，单位毫秒。from必须小于to，例如：1606557500911。

        :return: The to of this ListEventsRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListEventsRequest.

        查询数据截止时间UNIX时间戳，单位毫秒。from必须小于to，例如：1606557500911。

        :param to: The to of this ListEventsRequest.
        :type to: int
        """
        self._to = to

    @property
    def start(self):
        r"""Gets the start of this ListEventsRequest.

        分页起始值，类型为integer，默认值为0。

        :return: The start of this ListEventsRequest.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this ListEventsRequest.

        分页起始值，类型为integer，默认值为0。

        :param start: The start of this ListEventsRequest.
        :type start: int
        """
        self._start = start

    @property
    def limit(self):
        r"""Gets the limit of this ListEventsRequest.

        单次查询的条数限制，取值范围(0,100]，默认值为100，用于限制结果数据条数。

        :return: The limit of this ListEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEventsRequest.

        单次查询的条数限制，取值范围(0,100]，默认值为100，用于限制结果数据条数。

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
