# coding: utf-8

import six

from huaweicloudsdkcore.sdk_stream_response import SdkStreamResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadServerLogsResponse(SdkStreamResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_disposition': 'str',
        'content_transfer_encoding': 'str',
        'content_type': 'str'
    }

    attribute_map = {
        'content_disposition': 'Content-Disposition',
        'content_transfer_encoding': 'Content-Transfer-Encoding',
        'content_type': 'Content-Type'
    }

    def __init__(self, response, content_disposition=None, content_transfer_encoding=None, content_type=None):
        r"""DownloadServerLogsResponse

        The model defined in huaweicloud sdk

        :param content_disposition: 
        :type content_disposition: str
        :param content_transfer_encoding: 
        :type content_transfer_encoding: str
        :param content_type: 
        :type content_type: str
        """
        
        super(DownloadServerLogsResponse, self).__init__(response)

        self._content_disposition = None
        self._content_transfer_encoding = None
        self._content_type = None
        self.discriminator = None

        if content_disposition is not None:
            self.content_disposition = content_disposition
        if content_transfer_encoding is not None:
            self.content_transfer_encoding = content_transfer_encoding
        if content_type is not None:
            self.content_type = content_type

    @property
    def content_disposition(self):
        r"""Gets the content_disposition of this DownloadServerLogsResponse.

        :return: The content_disposition of this DownloadServerLogsResponse.
        :rtype: str
        """
        return self._content_disposition

    @content_disposition.setter
    def content_disposition(self, content_disposition):
        r"""Sets the content_disposition of this DownloadServerLogsResponse.

        :param content_disposition: The content_disposition of this DownloadServerLogsResponse.
        :type content_disposition: str
        """
        self._content_disposition = content_disposition

    @property
    def content_transfer_encoding(self):
        r"""Gets the content_transfer_encoding of this DownloadServerLogsResponse.

        :return: The content_transfer_encoding of this DownloadServerLogsResponse.
        :rtype: str
        """
        return self._content_transfer_encoding

    @content_transfer_encoding.setter
    def content_transfer_encoding(self, content_transfer_encoding):
        r"""Sets the content_transfer_encoding of this DownloadServerLogsResponse.

        :param content_transfer_encoding: The content_transfer_encoding of this DownloadServerLogsResponse.
        :type content_transfer_encoding: str
        """
        self._content_transfer_encoding = content_transfer_encoding

    @property
    def content_type(self):
        r"""Gets the content_type of this DownloadServerLogsResponse.

        :return: The content_type of this DownloadServerLogsResponse.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this DownloadServerLogsResponse.

        :param content_type: The content_type of this DownloadServerLogsResponse.
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
        if not isinstance(other, DownloadServerLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
