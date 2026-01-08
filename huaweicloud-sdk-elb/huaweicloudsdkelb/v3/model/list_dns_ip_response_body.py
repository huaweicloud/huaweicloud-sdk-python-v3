# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDnsIpResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ips': 'list[DnsIpResponse]'
    }

    attribute_map = {
        'ips': 'ips'
    }

    def __init__(self, ips=None):
        r"""ListDnsIpResponseBody

        The model defined in huaweicloud sdk

        :param ips: 负载均衡器dns ip信息列表。
        :type ips: list[:class:`huaweicloudsdkelb.v3.DnsIpResponse`]
        """
        
        

        self._ips = None
        self.discriminator = None

        if ips is not None:
            self.ips = ips

    @property
    def ips(self):
        r"""Gets the ips of this ListDnsIpResponseBody.

        负载均衡器dns ip信息列表。

        :return: The ips of this ListDnsIpResponseBody.
        :rtype: list[:class:`huaweicloudsdkelb.v3.DnsIpResponse`]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        r"""Sets the ips of this ListDnsIpResponseBody.

        负载均衡器dns ip信息列表。

        :param ips: The ips of this ListDnsIpResponseBody.
        :type ips: list[:class:`huaweicloudsdkelb.v3.DnsIpResponse`]
        """
        self._ips = ips

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListDnsIpResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
