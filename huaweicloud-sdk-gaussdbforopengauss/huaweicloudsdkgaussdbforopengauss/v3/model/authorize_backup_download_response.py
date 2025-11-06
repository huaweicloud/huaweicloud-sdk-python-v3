# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthorizeBackupDownloadResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'file_paths': 'list[str]'
    }

    attribute_map = {
        'bucket': 'bucket',
        'file_paths': 'file_paths'
    }

    def __init__(self, bucket=None, file_paths=None):
        r"""AuthorizeBackupDownloadResponse

        The model defined in huaweicloud sdk

        :param bucket: OBS桶名。
        :type bucket: str
        :param file_paths: 通过OBS Browser+下载备份文件的路径名称。
        :type file_paths: list[str]
        """
        
        super().__init__()

        self._bucket = None
        self._file_paths = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket
        if file_paths is not None:
            self.file_paths = file_paths

    @property
    def bucket(self):
        r"""Gets the bucket of this AuthorizeBackupDownloadResponse.

        OBS桶名。

        :return: The bucket of this AuthorizeBackupDownloadResponse.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this AuthorizeBackupDownloadResponse.

        OBS桶名。

        :param bucket: The bucket of this AuthorizeBackupDownloadResponse.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def file_paths(self):
        r"""Gets the file_paths of this AuthorizeBackupDownloadResponse.

        通过OBS Browser+下载备份文件的路径名称。

        :return: The file_paths of this AuthorizeBackupDownloadResponse.
        :rtype: list[str]
        """
        return self._file_paths

    @file_paths.setter
    def file_paths(self, file_paths):
        r"""Sets the file_paths of this AuthorizeBackupDownloadResponse.

        通过OBS Browser+下载备份文件的路径名称。

        :param file_paths: The file_paths of this AuthorizeBackupDownloadResponse.
        :type file_paths: list[str]
        """
        self._file_paths = file_paths

    def to_dict(self):
        import warnings
        warnings.warn("AuthorizeBackupDownloadResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, AuthorizeBackupDownloadResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
