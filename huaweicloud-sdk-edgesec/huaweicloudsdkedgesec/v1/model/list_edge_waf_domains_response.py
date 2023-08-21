# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEdgeWafDomainsResponse(SdkResponse):

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
        'domain_list': 'list[ShowWafDomainResponseBody]'
    }

    attribute_map = {
        'total': 'total',
        'domain_list': 'domain_list'
    }

    def __init__(self, total=None, domain_list=None):
        """ListEdgeWafDomainsResponse

        The model defined in huaweicloud sdk

        :param total: 全部防护域名的数量
        :type total: int
        :param domain_list: 详细的防护域名信息
        :type domain_list: list[:class:`huaweicloudsdkedgesec.v1.ShowWafDomainResponseBody`]
        """
        
        super(ListEdgeWafDomainsResponse, self).__init__()

        self._total = None
        self._domain_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if domain_list is not None:
            self.domain_list = domain_list

    @property
    def total(self):
        """Gets the total of this ListEdgeWafDomainsResponse.

        全部防护域名的数量

        :return: The total of this ListEdgeWafDomainsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListEdgeWafDomainsResponse.

        全部防护域名的数量

        :param total: The total of this ListEdgeWafDomainsResponse.
        :type total: int
        """
        self._total = total

    @property
    def domain_list(self):
        """Gets the domain_list of this ListEdgeWafDomainsResponse.

        详细的防护域名信息

        :return: The domain_list of this ListEdgeWafDomainsResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v1.ShowWafDomainResponseBody`]
        """
        return self._domain_list

    @domain_list.setter
    def domain_list(self, domain_list):
        """Sets the domain_list of this ListEdgeWafDomainsResponse.

        详细的防护域名信息

        :param domain_list: The domain_list of this ListEdgeWafDomainsResponse.
        :type domain_list: list[:class:`huaweicloudsdkedgesec.v1.ShowWafDomainResponseBody`]
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
        if not isinstance(other, ListEdgeWafDomainsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
