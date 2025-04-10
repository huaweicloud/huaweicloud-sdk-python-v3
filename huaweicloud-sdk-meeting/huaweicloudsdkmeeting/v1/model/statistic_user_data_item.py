# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticUserDataItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'user_login_count': 'str',
        'user_pc_login_count': 'str',
        'user_mobile_login_count': 'str',
        'user_activated_count': 'str',
        'user_login_devices_name': 'str',
        'user_login_devices_count': 'str'
    }

    attribute_map = {
        'time': 'time',
        'user_login_count': 'userLoginCount',
        'user_pc_login_count': 'userPCLoginCount',
        'user_mobile_login_count': 'userMobileLoginCount',
        'user_activated_count': 'userActivatedCount',
        'user_login_devices_name': 'userLoginDevicesName',
        'user_login_devices_count': 'userLoginDevicesCount'
    }

    def __init__(self, time=None, user_login_count=None, user_pc_login_count=None, user_mobile_login_count=None, user_activated_count=None, user_login_devices_name=None, user_login_devices_count=None):
        r"""StatisticUserDataItem

        The model defined in huaweicloud sdk

        :param time: 日期/月份。
        :type time: str
        :param user_login_count: 登录用户数。 category &#x3D; user_login_info时有效。
        :type user_login_count: str
        :param user_pc_login_count: PC端登录用户数。 category &#x3D; user_login_info时有效。
        :type user_pc_login_count: str
        :param user_mobile_login_count: 移动端登录用户数。 category &#x3D; user_login_info时有效。
        :type user_mobile_login_count: str
        :param user_activated_count: 激活用户数。 category &#x3D; user_activate_info时有效。
        :type user_activated_count: str
        :param user_login_devices_name: 用户登录设备名称。 category &#x3D; user_login_device_info时有效。
        :type user_login_devices_name: str
        :param user_login_devices_count: 用户登录设备数。 category &#x3D; user_login_device_info时有效。
        :type user_login_devices_count: str
        """
        
        

        self._time = None
        self._user_login_count = None
        self._user_pc_login_count = None
        self._user_mobile_login_count = None
        self._user_activated_count = None
        self._user_login_devices_name = None
        self._user_login_devices_count = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if user_login_count is not None:
            self.user_login_count = user_login_count
        if user_pc_login_count is not None:
            self.user_pc_login_count = user_pc_login_count
        if user_mobile_login_count is not None:
            self.user_mobile_login_count = user_mobile_login_count
        if user_activated_count is not None:
            self.user_activated_count = user_activated_count
        if user_login_devices_name is not None:
            self.user_login_devices_name = user_login_devices_name
        if user_login_devices_count is not None:
            self.user_login_devices_count = user_login_devices_count

    @property
    def time(self):
        r"""Gets the time of this StatisticUserDataItem.

        日期/月份。

        :return: The time of this StatisticUserDataItem.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this StatisticUserDataItem.

        日期/月份。

        :param time: The time of this StatisticUserDataItem.
        :type time: str
        """
        self._time = time

    @property
    def user_login_count(self):
        r"""Gets the user_login_count of this StatisticUserDataItem.

        登录用户数。 category = user_login_info时有效。

        :return: The user_login_count of this StatisticUserDataItem.
        :rtype: str
        """
        return self._user_login_count

    @user_login_count.setter
    def user_login_count(self, user_login_count):
        r"""Sets the user_login_count of this StatisticUserDataItem.

        登录用户数。 category = user_login_info时有效。

        :param user_login_count: The user_login_count of this StatisticUserDataItem.
        :type user_login_count: str
        """
        self._user_login_count = user_login_count

    @property
    def user_pc_login_count(self):
        r"""Gets the user_pc_login_count of this StatisticUserDataItem.

        PC端登录用户数。 category = user_login_info时有效。

        :return: The user_pc_login_count of this StatisticUserDataItem.
        :rtype: str
        """
        return self._user_pc_login_count

    @user_pc_login_count.setter
    def user_pc_login_count(self, user_pc_login_count):
        r"""Sets the user_pc_login_count of this StatisticUserDataItem.

        PC端登录用户数。 category = user_login_info时有效。

        :param user_pc_login_count: The user_pc_login_count of this StatisticUserDataItem.
        :type user_pc_login_count: str
        """
        self._user_pc_login_count = user_pc_login_count

    @property
    def user_mobile_login_count(self):
        r"""Gets the user_mobile_login_count of this StatisticUserDataItem.

        移动端登录用户数。 category = user_login_info时有效。

        :return: The user_mobile_login_count of this StatisticUserDataItem.
        :rtype: str
        """
        return self._user_mobile_login_count

    @user_mobile_login_count.setter
    def user_mobile_login_count(self, user_mobile_login_count):
        r"""Sets the user_mobile_login_count of this StatisticUserDataItem.

        移动端登录用户数。 category = user_login_info时有效。

        :param user_mobile_login_count: The user_mobile_login_count of this StatisticUserDataItem.
        :type user_mobile_login_count: str
        """
        self._user_mobile_login_count = user_mobile_login_count

    @property
    def user_activated_count(self):
        r"""Gets the user_activated_count of this StatisticUserDataItem.

        激活用户数。 category = user_activate_info时有效。

        :return: The user_activated_count of this StatisticUserDataItem.
        :rtype: str
        """
        return self._user_activated_count

    @user_activated_count.setter
    def user_activated_count(self, user_activated_count):
        r"""Sets the user_activated_count of this StatisticUserDataItem.

        激活用户数。 category = user_activate_info时有效。

        :param user_activated_count: The user_activated_count of this StatisticUserDataItem.
        :type user_activated_count: str
        """
        self._user_activated_count = user_activated_count

    @property
    def user_login_devices_name(self):
        r"""Gets the user_login_devices_name of this StatisticUserDataItem.

        用户登录设备名称。 category = user_login_device_info时有效。

        :return: The user_login_devices_name of this StatisticUserDataItem.
        :rtype: str
        """
        return self._user_login_devices_name

    @user_login_devices_name.setter
    def user_login_devices_name(self, user_login_devices_name):
        r"""Sets the user_login_devices_name of this StatisticUserDataItem.

        用户登录设备名称。 category = user_login_device_info时有效。

        :param user_login_devices_name: The user_login_devices_name of this StatisticUserDataItem.
        :type user_login_devices_name: str
        """
        self._user_login_devices_name = user_login_devices_name

    @property
    def user_login_devices_count(self):
        r"""Gets the user_login_devices_count of this StatisticUserDataItem.

        用户登录设备数。 category = user_login_device_info时有效。

        :return: The user_login_devices_count of this StatisticUserDataItem.
        :rtype: str
        """
        return self._user_login_devices_count

    @user_login_devices_count.setter
    def user_login_devices_count(self, user_login_devices_count):
        r"""Sets the user_login_devices_count of this StatisticUserDataItem.

        用户登录设备数。 category = user_login_device_info时有效。

        :param user_login_devices_count: The user_login_devices_count of this StatisticUserDataItem.
        :type user_login_devices_count: str
        """
        self._user_login_devices_count = user_login_devices_count

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
        if not isinstance(other, StatisticUserDataItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
