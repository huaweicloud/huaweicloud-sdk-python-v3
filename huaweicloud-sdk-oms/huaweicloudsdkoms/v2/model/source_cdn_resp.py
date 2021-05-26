# coding: utf-8

import pprint
import re

import six





class SourceCdnResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'protocol': 'str',
        'authentication_type': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'protocol': 'protocol',
        'authentication_type': 'authentication_type'
    }

    def __init__(self, domain=None, protocol=None, authentication_type=None):
        """SourceCdnResp - a model defined in huaweicloud sdk"""
        
        

        self._domain = None
        self._protocol = None
        self._authentication_type = None
        self.discriminator = None

        self.domain = domain
        self.protocol = protocol
        if authentication_type is not None:
            self.authentication_type = authentication_type

    @property
    def domain(self):
        """Gets the domain of this SourceCdnResp.

          从指定域名获取对象。

        :return: The domain of this SourceCdnResp.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this SourceCdnResp.

          从指定域名获取对象。

        :param domain: The domain of this SourceCdnResp.
        :type: str
        """
        self._domain = domain

    @property
    def protocol(self):
        """Gets the protocol of this SourceCdnResp.

        协议类型，支持http和https协议。

        :return: The protocol of this SourceCdnResp.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this SourceCdnResp.

        协议类型，支持http和https协议。

        :param protocol: The protocol of this SourceCdnResp.
        :type: str
        """
        self._protocol = protocol

    @property
    def authentication_type(self):
        """Gets the authentication_type of this SourceCdnResp.

        鉴权类型: NONE, QINIU_PRIVATE_AUTHENTICATION, ALIYUN_OSS_A, ALIYUN_OSS_B, ALIYUN_OSS_C, KSYUN_PRIVATE_AUTHENTICATION, AZURE_SAS_TOKEN

        :return: The authentication_type of this SourceCdnResp.
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """Sets the authentication_type of this SourceCdnResp.

        鉴权类型: NONE, QINIU_PRIVATE_AUTHENTICATION, ALIYUN_OSS_A, ALIYUN_OSS_B, ALIYUN_OSS_C, KSYUN_PRIVATE_AUTHENTICATION, AZURE_SAS_TOKEN

        :param authentication_type: The authentication_type of this SourceCdnResp.
        :type: str
        """
        self._authentication_type = authentication_type

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SourceCdnResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
