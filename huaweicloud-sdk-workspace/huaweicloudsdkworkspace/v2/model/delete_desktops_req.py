# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDesktopsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_ids': 'list[str]',
        'delete_users': 'bool',
        'email_notification': 'bool',
        'is_force_delete': 'bool'
    }

    attribute_map = {
        'desktop_ids': 'desktop_ids',
        'delete_users': 'delete_users',
        'email_notification': 'email_notification',
        'is_force_delete': 'is_force_delete'
    }

    def __init__(self, desktop_ids=None, delete_users=None, email_notification=None, is_force_delete=None):
        """DeleteDesktopsReq

        The model defined in huaweicloud sdk

        :param desktop_ids: 待删除的桌面ID列表。
        :type desktop_ids: list[str]
        :param delete_users: 删除桌面后，如果当前用户没有其它桌面，可以删除桌面用户。true：删除用户，false：不删除用户，默认为false。
        :type delete_users: bool
        :param email_notification: 是否邮件通知，true：邮件通知，false：不通知，默认值true。
        :type email_notification: bool
        :param is_force_delete: 是否强制删除，true：强制删除，false：不强制删除
        :type is_force_delete: bool
        """
        
        

        self._desktop_ids = None
        self._delete_users = None
        self._email_notification = None
        self._is_force_delete = None
        self.discriminator = None

        self.desktop_ids = desktop_ids
        if delete_users is not None:
            self.delete_users = delete_users
        if email_notification is not None:
            self.email_notification = email_notification
        if is_force_delete is not None:
            self.is_force_delete = is_force_delete

    @property
    def desktop_ids(self):
        """Gets the desktop_ids of this DeleteDesktopsReq.

        待删除的桌面ID列表。

        :return: The desktop_ids of this DeleteDesktopsReq.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        """Sets the desktop_ids of this DeleteDesktopsReq.

        待删除的桌面ID列表。

        :param desktop_ids: The desktop_ids of this DeleteDesktopsReq.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

    @property
    def delete_users(self):
        """Gets the delete_users of this DeleteDesktopsReq.

        删除桌面后，如果当前用户没有其它桌面，可以删除桌面用户。true：删除用户，false：不删除用户，默认为false。

        :return: The delete_users of this DeleteDesktopsReq.
        :rtype: bool
        """
        return self._delete_users

    @delete_users.setter
    def delete_users(self, delete_users):
        """Sets the delete_users of this DeleteDesktopsReq.

        删除桌面后，如果当前用户没有其它桌面，可以删除桌面用户。true：删除用户，false：不删除用户，默认为false。

        :param delete_users: The delete_users of this DeleteDesktopsReq.
        :type delete_users: bool
        """
        self._delete_users = delete_users

    @property
    def email_notification(self):
        """Gets the email_notification of this DeleteDesktopsReq.

        是否邮件通知，true：邮件通知，false：不通知，默认值true。

        :return: The email_notification of this DeleteDesktopsReq.
        :rtype: bool
        """
        return self._email_notification

    @email_notification.setter
    def email_notification(self, email_notification):
        """Sets the email_notification of this DeleteDesktopsReq.

        是否邮件通知，true：邮件通知，false：不通知，默认值true。

        :param email_notification: The email_notification of this DeleteDesktopsReq.
        :type email_notification: bool
        """
        self._email_notification = email_notification

    @property
    def is_force_delete(self):
        """Gets the is_force_delete of this DeleteDesktopsReq.

        是否强制删除，true：强制删除，false：不强制删除

        :return: The is_force_delete of this DeleteDesktopsReq.
        :rtype: bool
        """
        return self._is_force_delete

    @is_force_delete.setter
    def is_force_delete(self, is_force_delete):
        """Sets the is_force_delete of this DeleteDesktopsReq.

        是否强制删除，true：强制删除，false：不强制删除

        :param is_force_delete: The is_force_delete of this DeleteDesktopsReq.
        :type is_force_delete: bool
        """
        self._is_force_delete = is_force_delete

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
        if not isinstance(other, DeleteDesktopsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
