# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainsResponse(SdkResponse):

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
        'domain_used_quota': 'int',
        'domain_list': 'list[DomainInfo]'
    }

    attribute_map = {
        'total': 'total',
        'domain_used_quota': 'domain_used_quota',
        'domain_list': 'domain_list'
    }

    def __init__(self, total=None, domain_used_quota=None, domain_list=None):
        r"""ShowDomainsResponse

        The model defined in huaweicloud sdk

        :param total: 全部防护域名的数量
        :type total: int
        :param domain_used_quota: 域名已使用配额
        :type domain_used_quota: int
        :param domain_list: 详细的防护域名信息
        :type domain_list: list[:class:`huaweicloudsdkedgesec.v2.DomainInfo`]
        """
        
        super(ShowDomainsResponse, self).__init__()

        self._total = None
        self._domain_used_quota = None
        self._domain_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if domain_used_quota is not None:
            self.domain_used_quota = domain_used_quota
        if domain_list is not None:
            self.domain_list = domain_list

    @property
    def total(self):
        r"""Gets the total of this ShowDomainsResponse.

        全部防护域名的数量

        :return: The total of this ShowDomainsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowDomainsResponse.

        全部防护域名的数量

        :param total: The total of this ShowDomainsResponse.
        :type total: int
        """
        self._total = total

    @property
    def domain_used_quota(self):
        r"""Gets the domain_used_quota of this ShowDomainsResponse.

        域名已使用配额

        :return: The domain_used_quota of this ShowDomainsResponse.
        :rtype: int
        """
        return self._domain_used_quota

    @domain_used_quota.setter
    def domain_used_quota(self, domain_used_quota):
        r"""Sets the domain_used_quota of this ShowDomainsResponse.

        域名已使用配额

        :param domain_used_quota: The domain_used_quota of this ShowDomainsResponse.
        :type domain_used_quota: int
        """
        self._domain_used_quota = domain_used_quota

    @property
    def domain_list(self):
        r"""Gets the domain_list of this ShowDomainsResponse.

        详细的防护域名信息

        :return: The domain_list of this ShowDomainsResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v2.DomainInfo`]
        """
        return self._domain_list

    @domain_list.setter
    def domain_list(self, domain_list):
        r"""Sets the domain_list of this ShowDomainsResponse.

        详细的防护域名信息

        :param domain_list: The domain_list of this ShowDomainsResponse.
        :type domain_list: list[:class:`huaweicloudsdkedgesec.v2.DomainInfo`]
        """
        self._domain_list = domain_list

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
        if not isinstance(other, ShowDomainsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
