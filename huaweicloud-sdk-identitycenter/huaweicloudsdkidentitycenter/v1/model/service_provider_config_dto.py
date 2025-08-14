# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceProviderConfigDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audience': 'str',
        'require_request_signature': 'bool',
        'consumers': 'list[ConsumersDto]',
        'start_url': 'str'
    }

    attribute_map = {
        'audience': 'audience',
        'require_request_signature': 'require_request_signature',
        'consumers': 'consumers',
        'start_url': 'start_url'
    }

    def __init__(self, audience=None, require_request_signature=None, consumers=None, start_url=None):
        r"""ServiceProviderConfigDto

        The model defined in huaweicloud sdk

        :param audience: SAML受众
        :type audience: str
        :param require_request_signature: 是否需要签名
        :type require_request_signature: bool
        :param consumers: SAML响应接收方
        :type consumers: list[:class:`huaweicloudsdkidentitycenter.v1.ConsumersDto`]
        :param start_url: 应用程序启动Url
        :type start_url: str
        """
        
        

        self._audience = None
        self._require_request_signature = None
        self._consumers = None
        self._start_url = None
        self.discriminator = None

        self.audience = audience
        if require_request_signature is not None:
            self.require_request_signature = require_request_signature
        self.consumers = consumers
        if start_url is not None:
            self.start_url = start_url

    @property
    def audience(self):
        r"""Gets the audience of this ServiceProviderConfigDto.

        SAML受众

        :return: The audience of this ServiceProviderConfigDto.
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        r"""Sets the audience of this ServiceProviderConfigDto.

        SAML受众

        :param audience: The audience of this ServiceProviderConfigDto.
        :type audience: str
        """
        self._audience = audience

    @property
    def require_request_signature(self):
        r"""Gets the require_request_signature of this ServiceProviderConfigDto.

        是否需要签名

        :return: The require_request_signature of this ServiceProviderConfigDto.
        :rtype: bool
        """
        return self._require_request_signature

    @require_request_signature.setter
    def require_request_signature(self, require_request_signature):
        r"""Sets the require_request_signature of this ServiceProviderConfigDto.

        是否需要签名

        :param require_request_signature: The require_request_signature of this ServiceProviderConfigDto.
        :type require_request_signature: bool
        """
        self._require_request_signature = require_request_signature

    @property
    def consumers(self):
        r"""Gets the consumers of this ServiceProviderConfigDto.

        SAML响应接收方

        :return: The consumers of this ServiceProviderConfigDto.
        :rtype: list[:class:`huaweicloudsdkidentitycenter.v1.ConsumersDto`]
        """
        return self._consumers

    @consumers.setter
    def consumers(self, consumers):
        r"""Sets the consumers of this ServiceProviderConfigDto.

        SAML响应接收方

        :param consumers: The consumers of this ServiceProviderConfigDto.
        :type consumers: list[:class:`huaweicloudsdkidentitycenter.v1.ConsumersDto`]
        """
        self._consumers = consumers

    @property
    def start_url(self):
        r"""Gets the start_url of this ServiceProviderConfigDto.

        应用程序启动Url

        :return: The start_url of this ServiceProviderConfigDto.
        :rtype: str
        """
        return self._start_url

    @start_url.setter
    def start_url(self, start_url):
        r"""Sets the start_url of this ServiceProviderConfigDto.

        应用程序启动Url

        :param start_url: The start_url of this ServiceProviderConfigDto.
        :type start_url: str
        """
        self._start_url = start_url

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
        if not isinstance(other, ServiceProviderConfigDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
