# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopDetachInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'desktop_name': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'user_group': 'str',
        'detach_time': 'str',
        'type': 'str'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'desktop_name': 'desktop_name',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'user_group': 'user_group',
        'detach_time': 'detach_time',
        'type': 'type'
    }

    def __init__(self, desktop_id=None, desktop_name=None, user_id=None, user_name=None, user_group=None, detach_time=None, type=None):
        """DesktopDetachInfo

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面id
        :type desktop_id: str
        :param desktop_name: 桌面名称
        :type desktop_name: str
        :param user_id: 用户id
        :type user_id: str
        :param user_name: 用户名称
        :type user_name: str
        :param user_group: 用户权限
        :type user_group: str
        :param detach_time: 解绑时间
        :type detach_time: str
        :param type: 对象类型，可选值为： - USER：用户。 - GROUP：用户组。
        :type type: str
        """
        
        

        self._desktop_id = None
        self._desktop_name = None
        self._user_id = None
        self._user_name = None
        self._user_group = None
        self._detach_time = None
        self._type = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if user_group is not None:
            self.user_group = user_group
        if detach_time is not None:
            self.detach_time = detach_time
        if type is not None:
            self.type = type

    @property
    def desktop_id(self):
        """Gets the desktop_id of this DesktopDetachInfo.

        桌面id

        :return: The desktop_id of this DesktopDetachInfo.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this DesktopDetachInfo.

        桌面id

        :param desktop_id: The desktop_id of this DesktopDetachInfo.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def desktop_name(self):
        """Gets the desktop_name of this DesktopDetachInfo.

        桌面名称

        :return: The desktop_name of this DesktopDetachInfo.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        """Sets the desktop_name of this DesktopDetachInfo.

        桌面名称

        :param desktop_name: The desktop_name of this DesktopDetachInfo.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def user_id(self):
        """Gets the user_id of this DesktopDetachInfo.

        用户id

        :return: The user_id of this DesktopDetachInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DesktopDetachInfo.

        用户id

        :param user_id: The user_id of this DesktopDetachInfo.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this DesktopDetachInfo.

        用户名称

        :return: The user_name of this DesktopDetachInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this DesktopDetachInfo.

        用户名称

        :param user_name: The user_name of this DesktopDetachInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_group(self):
        """Gets the user_group of this DesktopDetachInfo.

        用户权限

        :return: The user_group of this DesktopDetachInfo.
        :rtype: str
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        """Sets the user_group of this DesktopDetachInfo.

        用户权限

        :param user_group: The user_group of this DesktopDetachInfo.
        :type user_group: str
        """
        self._user_group = user_group

    @property
    def detach_time(self):
        """Gets the detach_time of this DesktopDetachInfo.

        解绑时间

        :return: The detach_time of this DesktopDetachInfo.
        :rtype: str
        """
        return self._detach_time

    @detach_time.setter
    def detach_time(self, detach_time):
        """Sets the detach_time of this DesktopDetachInfo.

        解绑时间

        :param detach_time: The detach_time of this DesktopDetachInfo.
        :type detach_time: str
        """
        self._detach_time = detach_time

    @property
    def type(self):
        """Gets the type of this DesktopDetachInfo.

        对象类型，可选值为： - USER：用户。 - GROUP：用户组。

        :return: The type of this DesktopDetachInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DesktopDetachInfo.

        对象类型，可选值为： - USER：用户。 - GROUP：用户组。

        :param type: The type of this DesktopDetachInfo.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, DesktopDetachInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
