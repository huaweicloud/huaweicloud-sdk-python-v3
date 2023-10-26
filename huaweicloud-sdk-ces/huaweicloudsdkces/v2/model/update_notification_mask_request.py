# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNotificationMaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notification_mask_id': 'str',
        'body': 'UpdateNotificationMasksRequestBody'
    }

    attribute_map = {
        'notification_mask_id': 'notification_mask_id',
        'body': 'body'
    }

    def __init__(self, notification_mask_id=None, body=None):
        """UpdateNotificationMaskRequest

        The model defined in huaweicloud sdk

        :param notification_mask_id: 屏蔽规则ID
        :type notification_mask_id: str
        :param body: Body of the UpdateNotificationMaskRequest
        :type body: :class:`huaweicloudsdkces.v2.UpdateNotificationMasksRequestBody`
        """
        
        

        self._notification_mask_id = None
        self._body = None
        self.discriminator = None

        self.notification_mask_id = notification_mask_id
        if body is not None:
            self.body = body

    @property
    def notification_mask_id(self):
        """Gets the notification_mask_id of this UpdateNotificationMaskRequest.

        屏蔽规则ID

        :return: The notification_mask_id of this UpdateNotificationMaskRequest.
        :rtype: str
        """
        return self._notification_mask_id

    @notification_mask_id.setter
    def notification_mask_id(self, notification_mask_id):
        """Sets the notification_mask_id of this UpdateNotificationMaskRequest.

        屏蔽规则ID

        :param notification_mask_id: The notification_mask_id of this UpdateNotificationMaskRequest.
        :type notification_mask_id: str
        """
        self._notification_mask_id = notification_mask_id

    @property
    def body(self):
        """Gets the body of this UpdateNotificationMaskRequest.

        :return: The body of this UpdateNotificationMaskRequest.
        :rtype: :class:`huaweicloudsdkces.v2.UpdateNotificationMasksRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateNotificationMaskRequest.

        :param body: The body of this UpdateNotificationMaskRequest.
        :type body: :class:`huaweicloudsdkces.v2.UpdateNotificationMasksRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateNotificationMaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
