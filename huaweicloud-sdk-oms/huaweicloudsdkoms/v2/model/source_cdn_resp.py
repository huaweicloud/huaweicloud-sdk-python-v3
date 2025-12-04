# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        r"""SourceCdnResp

        The model defined in huaweicloud sdk

        :param domain:   从指定域名获取对象。
        :type domain: str
        :param protocol: 协议类型，支持http和https协议。
        :type protocol: str
        :param authentication_type: 鉴权类型: NONE：公开访问，无安全限制, QINIU_PRIVATE_AUTHENTICATION：七牛自定义URL签名, ALIYUN_OSS_A：阿里云  URL携带签名，简单通用, ALIYUN_OSS_B：阿里云  Header携带签名，用于API调用, ALIYUN_OSS_C：阿里云  STS临时安全令牌，最安全, KSYUN_PRIVATE_AUTHENTICATION：金山云  金山云自定义URL签名, AZURE_SAS_TOKEN：微软Azure  灵活安全的共享访问签名, TENCENT_COS_A:腾讯云  多次有效签名（不推荐）, TENCENT_COS_B:腾讯云  单次有效签名，安全性最高, TENCENT_COS_C:腾讯云  Header携带签名，用于API调用, TENCENT_COS_D:腾讯云  Header携带签名，用于API调用.
        :type authentication_type: str
        """
        
        

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
        r"""Gets the domain of this SourceCdnResp.

          从指定域名获取对象。

        :return: The domain of this SourceCdnResp.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this SourceCdnResp.

          从指定域名获取对象。

        :param domain: The domain of this SourceCdnResp.
        :type domain: str
        """
        self._domain = domain

    @property
    def protocol(self):
        r"""Gets the protocol of this SourceCdnResp.

        协议类型，支持http和https协议。

        :return: The protocol of this SourceCdnResp.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this SourceCdnResp.

        协议类型，支持http和https协议。

        :param protocol: The protocol of this SourceCdnResp.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def authentication_type(self):
        r"""Gets the authentication_type of this SourceCdnResp.

        鉴权类型: NONE：公开访问，无安全限制, QINIU_PRIVATE_AUTHENTICATION：七牛自定义URL签名, ALIYUN_OSS_A：阿里云  URL携带签名，简单通用, ALIYUN_OSS_B：阿里云  Header携带签名，用于API调用, ALIYUN_OSS_C：阿里云  STS临时安全令牌，最安全, KSYUN_PRIVATE_AUTHENTICATION：金山云  金山云自定义URL签名, AZURE_SAS_TOKEN：微软Azure  灵活安全的共享访问签名, TENCENT_COS_A:腾讯云  多次有效签名（不推荐）, TENCENT_COS_B:腾讯云  单次有效签名，安全性最高, TENCENT_COS_C:腾讯云  Header携带签名，用于API调用, TENCENT_COS_D:腾讯云  Header携带签名，用于API调用.

        :return: The authentication_type of this SourceCdnResp.
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        r"""Sets the authentication_type of this SourceCdnResp.

        鉴权类型: NONE：公开访问，无安全限制, QINIU_PRIVATE_AUTHENTICATION：七牛自定义URL签名, ALIYUN_OSS_A：阿里云  URL携带签名，简单通用, ALIYUN_OSS_B：阿里云  Header携带签名，用于API调用, ALIYUN_OSS_C：阿里云  STS临时安全令牌，最安全, KSYUN_PRIVATE_AUTHENTICATION：金山云  金山云自定义URL签名, AZURE_SAS_TOKEN：微软Azure  灵活安全的共享访问签名, TENCENT_COS_A:腾讯云  多次有效签名（不推荐）, TENCENT_COS_B:腾讯云  单次有效签名，安全性最高, TENCENT_COS_C:腾讯云  Header携带签名，用于API调用, TENCENT_COS_D:腾讯云  Header携带签名，用于API调用.

        :param authentication_type: The authentication_type of this SourceCdnResp.
        :type authentication_type: str
        """
        self._authentication_type = authentication_type

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
        if not isinstance(other, SourceCdnResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
