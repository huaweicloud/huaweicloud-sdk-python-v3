# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SendNotificationsReq:

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
        'notifications': 'str'
    }

    attribute_map = {
        'desktop_ids': 'desktop_ids',
        'notifications': 'notifications'
    }

    def __init__(self, desktop_ids=None, notifications=None):
        r"""SendNotificationsReq

        The model defined in huaweicloud sdk

        :param desktop_ids: 桌面列表。
        :type desktop_ids: list[str]
        :param notifications: 消息通知内容。
        :type notifications: str
        """
        
        

        self._desktop_ids = None
        self._notifications = None
        self.discriminator = None

        self.desktop_ids = desktop_ids
        self.notifications = notifications

    @property
    def desktop_ids(self):
        r"""Gets the desktop_ids of this SendNotificationsReq.

        桌面列表。

        :return: The desktop_ids of this SendNotificationsReq.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        r"""Sets the desktop_ids of this SendNotificationsReq.

        桌面列表。

        :param desktop_ids: The desktop_ids of this SendNotificationsReq.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

    @property
    def notifications(self):
        r"""Gets the notifications of this SendNotificationsReq.

        消息通知内容。

        :return: The notifications of this SendNotificationsReq.
        :rtype: str
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        r"""Sets the notifications of this SendNotificationsReq.

        消息通知内容。

        :param notifications: The notifications of this SendNotificationsReq.
        :type notifications: str
        """
        self._notifications = notifications

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
        if not isinstance(other, SendNotificationsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
