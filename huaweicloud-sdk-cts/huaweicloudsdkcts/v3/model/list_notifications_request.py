# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotificationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notification_type': 'str',
        'notification_name': 'str'
    }

    attribute_map = {
        'notification_type': 'notification_type',
        'notification_name': 'notification_name'
    }

    def __init__(self, notification_type=None, notification_name=None):
        """ListNotificationsRequest

        The model defined in huaweicloud sdk

        :param notification_type: 通知类型。
        :type notification_type: str
        :param notification_name: 标识关键操作通知名称。 在不传入该字段的情况下，将查询当前租户所有的关键操作通知。
        :type notification_name: str
        """
        
        

        self._notification_type = None
        self._notification_name = None
        self.discriminator = None

        self.notification_type = notification_type
        if notification_name is not None:
            self.notification_name = notification_name

    @property
    def notification_type(self):
        """Gets the notification_type of this ListNotificationsRequest.

        通知类型。

        :return: The notification_type of this ListNotificationsRequest.
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        """Sets the notification_type of this ListNotificationsRequest.

        通知类型。

        :param notification_type: The notification_type of this ListNotificationsRequest.
        :type notification_type: str
        """
        self._notification_type = notification_type

    @property
    def notification_name(self):
        """Gets the notification_name of this ListNotificationsRequest.

        标识关键操作通知名称。 在不传入该字段的情况下，将查询当前租户所有的关键操作通知。

        :return: The notification_name of this ListNotificationsRequest.
        :rtype: str
        """
        return self._notification_name

    @notification_name.setter
    def notification_name(self, notification_name):
        """Sets the notification_name of this ListNotificationsRequest.

        标识关键操作通知名称。 在不传入该字段的情况下，将查询当前租户所有的关键操作通知。

        :param notification_name: The notification_name of this ListNotificationsRequest.
        :type notification_name: str
        """
        self._notification_name = notification_name

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
        if not isinstance(other, ListNotificationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
