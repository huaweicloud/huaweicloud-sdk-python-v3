# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleDesktopInfo:

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
        'computer_name': 'str',
        'created': 'str',
        'ip_address': 'str',
        'user_name': 'str',
        'user_group': 'str',
        'sid': 'str',
        'ou_name': 'str'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'computer_name': 'computer_name',
        'created': 'created',
        'ip_address': 'ip_address',
        'user_name': 'user_name',
        'user_group': 'user_group',
        'sid': 'sid',
        'ou_name': 'ou_name'
    }

    def __init__(self, desktop_id=None, computer_name=None, created=None, ip_address=None, user_name=None, user_group=None, sid=None, ou_name=None):
        """SimpleDesktopInfo

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param computer_name: 桌面名。
        :type computer_name: str
        :param created: 创建时间。
        :type created: str
        :param ip_address: 桌面ip地址。
        :type ip_address: str
        :param user_name: 用户名。
        :type user_name: str
        :param user_group: 权限组。
        :type user_group: str
        :param sid: 桌面的SID信息。
        :type sid: str
        :param ou_name: ou名称。
        :type ou_name: str
        """
        
        

        self._desktop_id = None
        self._computer_name = None
        self._created = None
        self._ip_address = None
        self._user_name = None
        self._user_group = None
        self._sid = None
        self._ou_name = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if computer_name is not None:
            self.computer_name = computer_name
        if created is not None:
            self.created = created
        if ip_address is not None:
            self.ip_address = ip_address
        if user_name is not None:
            self.user_name = user_name
        if user_group is not None:
            self.user_group = user_group
        if sid is not None:
            self.sid = sid
        if ou_name is not None:
            self.ou_name = ou_name

    @property
    def desktop_id(self):
        """Gets the desktop_id of this SimpleDesktopInfo.

        桌面ID。

        :return: The desktop_id of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this SimpleDesktopInfo.

        桌面ID。

        :param desktop_id: The desktop_id of this SimpleDesktopInfo.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def computer_name(self):
        """Gets the computer_name of this SimpleDesktopInfo.

        桌面名。

        :return: The computer_name of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        """Sets the computer_name of this SimpleDesktopInfo.

        桌面名。

        :param computer_name: The computer_name of this SimpleDesktopInfo.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def created(self):
        """Gets the created of this SimpleDesktopInfo.

        创建时间。

        :return: The created of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SimpleDesktopInfo.

        创建时间。

        :param created: The created of this SimpleDesktopInfo.
        :type created: str
        """
        self._created = created

    @property
    def ip_address(self):
        """Gets the ip_address of this SimpleDesktopInfo.

        桌面ip地址。

        :return: The ip_address of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this SimpleDesktopInfo.

        桌面ip地址。

        :param ip_address: The ip_address of this SimpleDesktopInfo.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def user_name(self):
        """Gets the user_name of this SimpleDesktopInfo.

        用户名。

        :return: The user_name of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this SimpleDesktopInfo.

        用户名。

        :param user_name: The user_name of this SimpleDesktopInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_group(self):
        """Gets the user_group of this SimpleDesktopInfo.

        权限组。

        :return: The user_group of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        """Sets the user_group of this SimpleDesktopInfo.

        权限组。

        :param user_group: The user_group of this SimpleDesktopInfo.
        :type user_group: str
        """
        self._user_group = user_group

    @property
    def sid(self):
        """Gets the sid of this SimpleDesktopInfo.

        桌面的SID信息。

        :return: The sid of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this SimpleDesktopInfo.

        桌面的SID信息。

        :param sid: The sid of this SimpleDesktopInfo.
        :type sid: str
        """
        self._sid = sid

    @property
    def ou_name(self):
        """Gets the ou_name of this SimpleDesktopInfo.

        ou名称。

        :return: The ou_name of this SimpleDesktopInfo.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        """Sets the ou_name of this SimpleDesktopInfo.

        ou名称。

        :param ou_name: The ou_name of this SimpleDesktopInfo.
        :type ou_name: str
        """
        self._ou_name = ou_name

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
        if not isinstance(other, SimpleDesktopInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
