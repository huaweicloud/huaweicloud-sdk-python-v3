# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SendImmediateEventResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_id': 'str',
        'send_config': 'SendConfigResponse',
        'immediate_event': 'ImmediateEventResponseDTO'
    }

    attribute_map = {
        'event_id': 'event_id',
        'send_config': 'send_config',
        'immediate_event': 'immediate_event'
    }

    def __init__(self, event_id=None, send_config=None, immediate_event=None):
        """SendImmediateEventResponse

        The model defined in huaweicloud sdk

        :param event_id: **参数说明**：即时事件ID。
        :type event_id: str
        :param send_config: 
        :type send_config: :class:`huaweicloudsdkdris.v1.SendConfigResponse`
        :param immediate_event: 
        :type immediate_event: :class:`huaweicloudsdkdris.v1.ImmediateEventResponseDTO`
        """
        
        super(SendImmediateEventResponse, self).__init__()

        self._event_id = None
        self._send_config = None
        self._immediate_event = None
        self.discriminator = None

        if event_id is not None:
            self.event_id = event_id
        if send_config is not None:
            self.send_config = send_config
        if immediate_event is not None:
            self.immediate_event = immediate_event

    @property
    def event_id(self):
        """Gets the event_id of this SendImmediateEventResponse.

        **参数说明**：即时事件ID。

        :return: The event_id of this SendImmediateEventResponse.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this SendImmediateEventResponse.

        **参数说明**：即时事件ID。

        :param event_id: The event_id of this SendImmediateEventResponse.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def send_config(self):
        """Gets the send_config of this SendImmediateEventResponse.

        :return: The send_config of this SendImmediateEventResponse.
        :rtype: :class:`huaweicloudsdkdris.v1.SendConfigResponse`
        """
        return self._send_config

    @send_config.setter
    def send_config(self, send_config):
        """Sets the send_config of this SendImmediateEventResponse.

        :param send_config: The send_config of this SendImmediateEventResponse.
        :type send_config: :class:`huaweicloudsdkdris.v1.SendConfigResponse`
        """
        self._send_config = send_config

    @property
    def immediate_event(self):
        """Gets the immediate_event of this SendImmediateEventResponse.

        :return: The immediate_event of this SendImmediateEventResponse.
        :rtype: :class:`huaweicloudsdkdris.v1.ImmediateEventResponseDTO`
        """
        return self._immediate_event

    @immediate_event.setter
    def immediate_event(self, immediate_event):
        """Sets the immediate_event of this SendImmediateEventResponse.

        :param immediate_event: The immediate_event of this SendImmediateEventResponse.
        :type immediate_event: :class:`huaweicloudsdkdris.v1.ImmediateEventResponseDTO`
        """
        self._immediate_event = immediate_event

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
        if not isinstance(other, SendImmediateEventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
