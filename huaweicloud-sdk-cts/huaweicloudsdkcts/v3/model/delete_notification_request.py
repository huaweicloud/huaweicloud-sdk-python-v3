# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteNotificationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notification_id': 'str'
    }

    attribute_map = {
        'notification_id': 'notification_id'
    }

    def __init__(self, notification_id=None):
        """DeleteNotificationRequest

        The model defined in huaweicloud sdk

        :param notification_id: 标识关键操作通知id。 批量删除请使用逗号隔开，notification_id&#x3D;\&quot;xxx1,cccc2\&quot;
        :type notification_id: str
        """
        
        

        self._notification_id = None
        self.discriminator = None

        self.notification_id = notification_id

    @property
    def notification_id(self):
        """Gets the notification_id of this DeleteNotificationRequest.

        标识关键操作通知id。 批量删除请使用逗号隔开，notification_id=\"xxx1,cccc2\"

        :return: The notification_id of this DeleteNotificationRequest.
        :rtype: str
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        """Sets the notification_id of this DeleteNotificationRequest.

        标识关键操作通知id。 批量删除请使用逗号隔开，notification_id=\"xxx1,cccc2\"

        :param notification_id: The notification_id of this DeleteNotificationRequest.
        :type notification_id: str
        """
        self._notification_id = notification_id

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
        if not isinstance(other, DeleteNotificationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
