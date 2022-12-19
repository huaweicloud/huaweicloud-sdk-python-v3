# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SendImmediateEventsDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'send_config': 'SendConfig',
        'immediate_event': 'ImmediateEventDTO'
    }

    attribute_map = {
        'send_config': 'send_config',
        'immediate_event': 'immediate_event'
    }

    def __init__(self, send_config=None, immediate_event=None):
        """SendImmediateEventsDTO

        The model defined in huaweicloud sdk

        :param send_config: 
        :type send_config: :class:`huaweicloudsdkdris.v1.SendConfig`
        :param immediate_event: 
        :type immediate_event: :class:`huaweicloudsdkdris.v1.ImmediateEventDTO`
        """
        
        

        self._send_config = None
        self._immediate_event = None
        self.discriminator = None

        self.send_config = send_config
        self.immediate_event = immediate_event

    @property
    def send_config(self):
        """Gets the send_config of this SendImmediateEventsDTO.

        :return: The send_config of this SendImmediateEventsDTO.
        :rtype: :class:`huaweicloudsdkdris.v1.SendConfig`
        """
        return self._send_config

    @send_config.setter
    def send_config(self, send_config):
        """Sets the send_config of this SendImmediateEventsDTO.

        :param send_config: The send_config of this SendImmediateEventsDTO.
        :type send_config: :class:`huaweicloudsdkdris.v1.SendConfig`
        """
        self._send_config = send_config

    @property
    def immediate_event(self):
        """Gets the immediate_event of this SendImmediateEventsDTO.

        :return: The immediate_event of this SendImmediateEventsDTO.
        :rtype: :class:`huaweicloudsdkdris.v1.ImmediateEventDTO`
        """
        return self._immediate_event

    @immediate_event.setter
    def immediate_event(self, immediate_event):
        """Sets the immediate_event of this SendImmediateEventsDTO.

        :param immediate_event: The immediate_event of this SendImmediateEventsDTO.
        :type immediate_event: :class:`huaweicloudsdkdris.v1.ImmediateEventDTO`
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
        if not isinstance(other, SendImmediateEventsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
