# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecretEventRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_name': 'str',
        'body': 'UpdateSecretEventRequestBody'
    }

    attribute_map = {
        'event_name': 'event_name',
        'body': 'body'
    }

    def __init__(self, event_name=None, body=None):
        """UpdateSecretEventRequest

        The model defined in huaweicloud sdk

        :param event_name: 事件通知名称。
        :type event_name: str
        :param body: Body of the UpdateSecretEventRequest
        :type body: :class:`huaweicloudsdkcsms.v1.UpdateSecretEventRequestBody`
        """
        
        

        self._event_name = None
        self._body = None
        self.discriminator = None

        self.event_name = event_name
        if body is not None:
            self.body = body

    @property
    def event_name(self):
        """Gets the event_name of this UpdateSecretEventRequest.

        事件通知名称。

        :return: The event_name of this UpdateSecretEventRequest.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this UpdateSecretEventRequest.

        事件通知名称。

        :param event_name: The event_name of this UpdateSecretEventRequest.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def body(self):
        """Gets the body of this UpdateSecretEventRequest.

        :return: The body of this UpdateSecretEventRequest.
        :rtype: :class:`huaweicloudsdkcsms.v1.UpdateSecretEventRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateSecretEventRequest.

        :param body: The body of this UpdateSecretEventRequest.
        :type body: :class:`huaweicloudsdkcsms.v1.UpdateSecretEventRequestBody`
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
        if not isinstance(other, UpdateSecretEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
