# coding: utf-8

import pprint
import re

import six





class GetBackupDownloadLinkFiles:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'size': 'int',
        'download_link': 'str',
        'link_expired_time': 'str'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size',
        'download_link': 'download_link',
        'link_expired_time': 'link_expired_time'
    }

    def __init__(self, name=None, size=None, download_link=None, link_expired_time=None):
        """GetBackupDownloadLinkFiles - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._size = None
        self._download_link = None
        self._link_expired_time = None
        self.discriminator = None

        self.name = name
        self.size = size
        self.download_link = download_link
        self.link_expired_time = link_expired_time

    @property
    def name(self):
        """Gets the name of this GetBackupDownloadLinkFiles.

        文件名。

        :return: The name of this GetBackupDownloadLinkFiles.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetBackupDownloadLinkFiles.

        文件名。

        :param name: The name of this GetBackupDownloadLinkFiles.
        :type: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this GetBackupDownloadLinkFiles.

        文件大小，单位为KB。

        :return: The size of this GetBackupDownloadLinkFiles.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this GetBackupDownloadLinkFiles.

        文件大小，单位为KB。

        :param size: The size of this GetBackupDownloadLinkFiles.
        :type: int
        """
        self._size = size

    @property
    def download_link(self):
        """Gets the download_link of this GetBackupDownloadLinkFiles.

        文件下载链接。

        :return: The download_link of this GetBackupDownloadLinkFiles.
        :rtype: str
        """
        return self._download_link

    @download_link.setter
    def download_link(self, download_link):
        """Sets the download_link of this GetBackupDownloadLinkFiles.

        文件下载链接。

        :param download_link: The download_link of this GetBackupDownloadLinkFiles.
        :type: str
        """
        self._download_link = download_link

    @property
    def link_expired_time(self):
        """Gets the link_expired_time of this GetBackupDownloadLinkFiles.

        下载链接过期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The link_expired_time of this GetBackupDownloadLinkFiles.
        :rtype: str
        """
        return self._link_expired_time

    @link_expired_time.setter
    def link_expired_time(self, link_expired_time):
        """Sets the link_expired_time of this GetBackupDownloadLinkFiles.

        下载链接过期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param link_expired_time: The link_expired_time of this GetBackupDownloadLinkFiles.
        :type: str
        """
        self._link_expired_time = link_expired_time

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
        if not isinstance(other, GetBackupDownloadLinkFiles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
