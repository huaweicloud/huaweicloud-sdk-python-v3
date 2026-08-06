# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchFullsqlSwitchResponse(SdkResponse):

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
        'retention_days': 'int',
        'can_open': 'bool',
        'cant_open_msg': 'str',
        'last_open_time': 'float'
    }

    attribute_map = {
        'open_status': 'open_status',
        'retention_days': 'retention_days',
        'can_open': 'can_open',
        'cant_open_msg': 'cant_open_msg',
        'last_open_time': 'last_open_time'
    }

    def __init__(self, open_status=None, retention_days=None, can_open=None, cant_open_msg=None, last_open_time=None):
        r"""SwitchFullsqlSwitchResponse

        The model defined in huaweicloud sdk

        :param open_status: 开关状态
        :type open_status: int
        :param retention_days: 保留天数
        :type retention_days: int
        :param can_open: 是否能开启
        :type can_open: bool
        :param cant_open_msg: 不能开启的原因
        :type cant_open_msg: str
        :param last_open_time: 上次开启时间
        :type last_open_time: float
        """
        
        super().__init__()

        self._open_status = None
        self._retention_days = None
        self._can_open = None
        self._cant_open_msg = None
        self._last_open_time = None
        self.discriminator = None

        if open_status is not None:
            self.open_status = open_status
        if retention_days is not None:
            self.retention_days = retention_days
        if can_open is not None:
            self.can_open = can_open
        if cant_open_msg is not None:
            self.cant_open_msg = cant_open_msg
        if last_open_time is not None:
            self.last_open_time = last_open_time

    @property
    def open_status(self):
        r"""Gets the open_status of this SwitchFullsqlSwitchResponse.

        开关状态

        :return: The open_status of this SwitchFullsqlSwitchResponse.
        :rtype: int
        """
        return self._open_status

    @open_status.setter
    def open_status(self, open_status):
        r"""Sets the open_status of this SwitchFullsqlSwitchResponse.

        开关状态

        :param open_status: The open_status of this SwitchFullsqlSwitchResponse.
        :type open_status: int
        """
        self._open_status = open_status

    @property
    def retention_days(self):
        r"""Gets the retention_days of this SwitchFullsqlSwitchResponse.

        保留天数

        :return: The retention_days of this SwitchFullsqlSwitchResponse.
        :rtype: int
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        r"""Sets the retention_days of this SwitchFullsqlSwitchResponse.

        保留天数

        :param retention_days: The retention_days of this SwitchFullsqlSwitchResponse.
        :type retention_days: int
        """
        self._retention_days = retention_days

    @property
    def can_open(self):
        r"""Gets the can_open of this SwitchFullsqlSwitchResponse.

        是否能开启

        :return: The can_open of this SwitchFullsqlSwitchResponse.
        :rtype: bool
        """
        return self._can_open

    @can_open.setter
    def can_open(self, can_open):
        r"""Sets the can_open of this SwitchFullsqlSwitchResponse.

        是否能开启

        :param can_open: The can_open of this SwitchFullsqlSwitchResponse.
        :type can_open: bool
        """
        self._can_open = can_open

    @property
    def cant_open_msg(self):
        r"""Gets the cant_open_msg of this SwitchFullsqlSwitchResponse.

        不能开启的原因

        :return: The cant_open_msg of this SwitchFullsqlSwitchResponse.
        :rtype: str
        """
        return self._cant_open_msg

    @cant_open_msg.setter
    def cant_open_msg(self, cant_open_msg):
        r"""Sets the cant_open_msg of this SwitchFullsqlSwitchResponse.

        不能开启的原因

        :param cant_open_msg: The cant_open_msg of this SwitchFullsqlSwitchResponse.
        :type cant_open_msg: str
        """
        self._cant_open_msg = cant_open_msg

    @property
    def last_open_time(self):
        r"""Gets the last_open_time of this SwitchFullsqlSwitchResponse.

        上次开启时间

        :return: The last_open_time of this SwitchFullsqlSwitchResponse.
        :rtype: float
        """
        return self._last_open_time

    @last_open_time.setter
    def last_open_time(self, last_open_time):
        r"""Sets the last_open_time of this SwitchFullsqlSwitchResponse.

        上次开启时间

        :param last_open_time: The last_open_time of this SwitchFullsqlSwitchResponse.
        :type last_open_time: float
        """
        self._last_open_time = last_open_time

    def to_dict(self):
        import warnings
        warnings.warn("SwitchFullsqlSwitchResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, SwitchFullsqlSwitchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
