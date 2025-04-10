# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileInfo:

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
        'updated_time': 'str',
        'download_link': 'str',
        'link_expired_time': 'str'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size',
        'updated_time': 'updated_time',
        'download_link': 'download_link',
        'link_expired_time': 'link_expired_time'
    }

    def __init__(self, name=None, size=None, updated_time=None, download_link=None, link_expired_time=None):
        r"""FileInfo

        The model defined in huaweicloud sdk

        :param name: 文件名。
        :type name: str
        :param size: 文件大小，单位：KB。
        :type size: int
        :param updated_time: SQL文件最后一次修改时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始，Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type updated_time: str
        :param download_link: 文件下载链接。
        :type download_link: str
        :param link_expired_time: 下载链接过期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始，Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type link_expired_time: str
        """
        
        

        self._name = None
        self._size = None
        self._updated_time = None
        self._download_link = None
        self._link_expired_time = None
        self.discriminator = None

        self.name = name
        self.size = size
        self.updated_time = updated_time
        self.download_link = download_link
        self.link_expired_time = link_expired_time

    @property
    def name(self):
        r"""Gets the name of this FileInfo.

        文件名。

        :return: The name of this FileInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FileInfo.

        文件名。

        :param name: The name of this FileInfo.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        r"""Gets the size of this FileInfo.

        文件大小，单位：KB。

        :return: The size of this FileInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this FileInfo.

        文件大小，单位：KB。

        :param size: The size of this FileInfo.
        :type size: int
        """
        self._size = size

    @property
    def updated_time(self):
        r"""Gets the updated_time of this FileInfo.

        SQL文件最后一次修改时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始，Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The updated_time of this FileInfo.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this FileInfo.

        SQL文件最后一次修改时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始，Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param updated_time: The updated_time of this FileInfo.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def download_link(self):
        r"""Gets the download_link of this FileInfo.

        文件下载链接。

        :return: The download_link of this FileInfo.
        :rtype: str
        """
        return self._download_link

    @download_link.setter
    def download_link(self, download_link):
        r"""Sets the download_link of this FileInfo.

        文件下载链接。

        :param download_link: The download_link of this FileInfo.
        :type download_link: str
        """
        self._download_link = download_link

    @property
    def link_expired_time(self):
        r"""Gets the link_expired_time of this FileInfo.

        下载链接过期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始，Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The link_expired_time of this FileInfo.
        :rtype: str
        """
        return self._link_expired_time

    @link_expired_time.setter
    def link_expired_time(self, link_expired_time):
        r"""Sets the link_expired_time of this FileInfo.

        下载链接过期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始，Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param link_expired_time: The link_expired_time of this FileInfo.
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
        if not isinstance(other, FileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
