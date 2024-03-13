# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSmartChatRoomsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'smart_chat_rooms': 'list[SmartChatRoomBaseInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'smart_chat_rooms': 'smart_chat_rooms',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, count=None, smart_chat_rooms=None, x_request_id=None):
        """ListSmartChatRoomsResponse

        The model defined in huaweicloud sdk

        :param count: 智能交互对话直播间总数。
        :type count: int
        :param smart_chat_rooms: 智能交互对话直播间列表。
        :type smart_chat_rooms: list[:class:`huaweicloudsdkmetastudio.v1.SmartChatRoomBaseInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListSmartChatRoomsResponse, self).__init__()

        self._count = None
        self._smart_chat_rooms = None
        self._x_request_id = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if smart_chat_rooms is not None:
            self.smart_chat_rooms = smart_chat_rooms
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def count(self):
        """Gets the count of this ListSmartChatRoomsResponse.

        智能交互对话直播间总数。

        :return: The count of this ListSmartChatRoomsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListSmartChatRoomsResponse.

        智能交互对话直播间总数。

        :param count: The count of this ListSmartChatRoomsResponse.
        :type count: int
        """
        self._count = count

    @property
    def smart_chat_rooms(self):
        """Gets the smart_chat_rooms of this ListSmartChatRoomsResponse.

        智能交互对话直播间列表。

        :return: The smart_chat_rooms of this ListSmartChatRoomsResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.SmartChatRoomBaseInfo`]
        """
        return self._smart_chat_rooms

    @smart_chat_rooms.setter
    def smart_chat_rooms(self, smart_chat_rooms):
        """Sets the smart_chat_rooms of this ListSmartChatRoomsResponse.

        智能交互对话直播间列表。

        :param smart_chat_rooms: The smart_chat_rooms of this ListSmartChatRoomsResponse.
        :type smart_chat_rooms: list[:class:`huaweicloudsdkmetastudio.v1.SmartChatRoomBaseInfo`]
        """
        self._smart_chat_rooms = smart_chat_rooms

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListSmartChatRoomsResponse.

        :return: The x_request_id of this ListSmartChatRoomsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListSmartChatRoomsResponse.

        :param x_request_id: The x_request_id of this ListSmartChatRoomsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListSmartChatRoomsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
