# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadDdlLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'download_files': 'list[DownLoadFileInfoItem]'
    }

    attribute_map = {
        'download_files': 'download_files'
    }

    def __init__(self, download_files=None):
        r"""DownloadDdlLogsResponse

        The model defined in huaweicloud sdk

        :param download_files: **参数解释**：  每个日志文件的下载链接详情。  **取值范围**：  不涉及。 
        :type download_files: list[:class:`huaweicloudsdkgaussdb.v3.DownLoadFileInfoItem`]
        """
        
        super().__init__()

        self._download_files = None
        self.discriminator = None

        if download_files is not None:
            self.download_files = download_files

    @property
    def download_files(self):
        r"""Gets the download_files of this DownloadDdlLogsResponse.

        **参数解释**：  每个日志文件的下载链接详情。  **取值范围**：  不涉及。 

        :return: The download_files of this DownloadDdlLogsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.DownLoadFileInfoItem`]
        """
        return self._download_files

    @download_files.setter
    def download_files(self, download_files):
        r"""Sets the download_files of this DownloadDdlLogsResponse.

        **参数解释**：  每个日志文件的下载链接详情。  **取值范围**：  不涉及。 

        :param download_files: The download_files of this DownloadDdlLogsResponse.
        :type download_files: list[:class:`huaweicloudsdkgaussdb.v3.DownLoadFileInfoItem`]
        """
        self._download_files = download_files

    def to_dict(self):
        import warnings
        warnings.warn("DownloadDdlLogsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DownloadDdlLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
