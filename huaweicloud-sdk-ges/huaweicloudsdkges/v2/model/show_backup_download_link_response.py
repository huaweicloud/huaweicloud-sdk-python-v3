# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackupDownloadLinkResponse(SdkResponse):

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
        'files': 'list[BackupDownloadLink]'
    }

    attribute_map = {
        'bucket': 'bucket',
        'files': 'files'
    }

    def __init__(self, bucket=None, files=None):
        r"""ShowBackupDownloadLinkResponse

        The model defined in huaweicloud sdk

        :param bucket: 文件所在的桶名。
        :type bucket: str
        :param files: 备份包含的文件列表。
        :type files: list[:class:`huaweicloudsdkges.v2.BackupDownloadLink`]
        """
        
        super(ShowBackupDownloadLinkResponse, self).__init__()

        self._bucket = None
        self._files = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket
        if files is not None:
            self.files = files

    @property
    def bucket(self):
        r"""Gets the bucket of this ShowBackupDownloadLinkResponse.

        文件所在的桶名。

        :return: The bucket of this ShowBackupDownloadLinkResponse.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this ShowBackupDownloadLinkResponse.

        文件所在的桶名。

        :param bucket: The bucket of this ShowBackupDownloadLinkResponse.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def files(self):
        r"""Gets the files of this ShowBackupDownloadLinkResponse.

        备份包含的文件列表。

        :return: The files of this ShowBackupDownloadLinkResponse.
        :rtype: list[:class:`huaweicloudsdkges.v2.BackupDownloadLink`]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this ShowBackupDownloadLinkResponse.

        备份包含的文件列表。

        :param files: The files of this ShowBackupDownloadLinkResponse.
        :type files: list[:class:`huaweicloudsdkges.v2.BackupDownloadLink`]
        """
        self._files = files

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
        if not isinstance(other, ShowBackupDownloadLinkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
