# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


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
        'files': 'list[GetBackupDownloadLinkFiles]',
        'bucket': 'str'
    }

    attribute_map = {
        'files': 'files',
        'bucket': 'bucket'
    }

    def __init__(self, files=None, bucket=None):
        """ShowBackupDownloadLinkResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._files = None
        self._bucket = None
        self.discriminator = None

        if files is not None:
            self.files = files
        if bucket is not None:
            self.bucket = bucket

    @property
    def files(self):
        """Gets the files of this ShowBackupDownloadLinkResponse.

        备份文件信息。

        :return: The files of this ShowBackupDownloadLinkResponse.
        :rtype: list[GetBackupDownloadLinkFiles]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ShowBackupDownloadLinkResponse.

        备份文件信息。

        :param files: The files of this ShowBackupDownloadLinkResponse.
        :type: list[GetBackupDownloadLinkFiles]
        """
        self._files = files

    @property
    def bucket(self):
        """Gets the bucket of this ShowBackupDownloadLinkResponse.

        OBS桶名。

        :return: The bucket of this ShowBackupDownloadLinkResponse.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this ShowBackupDownloadLinkResponse.

        OBS桶名。

        :param bucket: The bucket of this ShowBackupDownloadLinkResponse.
        :type: str
        """
        self._bucket = bucket

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowBackupDownloadLinkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
