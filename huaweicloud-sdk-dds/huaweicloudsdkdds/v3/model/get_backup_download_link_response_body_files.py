# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetBackupDownloadLinkResponseBodyFiles:

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
        'link_expired_time': 'str',
        'group_id': 'str',
        'group_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size',
        'download_link': 'download_link',
        'link_expired_time': 'link_expired_time',
        'group_id': 'group_id',
        'group_name': 'group_name'
    }

    def __init__(self, name=None, size=None, download_link=None, link_expired_time=None, group_id=None, group_name=None):
        r"""GetBackupDownloadLinkResponseBodyFiles

        The model defined in huaweicloud sdk

        :param name: 文件名。
        :type name: str
        :param size: 文件大小，单位为KB。
        :type size: int
        :param download_link: 文件下载链接。
        :type download_link: str
        :param link_expired_time: 下载链接过期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，例如UTC时间偏移显示为+0000。
        :type link_expired_time: str
        :param group_id: 组ID。
        :type group_id: str
        :param group_name: 组名。
        :type group_name: str
        """
        
        

        self._name = None
        self._size = None
        self._download_link = None
        self._link_expired_time = None
        self._group_id = None
        self._group_name = None
        self.discriminator = None

        self.name = name
        self.size = size
        self.download_link = download_link
        self.link_expired_time = link_expired_time
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name

    @property
    def name(self):
        r"""Gets the name of this GetBackupDownloadLinkResponseBodyFiles.

        文件名。

        :return: The name of this GetBackupDownloadLinkResponseBodyFiles.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GetBackupDownloadLinkResponseBodyFiles.

        文件名。

        :param name: The name of this GetBackupDownloadLinkResponseBodyFiles.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        r"""Gets the size of this GetBackupDownloadLinkResponseBodyFiles.

        文件大小，单位为KB。

        :return: The size of this GetBackupDownloadLinkResponseBodyFiles.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this GetBackupDownloadLinkResponseBodyFiles.

        文件大小，单位为KB。

        :param size: The size of this GetBackupDownloadLinkResponseBodyFiles.
        :type size: int
        """
        self._size = size

    @property
    def download_link(self):
        r"""Gets the download_link of this GetBackupDownloadLinkResponseBodyFiles.

        文件下载链接。

        :return: The download_link of this GetBackupDownloadLinkResponseBodyFiles.
        :rtype: str
        """
        return self._download_link

    @download_link.setter
    def download_link(self, download_link):
        r"""Sets the download_link of this GetBackupDownloadLinkResponseBodyFiles.

        文件下载链接。

        :param download_link: The download_link of this GetBackupDownloadLinkResponseBodyFiles.
        :type download_link: str
        """
        self._download_link = download_link

    @property
    def link_expired_time(self):
        r"""Gets the link_expired_time of this GetBackupDownloadLinkResponseBodyFiles.

        下载链接过期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，例如UTC时间偏移显示为+0000。

        :return: The link_expired_time of this GetBackupDownloadLinkResponseBodyFiles.
        :rtype: str
        """
        return self._link_expired_time

    @link_expired_time.setter
    def link_expired_time(self, link_expired_time):
        r"""Sets the link_expired_time of this GetBackupDownloadLinkResponseBodyFiles.

        下载链接过期时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，例如UTC时间偏移显示为+0000。

        :param link_expired_time: The link_expired_time of this GetBackupDownloadLinkResponseBodyFiles.
        :type link_expired_time: str
        """
        self._link_expired_time = link_expired_time

    @property
    def group_id(self):
        r"""Gets the group_id of this GetBackupDownloadLinkResponseBodyFiles.

        组ID。

        :return: The group_id of this GetBackupDownloadLinkResponseBodyFiles.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this GetBackupDownloadLinkResponseBodyFiles.

        组ID。

        :param group_id: The group_id of this GetBackupDownloadLinkResponseBodyFiles.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this GetBackupDownloadLinkResponseBodyFiles.

        组名。

        :return: The group_name of this GetBackupDownloadLinkResponseBodyFiles.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this GetBackupDownloadLinkResponseBodyFiles.

        组名。

        :param group_name: The group_name of this GetBackupDownloadLinkResponseBodyFiles.
        :type group_name: str
        """
        self._group_name = group_name

    def to_dict(self):
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
        if not isinstance(other, GetBackupDownloadLinkResponseBodyFiles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
