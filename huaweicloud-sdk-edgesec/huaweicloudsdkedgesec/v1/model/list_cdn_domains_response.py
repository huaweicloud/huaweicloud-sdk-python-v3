# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCdnDomainsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'count': 'int',
        'domains': 'list[ShowCdnDomainResponseBody]'
    }

    attribute_map = {
        'total': 'total',
        'count': 'count',
        'domains': 'domains'
    }

    def __init__(self, total=None, count=None, domains=None):
        """ListCdnDomainsResponse

        The model defined in huaweicloud sdk

        :param total: 全部CDN域名的数量
        :type total: int
        :param count: 查询结果CDN域名的数量
        :type count: int
        :param domains: 详细的CDN域名信息
        :type domains: list[:class:`huaweicloudsdkedgesec.v1.ShowCdnDomainResponseBody`]
        """
        
        super(ListCdnDomainsResponse, self).__init__()

        self._total = None
        self._count = None
        self._domains = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if count is not None:
            self.count = count
        if domains is not None:
            self.domains = domains

    @property
    def total(self):
        """Gets the total of this ListCdnDomainsResponse.

        全部CDN域名的数量

        :return: The total of this ListCdnDomainsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListCdnDomainsResponse.

        全部CDN域名的数量

        :param total: The total of this ListCdnDomainsResponse.
        :type total: int
        """
        self._total = total

    @property
    def count(self):
        """Gets the count of this ListCdnDomainsResponse.

        查询结果CDN域名的数量

        :return: The count of this ListCdnDomainsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListCdnDomainsResponse.

        查询结果CDN域名的数量

        :param count: The count of this ListCdnDomainsResponse.
        :type count: int
        """
        self._count = count

    @property
    def domains(self):
        """Gets the domains of this ListCdnDomainsResponse.

        详细的CDN域名信息

        :return: The domains of this ListCdnDomainsResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v1.ShowCdnDomainResponseBody`]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this ListCdnDomainsResponse.

        详细的CDN域名信息

        :param domains: The domains of this ListCdnDomainsResponse.
        :type domains: list[:class:`huaweicloudsdkedgesec.v1.ShowCdnDomainResponseBody`]
        """
        self._domains = domains

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
        if not isinstance(other, ListCdnDomainsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
