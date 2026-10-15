# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BigKeyHotKeySwitchStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'open_status': 'int',
        'retention_hours': 'int',
        'can_open': 'bool',
        'cant_open_msg': 'str',
        'last_open_time': 'int'
    }

    attribute_map = {
        'open_status': 'open_status',
        'retention_hours': 'retention_hours',
        'can_open': 'can_open',
        'cant_open_msg': 'cant_open_msg',
        'last_open_time': 'last_open_time'
    }

    def __init__(self, open_status=None, retention_hours=None, can_open=None, cant_open_msg=None, last_open_time=None):
        r"""BigKeyHotKeySwitchStatus

        The model defined in huaweicloud sdk

        :param open_status: 开关状态。0-关闭，1-开启
        :type open_status: int
        :param retention_hours: 数据保留小时数
        :type retention_hours: int
        :param can_open: 是否可以开启
        :type can_open: bool
        :param cant_open_msg: 无法开启的原因（如内核版本不满足等）
        :type cant_open_msg: str
        :param last_open_time: 最后开启时间（毫秒时间戳）
        :type last_open_time: int
        """
        
        

        self._open_status = None
        self._retention_hours = None
        self._can_open = None
        self._cant_open_msg = None
        self._last_open_time = None
        self.discriminator = None

        if open_status is not None:
            self.open_status = open_status
        if retention_hours is not None:
            self.retention_hours = retention_hours
        if can_open is not None:
            self.can_open = can_open
        if cant_open_msg is not None:
            self.cant_open_msg = cant_open_msg
        if last_open_time is not None:
            self.last_open_time = last_open_time

    @property
    def open_status(self):
        r"""Gets the open_status of this BigKeyHotKeySwitchStatus.

        开关状态。0-关闭，1-开启

        :return: The open_status of this BigKeyHotKeySwitchStatus.
        :rtype: int
        """
        return self._open_status

    @open_status.setter
    def open_status(self, open_status):
        r"""Sets the open_status of this BigKeyHotKeySwitchStatus.

        开关状态。0-关闭，1-开启

        :param open_status: The open_status of this BigKeyHotKeySwitchStatus.
        :type open_status: int
        """
        self._open_status = open_status

    @property
    def retention_hours(self):
        r"""Gets the retention_hours of this BigKeyHotKeySwitchStatus.

        数据保留小时数

        :return: The retention_hours of this BigKeyHotKeySwitchStatus.
        :rtype: int
        """
        return self._retention_hours

    @retention_hours.setter
    def retention_hours(self, retention_hours):
        r"""Sets the retention_hours of this BigKeyHotKeySwitchStatus.

        数据保留小时数

        :param retention_hours: The retention_hours of this BigKeyHotKeySwitchStatus.
        :type retention_hours: int
        """
        self._retention_hours = retention_hours

    @property
    def can_open(self):
        r"""Gets the can_open of this BigKeyHotKeySwitchStatus.

        是否可以开启

        :return: The can_open of this BigKeyHotKeySwitchStatus.
        :rtype: bool
        """
        return self._can_open

    @can_open.setter
    def can_open(self, can_open):
        r"""Sets the can_open of this BigKeyHotKeySwitchStatus.

        是否可以开启

        :param can_open: The can_open of this BigKeyHotKeySwitchStatus.
        :type can_open: bool
        """
        self._can_open = can_open

    @property
    def cant_open_msg(self):
        r"""Gets the cant_open_msg of this BigKeyHotKeySwitchStatus.

        无法开启的原因（如内核版本不满足等）

        :return: The cant_open_msg of this BigKeyHotKeySwitchStatus.
        :rtype: str
        """
        return self._cant_open_msg

    @cant_open_msg.setter
    def cant_open_msg(self, cant_open_msg):
        r"""Sets the cant_open_msg of this BigKeyHotKeySwitchStatus.

        无法开启的原因（如内核版本不满足等）

        :param cant_open_msg: The cant_open_msg of this BigKeyHotKeySwitchStatus.
        :type cant_open_msg: str
        """
        self._cant_open_msg = cant_open_msg

    @property
    def last_open_time(self):
        r"""Gets the last_open_time of this BigKeyHotKeySwitchStatus.

        最后开启时间（毫秒时间戳）

        :return: The last_open_time of this BigKeyHotKeySwitchStatus.
        :rtype: int
        """
        return self._last_open_time

    @last_open_time.setter
    def last_open_time(self, last_open_time):
        r"""Sets the last_open_time of this BigKeyHotKeySwitchStatus.

        最后开启时间（毫秒时间戳）

        :param last_open_time: The last_open_time of this BigKeyHotKeySwitchStatus.
        :type last_open_time: int
        """
        self._last_open_time = last_open_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BigKeyHotKeySwitchStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
