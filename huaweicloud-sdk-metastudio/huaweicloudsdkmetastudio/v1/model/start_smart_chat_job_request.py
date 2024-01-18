# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartSmartChatJobRequest:

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
        'robot_id': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'room_id': 'room_id',
        'robot_id': 'robot_id'
    }

    def __init__(self, x_app_user_id=None, room_id=None, robot_id=None):
        """StartSmartChatJobRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。 &gt; * 不允许输入中文。
        :type x_app_user_id: str
        :param room_id: 直播间ID。
        :type room_id: str
        :param robot_id: 机器人ID。
        :type robot_id: str
        """
        
        

        self._x_app_user_id = None
        self._room_id = None
        self._robot_id = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        self.room_id = room_id
        self.robot_id = robot_id

    @property
    def x_app_user_id(self):
        """Gets the x_app_user_id of this StartSmartChatJobRequest.

        第三方用户ID。 > * 不允许输入中文。

        :return: The x_app_user_id of this StartSmartChatJobRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        """Sets the x_app_user_id of this StartSmartChatJobRequest.

        第三方用户ID。 > * 不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this StartSmartChatJobRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def room_id(self):
        """Gets the room_id of this StartSmartChatJobRequest.

        直播间ID。

        :return: The room_id of this StartSmartChatJobRequest.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this StartSmartChatJobRequest.

        直播间ID。

        :param room_id: The room_id of this StartSmartChatJobRequest.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def robot_id(self):
        """Gets the robot_id of this StartSmartChatJobRequest.

        机器人ID。

        :return: The robot_id of this StartSmartChatJobRequest.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        """Sets the robot_id of this StartSmartChatJobRequest.

        机器人ID。

        :param robot_id: The robot_id of this StartSmartChatJobRequest.
        :type robot_id: str
        """
        self._robot_id = robot_id

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
        if not isinstance(other, StartSmartChatJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
