# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRobotResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'robot_id': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'robot_id': 'robot_id',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, robot_id=None, x_request_id=None):
        r"""CreateRobotResponse

        The model defined in huaweicloud sdk

        :param robot_id: 应用ID。
        :type robot_id: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CreateRobotResponse, self).__init__()

        self._robot_id = None
        self._x_request_id = None
        self.discriminator = None

        if robot_id is not None:
            self.robot_id = robot_id
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def robot_id(self):
        r"""Gets the robot_id of this CreateRobotResponse.

        应用ID。

        :return: The robot_id of this CreateRobotResponse.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this CreateRobotResponse.

        应用ID。

        :param robot_id: The robot_id of this CreateRobotResponse.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CreateRobotResponse.

        :return: The x_request_id of this CreateRobotResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CreateRobotResponse.

        :param x_request_id: The x_request_id of this CreateRobotResponse.
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
        if not isinstance(other, CreateRobotResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
