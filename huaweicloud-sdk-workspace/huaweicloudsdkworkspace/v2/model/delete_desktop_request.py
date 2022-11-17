# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDesktopRequest:

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
        'delete_users': 'bool',
        'email_notification': 'bool'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'delete_users': 'delete_users',
        'email_notification': 'email_notification'
    }

    def __init__(self, desktop_id=None, delete_users=None, email_notification=None):
        """DeleteDesktopRequest

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param delete_users: 删除桌面后，如果当前用户没有其它桌面，可以删除桌面用户。true：删除用户，false：不删除用户，默认为false。
        :type delete_users: bool
        :param email_notification: 删除桌面后，是否给桌面用户发送系统通知邮件。true：发送，false：不发送。默认为true。
        :type email_notification: bool
        """
        
        

        self._desktop_id = None
        self._delete_users = None
        self._email_notification = None
        self.discriminator = None

        self.desktop_id = desktop_id
        if delete_users is not None:
            self.delete_users = delete_users
        if email_notification is not None:
            self.email_notification = email_notification

    @property
    def desktop_id(self):
        """Gets the desktop_id of this DeleteDesktopRequest.

        桌面ID。

        :return: The desktop_id of this DeleteDesktopRequest.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this DeleteDesktopRequest.

        桌面ID。

        :param desktop_id: The desktop_id of this DeleteDesktopRequest.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def delete_users(self):
        """Gets the delete_users of this DeleteDesktopRequest.

        删除桌面后，如果当前用户没有其它桌面，可以删除桌面用户。true：删除用户，false：不删除用户，默认为false。

        :return: The delete_users of this DeleteDesktopRequest.
        :rtype: bool
        """
        return self._delete_users

    @delete_users.setter
    def delete_users(self, delete_users):
        """Sets the delete_users of this DeleteDesktopRequest.

        删除桌面后，如果当前用户没有其它桌面，可以删除桌面用户。true：删除用户，false：不删除用户，默认为false。

        :param delete_users: The delete_users of this DeleteDesktopRequest.
        :type delete_users: bool
        """
        self._delete_users = delete_users

    @property
    def email_notification(self):
        """Gets the email_notification of this DeleteDesktopRequest.

        删除桌面后，是否给桌面用户发送系统通知邮件。true：发送，false：不发送。默认为true。

        :return: The email_notification of this DeleteDesktopRequest.
        :rtype: bool
        """
        return self._email_notification

    @email_notification.setter
    def email_notification(self, email_notification):
        """Sets the email_notification of this DeleteDesktopRequest.

        删除桌面后，是否给桌面用户发送系统通知邮件。true：发送，false：不发送。默认为true。

        :param email_notification: The email_notification of this DeleteDesktopRequest.
        :type email_notification: bool
        """
        self._email_notification = email_notification

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
        if not isinstance(other, DeleteDesktopRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
