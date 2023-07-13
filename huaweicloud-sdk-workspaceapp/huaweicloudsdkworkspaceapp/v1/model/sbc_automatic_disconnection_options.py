# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SbcAutomaticDisconnectionOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disconnection_waiting_time': 'int',
        'sbc_auto_logout': 'bool',
        'auto_logout_options': 'AutoLogoutOptions'
    }

    attribute_map = {
        'disconnection_waiting_time': 'disconnection_waiting_time',
        'sbc_auto_logout': 'sbc_auto_logout',
        'auto_logout_options': 'auto_logout_options'
    }

    def __init__(self, disconnection_waiting_time=None, sbc_auto_logout=None, auto_logout_options=None):
        """SbcAutomaticDisconnectionOptions

        The model defined in huaweicloud sdk

        :param disconnection_waiting_time: 等待时间（分钟）
        :type disconnection_waiting_time: int
        :param sbc_auto_logout: 是否自动注销。取值为：false：表示是。true：表示否。
        :type sbc_auto_logout: bool
        :param auto_logout_options: 
        :type auto_logout_options: :class:`huaweicloudsdkworkspaceapp.v1.AutoLogoutOptions`
        """
        
        

        self._disconnection_waiting_time = None
        self._sbc_auto_logout = None
        self._auto_logout_options = None
        self.discriminator = None

        if disconnection_waiting_time is not None:
            self.disconnection_waiting_time = disconnection_waiting_time
        if sbc_auto_logout is not None:
            self.sbc_auto_logout = sbc_auto_logout
        if auto_logout_options is not None:
            self.auto_logout_options = auto_logout_options

    @property
    def disconnection_waiting_time(self):
        """Gets the disconnection_waiting_time of this SbcAutomaticDisconnectionOptions.

        等待时间（分钟）

        :return: The disconnection_waiting_time of this SbcAutomaticDisconnectionOptions.
        :rtype: int
        """
        return self._disconnection_waiting_time

    @disconnection_waiting_time.setter
    def disconnection_waiting_time(self, disconnection_waiting_time):
        """Sets the disconnection_waiting_time of this SbcAutomaticDisconnectionOptions.

        等待时间（分钟）

        :param disconnection_waiting_time: The disconnection_waiting_time of this SbcAutomaticDisconnectionOptions.
        :type disconnection_waiting_time: int
        """
        self._disconnection_waiting_time = disconnection_waiting_time

    @property
    def sbc_auto_logout(self):
        """Gets the sbc_auto_logout of this SbcAutomaticDisconnectionOptions.

        是否自动注销。取值为：false：表示是。true：表示否。

        :return: The sbc_auto_logout of this SbcAutomaticDisconnectionOptions.
        :rtype: bool
        """
        return self._sbc_auto_logout

    @sbc_auto_logout.setter
    def sbc_auto_logout(self, sbc_auto_logout):
        """Sets the sbc_auto_logout of this SbcAutomaticDisconnectionOptions.

        是否自动注销。取值为：false：表示是。true：表示否。

        :param sbc_auto_logout: The sbc_auto_logout of this SbcAutomaticDisconnectionOptions.
        :type sbc_auto_logout: bool
        """
        self._sbc_auto_logout = sbc_auto_logout

    @property
    def auto_logout_options(self):
        """Gets the auto_logout_options of this SbcAutomaticDisconnectionOptions.

        :return: The auto_logout_options of this SbcAutomaticDisconnectionOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AutoLogoutOptions`
        """
        return self._auto_logout_options

    @auto_logout_options.setter
    def auto_logout_options(self, auto_logout_options):
        """Sets the auto_logout_options of this SbcAutomaticDisconnectionOptions.

        :param auto_logout_options: The auto_logout_options of this SbcAutomaticDisconnectionOptions.
        :type auto_logout_options: :class:`huaweicloudsdkworkspaceapp.v1.AutoLogoutOptions`
        """
        self._auto_logout_options = auto_logout_options

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
        if not isinstance(other, SbcAutomaticDisconnectionOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
