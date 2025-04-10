# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeyChainInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'auth_type': 'str',
        'timeout': 'int'
    }

    attribute_map = {
        'key': 'key',
        'auth_type': 'auth_type',
        'timeout': 'timeout'
    }

    def __init__(self, key=None, auth_type=None, timeout=None):
        r"""KeyChainInfo

        The model defined in huaweicloud sdk

        :param key: 防盗链Key值，由32个字符组成，支持大写字母、小写字母、数字。不可为纯数字或纯字母。
        :type key: str
        :param auth_type: 计算鉴权串的方式： - d_sha256：鉴权方式D，采用HMAC-SHA256算法，建议优先选择此方式； - c_aes：鉴权方式C，采用对称加密算法； - b_md5：鉴权方式B，采用MD5信息摘要算法； - a_md5：鉴权方式A，采用MD5信息摘要算法。  &gt; 鉴权方式ABC存在安全风险，鉴权方式D拥有更高的安全性，建议您优先使用鉴权方式D。
        :type auth_type: str
        :param timeout: URL鉴权信息的超时时长  取值范围：[60，2592000]，即1分钟-30天  单位：秒  鉴权信息中携带的请求时间与直播服务收到请求时的时间的最大差值，用于检查直播推流URL或者直播播放URL是否已过期
        :type timeout: int
        """
        
        

        self._key = None
        self._auth_type = None
        self._timeout = None
        self.discriminator = None

        self.key = key
        self.auth_type = auth_type
        self.timeout = timeout

    @property
    def key(self):
        r"""Gets the key of this KeyChainInfo.

        防盗链Key值，由32个字符组成，支持大写字母、小写字母、数字。不可为纯数字或纯字母。

        :return: The key of this KeyChainInfo.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this KeyChainInfo.

        防盗链Key值，由32个字符组成，支持大写字母、小写字母、数字。不可为纯数字或纯字母。

        :param key: The key of this KeyChainInfo.
        :type key: str
        """
        self._key = key

    @property
    def auth_type(self):
        r"""Gets the auth_type of this KeyChainInfo.

        计算鉴权串的方式： - d_sha256：鉴权方式D，采用HMAC-SHA256算法，建议优先选择此方式； - c_aes：鉴权方式C，采用对称加密算法； - b_md5：鉴权方式B，采用MD5信息摘要算法； - a_md5：鉴权方式A，采用MD5信息摘要算法。  > 鉴权方式ABC存在安全风险，鉴权方式D拥有更高的安全性，建议您优先使用鉴权方式D。

        :return: The auth_type of this KeyChainInfo.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this KeyChainInfo.

        计算鉴权串的方式： - d_sha256：鉴权方式D，采用HMAC-SHA256算法，建议优先选择此方式； - c_aes：鉴权方式C，采用对称加密算法； - b_md5：鉴权方式B，采用MD5信息摘要算法； - a_md5：鉴权方式A，采用MD5信息摘要算法。  > 鉴权方式ABC存在安全风险，鉴权方式D拥有更高的安全性，建议您优先使用鉴权方式D。

        :param auth_type: The auth_type of this KeyChainInfo.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def timeout(self):
        r"""Gets the timeout of this KeyChainInfo.

        URL鉴权信息的超时时长  取值范围：[60，2592000]，即1分钟-30天  单位：秒  鉴权信息中携带的请求时间与直播服务收到请求时的时间的最大差值，用于检查直播推流URL或者直播播放URL是否已过期

        :return: The timeout of this KeyChainInfo.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this KeyChainInfo.

        URL鉴权信息的超时时长  取值范围：[60，2592000]，即1分钟-30天  单位：秒  鉴权信息中携带的请求时间与直播服务收到请求时的时间的最大差值，用于检查直播推流URL或者直播播放URL是否已过期

        :param timeout: The timeout of this KeyChainInfo.
        :type timeout: int
        """
        self._timeout = timeout

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
        if not isinstance(other, KeyChainInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
