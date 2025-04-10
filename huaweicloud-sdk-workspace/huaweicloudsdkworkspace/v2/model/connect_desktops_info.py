# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectDesktopsInfo:

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
        'connect_status': 'str',
        'attach_users': 'list[AttachUsersInfo]'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'desktop_name': 'desktop_name',
        'connect_status': 'connect_status',
        'attach_users': 'attach_users'
    }

    def __init__(self, desktop_id=None, desktop_name=None, connect_status=None, attach_users=None):
        r"""ConnectDesktopsInfo

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面id。
        :type desktop_id: str
        :param desktop_name: 桌面名称。
        :type desktop_name: str
        :param connect_status: 桌面的连接状态。  - UNREGISTER：表示桌面未注册时的状态（桌面启动后，会自动注册）。关机后也会出现未注册的状态。 - REGISTERED：表示桌面注册以后，等待用户连接的状态。 - CONNECTED：表示用户已经成功连接，正在使用桌面。 - DISCONNECTED：表示桌面与客户端断开会话后显示的状态，可能为关闭客户端窗口，或客户端与桌面网络断开引起。
        :type connect_status: str
        :param attach_users: 桌面已分配的用户或用户组信息列表。
        :type attach_users: list[:class:`huaweicloudsdkworkspace.v2.AttachUsersInfo`]
        """
        
        

        self._desktop_id = None
        self._desktop_name = None
        self._connect_status = None
        self._attach_users = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if connect_status is not None:
            self.connect_status = connect_status
        if attach_users is not None:
            self.attach_users = attach_users

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this ConnectDesktopsInfo.

        桌面id。

        :return: The desktop_id of this ConnectDesktopsInfo.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this ConnectDesktopsInfo.

        桌面id。

        :param desktop_id: The desktop_id of this ConnectDesktopsInfo.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def desktop_name(self):
        r"""Gets the desktop_name of this ConnectDesktopsInfo.

        桌面名称。

        :return: The desktop_name of this ConnectDesktopsInfo.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        r"""Sets the desktop_name of this ConnectDesktopsInfo.

        桌面名称。

        :param desktop_name: The desktop_name of this ConnectDesktopsInfo.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def connect_status(self):
        r"""Gets the connect_status of this ConnectDesktopsInfo.

        桌面的连接状态。  - UNREGISTER：表示桌面未注册时的状态（桌面启动后，会自动注册）。关机后也会出现未注册的状态。 - REGISTERED：表示桌面注册以后，等待用户连接的状态。 - CONNECTED：表示用户已经成功连接，正在使用桌面。 - DISCONNECTED：表示桌面与客户端断开会话后显示的状态，可能为关闭客户端窗口，或客户端与桌面网络断开引起。

        :return: The connect_status of this ConnectDesktopsInfo.
        :rtype: str
        """
        return self._connect_status

    @connect_status.setter
    def connect_status(self, connect_status):
        r"""Sets the connect_status of this ConnectDesktopsInfo.

        桌面的连接状态。  - UNREGISTER：表示桌面未注册时的状态（桌面启动后，会自动注册）。关机后也会出现未注册的状态。 - REGISTERED：表示桌面注册以后，等待用户连接的状态。 - CONNECTED：表示用户已经成功连接，正在使用桌面。 - DISCONNECTED：表示桌面与客户端断开会话后显示的状态，可能为关闭客户端窗口，或客户端与桌面网络断开引起。

        :param connect_status: The connect_status of this ConnectDesktopsInfo.
        :type connect_status: str
        """
        self._connect_status = connect_status

    @property
    def attach_users(self):
        r"""Gets the attach_users of this ConnectDesktopsInfo.

        桌面已分配的用户或用户组信息列表。

        :return: The attach_users of this ConnectDesktopsInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AttachUsersInfo`]
        """
        return self._attach_users

    @attach_users.setter
    def attach_users(self, attach_users):
        r"""Sets the attach_users of this ConnectDesktopsInfo.

        桌面已分配的用户或用户组信息列表。

        :param attach_users: The attach_users of this ConnectDesktopsInfo.
        :type attach_users: list[:class:`huaweicloudsdkworkspace.v2.AttachUsersInfo`]
        """
        self._attach_users = attach_users

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
        if not isinstance(other, ConnectDesktopsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
