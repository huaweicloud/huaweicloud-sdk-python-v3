# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecretRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider': 'str',
        'body': 'SecretRequestBody'
    }

    attribute_map = {
        'provider': 'provider',
        'body': 'body'
    }

    def __init__(self, provider=None, body=None):
        """CreateSecretRequest

        The model defined in huaweicloud sdk

        :param provider: 服务提供者：ief或hilens，选择设备纳管到不同的平台。不填默认为hilens平台
        :type provider: str
        :param body: Body of the CreateSecretRequest
        :type body: :class:`huaweicloudsdkhilens.v3.SecretRequestBody`
        """
        
        

        self._provider = None
        self._body = None
        self.discriminator = None

        if provider is not None:
            self.provider = provider
        if body is not None:
            self.body = body

    @property
    def provider(self):
        """Gets the provider of this CreateSecretRequest.

        服务提供者：ief或hilens，选择设备纳管到不同的平台。不填默认为hilens平台

        :return: The provider of this CreateSecretRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CreateSecretRequest.

        服务提供者：ief或hilens，选择设备纳管到不同的平台。不填默认为hilens平台

        :param provider: The provider of this CreateSecretRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def body(self):
        """Gets the body of this CreateSecretRequest.

        :return: The body of this CreateSecretRequest.
        :rtype: :class:`huaweicloudsdkhilens.v3.SecretRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateSecretRequest.

        :param body: The body of this CreateSecretRequest.
        :type body: :class:`huaweicloudsdkhilens.v3.SecretRequestBody`
        """
        self._body = body

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
        if not isinstance(other, CreateSecretRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
