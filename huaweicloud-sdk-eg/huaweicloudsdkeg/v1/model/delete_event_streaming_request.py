# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteEventStreamingRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eventstreaming_id': 'str'
    }

    attribute_map = {
        'eventstreaming_id': 'eventstreaming_id'
    }

    def __init__(self, eventstreaming_id=None):
        r"""DeleteEventStreamingRequest

        The model defined in huaweicloud sdk

        :param eventstreaming_id: 事件流ID
        :type eventstreaming_id: str
        """
        
        

        self._eventstreaming_id = None
        self.discriminator = None

        self.eventstreaming_id = eventstreaming_id

    @property
    def eventstreaming_id(self):
        r"""Gets the eventstreaming_id of this DeleteEventStreamingRequest.

        事件流ID

        :return: The eventstreaming_id of this DeleteEventStreamingRequest.
        :rtype: str
        """
        return self._eventstreaming_id

    @eventstreaming_id.setter
    def eventstreaming_id(self, eventstreaming_id):
        r"""Sets the eventstreaming_id of this DeleteEventStreamingRequest.

        事件流ID

        :param eventstreaming_id: The eventstreaming_id of this DeleteEventStreamingRequest.
        :type eventstreaming_id: str
        """
        self._eventstreaming_id = eventstreaming_id

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
        if not isinstance(other, DeleteEventStreamingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
