# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportIpBlacklistResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'body': 'str',
        'content_disposition': 'str',
        'content_type': 'str'
    }

    attribute_map = {
        'body': 'body',
        'content_disposition': 'Content-Disposition',
        'content_type': 'Content-Type'
    }

    def __init__(self, body=None, content_disposition=None, content_type=None):
        r"""ExportIpBlacklistResponse

        The model defined in huaweicloud sdk

        :param body: 
        :type body: str
        :param content_disposition: 
        :type content_disposition: str
        :param content_type: 
        :type content_type: str
        """
        
        super(ExportIpBlacklistResponse, self).__init__()

        self._body = None
        self._content_disposition = None
        self._content_type = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if content_disposition is not None:
            self.content_disposition = content_disposition
        if content_type is not None:
            self.content_type = content_type

    @property
    def body(self):
        r"""Gets the body of this ExportIpBlacklistResponse.

        :return: The body of this ExportIpBlacklistResponse.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ExportIpBlacklistResponse.

        :param body: The body of this ExportIpBlacklistResponse.
        :type body: str
        """
        self._body = body

    @property
    def content_disposition(self):
        r"""Gets the content_disposition of this ExportIpBlacklistResponse.

        :return: The content_disposition of this ExportIpBlacklistResponse.
        :rtype: str
        """
        return self._content_disposition

    @content_disposition.setter
    def content_disposition(self, content_disposition):
        r"""Sets the content_disposition of this ExportIpBlacklistResponse.

        :param content_disposition: The content_disposition of this ExportIpBlacklistResponse.
        :type content_disposition: str
        """
        self._content_disposition = content_disposition

    @property
    def content_type(self):
        r"""Gets the content_type of this ExportIpBlacklistResponse.

        :return: The content_type of this ExportIpBlacklistResponse.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this ExportIpBlacklistResponse.

        :param content_type: The content_type of this ExportIpBlacklistResponse.
        :type content_type: str
        """
        self._content_type = content_type

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
        if not isinstance(other, ExportIpBlacklistResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
