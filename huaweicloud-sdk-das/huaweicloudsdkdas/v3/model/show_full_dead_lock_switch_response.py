# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFullDeadLockSwitchResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch_on': 'bool',
        'retention_hours': 'int',
        'can_open': 'bool',
        'cant_open_msg': 'str'
    }

    attribute_map = {
        'switch_on': 'switch_on',
        'retention_hours': 'retention_hours',
        'can_open': 'can_open',
        'cant_open_msg': 'cant_open_msg'
    }

    def __init__(self, switch_on=None, retention_hours=None, can_open=None, cant_open_msg=None):
        r"""ShowFullDeadLockSwitchResponse

        The model defined in huaweicloud sdk

        :param switch_on: 开关状态
        :type switch_on: bool
        :param retention_hours: 保存时长
        :type retention_hours: int
        :param can_open: 是否可以开启
        :type can_open: bool
        :param cant_open_msg: 无法开启原因
        :type cant_open_msg: str
        """
        
        super(ShowFullDeadLockSwitchResponse, self).__init__()

        self._switch_on = None
        self._retention_hours = None
        self._can_open = None
        self._cant_open_msg = None
        self.discriminator = None

        if switch_on is not None:
            self.switch_on = switch_on
        if retention_hours is not None:
            self.retention_hours = retention_hours
        if can_open is not None:
            self.can_open = can_open
        if cant_open_msg is not None:
            self.cant_open_msg = cant_open_msg

    @property
    def switch_on(self):
        r"""Gets the switch_on of this ShowFullDeadLockSwitchResponse.

        开关状态

        :return: The switch_on of this ShowFullDeadLockSwitchResponse.
        :rtype: bool
        """
        return self._switch_on

    @switch_on.setter
    def switch_on(self, switch_on):
        r"""Sets the switch_on of this ShowFullDeadLockSwitchResponse.

        开关状态

        :param switch_on: The switch_on of this ShowFullDeadLockSwitchResponse.
        :type switch_on: bool
        """
        self._switch_on = switch_on

    @property
    def retention_hours(self):
        r"""Gets the retention_hours of this ShowFullDeadLockSwitchResponse.

        保存时长

        :return: The retention_hours of this ShowFullDeadLockSwitchResponse.
        :rtype: int
        """
        return self._retention_hours

    @retention_hours.setter
    def retention_hours(self, retention_hours):
        r"""Sets the retention_hours of this ShowFullDeadLockSwitchResponse.

        保存时长

        :param retention_hours: The retention_hours of this ShowFullDeadLockSwitchResponse.
        :type retention_hours: int
        """
        self._retention_hours = retention_hours

    @property
    def can_open(self):
        r"""Gets the can_open of this ShowFullDeadLockSwitchResponse.

        是否可以开启

        :return: The can_open of this ShowFullDeadLockSwitchResponse.
        :rtype: bool
        """
        return self._can_open

    @can_open.setter
    def can_open(self, can_open):
        r"""Sets the can_open of this ShowFullDeadLockSwitchResponse.

        是否可以开启

        :param can_open: The can_open of this ShowFullDeadLockSwitchResponse.
        :type can_open: bool
        """
        self._can_open = can_open

    @property
    def cant_open_msg(self):
        r"""Gets the cant_open_msg of this ShowFullDeadLockSwitchResponse.

        无法开启原因

        :return: The cant_open_msg of this ShowFullDeadLockSwitchResponse.
        :rtype: str
        """
        return self._cant_open_msg

    @cant_open_msg.setter
    def cant_open_msg(self, cant_open_msg):
        r"""Sets the cant_open_msg of this ShowFullDeadLockSwitchResponse.

        无法开启原因

        :param cant_open_msg: The cant_open_msg of this ShowFullDeadLockSwitchResponse.
        :type cant_open_msg: str
        """
        self._cant_open_msg = cant_open_msg

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
        if not isinstance(other, ShowFullDeadLockSwitchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
