# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadObject:

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
        'size': 'float',
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
        """DownloadObject

        The model defined in huaweicloud sdk

        :param name: 文件名称。
        :type name: str
        :param size: 文件大小。
        :type size: float
        :param download_link: 下载链接。
        :type download_link: str
        :param link_expired_time: 链接过期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type link_expired_time: str
        """
        
        

        self._name = None
        self._size = None
        self._download_link = None
        self._link_expired_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if download_link is not None:
            self.download_link = download_link
        if link_expired_time is not None:
            self.link_expired_time = link_expired_time

    @property
    def name(self):
        """Gets the name of this DownloadObject.

        文件名称。

        :return: The name of this DownloadObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DownloadObject.

        文件名称。

        :param name: The name of this DownloadObject.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this DownloadObject.

        文件大小。

        :return: The size of this DownloadObject.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DownloadObject.

        文件大小。

        :param size: The size of this DownloadObject.
        :type size: float
        """
        self._size = size

    @property
    def download_link(self):
        """Gets the download_link of this DownloadObject.

        下载链接。

        :return: The download_link of this DownloadObject.
        :rtype: str
        """
        return self._download_link

    @download_link.setter
    def download_link(self, download_link):
        """Sets the download_link of this DownloadObject.

        下载链接。

        :param download_link: The download_link of this DownloadObject.
        :type download_link: str
        """
        self._download_link = download_link

    @property
    def link_expired_time(self):
        """Gets the link_expired_time of this DownloadObject.

        链接过期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The link_expired_time of this DownloadObject.
        :rtype: str
        """
        return self._link_expired_time

    @link_expired_time.setter
    def link_expired_time(self, link_expired_time):
        """Sets the link_expired_time of this DownloadObject.

        链接过期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param link_expired_time: The link_expired_time of this DownloadObject.
        :type link_expired_time: str
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
        if not isinstance(other, DownloadObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
