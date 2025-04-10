# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateActiveCodeReq:

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
        'room_id': 'str',
        'valid_period': 'int'
    }

    attribute_map = {
        'robot_id': 'robot_id',
        'room_id': 'room_id',
        'valid_period': 'valid_period'
    }

    def __init__(self, robot_id=None, room_id=None, valid_period=None):
        r"""CreateActiveCodeReq

        The model defined in huaweicloud sdk

        :param robot_id: 应用ID。
        :type robot_id: str
        :param room_id: 智能交互对话ID。
        :type room_id: str
        :param valid_period: 有效天数（0表示长期有效）。
        :type valid_period: int
        """
        
        

        self._robot_id = None
        self._room_id = None
        self._valid_period = None
        self.discriminator = None

        self.robot_id = robot_id
        self.room_id = room_id
        self.valid_period = valid_period

    @property
    def robot_id(self):
        r"""Gets the robot_id of this CreateActiveCodeReq.

        应用ID。

        :return: The robot_id of this CreateActiveCodeReq.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this CreateActiveCodeReq.

        应用ID。

        :param robot_id: The robot_id of this CreateActiveCodeReq.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def room_id(self):
        r"""Gets the room_id of this CreateActiveCodeReq.

        智能交互对话ID。

        :return: The room_id of this CreateActiveCodeReq.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        r"""Sets the room_id of this CreateActiveCodeReq.

        智能交互对话ID。

        :param room_id: The room_id of this CreateActiveCodeReq.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def valid_period(self):
        r"""Gets the valid_period of this CreateActiveCodeReq.

        有效天数（0表示长期有效）。

        :return: The valid_period of this CreateActiveCodeReq.
        :rtype: int
        """
        return self._valid_period

    @valid_period.setter
    def valid_period(self, valid_period):
        r"""Sets the valid_period of this CreateActiveCodeReq.

        有效天数（0表示长期有效）。

        :param valid_period: The valid_period of this CreateActiveCodeReq.
        :type valid_period: int
        """
        self._valid_period = valid_period

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
        if not isinstance(other, CreateActiveCodeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
