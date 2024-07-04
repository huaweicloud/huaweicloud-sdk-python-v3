# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomIngressPortDomainsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'total': 'int',
        'domain_infos': 'list[PortBindingDomainInfo]'
    }

    attribute_map = {
        'size': 'size',
        'total': 'total',
        'domain_infos': 'domain_infos'
    }

    def __init__(self, size=None, total=None, domain_infos=None):
        """ListCustomIngressPortDomainsResponse

        The model defined in huaweicloud sdk

        :param size: 本次返回的列表长度
        :type size: int
        :param total: 满足条件的记录数
        :type total: int
        :param domain_infos: 入方向端口绑定的域名信息列表。
        :type domain_infos: list[:class:`huaweicloudsdkapig.v2.PortBindingDomainInfo`]
        """
        
        super(ListCustomIngressPortDomainsResponse, self).__init__()

        self._size = None
        self._total = None
        self._domain_infos = None
        self.discriminator = None

        self.size = size
        self.total = total
        if domain_infos is not None:
            self.domain_infos = domain_infos

    @property
    def size(self):
        """Gets the size of this ListCustomIngressPortDomainsResponse.

        本次返回的列表长度

        :return: The size of this ListCustomIngressPortDomainsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListCustomIngressPortDomainsResponse.

        本次返回的列表长度

        :param size: The size of this ListCustomIngressPortDomainsResponse.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        """Gets the total of this ListCustomIngressPortDomainsResponse.

        满足条件的记录数

        :return: The total of this ListCustomIngressPortDomainsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListCustomIngressPortDomainsResponse.

        满足条件的记录数

        :param total: The total of this ListCustomIngressPortDomainsResponse.
        :type total: int
        """
        self._total = total

    @property
    def domain_infos(self):
        """Gets the domain_infos of this ListCustomIngressPortDomainsResponse.

        入方向端口绑定的域名信息列表。

        :return: The domain_infos of this ListCustomIngressPortDomainsResponse.
        :rtype: list[:class:`huaweicloudsdkapig.v2.PortBindingDomainInfo`]
        """
        return self._domain_infos

    @domain_infos.setter
    def domain_infos(self, domain_infos):
        """Sets the domain_infos of this ListCustomIngressPortDomainsResponse.

        入方向端口绑定的域名信息列表。

        :param domain_infos: The domain_infos of this ListCustomIngressPortDomainsResponse.
        :type domain_infos: list[:class:`huaweicloudsdkapig.v2.PortBindingDomainInfo`]
        """
        self._domain_infos = domain_infos

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
        if not isinstance(other, ListCustomIngressPortDomainsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
