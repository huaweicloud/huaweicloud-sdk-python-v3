# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDisasterRecoveryReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dr_sync_period': 'str',
        'send_request': 'int',
        'primary_to_role': 'str',
        'reset_action': 'str',
        'standby_to_role': 'str',
        'dr_status': 'str'
    }

    attribute_map = {
        'dr_sync_period': 'dr_sync_period',
        'send_request': 'send_request',
        'primary_to_role': 'primary_to_role',
        'reset_action': 'reset_action',
        'standby_to_role': 'standby_to_role',
        'dr_status': 'dr_status'
    }

    def __init__(self, dr_sync_period=None, send_request=None, primary_to_role=None, reset_action=None, standby_to_role=None, dr_status=None):
        """UpdateDisasterRecoveryReq

        The model defined in huaweicloud sdk

        :param dr_sync_period: 容灾同步周期
        :type dr_sync_period: str
        :param send_request: 是否发送请求
        :type send_request: int
        :param primary_to_role: 主集群角色
        :type primary_to_role: str
        :param reset_action: 设置容灾动作
        :type reset_action: str
        :param standby_to_role: 备集群角色
        :type standby_to_role: str
        :param dr_status: 容灾状态
        :type dr_status: str
        """
        
        

        self._dr_sync_period = None
        self._send_request = None
        self._primary_to_role = None
        self._reset_action = None
        self._standby_to_role = None
        self._dr_status = None
        self.discriminator = None

        if dr_sync_period is not None:
            self.dr_sync_period = dr_sync_period
        if send_request is not None:
            self.send_request = send_request
        if primary_to_role is not None:
            self.primary_to_role = primary_to_role
        if reset_action is not None:
            self.reset_action = reset_action
        if standby_to_role is not None:
            self.standby_to_role = standby_to_role
        if dr_status is not None:
            self.dr_status = dr_status

    @property
    def dr_sync_period(self):
        """Gets the dr_sync_period of this UpdateDisasterRecoveryReq.

        容灾同步周期

        :return: The dr_sync_period of this UpdateDisasterRecoveryReq.
        :rtype: str
        """
        return self._dr_sync_period

    @dr_sync_period.setter
    def dr_sync_period(self, dr_sync_period):
        """Sets the dr_sync_period of this UpdateDisasterRecoveryReq.

        容灾同步周期

        :param dr_sync_period: The dr_sync_period of this UpdateDisasterRecoveryReq.
        :type dr_sync_period: str
        """
        self._dr_sync_period = dr_sync_period

    @property
    def send_request(self):
        """Gets the send_request of this UpdateDisasterRecoveryReq.

        是否发送请求

        :return: The send_request of this UpdateDisasterRecoveryReq.
        :rtype: int
        """
        return self._send_request

    @send_request.setter
    def send_request(self, send_request):
        """Sets the send_request of this UpdateDisasterRecoveryReq.

        是否发送请求

        :param send_request: The send_request of this UpdateDisasterRecoveryReq.
        :type send_request: int
        """
        self._send_request = send_request

    @property
    def primary_to_role(self):
        """Gets the primary_to_role of this UpdateDisasterRecoveryReq.

        主集群角色

        :return: The primary_to_role of this UpdateDisasterRecoveryReq.
        :rtype: str
        """
        return self._primary_to_role

    @primary_to_role.setter
    def primary_to_role(self, primary_to_role):
        """Sets the primary_to_role of this UpdateDisasterRecoveryReq.

        主集群角色

        :param primary_to_role: The primary_to_role of this UpdateDisasterRecoveryReq.
        :type primary_to_role: str
        """
        self._primary_to_role = primary_to_role

    @property
    def reset_action(self):
        """Gets the reset_action of this UpdateDisasterRecoveryReq.

        设置容灾动作

        :return: The reset_action of this UpdateDisasterRecoveryReq.
        :rtype: str
        """
        return self._reset_action

    @reset_action.setter
    def reset_action(self, reset_action):
        """Sets the reset_action of this UpdateDisasterRecoveryReq.

        设置容灾动作

        :param reset_action: The reset_action of this UpdateDisasterRecoveryReq.
        :type reset_action: str
        """
        self._reset_action = reset_action

    @property
    def standby_to_role(self):
        """Gets the standby_to_role of this UpdateDisasterRecoveryReq.

        备集群角色

        :return: The standby_to_role of this UpdateDisasterRecoveryReq.
        :rtype: str
        """
        return self._standby_to_role

    @standby_to_role.setter
    def standby_to_role(self, standby_to_role):
        """Sets the standby_to_role of this UpdateDisasterRecoveryReq.

        备集群角色

        :param standby_to_role: The standby_to_role of this UpdateDisasterRecoveryReq.
        :type standby_to_role: str
        """
        self._standby_to_role = standby_to_role

    @property
    def dr_status(self):
        """Gets the dr_status of this UpdateDisasterRecoveryReq.

        容灾状态

        :return: The dr_status of this UpdateDisasterRecoveryReq.
        :rtype: str
        """
        return self._dr_status

    @dr_status.setter
    def dr_status(self, dr_status):
        """Sets the dr_status of this UpdateDisasterRecoveryReq.

        容灾状态

        :param dr_status: The dr_status of this UpdateDisasterRecoveryReq.
        :type dr_status: str
        """
        self._dr_status = dr_status

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
        if not isinstance(other, UpdateDisasterRecoveryReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
