# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSlowLogArchiveLinkResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'download_link': 'str'
    }

    attribute_map = {
        'download_link': 'download_link'
    }

    def __init__(self, download_link=None):
        r"""ShowSlowLogArchiveLinkResponse

        The model defined in huaweicloud sdk

        :param download_link: 慢日志归档文件下载地址
        :type download_link: str
        """
        
        super().__init__()

        self._download_link = None
        self.discriminator = None

        if download_link is not None:
            self.download_link = download_link

    @property
    def download_link(self):
        r"""Gets the download_link of this ShowSlowLogArchiveLinkResponse.

        慢日志归档文件下载地址

        :return: The download_link of this ShowSlowLogArchiveLinkResponse.
        :rtype: str
        """
        return self._download_link

    @download_link.setter
    def download_link(self, download_link):
        r"""Sets the download_link of this ShowSlowLogArchiveLinkResponse.

        慢日志归档文件下载地址

        :param download_link: The download_link of this ShowSlowLogArchiveLinkResponse.
        :type download_link: str
        """
        self._download_link = download_link

    def to_dict(self):
        import warnings
        warnings.warn("ShowSlowLogArchiveLinkResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSlowLogArchiveLinkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
