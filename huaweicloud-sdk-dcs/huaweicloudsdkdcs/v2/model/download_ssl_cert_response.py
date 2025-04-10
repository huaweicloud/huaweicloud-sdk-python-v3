# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadSslCertResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'link': 'str',
        'bucket_name': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'link': 'link',
        'bucket_name': 'bucket_name'
    }

    def __init__(self, file_name=None, link=None, bucket_name=None):
        r"""DownloadSslCertResponse

        The model defined in huaweicloud sdk

        :param file_name: SSL证书文件名。
        :type file_name: str
        :param link: SSL证书下载链接。
        :type link: str
        :param bucket_name: 保存SSL证书的obs桶名。
        :type bucket_name: str
        """
        
        super(DownloadSslCertResponse, self).__init__()

        self._file_name = None
        self._link = None
        self._bucket_name = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if link is not None:
            self.link = link
        if bucket_name is not None:
            self.bucket_name = bucket_name

    @property
    def file_name(self):
        r"""Gets the file_name of this DownloadSslCertResponse.

        SSL证书文件名。

        :return: The file_name of this DownloadSslCertResponse.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this DownloadSslCertResponse.

        SSL证书文件名。

        :param file_name: The file_name of this DownloadSslCertResponse.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def link(self):
        r"""Gets the link of this DownloadSslCertResponse.

        SSL证书下载链接。

        :return: The link of this DownloadSslCertResponse.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        r"""Sets the link of this DownloadSslCertResponse.

        SSL证书下载链接。

        :param link: The link of this DownloadSslCertResponse.
        :type link: str
        """
        self._link = link

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this DownloadSslCertResponse.

        保存SSL证书的obs桶名。

        :return: The bucket_name of this DownloadSslCertResponse.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this DownloadSslCertResponse.

        保存SSL证书的obs桶名。

        :param bucket_name: The bucket_name of this DownloadSslCertResponse.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

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
        if not isinstance(other, DownloadSslCertResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
