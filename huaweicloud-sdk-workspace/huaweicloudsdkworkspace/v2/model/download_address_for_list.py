# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadAddressForList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'download_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'download_url': 'download_url'
    }

    def __init__(self, id=None, download_url=None):
        r"""DownloadAddressForList

        The model defined in huaweicloud sdk

        :param id: 录屏记录（文件）UUID。
        :type id: str
        :param download_url: 下载地址。
        :type download_url: str
        """
        
        

        self._id = None
        self._download_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if download_url is not None:
            self.download_url = download_url

    @property
    def id(self):
        r"""Gets the id of this DownloadAddressForList.

        录屏记录（文件）UUID。

        :return: The id of this DownloadAddressForList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DownloadAddressForList.

        录屏记录（文件）UUID。

        :param id: The id of this DownloadAddressForList.
        :type id: str
        """
        self._id = id

    @property
    def download_url(self):
        r"""Gets the download_url of this DownloadAddressForList.

        下载地址。

        :return: The download_url of this DownloadAddressForList.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        r"""Sets the download_url of this DownloadAddressForList.

        下载地址。

        :param download_url: The download_url of this DownloadAddressForList.
        :type download_url: str
        """
        self._download_url = download_url

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
        if not isinstance(other, DownloadAddressForList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
