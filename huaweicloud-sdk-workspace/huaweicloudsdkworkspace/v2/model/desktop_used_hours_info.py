# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopUsedHoursInfo:

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
        'desktop_username': 'str',
        'used_info_list': 'list[DesktopUsedInfo]'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'desktop_username': 'desktop_username',
        'used_info_list': 'used_info_list'
    }

    def __init__(self, desktop_id=None, desktop_username=None, used_info_list=None):
        """DesktopUsedHoursInfo

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面Id。
        :type desktop_id: str
        :param desktop_username: 使用的用户。
        :type desktop_username: str
        :param used_info_list: 桌面使用时间列表。
        :type used_info_list: list[:class:`huaweicloudsdkworkspace.v2.DesktopUsedInfo`]
        """
        
        

        self._desktop_id = None
        self._desktop_username = None
        self._used_info_list = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_username is not None:
            self.desktop_username = desktop_username
        if used_info_list is not None:
            self.used_info_list = used_info_list

    @property
    def desktop_id(self):
        """Gets the desktop_id of this DesktopUsedHoursInfo.

        桌面Id。

        :return: The desktop_id of this DesktopUsedHoursInfo.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this DesktopUsedHoursInfo.

        桌面Id。

        :param desktop_id: The desktop_id of this DesktopUsedHoursInfo.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def desktop_username(self):
        """Gets the desktop_username of this DesktopUsedHoursInfo.

        使用的用户。

        :return: The desktop_username of this DesktopUsedHoursInfo.
        :rtype: str
        """
        return self._desktop_username

    @desktop_username.setter
    def desktop_username(self, desktop_username):
        """Sets the desktop_username of this DesktopUsedHoursInfo.

        使用的用户。

        :param desktop_username: The desktop_username of this DesktopUsedHoursInfo.
        :type desktop_username: str
        """
        self._desktop_username = desktop_username

    @property
    def used_info_list(self):
        """Gets the used_info_list of this DesktopUsedHoursInfo.

        桌面使用时间列表。

        :return: The used_info_list of this DesktopUsedHoursInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.DesktopUsedInfo`]
        """
        return self._used_info_list

    @used_info_list.setter
    def used_info_list(self, used_info_list):
        """Sets the used_info_list of this DesktopUsedHoursInfo.

        桌面使用时间列表。

        :param used_info_list: The used_info_list of this DesktopUsedHoursInfo.
        :type used_info_list: list[:class:`huaweicloudsdkworkspace.v2.DesktopUsedInfo`]
        """
        self._used_info_list = used_info_list

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
        if not isinstance(other, DesktopUsedHoursInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
