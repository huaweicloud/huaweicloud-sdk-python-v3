# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InfluxDB2ConnectionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'token': 'str',
        'trust_certs': 'object',
        'verify_hostname': 'bool'
    }

    attribute_map = {
        'token': 'token',
        'trust_certs': 'trust_certs',
        'verify_hostname': 'verify_hostname'
    }

    def __init__(self, token=None, trust_certs=None, verify_hostname=None):
        r"""InfluxDB2ConnectionInfo

        The model defined in huaweicloud sdk

        :param token: 鉴权token
        :type token: str
        :param trust_certs: 客户端信任证书列表
        :type trust_certs: object
        :param verify_hostname: 客户端是否开启校验域名
        :type verify_hostname: bool
        """
        
        

        self._token = None
        self._trust_certs = None
        self._verify_hostname = None
        self.discriminator = None

        self.token = token
        if trust_certs is not None:
            self.trust_certs = trust_certs
        if verify_hostname is not None:
            self.verify_hostname = verify_hostname

    @property
    def token(self):
        r"""Gets the token of this InfluxDB2ConnectionInfo.

        鉴权token

        :return: The token of this InfluxDB2ConnectionInfo.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this InfluxDB2ConnectionInfo.

        鉴权token

        :param token: The token of this InfluxDB2ConnectionInfo.
        :type token: str
        """
        self._token = token

    @property
    def trust_certs(self):
        r"""Gets the trust_certs of this InfluxDB2ConnectionInfo.

        客户端信任证书列表

        :return: The trust_certs of this InfluxDB2ConnectionInfo.
        :rtype: object
        """
        return self._trust_certs

    @trust_certs.setter
    def trust_certs(self, trust_certs):
        r"""Sets the trust_certs of this InfluxDB2ConnectionInfo.

        客户端信任证书列表

        :param trust_certs: The trust_certs of this InfluxDB2ConnectionInfo.
        :type trust_certs: object
        """
        self._trust_certs = trust_certs

    @property
    def verify_hostname(self):
        r"""Gets the verify_hostname of this InfluxDB2ConnectionInfo.

        客户端是否开启校验域名

        :return: The verify_hostname of this InfluxDB2ConnectionInfo.
        :rtype: bool
        """
        return self._verify_hostname

    @verify_hostname.setter
    def verify_hostname(self, verify_hostname):
        r"""Sets the verify_hostname of this InfluxDB2ConnectionInfo.

        客户端是否开启校验域名

        :param verify_hostname: The verify_hostname of this InfluxDB2ConnectionInfo.
        :type verify_hostname: bool
        """
        self._verify_hostname = verify_hostname

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
        if not isinstance(other, InfluxDB2ConnectionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
