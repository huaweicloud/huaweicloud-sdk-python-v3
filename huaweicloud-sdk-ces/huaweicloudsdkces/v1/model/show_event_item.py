# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEventItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_name': 'str',
        'event_source': 'str',
        'time': 'int',
        'detail': 'ShowEventItemDetail'
    }

    attribute_map = {
        'event_name': 'event_name',
        'event_source': 'event_source',
        'time': 'time',
        'detail': 'detail'
    }

    def __init__(self, event_name=None, event_source=None, time=None, detail=None):
        """ShowEventItem

        The model defined in huaweicloud sdk

        :param event_name: 事件名称。  必须以字母开头，只能包含0-9/a-z/A-Z/_，长度最短为1，最大为64。
        :type event_name: str
        :param event_source: 事件来源。 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，总长度最短为3，最大为32。
        :type event_source: str
        :param time: 事件发生时间。UNIX时间戳，单位毫秒。  说明： 因为客户端到服务器端有延时，因此插入数据的时间戳应该在[当前时间-1小时+20秒，当前时间+10分钟-20秒]区间内，保证到达服务器时不会因为传输时延造成数据不能插入数据库。
        :type time: int
        :param detail: 
        :type detail: :class:`huaweicloudsdkces.v1.ShowEventItemDetail`
        """
        
        

        self._event_name = None
        self._event_source = None
        self._time = None
        self._detail = None
        self.discriminator = None

        self.event_name = event_name
        self.event_source = event_source
        self.time = time
        self.detail = detail

    @property
    def event_name(self):
        """Gets the event_name of this ShowEventItem.

        事件名称。  必须以字母开头，只能包含0-9/a-z/A-Z/_，长度最短为1，最大为64。

        :return: The event_name of this ShowEventItem.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this ShowEventItem.

        事件名称。  必须以字母开头，只能包含0-9/a-z/A-Z/_，长度最短为1，最大为64。

        :param event_name: The event_name of this ShowEventItem.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def event_source(self):
        """Gets the event_source of this ShowEventItem.

        事件来源。 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，总长度最短为3，最大为32。

        :return: The event_source of this ShowEventItem.
        :rtype: str
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        """Sets the event_source of this ShowEventItem.

        事件来源。 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_，总长度最短为3，最大为32。

        :param event_source: The event_source of this ShowEventItem.
        :type event_source: str
        """
        self._event_source = event_source

    @property
    def time(self):
        """Gets the time of this ShowEventItem.

        事件发生时间。UNIX时间戳，单位毫秒。  说明： 因为客户端到服务器端有延时，因此插入数据的时间戳应该在[当前时间-1小时+20秒，当前时间+10分钟-20秒]区间内，保证到达服务器时不会因为传输时延造成数据不能插入数据库。

        :return: The time of this ShowEventItem.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ShowEventItem.

        事件发生时间。UNIX时间戳，单位毫秒。  说明： 因为客户端到服务器端有延时，因此插入数据的时间戳应该在[当前时间-1小时+20秒，当前时间+10分钟-20秒]区间内，保证到达服务器时不会因为传输时延造成数据不能插入数据库。

        :param time: The time of this ShowEventItem.
        :type time: int
        """
        self._time = time

    @property
    def detail(self):
        """Gets the detail of this ShowEventItem.

        :return: The detail of this ShowEventItem.
        :rtype: :class:`huaweicloudsdkces.v1.ShowEventItemDetail`
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ShowEventItem.

        :param detail: The detail of this ShowEventItem.
        :type detail: :class:`huaweicloudsdkces.v1.ShowEventItemDetail`
        """
        self._detail = detail

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
        if not isinstance(other, ShowEventItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
