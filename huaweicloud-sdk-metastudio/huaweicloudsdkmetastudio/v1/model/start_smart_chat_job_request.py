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
        'robot_id': 'str',
        'body': 'SmartChatJobsReq'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'room_id': 'room_id',
        'robot_id': 'robot_id',
        'body': 'body'
    }

    def __init__(self, x_app_user_id=None, room_id=None, robot_id=None, body=None):
        r"""StartSmartChatJobRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param room_id: 智能交互对话ID，获取方法请参考[创建智能交互对话直播间](CreateSmartChatRoom.xml)。
        :type room_id: str
        :param robot_id: 应用ID，获取方法请参考[创建应用](CreateRobot.xml)。
        :type robot_id: str
        :param body: Body of the StartSmartChatJobRequest
        :type body: :class:`huaweicloudsdkmetastudio.v1.SmartChatJobsReq`
        """
        
        

        self._x_app_user_id = None
        self._room_id = None
        self._robot_id = None
        self._body = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        self.room_id = room_id
        self.robot_id = robot_id
        if body is not None:
            self.body = body

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this StartSmartChatJobRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this StartSmartChatJobRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this StartSmartChatJobRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this StartSmartChatJobRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def room_id(self):
        r"""Gets the room_id of this StartSmartChatJobRequest.

        智能交互对话ID，获取方法请参考[创建智能交互对话直播间](CreateSmartChatRoom.xml)。

        :return: The room_id of this StartSmartChatJobRequest.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        r"""Sets the room_id of this StartSmartChatJobRequest.

        智能交互对话ID，获取方法请参考[创建智能交互对话直播间](CreateSmartChatRoom.xml)。

        :param room_id: The room_id of this StartSmartChatJobRequest.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def robot_id(self):
        r"""Gets the robot_id of this StartSmartChatJobRequest.

        应用ID，获取方法请参考[创建应用](CreateRobot.xml)。

        :return: The robot_id of this StartSmartChatJobRequest.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this StartSmartChatJobRequest.

        应用ID，获取方法请参考[创建应用](CreateRobot.xml)。

        :param robot_id: The robot_id of this StartSmartChatJobRequest.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def body(self):
        r"""Gets the body of this StartSmartChatJobRequest.

        :return: The body of this StartSmartChatJobRequest.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SmartChatJobsReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this StartSmartChatJobRequest.

        :param body: The body of this StartSmartChatJobRequest.
        :type body: :class:`huaweicloudsdkmetastudio.v1.SmartChatJobsReq`
        """
        self._body = body

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
