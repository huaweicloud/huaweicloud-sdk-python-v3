# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UrlDomainBaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url_domain': 'str',
        'id': 'str',
        'status': 'int',
        'min_ssl_version': 'str'
    }

    attribute_map = {
        'url_domain': 'url_domain',
        'id': 'id',
        'status': 'status',
        'min_ssl_version': 'min_ssl_version'
    }

    def __init__(self, url_domain=None, id=None, status=None, min_ssl_version=None):
        """UrlDomainBaseInfo

        The model defined in huaweicloud sdk

        :param url_domain: 自定义域名
        :type url_domain: str
        :param id: 自定义域名的编号
        :type id: str
        :param status: CNAME解析状态 - 1: 未解析 - 2: 解析中 - 3: 解析成功 - 4: 解析失败
        :type status: int
        :param min_ssl_version: 支持的最小SSL版本
        :type min_ssl_version: str
        """
        
        

        self._url_domain = None
        self._id = None
        self._status = None
        self._min_ssl_version = None
        self.discriminator = None

        self.url_domain = url_domain
        self.id = id
        self.status = status
        self.min_ssl_version = min_ssl_version

    @property
    def url_domain(self):
        """Gets the url_domain of this UrlDomainBaseInfo.

        自定义域名

        :return: The url_domain of this UrlDomainBaseInfo.
        :rtype: str
        """
        return self._url_domain

    @url_domain.setter
    def url_domain(self, url_domain):
        """Sets the url_domain of this UrlDomainBaseInfo.

        自定义域名

        :param url_domain: The url_domain of this UrlDomainBaseInfo.
        :type url_domain: str
        """
        self._url_domain = url_domain

    @property
    def id(self):
        """Gets the id of this UrlDomainBaseInfo.

        自定义域名的编号

        :return: The id of this UrlDomainBaseInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UrlDomainBaseInfo.

        自定义域名的编号

        :param id: The id of this UrlDomainBaseInfo.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this UrlDomainBaseInfo.

        CNAME解析状态 - 1: 未解析 - 2: 解析中 - 3: 解析成功 - 4: 解析失败

        :return: The status of this UrlDomainBaseInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UrlDomainBaseInfo.

        CNAME解析状态 - 1: 未解析 - 2: 解析中 - 3: 解析成功 - 4: 解析失败

        :param status: The status of this UrlDomainBaseInfo.
        :type status: int
        """
        self._status = status

    @property
    def min_ssl_version(self):
        """Gets the min_ssl_version of this UrlDomainBaseInfo.

        支持的最小SSL版本

        :return: The min_ssl_version of this UrlDomainBaseInfo.
        :rtype: str
        """
        return self._min_ssl_version

    @min_ssl_version.setter
    def min_ssl_version(self, min_ssl_version):
        """Sets the min_ssl_version of this UrlDomainBaseInfo.

        支持的最小SSL版本

        :param min_ssl_version: The min_ssl_version of this UrlDomainBaseInfo.
        :type min_ssl_version: str
        """
        self._min_ssl_version = min_ssl_version

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
        if not isinstance(other, UrlDomainBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
