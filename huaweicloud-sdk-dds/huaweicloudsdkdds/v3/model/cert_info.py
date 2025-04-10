# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'download_link': 'str'
    }

    attribute_map = {
        'category': 'category',
        'download_link': 'download_link'
    }

    def __init__(self, category=None, download_link=None):
        r"""CertInfo

        The model defined in huaweicloud sdk

        :param category: 证书种类
        :type category: str
        :param download_link: 证书下载链接
        :type download_link: str
        """
        
        

        self._category = None
        self._download_link = None
        self.discriminator = None

        self.category = category
        self.download_link = download_link

    @property
    def category(self):
        r"""Gets the category of this CertInfo.

        证书种类

        :return: The category of this CertInfo.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CertInfo.

        证书种类

        :param category: The category of this CertInfo.
        :type category: str
        """
        self._category = category

    @property
    def download_link(self):
        r"""Gets the download_link of this CertInfo.

        证书下载链接

        :return: The download_link of this CertInfo.
        :rtype: str
        """
        return self._download_link

    @download_link.setter
    def download_link(self, download_link):
        r"""Sets the download_link of this CertInfo.

        证书下载链接

        :param download_link: The download_link of this CertInfo.
        :type download_link: str
        """
        self._download_link = download_link

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
        if not isinstance(other, CertInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
