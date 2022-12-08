# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSasTokenResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_id': 'str',
        'expiry': 'str',
        'signature': 'str'
    }

    attribute_map = {
        'client_id': 'client_id',
        'expiry': 'expiry',
        'signature': 'signature'
    }

    def __init__(self, client_id=None, expiry=None, signature=None):
        """CreateSasTokenResponse

        The model defined in huaweicloud sdk

        :param client_id: API key的client_id
        :type client_id: str
        :param expiry: 超期时间，UTC格式
        :type expiry: str
        :param signature: 签名字符串
        :type signature: str
        """
        
        super(CreateSasTokenResponse, self).__init__()

        self._client_id = None
        self._expiry = None
        self._signature = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if expiry is not None:
            self.expiry = expiry
        if signature is not None:
            self.signature = signature

    @property
    def client_id(self):
        """Gets the client_id of this CreateSasTokenResponse.

        API key的client_id

        :return: The client_id of this CreateSasTokenResponse.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this CreateSasTokenResponse.

        API key的client_id

        :param client_id: The client_id of this CreateSasTokenResponse.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def expiry(self):
        """Gets the expiry of this CreateSasTokenResponse.

        超期时间，UTC格式

        :return: The expiry of this CreateSasTokenResponse.
        :rtype: str
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this CreateSasTokenResponse.

        超期时间，UTC格式

        :param expiry: The expiry of this CreateSasTokenResponse.
        :type expiry: str
        """
        self._expiry = expiry

    @property
    def signature(self):
        """Gets the signature of this CreateSasTokenResponse.

        签名字符串

        :return: The signature of this CreateSasTokenResponse.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this CreateSasTokenResponse.

        签名字符串

        :param signature: The signature of this CreateSasTokenResponse.
        :type signature: str
        """
        self._signature = signature

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
        if not isinstance(other, CreateSasTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
