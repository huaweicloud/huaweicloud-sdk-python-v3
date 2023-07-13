# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEventStreamingRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eventstreaming_id': 'str',
        'body': 'EventStreamingUpdateReq'
    }

    attribute_map = {
        'eventstreaming_id': 'eventstreaming_id',
        'body': 'body'
    }

    def __init__(self, eventstreaming_id=None, body=None):
        """UpdateEventStreamingRequest

        The model defined in huaweicloud sdk

        :param eventstreaming_id: 事件流ID
        :type eventstreaming_id: str
        :param body: Body of the UpdateEventStreamingRequest
        :type body: :class:`huaweicloudsdkeg.v1.EventStreamingUpdateReq`
        """
        
        

        self._eventstreaming_id = None
        self._body = None
        self.discriminator = None

        self.eventstreaming_id = eventstreaming_id
        if body is not None:
            self.body = body

    @property
    def eventstreaming_id(self):
        """Gets the eventstreaming_id of this UpdateEventStreamingRequest.

        事件流ID

        :return: The eventstreaming_id of this UpdateEventStreamingRequest.
        :rtype: str
        """
        return self._eventstreaming_id

    @eventstreaming_id.setter
    def eventstreaming_id(self, eventstreaming_id):
        """Sets the eventstreaming_id of this UpdateEventStreamingRequest.

        事件流ID

        :param eventstreaming_id: The eventstreaming_id of this UpdateEventStreamingRequest.
        :type eventstreaming_id: str
        """
        self._eventstreaming_id = eventstreaming_id

    @property
    def body(self):
        """Gets the body of this UpdateEventStreamingRequest.

        :return: The body of this UpdateEventStreamingRequest.
        :rtype: :class:`huaweicloudsdkeg.v1.EventStreamingUpdateReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateEventStreamingRequest.

        :param body: The body of this UpdateEventStreamingRequest.
        :type body: :class:`huaweicloudsdkeg.v1.EventStreamingUpdateReq`
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
        if not isinstance(other, UpdateEventStreamingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
