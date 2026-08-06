# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLockBlockingSwitchResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'bool',
        'switch_on': 'bool',
        'retention_hours': 'int',
        'retry': 'bool',
        'error_msg': 'str',
        'can_open': 'bool',
        'cant_open_msg': 'str'
    }

    attribute_map = {
        'success': 'success',
        'switch_on': 'switch_on',
        'retention_hours': 'retention_hours',
        'retry': 'retry',
        'error_msg': 'error_msg',
        'can_open': 'can_open',
        'cant_open_msg': 'cant_open_msg'
    }

    def __init__(self, success=None, switch_on=None, retention_hours=None, retry=None, error_msg=None, can_open=None, cant_open_msg=None):
        r"""ShowLockBlockingSwitchResponse

        The model defined in huaweicloud sdk

        :param success: 是否成功
        :type success: bool
        :param switch_on: 开关状态
        :type switch_on: bool
        :param retention_hours: 保存时长
        :type retention_hours: int
        :param retry: 是否需要重试
        :type retry: bool
        :param error_msg: 错误信息
        :type error_msg: str
        :param can_open: 是否可以开启
        :type can_open: bool
        :param cant_open_msg: 无法开启原因
        :type cant_open_msg: str
        """
        
        super().__init__()

        self._success = None
        self._switch_on = None
        self._retention_hours = None
        self._retry = None
        self._error_msg = None
        self._can_open = None
        self._cant_open_msg = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if switch_on is not None:
            self.switch_on = switch_on
        if retention_hours is not None:
            self.retention_hours = retention_hours
        if retry is not None:
            self.retry = retry
        if error_msg is not None:
            self.error_msg = error_msg
        if can_open is not None:
            self.can_open = can_open
        if cant_open_msg is not None:
            self.cant_open_msg = cant_open_msg

    @property
    def success(self):
        r"""Gets the success of this ShowLockBlockingSwitchResponse.

        是否成功

        :return: The success of this ShowLockBlockingSwitchResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ShowLockBlockingSwitchResponse.

        是否成功

        :param success: The success of this ShowLockBlockingSwitchResponse.
        :type success: bool
        """
        self._success = success

    @property
    def switch_on(self):
        r"""Gets the switch_on of this ShowLockBlockingSwitchResponse.

        开关状态

        :return: The switch_on of this ShowLockBlockingSwitchResponse.
        :rtype: bool
        """
        return self._switch_on

    @switch_on.setter
    def switch_on(self, switch_on):
        r"""Sets the switch_on of this ShowLockBlockingSwitchResponse.

        开关状态

        :param switch_on: The switch_on of this ShowLockBlockingSwitchResponse.
        :type switch_on: bool
        """
        self._switch_on = switch_on

    @property
    def retention_hours(self):
        r"""Gets the retention_hours of this ShowLockBlockingSwitchResponse.

        保存时长

        :return: The retention_hours of this ShowLockBlockingSwitchResponse.
        :rtype: int
        """
        return self._retention_hours

    @retention_hours.setter
    def retention_hours(self, retention_hours):
        r"""Sets the retention_hours of this ShowLockBlockingSwitchResponse.

        保存时长

        :param retention_hours: The retention_hours of this ShowLockBlockingSwitchResponse.
        :type retention_hours: int
        """
        self._retention_hours = retention_hours

    @property
    def retry(self):
        r"""Gets the retry of this ShowLockBlockingSwitchResponse.

        是否需要重试

        :return: The retry of this ShowLockBlockingSwitchResponse.
        :rtype: bool
        """
        return self._retry

    @retry.setter
    def retry(self, retry):
        r"""Sets the retry of this ShowLockBlockingSwitchResponse.

        是否需要重试

        :param retry: The retry of this ShowLockBlockingSwitchResponse.
        :type retry: bool
        """
        self._retry = retry

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ShowLockBlockingSwitchResponse.

        错误信息

        :return: The error_msg of this ShowLockBlockingSwitchResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ShowLockBlockingSwitchResponse.

        错误信息

        :param error_msg: The error_msg of this ShowLockBlockingSwitchResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def can_open(self):
        r"""Gets the can_open of this ShowLockBlockingSwitchResponse.

        是否可以开启

        :return: The can_open of this ShowLockBlockingSwitchResponse.
        :rtype: bool
        """
        return self._can_open

    @can_open.setter
    def can_open(self, can_open):
        r"""Sets the can_open of this ShowLockBlockingSwitchResponse.

        是否可以开启

        :param can_open: The can_open of this ShowLockBlockingSwitchResponse.
        :type can_open: bool
        """
        self._can_open = can_open

    @property
    def cant_open_msg(self):
        r"""Gets the cant_open_msg of this ShowLockBlockingSwitchResponse.

        无法开启原因

        :return: The cant_open_msg of this ShowLockBlockingSwitchResponse.
        :rtype: str
        """
        return self._cant_open_msg

    @cant_open_msg.setter
    def cant_open_msg(self, cant_open_msg):
        r"""Sets the cant_open_msg of this ShowLockBlockingSwitchResponse.

        无法开启原因

        :param cant_open_msg: The cant_open_msg of this ShowLockBlockingSwitchResponse.
        :type cant_open_msg: str
        """
        self._cant_open_msg = cant_open_msg

    def to_dict(self):
        import warnings
        warnings.warn("ShowLockBlockingSwitchResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowLockBlockingSwitchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
