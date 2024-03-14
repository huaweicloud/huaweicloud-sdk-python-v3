# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActiveCodeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'active_code_id': 'str',
        'active_code': 'str',
        'robot_id': 'str',
        'room_id': 'str',
        'valid_period': 'int',
        'expire_time': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'active_code_id': 'active_code_id',
        'active_code': 'active_code',
        'robot_id': 'robot_id',
        'room_id': 'room_id',
        'valid_period': 'valid_period',
        'expire_time': 'expire_time',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, active_code_id=None, active_code=None, robot_id=None, room_id=None, valid_period=None, expire_time=None, create_time=None, update_time=None):
        """ActiveCodeInfo

        The model defined in huaweicloud sdk

        :param active_code_id: 激活码ID。
        :type active_code_id: str
        :param active_code: 激活码。
        :type active_code: str
        :param robot_id: 应用ID。
        :type robot_id: str
        :param room_id: 智能交互对话ID。
        :type room_id: str
        :param valid_period: 有效天数（0表示长期有效）。
        :type valid_period: int
        :param expire_time: 过期时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type expire_time: str
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        """
        
        

        self._active_code_id = None
        self._active_code = None
        self._robot_id = None
        self._room_id = None
        self._valid_period = None
        self._expire_time = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if active_code_id is not None:
            self.active_code_id = active_code_id
        if active_code is not None:
            self.active_code = active_code
        if robot_id is not None:
            self.robot_id = robot_id
        if room_id is not None:
            self.room_id = room_id
        if valid_period is not None:
            self.valid_period = valid_period
        if expire_time is not None:
            self.expire_time = expire_time
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def active_code_id(self):
        """Gets the active_code_id of this ActiveCodeInfo.

        激活码ID。

        :return: The active_code_id of this ActiveCodeInfo.
        :rtype: str
        """
        return self._active_code_id

    @active_code_id.setter
    def active_code_id(self, active_code_id):
        """Sets the active_code_id of this ActiveCodeInfo.

        激活码ID。

        :param active_code_id: The active_code_id of this ActiveCodeInfo.
        :type active_code_id: str
        """
        self._active_code_id = active_code_id

    @property
    def active_code(self):
        """Gets the active_code of this ActiveCodeInfo.

        激活码。

        :return: The active_code of this ActiveCodeInfo.
        :rtype: str
        """
        return self._active_code

    @active_code.setter
    def active_code(self, active_code):
        """Sets the active_code of this ActiveCodeInfo.

        激活码。

        :param active_code: The active_code of this ActiveCodeInfo.
        :type active_code: str
        """
        self._active_code = active_code

    @property
    def robot_id(self):
        """Gets the robot_id of this ActiveCodeInfo.

        应用ID。

        :return: The robot_id of this ActiveCodeInfo.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        """Sets the robot_id of this ActiveCodeInfo.

        应用ID。

        :param robot_id: The robot_id of this ActiveCodeInfo.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def room_id(self):
        """Gets the room_id of this ActiveCodeInfo.

        智能交互对话ID。

        :return: The room_id of this ActiveCodeInfo.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this ActiveCodeInfo.

        智能交互对话ID。

        :param room_id: The room_id of this ActiveCodeInfo.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def valid_period(self):
        """Gets the valid_period of this ActiveCodeInfo.

        有效天数（0表示长期有效）。

        :return: The valid_period of this ActiveCodeInfo.
        :rtype: int
        """
        return self._valid_period

    @valid_period.setter
    def valid_period(self, valid_period):
        """Sets the valid_period of this ActiveCodeInfo.

        有效天数（0表示长期有效）。

        :param valid_period: The valid_period of this ActiveCodeInfo.
        :type valid_period: int
        """
        self._valid_period = valid_period

    @property
    def expire_time(self):
        """Gets the expire_time of this ActiveCodeInfo.

        过期时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The expire_time of this ActiveCodeInfo.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this ActiveCodeInfo.

        过期时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param expire_time: The expire_time of this ActiveCodeInfo.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def create_time(self):
        """Gets the create_time of this ActiveCodeInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this ActiveCodeInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ActiveCodeInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this ActiveCodeInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ActiveCodeInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this ActiveCodeInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ActiveCodeInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this ActiveCodeInfo.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, ActiveCodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
