# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpExchangeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exchanged_ip': 'list[str]',
        'is_exchange_domain': 'bool'
    }

    attribute_map = {
        'exchanged_ip': 'exchanged_ip',
        'is_exchange_domain': 'is_exchange_domain'
    }

    def __init__(self, exchanged_ip=None, is_exchange_domain=None):
        r"""IpExchangeRequest

        The model defined in huaweicloud sdk

        :param exchanged_ip: 待交换的ip地址
        :type exchanged_ip: list[str]
        :param is_exchange_domain: 是否交换domain
        :type is_exchange_domain: bool
        """
        
        

        self._exchanged_ip = None
        self._is_exchange_domain = None
        self.discriminator = None

        self.exchanged_ip = exchanged_ip
        self.is_exchange_domain = is_exchange_domain

    @property
    def exchanged_ip(self):
        r"""Gets the exchanged_ip of this IpExchangeRequest.

        待交换的ip地址

        :return: The exchanged_ip of this IpExchangeRequest.
        :rtype: list[str]
        """
        return self._exchanged_ip

    @exchanged_ip.setter
    def exchanged_ip(self, exchanged_ip):
        r"""Sets the exchanged_ip of this IpExchangeRequest.

        待交换的ip地址

        :param exchanged_ip: The exchanged_ip of this IpExchangeRequest.
        :type exchanged_ip: list[str]
        """
        self._exchanged_ip = exchanged_ip

    @property
    def is_exchange_domain(self):
        r"""Gets the is_exchange_domain of this IpExchangeRequest.

        是否交换domain

        :return: The is_exchange_domain of this IpExchangeRequest.
        :rtype: bool
        """
        return self._is_exchange_domain

    @is_exchange_domain.setter
    def is_exchange_domain(self, is_exchange_domain):
        r"""Sets the is_exchange_domain of this IpExchangeRequest.

        是否交换domain

        :param is_exchange_domain: The is_exchange_domain of this IpExchangeRequest.
        :type is_exchange_domain: bool
        """
        self._is_exchange_domain = is_exchange_domain

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
        if not isinstance(other, IpExchangeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
