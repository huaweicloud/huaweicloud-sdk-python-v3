# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadAgentFileResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'headers': 'dict(str, str)',
        'file_name': 'str'
    }

    attribute_map = {
        'url': 'url',
        'headers': 'headers',
        'file_name': 'file_name'
    }

    def __init__(self, url=None, headers=None, file_name=None):
        r"""UploadAgentFileResponse

        The model defined in huaweicloud sdk

        :param url: 临时url
        :type url: str
        :param headers: headers
        :type headers: dict(str, str)
        :param file_name: 文件名
        :type file_name: str
        """
        
        super().__init__()

        self._url = None
        self._headers = None
        self._file_name = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if headers is not None:
            self.headers = headers
        if file_name is not None:
            self.file_name = file_name

    @property
    def url(self):
        r"""Gets the url of this UploadAgentFileResponse.

        临时url

        :return: The url of this UploadAgentFileResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this UploadAgentFileResponse.

        临时url

        :param url: The url of this UploadAgentFileResponse.
        :type url: str
        """
        self._url = url

    @property
    def headers(self):
        r"""Gets the headers of this UploadAgentFileResponse.

        headers

        :return: The headers of this UploadAgentFileResponse.
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        r"""Sets the headers of this UploadAgentFileResponse.

        headers

        :param headers: The headers of this UploadAgentFileResponse.
        :type headers: dict(str, str)
        """
        self._headers = headers

    @property
    def file_name(self):
        r"""Gets the file_name of this UploadAgentFileResponse.

        文件名

        :return: The file_name of this UploadAgentFileResponse.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this UploadAgentFileResponse.

        文件名

        :param file_name: The file_name of this UploadAgentFileResponse.
        :type file_name: str
        """
        self._file_name = file_name

    def to_dict(self):
        import warnings
        warnings.warn("UploadAgentFileResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UploadAgentFileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
