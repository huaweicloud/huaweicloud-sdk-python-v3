# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainOriginHost:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'origin_host_type': 'str',
        'customize_domain': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'origin_host_type': 'origin_host_type',
        'customize_domain': 'customize_domain'
    }

    def __init__(self, domain_id=None, origin_host_type=None, customize_domain=None):
        """DomainOriginHost

        The model defined in huaweicloud sdk

        :param domain_id: 域名ID。
        :type domain_id: str
        :param origin_host_type: 回源host的类型,accelerate：选择加速域名作为回源host域名,customize：使用自定义的域名作为回源host域名。
        :type origin_host_type: str
        :param customize_domain: 自定义回源host域名。
        :type customize_domain: str
        """
        
        

        self._domain_id = None
        self._origin_host_type = None
        self._customize_domain = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        self.origin_host_type = origin_host_type
        if customize_domain is not None:
            self.customize_domain = customize_domain

    @property
    def domain_id(self):
        """Gets the domain_id of this DomainOriginHost.

        域名ID。

        :return: The domain_id of this DomainOriginHost.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this DomainOriginHost.

        域名ID。

        :param domain_id: The domain_id of this DomainOriginHost.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def origin_host_type(self):
        """Gets the origin_host_type of this DomainOriginHost.

        回源host的类型,accelerate：选择加速域名作为回源host域名,customize：使用自定义的域名作为回源host域名。

        :return: The origin_host_type of this DomainOriginHost.
        :rtype: str
        """
        return self._origin_host_type

    @origin_host_type.setter
    def origin_host_type(self, origin_host_type):
        """Sets the origin_host_type of this DomainOriginHost.

        回源host的类型,accelerate：选择加速域名作为回源host域名,customize：使用自定义的域名作为回源host域名。

        :param origin_host_type: The origin_host_type of this DomainOriginHost.
        :type origin_host_type: str
        """
        self._origin_host_type = origin_host_type

    @property
    def customize_domain(self):
        """Gets the customize_domain of this DomainOriginHost.

        自定义回源host域名。

        :return: The customize_domain of this DomainOriginHost.
        :rtype: str
        """
        return self._customize_domain

    @customize_domain.setter
    def customize_domain(self, customize_domain):
        """Sets the customize_domain of this DomainOriginHost.

        自定义回源host域名。

        :param customize_domain: The customize_domain of this DomainOriginHost.
        :type customize_domain: str
        """
        self._customize_domain = customize_domain

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
        if not isinstance(other, DomainOriginHost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
