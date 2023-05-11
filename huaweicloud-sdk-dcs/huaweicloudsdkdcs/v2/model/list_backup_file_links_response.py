# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackupFileLinksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_path': 'str',
        'bucket_name': 'str',
        'links': 'list[LinksItem]'
    }

    attribute_map = {
        'file_path': 'file_path',
        'bucket_name': 'bucket_name',
        'links': 'links'
    }

    def __init__(self, file_path=None, bucket_name=None, links=None):
        """ListBackupFileLinksResponse

        The model defined in huaweicloud sdk

        :param file_path: OBS桶内文件路径。
        :type file_path: str
        :param bucket_name: OBS桶名。
        :type bucket_name: str
        :param links: 备份文件下链接集合，链接数最大为64个。
        :type links: list[:class:`huaweicloudsdkdcs.v2.LinksItem`]
        """
        
        super(ListBackupFileLinksResponse, self).__init__()

        self._file_path = None
        self._bucket_name = None
        self._links = None
        self.discriminator = None

        if file_path is not None:
            self.file_path = file_path
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if links is not None:
            self.links = links

    @property
    def file_path(self):
        """Gets the file_path of this ListBackupFileLinksResponse.

        OBS桶内文件路径。

        :return: The file_path of this ListBackupFileLinksResponse.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this ListBackupFileLinksResponse.

        OBS桶内文件路径。

        :param file_path: The file_path of this ListBackupFileLinksResponse.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def bucket_name(self):
        """Gets the bucket_name of this ListBackupFileLinksResponse.

        OBS桶名。

        :return: The bucket_name of this ListBackupFileLinksResponse.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this ListBackupFileLinksResponse.

        OBS桶名。

        :param bucket_name: The bucket_name of this ListBackupFileLinksResponse.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def links(self):
        """Gets the links of this ListBackupFileLinksResponse.

        备份文件下链接集合，链接数最大为64个。

        :return: The links of this ListBackupFileLinksResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.LinksItem`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ListBackupFileLinksResponse.

        备份文件下链接集合，链接数最大为64个。

        :param links: The links of this ListBackupFileLinksResponse.
        :type links: list[:class:`huaweicloudsdkdcs.v2.LinksItem`]
        """
        self._links = links

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
        if not isinstance(other, ListBackupFileLinksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
