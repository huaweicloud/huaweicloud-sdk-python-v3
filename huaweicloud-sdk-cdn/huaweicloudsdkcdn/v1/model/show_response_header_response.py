# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResponseHeaderResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'headers': 'HeaderMap',
        'x_request_id': 'str'
    }

    attribute_map = {
        'headers': 'headers',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, headers=None, x_request_id=None):
        """ShowResponseHeaderResponse

        The model defined in huaweicloud sdk

        :param headers: 
        :type headers: :class:`huaweicloudsdkcdn.v1.HeaderMap`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowResponseHeaderResponse, self).__init__()

        self._headers = None
        self._x_request_id = None
        self.discriminator = None

        if headers is not None:
            self.headers = headers
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def headers(self):
        """Gets the headers of this ShowResponseHeaderResponse.

        :return: The headers of this ShowResponseHeaderResponse.
        :rtype: :class:`huaweicloudsdkcdn.v1.HeaderMap`
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this ShowResponseHeaderResponse.

        :param headers: The headers of this ShowResponseHeaderResponse.
        :type headers: :class:`huaweicloudsdkcdn.v1.HeaderMap`
        """
        self._headers = headers

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowResponseHeaderResponse.

        :return: The x_request_id of this ShowResponseHeaderResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowResponseHeaderResponse.

        :param x_request_id: The x_request_id of this ShowResponseHeaderResponse.
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
        if not isinstance(other, ShowResponseHeaderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
