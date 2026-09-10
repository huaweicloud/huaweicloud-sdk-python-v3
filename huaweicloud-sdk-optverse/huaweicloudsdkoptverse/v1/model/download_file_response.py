# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadFileResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'download_url': 'str',
        'content': 'str'
    }

    attribute_map = {
        'download_url': 'download_url',
        'content': 'content'
    }

    def __init__(self, download_url=None, content=None):
        r"""DownloadFileResponse

        The model defined in huaweicloud sdk

        :param download_url: 参数解释： 对话ID。 约束限制： 不涉及 取值范围： 不涉及 默认取值： 不涉及
        :type download_url: str
        :param content: **参数解释**：   文件内容。   **约束限制**：   不涉及   **取值范围**：   不涉及 **默认取值**：   不涉及 
        :type content: str
        """
        
        super().__init__()

        self._download_url = None
        self._content = None
        self.discriminator = None

        if download_url is not None:
            self.download_url = download_url
        if content is not None:
            self.content = content

    @property
    def download_url(self):
        r"""Gets the download_url of this DownloadFileResponse.

        参数解释： 对话ID。 约束限制： 不涉及 取值范围： 不涉及 默认取值： 不涉及

        :return: The download_url of this DownloadFileResponse.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        r"""Sets the download_url of this DownloadFileResponse.

        参数解释： 对话ID。 约束限制： 不涉及 取值范围： 不涉及 默认取值： 不涉及

        :param download_url: The download_url of this DownloadFileResponse.
        :type download_url: str
        """
        self._download_url = download_url

    @property
    def content(self):
        r"""Gets the content of this DownloadFileResponse.

        **参数解释**：   文件内容。   **约束限制**：   不涉及   **取值范围**：   不涉及 **默认取值**：   不涉及 

        :return: The content of this DownloadFileResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this DownloadFileResponse.

        **参数解释**：   文件内容。   **约束限制**：   不涉及   **取值范围**：   不涉及 **默认取值**：   不涉及 

        :param content: The content of this DownloadFileResponse.
        :type content: str
        """
        self._content = content

    def to_dict(self):
        import warnings
        warnings.warn("DownloadFileResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DownloadFileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
