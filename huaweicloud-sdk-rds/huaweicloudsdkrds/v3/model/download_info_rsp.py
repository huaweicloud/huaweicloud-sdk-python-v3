# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadInfoRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'download_link': 'str',
        'category': 'str'
    }

    attribute_map = {
        'download_link': 'download_link',
        'category': 'category'
    }

    def __init__(self, download_link=None, category=None):
        r"""DownloadInfoRsp

        The model defined in huaweicloud sdk

        :param download_link: 证书下载地址
        :type download_link: str
        :param category: 证书类型
        :type category: str
        """
        
        

        self._download_link = None
        self._category = None
        self.discriminator = None

        self.download_link = download_link
        self.category = category

    @property
    def download_link(self):
        r"""Gets the download_link of this DownloadInfoRsp.

        证书下载地址

        :return: The download_link of this DownloadInfoRsp.
        :rtype: str
        """
        return self._download_link

    @download_link.setter
    def download_link(self, download_link):
        r"""Sets the download_link of this DownloadInfoRsp.

        证书下载地址

        :param download_link: The download_link of this DownloadInfoRsp.
        :type download_link: str
        """
        self._download_link = download_link

    @property
    def category(self):
        r"""Gets the category of this DownloadInfoRsp.

        证书类型

        :return: The category of this DownloadInfoRsp.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this DownloadInfoRsp.

        证书类型

        :param category: The category of this DownloadInfoRsp.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, DownloadInfoRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
