# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSmartChatJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'room_id': 'str',
        'state': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'room_id': 'room_id',
        'state': 'state',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_app_user_id=None, room_id=None, state=None, offset=None, limit=None):
        r"""ListSmartChatJobRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param room_id: 智能交互对话ID，获取方法请参考[创建智能交互对话直播间](CreateSmartChatRoom.xml)。
        :type room_id: str
        :param state: 任务状态，默认所有状态。  可多个状态查询，使用英文逗号分隔。  如state&#x3D;CREATING,PUBLISHED
        :type state: str
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        """
        
        

        self._x_app_user_id = None
        self._room_id = None
        self._state = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        self.room_id = room_id
        if state is not None:
            self.state = state
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ListSmartChatJobRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListSmartChatJobRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ListSmartChatJobRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListSmartChatJobRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def room_id(self):
        r"""Gets the room_id of this ListSmartChatJobRequest.

        智能交互对话ID，获取方法请参考[创建智能交互对话直播间](CreateSmartChatRoom.xml)。

        :return: The room_id of this ListSmartChatJobRequest.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        r"""Sets the room_id of this ListSmartChatJobRequest.

        智能交互对话ID，获取方法请参考[创建智能交互对话直播间](CreateSmartChatRoom.xml)。

        :param room_id: The room_id of this ListSmartChatJobRequest.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def state(self):
        r"""Gets the state of this ListSmartChatJobRequest.

        任务状态，默认所有状态。  可多个状态查询，使用英文逗号分隔。  如state=CREATING,PUBLISHED

        :return: The state of this ListSmartChatJobRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListSmartChatJobRequest.

        任务状态，默认所有状态。  可多个状态查询，使用英文逗号分隔。  如state=CREATING,PUBLISHED

        :param state: The state of this ListSmartChatJobRequest.
        :type state: str
        """
        self._state = state

    @property
    def offset(self):
        r"""Gets the offset of this ListSmartChatJobRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListSmartChatJobRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSmartChatJobRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListSmartChatJobRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSmartChatJobRequest.

        每页显示的条目数量。

        :return: The limit of this ListSmartChatJobRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSmartChatJobRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListSmartChatJobRequest.
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
        if not isinstance(other, ListSmartChatJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
