# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDetailOfEventTraceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_id': 'str',
        'event_source': 'str',
        'event_type': 'str',
        'receive_time': 'str',
        'channel_id': 'str',
        'channel_name': 'str',
        'deliver_list': 'list[DeliverItem]'
    }

    attribute_map = {
        'event_id': 'eventId',
        'event_source': 'eventSource',
        'event_type': 'eventType',
        'receive_time': 'receiveTime',
        'channel_id': 'channelId',
        'channel_name': 'channelName',
        'deliver_list': 'deliverList'
    }

    def __init__(self, event_id=None, event_source=None, event_type=None, receive_time=None, channel_id=None, channel_name=None, deliver_list=None):
        """ShowDetailOfEventTraceResponse

        The model defined in huaweicloud sdk

        :param event_id: 事件ID
        :type event_id: str
        :param event_source: 事件源
        :type event_source: str
        :param event_type: 事件类型
        :type event_type: str
        :param receive_time: 接收时间
        :type receive_time: str
        :param channel_id: 通道ID
        :type channel_id: str
        :param channel_name: 通道名称
        :type channel_name: str
        :param deliver_list: 事件投递列表
        :type deliver_list: list[:class:`huaweicloudsdkeg.v1.DeliverItem`]
        """
        
        super(ShowDetailOfEventTraceResponse, self).__init__()

        self._event_id = None
        self._event_source = None
        self._event_type = None
        self._receive_time = None
        self._channel_id = None
        self._channel_name = None
        self._deliver_list = None
        self.discriminator = None

        if event_id is not None:
            self.event_id = event_id
        if event_source is not None:
            self.event_source = event_source
        if event_type is not None:
            self.event_type = event_type
        if receive_time is not None:
            self.receive_time = receive_time
        if channel_id is not None:
            self.channel_id = channel_id
        if channel_name is not None:
            self.channel_name = channel_name
        if deliver_list is not None:
            self.deliver_list = deliver_list

    @property
    def event_id(self):
        """Gets the event_id of this ShowDetailOfEventTraceResponse.

        事件ID

        :return: The event_id of this ShowDetailOfEventTraceResponse.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this ShowDetailOfEventTraceResponse.

        事件ID

        :param event_id: The event_id of this ShowDetailOfEventTraceResponse.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def event_source(self):
        """Gets the event_source of this ShowDetailOfEventTraceResponse.

        事件源

        :return: The event_source of this ShowDetailOfEventTraceResponse.
        :rtype: str
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        """Sets the event_source of this ShowDetailOfEventTraceResponse.

        事件源

        :param event_source: The event_source of this ShowDetailOfEventTraceResponse.
        :type event_source: str
        """
        self._event_source = event_source

    @property
    def event_type(self):
        """Gets the event_type of this ShowDetailOfEventTraceResponse.

        事件类型

        :return: The event_type of this ShowDetailOfEventTraceResponse.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ShowDetailOfEventTraceResponse.

        事件类型

        :param event_type: The event_type of this ShowDetailOfEventTraceResponse.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def receive_time(self):
        """Gets the receive_time of this ShowDetailOfEventTraceResponse.

        接收时间

        :return: The receive_time of this ShowDetailOfEventTraceResponse.
        :rtype: str
        """
        return self._receive_time

    @receive_time.setter
    def receive_time(self, receive_time):
        """Sets the receive_time of this ShowDetailOfEventTraceResponse.

        接收时间

        :param receive_time: The receive_time of this ShowDetailOfEventTraceResponse.
        :type receive_time: str
        """
        self._receive_time = receive_time

    @property
    def channel_id(self):
        """Gets the channel_id of this ShowDetailOfEventTraceResponse.

        通道ID

        :return: The channel_id of this ShowDetailOfEventTraceResponse.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this ShowDetailOfEventTraceResponse.

        通道ID

        :param channel_id: The channel_id of this ShowDetailOfEventTraceResponse.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def channel_name(self):
        """Gets the channel_name of this ShowDetailOfEventTraceResponse.

        通道名称

        :return: The channel_name of this ShowDetailOfEventTraceResponse.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """Sets the channel_name of this ShowDetailOfEventTraceResponse.

        通道名称

        :param channel_name: The channel_name of this ShowDetailOfEventTraceResponse.
        :type channel_name: str
        """
        self._channel_name = channel_name

    @property
    def deliver_list(self):
        """Gets the deliver_list of this ShowDetailOfEventTraceResponse.

        事件投递列表

        :return: The deliver_list of this ShowDetailOfEventTraceResponse.
        :rtype: list[:class:`huaweicloudsdkeg.v1.DeliverItem`]
        """
        return self._deliver_list

    @deliver_list.setter
    def deliver_list(self, deliver_list):
        """Sets the deliver_list of this ShowDetailOfEventTraceResponse.

        事件投递列表

        :param deliver_list: The deliver_list of this ShowDetailOfEventTraceResponse.
        :type deliver_list: list[:class:`huaweicloudsdkeg.v1.DeliverItem`]
        """
        self._deliver_list = deliver_list

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
        if not isinstance(other, ShowDetailOfEventTraceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
