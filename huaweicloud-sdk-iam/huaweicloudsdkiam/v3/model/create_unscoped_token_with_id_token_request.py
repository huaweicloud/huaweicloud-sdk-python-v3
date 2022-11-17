# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUnscopedTokenWithIdTokenRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'idp_id': 'str',
        'protocol_id': 'str',
        'authorization': 'str'
    }

    attribute_map = {
        'idp_id': 'idp_id',
        'protocol_id': 'protocol_id',
        'authorization': 'Authorization'
    }

    def __init__(self, idp_id=None, protocol_id=None, authorization=None):
        """CreateUnscopedTokenWithIdTokenRequest

        The model defined in huaweicloud sdk

        :param idp_id: 身份提供商id。
        :type idp_id: str
        :param protocol_id: 协议id。
        :type protocol_id: str
        :param authorization: OpenID Connect身份提供商的ID Token，格式为Bearer {ID Token}。
        :type authorization: str
        """
        
        

        self._idp_id = None
        self._protocol_id = None
        self._authorization = None
        self.discriminator = None

        self.idp_id = idp_id
        self.protocol_id = protocol_id
        self.authorization = authorization

    @property
    def idp_id(self):
        """Gets the idp_id of this CreateUnscopedTokenWithIdTokenRequest.

        身份提供商id。

        :return: The idp_id of this CreateUnscopedTokenWithIdTokenRequest.
        :rtype: str
        """
        return self._idp_id

    @idp_id.setter
    def idp_id(self, idp_id):
        """Sets the idp_id of this CreateUnscopedTokenWithIdTokenRequest.

        身份提供商id。

        :param idp_id: The idp_id of this CreateUnscopedTokenWithIdTokenRequest.
        :type idp_id: str
        """
        self._idp_id = idp_id

    @property
    def protocol_id(self):
        """Gets the protocol_id of this CreateUnscopedTokenWithIdTokenRequest.

        协议id。

        :return: The protocol_id of this CreateUnscopedTokenWithIdTokenRequest.
        :rtype: str
        """
        return self._protocol_id

    @protocol_id.setter
    def protocol_id(self, protocol_id):
        """Sets the protocol_id of this CreateUnscopedTokenWithIdTokenRequest.

        协议id。

        :param protocol_id: The protocol_id of this CreateUnscopedTokenWithIdTokenRequest.
        :type protocol_id: str
        """
        self._protocol_id = protocol_id

    @property
    def authorization(self):
        """Gets the authorization of this CreateUnscopedTokenWithIdTokenRequest.

        OpenID Connect身份提供商的ID Token，格式为Bearer {ID Token}。

        :return: The authorization of this CreateUnscopedTokenWithIdTokenRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this CreateUnscopedTokenWithIdTokenRequest.

        OpenID Connect身份提供商的ID Token，格式为Bearer {ID Token}。

        :param authorization: The authorization of this CreateUnscopedTokenWithIdTokenRequest.
        :type authorization: str
        """
        self._authorization = authorization

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
        if not isinstance(other, CreateUnscopedTokenWithIdTokenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
