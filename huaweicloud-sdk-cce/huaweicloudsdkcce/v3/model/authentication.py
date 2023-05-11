# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Authentication:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mode': 'str',
        'authenticating_proxy': 'AuthenticatingProxy'
    }

    attribute_map = {
        'mode': 'mode',
        'authenticating_proxy': 'authenticatingProxy'
    }

    def __init__(self, mode=None, authenticating_proxy=None):
        """Authentication

        The model defined in huaweicloud sdk

        :param mode: 集群认证模式。 - kubernetes 1.11及之前版本的集群支持“x509”、“rbac”和“authenticating_proxy”，默认取值为“x509”。 - kubernetes 1.13及以上版本的集群支持“rbac”和“authenticating_proxy”，默认取值为“rbac”。
        :type mode: str
        :param authenticating_proxy: 
        :type authenticating_proxy: :class:`huaweicloudsdkcce.v3.AuthenticatingProxy`
        """
        
        

        self._mode = None
        self._authenticating_proxy = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if authenticating_proxy is not None:
            self.authenticating_proxy = authenticating_proxy

    @property
    def mode(self):
        """Gets the mode of this Authentication.

        集群认证模式。 - kubernetes 1.11及之前版本的集群支持“x509”、“rbac”和“authenticating_proxy”，默认取值为“x509”。 - kubernetes 1.13及以上版本的集群支持“rbac”和“authenticating_proxy”，默认取值为“rbac”。

        :return: The mode of this Authentication.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Authentication.

        集群认证模式。 - kubernetes 1.11及之前版本的集群支持“x509”、“rbac”和“authenticating_proxy”，默认取值为“x509”。 - kubernetes 1.13及以上版本的集群支持“rbac”和“authenticating_proxy”，默认取值为“rbac”。

        :param mode: The mode of this Authentication.
        :type mode: str
        """
        self._mode = mode

    @property
    def authenticating_proxy(self):
        """Gets the authenticating_proxy of this Authentication.

        :return: The authenticating_proxy of this Authentication.
        :rtype: :class:`huaweicloudsdkcce.v3.AuthenticatingProxy`
        """
        return self._authenticating_proxy

    @authenticating_proxy.setter
    def authenticating_proxy(self, authenticating_proxy):
        """Sets the authenticating_proxy of this Authentication.

        :param authenticating_proxy: The authenticating_proxy of this Authentication.
        :type authenticating_proxy: :class:`huaweicloudsdkcce.v3.AuthenticatingProxy`
        """
        self._authenticating_proxy = authenticating_proxy

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
        if not isinstance(other, Authentication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
