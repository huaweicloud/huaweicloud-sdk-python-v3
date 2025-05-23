# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAttachedDomainsV2Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificate_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'url_domain': 'str'
    }

    attribute_map = {
        'certificate_id': 'certificate_id',
        'offset': 'offset',
        'limit': 'limit',
        'url_domain': 'url_domain'
    }

    def __init__(self, certificate_id=None, offset=None, limit=None, url_domain=None):
        r"""ListAttachedDomainsV2Request

        The model defined in huaweicloud sdk

        :param certificate_id: 证书的编号
        :type certificate_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param url_domain: 独立域名
        :type url_domain: str
        """
        
        

        self._certificate_id = None
        self._offset = None
        self._limit = None
        self._url_domain = None
        self.discriminator = None

        self.certificate_id = certificate_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if url_domain is not None:
            self.url_domain = url_domain

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this ListAttachedDomainsV2Request.

        证书的编号

        :return: The certificate_id of this ListAttachedDomainsV2Request.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this ListAttachedDomainsV2Request.

        证书的编号

        :param certificate_id: The certificate_id of this ListAttachedDomainsV2Request.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def offset(self):
        r"""Gets the offset of this ListAttachedDomainsV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListAttachedDomainsV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAttachedDomainsV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListAttachedDomainsV2Request.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAttachedDomainsV2Request.

        每页显示的条目数量

        :return: The limit of this ListAttachedDomainsV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAttachedDomainsV2Request.

        每页显示的条目数量

        :param limit: The limit of this ListAttachedDomainsV2Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def url_domain(self):
        r"""Gets the url_domain of this ListAttachedDomainsV2Request.

        独立域名

        :return: The url_domain of this ListAttachedDomainsV2Request.
        :rtype: str
        """
        return self._url_domain

    @url_domain.setter
    def url_domain(self, url_domain):
        r"""Sets the url_domain of this ListAttachedDomainsV2Request.

        独立域名

        :param url_domain: The url_domain of this ListAttachedDomainsV2Request.
        :type url_domain: str
        """
        self._url_domain = url_domain

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
        if not isinstance(other, ListAttachedDomainsV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
