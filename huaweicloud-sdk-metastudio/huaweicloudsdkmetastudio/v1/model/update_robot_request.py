# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRobotRequest:

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
        'robot_id': 'str',
        'body': 'UpdateRobotReq'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'robot_id': 'robot_id',
        'body': 'body'
    }

    def __init__(self, x_app_user_id=None, robot_id=None, body=None):
        r"""UpdateRobotRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param robot_id: 应用ID。
        :type robot_id: str
        :param body: Body of the UpdateRobotRequest
        :type body: :class:`huaweicloudsdkmetastudio.v1.UpdateRobotReq`
        """
        
        

        self._x_app_user_id = None
        self._robot_id = None
        self._body = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        self.robot_id = robot_id
        if body is not None:
            self.body = body

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this UpdateRobotRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this UpdateRobotRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this UpdateRobotRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this UpdateRobotRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def robot_id(self):
        r"""Gets the robot_id of this UpdateRobotRequest.

        应用ID。

        :return: The robot_id of this UpdateRobotRequest.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this UpdateRobotRequest.

        应用ID。

        :param robot_id: The robot_id of this UpdateRobotRequest.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def body(self):
        r"""Gets the body of this UpdateRobotRequest.

        :return: The body of this UpdateRobotRequest.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateRobotReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateRobotRequest.

        :param body: The body of this UpdateRobotRequest.
        :type body: :class:`huaweicloudsdkmetastudio.v1.UpdateRobotReq`
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
        if not isinstance(other, UpdateRobotRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
