# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UrlDomain:

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
        'domain': 'str',
        'cname_status': 'int',
        'ssl_id': 'str',
        'ssl_name': 'str',
        'min_ssl_version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'domain': 'domain',
        'cname_status': 'cname_status',
        'ssl_id': 'ssl_id',
        'ssl_name': 'ssl_name',
        'min_ssl_version': 'min_ssl_version'
    }

    def __init__(self, id=None, domain=None, cname_status=None, ssl_id=None, ssl_name=None, min_ssl_version=None):
        """UrlDomain

        The model defined in huaweicloud sdk

        :param id: 域名编号
        :type id: str
        :param domain: 访问域名
        :type domain: str
        :param cname_status: 域名cname状态： - 1：未解析 - 2：解析中 - 3：解析成功 - 4：解析失败
        :type cname_status: int
        :param ssl_id: SSL证书编号
        :type ssl_id: str
        :param ssl_name: SSL证书名称
        :type ssl_name: str
        :param min_ssl_version: 最小ssl协议版本号。支持TLSv1.1或TLSv1.2
        :type min_ssl_version: str
        """
        
        

        self._id = None
        self._domain = None
        self._cname_status = None
        self._ssl_id = None
        self._ssl_name = None
        self._min_ssl_version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain is not None:
            self.domain = domain
        if cname_status is not None:
            self.cname_status = cname_status
        if ssl_id is not None:
            self.ssl_id = ssl_id
        if ssl_name is not None:
            self.ssl_name = ssl_name
        if min_ssl_version is not None:
            self.min_ssl_version = min_ssl_version

    @property
    def id(self):
        """Gets the id of this UrlDomain.

        域名编号

        :return: The id of this UrlDomain.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UrlDomain.

        域名编号

        :param id: The id of this UrlDomain.
        :type id: str
        """
        self._id = id

    @property
    def domain(self):
        """Gets the domain of this UrlDomain.

        访问域名

        :return: The domain of this UrlDomain.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this UrlDomain.

        访问域名

        :param domain: The domain of this UrlDomain.
        :type domain: str
        """
        self._domain = domain

    @property
    def cname_status(self):
        """Gets the cname_status of this UrlDomain.

        域名cname状态： - 1：未解析 - 2：解析中 - 3：解析成功 - 4：解析失败

        :return: The cname_status of this UrlDomain.
        :rtype: int
        """
        return self._cname_status

    @cname_status.setter
    def cname_status(self, cname_status):
        """Sets the cname_status of this UrlDomain.

        域名cname状态： - 1：未解析 - 2：解析中 - 3：解析成功 - 4：解析失败

        :param cname_status: The cname_status of this UrlDomain.
        :type cname_status: int
        """
        self._cname_status = cname_status

    @property
    def ssl_id(self):
        """Gets the ssl_id of this UrlDomain.

        SSL证书编号

        :return: The ssl_id of this UrlDomain.
        :rtype: str
        """
        return self._ssl_id

    @ssl_id.setter
    def ssl_id(self, ssl_id):
        """Sets the ssl_id of this UrlDomain.

        SSL证书编号

        :param ssl_id: The ssl_id of this UrlDomain.
        :type ssl_id: str
        """
        self._ssl_id = ssl_id

    @property
    def ssl_name(self):
        """Gets the ssl_name of this UrlDomain.

        SSL证书名称

        :return: The ssl_name of this UrlDomain.
        :rtype: str
        """
        return self._ssl_name

    @ssl_name.setter
    def ssl_name(self, ssl_name):
        """Sets the ssl_name of this UrlDomain.

        SSL证书名称

        :param ssl_name: The ssl_name of this UrlDomain.
        :type ssl_name: str
        """
        self._ssl_name = ssl_name

    @property
    def min_ssl_version(self):
        """Gets the min_ssl_version of this UrlDomain.

        最小ssl协议版本号。支持TLSv1.1或TLSv1.2

        :return: The min_ssl_version of this UrlDomain.
        :rtype: str
        """
        return self._min_ssl_version

    @min_ssl_version.setter
    def min_ssl_version(self, min_ssl_version):
        """Sets the min_ssl_version of this UrlDomain.

        最小ssl协议版本号。支持TLSv1.1或TLSv1.2

        :param min_ssl_version: The min_ssl_version of this UrlDomain.
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
        if not isinstance(other, UrlDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
