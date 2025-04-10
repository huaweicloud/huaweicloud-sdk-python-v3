# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CasServiceResponseAuthenticationSuccess:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user': 'str',
        'proxy_granting_ticket': 'str',
        'proxies': 'list[str]',
        'attributes': 'CasAuthenticationSuccessAttributes'
    }

    attribute_map = {
        'user': 'user',
        'proxy_granting_ticket': 'proxyGrantingTicket',
        'proxies': 'proxies',
        'attributes': 'attributes'
    }

    def __init__(self, user=None, proxy_granting_ticket=None, proxies=None, attributes=None):
        r"""CasServiceResponseAuthenticationSuccess

        The model defined in huaweicloud sdk

        :param user: 用户标识
        :type user: str
        :param proxy_granting_ticket: 代理授权凭据
        :type proxy_granting_ticket: str
        :param proxies: 代理
        :type proxies: list[str]
        :param attributes: 
        :type attributes: :class:`huaweicloudsdkorgid.v1.CasAuthenticationSuccessAttributes`
        """
        
        

        self._user = None
        self._proxy_granting_ticket = None
        self._proxies = None
        self._attributes = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if proxy_granting_ticket is not None:
            self.proxy_granting_ticket = proxy_granting_ticket
        if proxies is not None:
            self.proxies = proxies
        if attributes is not None:
            self.attributes = attributes

    @property
    def user(self):
        r"""Gets the user of this CasServiceResponseAuthenticationSuccess.

        用户标识

        :return: The user of this CasServiceResponseAuthenticationSuccess.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this CasServiceResponseAuthenticationSuccess.

        用户标识

        :param user: The user of this CasServiceResponseAuthenticationSuccess.
        :type user: str
        """
        self._user = user

    @property
    def proxy_granting_ticket(self):
        r"""Gets the proxy_granting_ticket of this CasServiceResponseAuthenticationSuccess.

        代理授权凭据

        :return: The proxy_granting_ticket of this CasServiceResponseAuthenticationSuccess.
        :rtype: str
        """
        return self._proxy_granting_ticket

    @proxy_granting_ticket.setter
    def proxy_granting_ticket(self, proxy_granting_ticket):
        r"""Sets the proxy_granting_ticket of this CasServiceResponseAuthenticationSuccess.

        代理授权凭据

        :param proxy_granting_ticket: The proxy_granting_ticket of this CasServiceResponseAuthenticationSuccess.
        :type proxy_granting_ticket: str
        """
        self._proxy_granting_ticket = proxy_granting_ticket

    @property
    def proxies(self):
        r"""Gets the proxies of this CasServiceResponseAuthenticationSuccess.

        代理

        :return: The proxies of this CasServiceResponseAuthenticationSuccess.
        :rtype: list[str]
        """
        return self._proxies

    @proxies.setter
    def proxies(self, proxies):
        r"""Sets the proxies of this CasServiceResponseAuthenticationSuccess.

        代理

        :param proxies: The proxies of this CasServiceResponseAuthenticationSuccess.
        :type proxies: list[str]
        """
        self._proxies = proxies

    @property
    def attributes(self):
        r"""Gets the attributes of this CasServiceResponseAuthenticationSuccess.

        :return: The attributes of this CasServiceResponseAuthenticationSuccess.
        :rtype: :class:`huaweicloudsdkorgid.v1.CasAuthenticationSuccessAttributes`
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this CasServiceResponseAuthenticationSuccess.

        :param attributes: The attributes of this CasServiceResponseAuthenticationSuccess.
        :type attributes: :class:`huaweicloudsdkorgid.v1.CasAuthenticationSuccessAttributes`
        """
        self._attributes = attributes

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
        if not isinstance(other, CasServiceResponseAuthenticationSuccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
