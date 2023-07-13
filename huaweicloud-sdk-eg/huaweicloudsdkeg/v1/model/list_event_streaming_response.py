# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventStreamingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'body': 'list[EventStreamingDetail]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'body': 'body',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, body=None, x_request_id=None):
        """ListEventStreamingResponse

        The model defined in huaweicloud sdk

        :param body: 
        :type body: list[:class:`huaweicloudsdkeg.v1.EventStreamingDetail`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListEventStreamingResponse, self).__init__()

        self._body = None
        self._x_request_id = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def body(self):
        """Gets the body of this ListEventStreamingResponse.

        :return: The body of this ListEventStreamingResponse.
        :rtype: list[:class:`huaweicloudsdkeg.v1.EventStreamingDetail`]
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListEventStreamingResponse.

        :param body: The body of this ListEventStreamingResponse.
        :type body: list[:class:`huaweicloudsdkeg.v1.EventStreamingDetail`]
        """
        self._body = body

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListEventStreamingResponse.

        :return: The x_request_id of this ListEventStreamingResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListEventStreamingResponse.

        :param x_request_id: The x_request_id of this ListEventStreamingResponse.
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
        if not isinstance(other, ListEventStreamingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
