# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceCdnReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'authentication_key': 'str',
        'authentication_type': 'str',
        'domain': 'str',
        'protocol': 'str'
    }

    attribute_map = {
        'authentication_key': 'authentication_key',
        'authentication_type': 'authentication_type',
        'domain': 'domain',
        'protocol': 'protocol'
    }

    def __init__(self, authentication_key=None, authentication_type=None, domain=None, protocol=None):
        """SourceCdnReq

        The model defined in huaweicloud sdk

        :param authentication_key: CDN鉴权秘钥，如果CDN需要进行鉴权，则此选项为必选。  无需授权：无需配置此项。 Qiniu：无需配置此项。 Aliyun：根据authentication_type指定的鉴权方式配置此项。 KingsoftCloud：无需配置此项。
        :type authentication_key: str
        :param authentication_type: 鉴权类型: NONE, QINIU_PRIVATE_AUTHENTICATION, ALIYUN_OSS_A, ALIYUN_OSS_B, ALIYUN_OSS_C, KSYUN_PRIVATE_AUTHENTICATION, AZURE_SAS_TOKEN
        :type authentication_type: str
        :param domain:   从指定域名获取对象。
        :type domain: str
        :param protocol: 协议类型，支持http和https协议。
        :type protocol: str
        """
        
        

        self._authentication_key = None
        self._authentication_type = None
        self._domain = None
        self._protocol = None
        self.discriminator = None

        if authentication_key is not None:
            self.authentication_key = authentication_key
        self.authentication_type = authentication_type
        self.domain = domain
        self.protocol = protocol

    @property
    def authentication_key(self):
        """Gets the authentication_key of this SourceCdnReq.

        CDN鉴权秘钥，如果CDN需要进行鉴权，则此选项为必选。  无需授权：无需配置此项。 Qiniu：无需配置此项。 Aliyun：根据authentication_type指定的鉴权方式配置此项。 KingsoftCloud：无需配置此项。

        :return: The authentication_key of this SourceCdnReq.
        :rtype: str
        """
        return self._authentication_key

    @authentication_key.setter
    def authentication_key(self, authentication_key):
        """Sets the authentication_key of this SourceCdnReq.

        CDN鉴权秘钥，如果CDN需要进行鉴权，则此选项为必选。  无需授权：无需配置此项。 Qiniu：无需配置此项。 Aliyun：根据authentication_type指定的鉴权方式配置此项。 KingsoftCloud：无需配置此项。

        :param authentication_key: The authentication_key of this SourceCdnReq.
        :type authentication_key: str
        """
        self._authentication_key = authentication_key

    @property
    def authentication_type(self):
        """Gets the authentication_type of this SourceCdnReq.

        鉴权类型: NONE, QINIU_PRIVATE_AUTHENTICATION, ALIYUN_OSS_A, ALIYUN_OSS_B, ALIYUN_OSS_C, KSYUN_PRIVATE_AUTHENTICATION, AZURE_SAS_TOKEN

        :return: The authentication_type of this SourceCdnReq.
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """Sets the authentication_type of this SourceCdnReq.

        鉴权类型: NONE, QINIU_PRIVATE_AUTHENTICATION, ALIYUN_OSS_A, ALIYUN_OSS_B, ALIYUN_OSS_C, KSYUN_PRIVATE_AUTHENTICATION, AZURE_SAS_TOKEN

        :param authentication_type: The authentication_type of this SourceCdnReq.
        :type authentication_type: str
        """
        self._authentication_type = authentication_type

    @property
    def domain(self):
        """Gets the domain of this SourceCdnReq.

          从指定域名获取对象。

        :return: The domain of this SourceCdnReq.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this SourceCdnReq.

          从指定域名获取对象。

        :param domain: The domain of this SourceCdnReq.
        :type domain: str
        """
        self._domain = domain

    @property
    def protocol(self):
        """Gets the protocol of this SourceCdnReq.

        协议类型，支持http和https协议。

        :return: The protocol of this SourceCdnReq.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this SourceCdnReq.

        协议类型，支持http和https协议。

        :param protocol: The protocol of this SourceCdnReq.
        :type protocol: str
        """
        self._protocol = protocol

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
        if not isinstance(other, SourceCdnReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
