# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteEventStreamingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_streaming_id': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'event_streaming_id': 'eventStreamingID',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, event_streaming_id=None, x_request_id=None):
        """DeleteEventStreamingResponse

        The model defined in huaweicloud sdk

        :param event_streaming_id: 事件流ID
        :type event_streaming_id: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(DeleteEventStreamingResponse, self).__init__()

        self._event_streaming_id = None
        self._x_request_id = None
        self.discriminator = None

        if event_streaming_id is not None:
            self.event_streaming_id = event_streaming_id
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def event_streaming_id(self):
        """Gets the event_streaming_id of this DeleteEventStreamingResponse.

        事件流ID

        :return: The event_streaming_id of this DeleteEventStreamingResponse.
        :rtype: str
        """
        return self._event_streaming_id

    @event_streaming_id.setter
    def event_streaming_id(self, event_streaming_id):
        """Sets the event_streaming_id of this DeleteEventStreamingResponse.

        事件流ID

        :param event_streaming_id: The event_streaming_id of this DeleteEventStreamingResponse.
        :type event_streaming_id: str
        """
        self._event_streaming_id = event_streaming_id

    @property
    def x_request_id(self):
        """Gets the x_request_id of this DeleteEventStreamingResponse.

        :return: The x_request_id of this DeleteEventStreamingResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this DeleteEventStreamingResponse.

        :param x_request_id: The x_request_id of this DeleteEventStreamingResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, DeleteEventStreamingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
