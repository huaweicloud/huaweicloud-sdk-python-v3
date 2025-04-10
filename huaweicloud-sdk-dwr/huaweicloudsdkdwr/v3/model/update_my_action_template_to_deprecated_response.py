# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMyActionTemplateToDeprecatedResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_request_id': 'str',
        'content_length': 'str'
    }

    attribute_map = {
        'x_request_id': 'x-request-id',
        'content_length': 'Content-Length'
    }

    def __init__(self, x_request_id=None, content_length=None):
        r"""UpdateMyActionTemplateToDeprecatedResponse

        The model defined in huaweicloud sdk

        :param x_request_id: 
        :type x_request_id: str
        :param content_length: 
        :type content_length: str
        """
        
        super(UpdateMyActionTemplateToDeprecatedResponse, self).__init__()

        self._x_request_id = None
        self._content_length = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        if content_length is not None:
            self.content_length = content_length

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this UpdateMyActionTemplateToDeprecatedResponse.

        :return: The x_request_id of this UpdateMyActionTemplateToDeprecatedResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this UpdateMyActionTemplateToDeprecatedResponse.

        :param x_request_id: The x_request_id of this UpdateMyActionTemplateToDeprecatedResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def content_length(self):
        r"""Gets the content_length of this UpdateMyActionTemplateToDeprecatedResponse.

        :return: The content_length of this UpdateMyActionTemplateToDeprecatedResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this UpdateMyActionTemplateToDeprecatedResponse.

        :param content_length: The content_length of this UpdateMyActionTemplateToDeprecatedResponse.
        :type content_length: str
        """
        self._content_length = content_length

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
        if not isinstance(other, UpdateMyActionTemplateToDeprecatedResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
