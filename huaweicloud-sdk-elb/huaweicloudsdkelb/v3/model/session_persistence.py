# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SessionPersistence:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cookie_name': 'str',
        'type': 'str',
        'persistence_timeout': 'int'
    }

    attribute_map = {
        'cookie_name': 'cookie_name',
        'type': 'type',
        'persistence_timeout': 'persistence_timeout'
    }

    def __init__(self, cookie_name=None, type=None, persistence_timeout=None):
        r"""SessionPersistence

        The model defined in huaweicloud sdk

        :param cookie_name: **参数解释**：cookie名称。  **取值范围**：最大长度1024个字符。  [不支持该字段，请勿使用。](tag:hws_eu,hcso_dt)
        :type cookie_name: str
        :param type: **参数解释**：会话保持类型。  **取值范围**： - SOURCE_IP：基于源IP地址的会话保持，也就是根据客户端的源IP地址将流量持续转发到同一后端服务器（member）。 - HTTP_COOKIE：通过在HTTP响应中插入一个特殊的Cookie，实现会话保持。负载均衡会在后续请求中识别该Cookie，并将请求转发到对应的后端服务器。 - APP_COOKIE：基于应用层Cookie的会话保持。与HTTP_COOKIE不同的是，APP_COOKIE要求后端服务在响应中插入一个指定名称的Cookie，负载均衡器识别后，将后续请求转发到相同后端member。  [荷兰region不支持QUIC。](tag:dt) [不支持QUIC。](tag:tm)
        :type type: str
        :param persistence_timeout: **参数解释**：会话保持的时间。当type为APP_COOKIE时不生效。  **取值范围**： - 若pool的protocol为TCP、UDP和QUIC则范围为[1,60]（分钟），默认值1。 - 若pool的protocol为HTTP和HTTPS则范围为[1,1440]（分钟），默认值1440。  [荷兰region不支持QUIC。](tag:dt)
        :type persistence_timeout: int
        """
        
        

        self._cookie_name = None
        self._type = None
        self._persistence_timeout = None
        self.discriminator = None

        if cookie_name is not None:
            self.cookie_name = cookie_name
        self.type = type
        if persistence_timeout is not None:
            self.persistence_timeout = persistence_timeout

    @property
    def cookie_name(self):
        r"""Gets the cookie_name of this SessionPersistence.

        **参数解释**：cookie名称。  **取值范围**：最大长度1024个字符。  [不支持该字段，请勿使用。](tag:hws_eu,hcso_dt)

        :return: The cookie_name of this SessionPersistence.
        :rtype: str
        """
        return self._cookie_name

    @cookie_name.setter
    def cookie_name(self, cookie_name):
        r"""Sets the cookie_name of this SessionPersistence.

        **参数解释**：cookie名称。  **取值范围**：最大长度1024个字符。  [不支持该字段，请勿使用。](tag:hws_eu,hcso_dt)

        :param cookie_name: The cookie_name of this SessionPersistence.
        :type cookie_name: str
        """
        self._cookie_name = cookie_name

    @property
    def type(self):
        r"""Gets the type of this SessionPersistence.

        **参数解释**：会话保持类型。  **取值范围**： - SOURCE_IP：基于源IP地址的会话保持，也就是根据客户端的源IP地址将流量持续转发到同一后端服务器（member）。 - HTTP_COOKIE：通过在HTTP响应中插入一个特殊的Cookie，实现会话保持。负载均衡会在后续请求中识别该Cookie，并将请求转发到对应的后端服务器。 - APP_COOKIE：基于应用层Cookie的会话保持。与HTTP_COOKIE不同的是，APP_COOKIE要求后端服务在响应中插入一个指定名称的Cookie，负载均衡器识别后，将后续请求转发到相同后端member。  [荷兰region不支持QUIC。](tag:dt) [不支持QUIC。](tag:tm)

        :return: The type of this SessionPersistence.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SessionPersistence.

        **参数解释**：会话保持类型。  **取值范围**： - SOURCE_IP：基于源IP地址的会话保持，也就是根据客户端的源IP地址将流量持续转发到同一后端服务器（member）。 - HTTP_COOKIE：通过在HTTP响应中插入一个特殊的Cookie，实现会话保持。负载均衡会在后续请求中识别该Cookie，并将请求转发到对应的后端服务器。 - APP_COOKIE：基于应用层Cookie的会话保持。与HTTP_COOKIE不同的是，APP_COOKIE要求后端服务在响应中插入一个指定名称的Cookie，负载均衡器识别后，将后续请求转发到相同后端member。  [荷兰region不支持QUIC。](tag:dt) [不支持QUIC。](tag:tm)

        :param type: The type of this SessionPersistence.
        :type type: str
        """
        self._type = type

    @property
    def persistence_timeout(self):
        r"""Gets the persistence_timeout of this SessionPersistence.

        **参数解释**：会话保持的时间。当type为APP_COOKIE时不生效。  **取值范围**： - 若pool的protocol为TCP、UDP和QUIC则范围为[1,60]（分钟），默认值1。 - 若pool的protocol为HTTP和HTTPS则范围为[1,1440]（分钟），默认值1440。  [荷兰region不支持QUIC。](tag:dt)

        :return: The persistence_timeout of this SessionPersistence.
        :rtype: int
        """
        return self._persistence_timeout

    @persistence_timeout.setter
    def persistence_timeout(self, persistence_timeout):
        r"""Sets the persistence_timeout of this SessionPersistence.

        **参数解释**：会话保持的时间。当type为APP_COOKIE时不生效。  **取值范围**： - 若pool的protocol为TCP、UDP和QUIC则范围为[1,60]（分钟），默认值1。 - 若pool的protocol为HTTP和HTTPS则范围为[1,1440]（分钟），默认值1440。  [荷兰region不支持QUIC。](tag:dt)

        :param persistence_timeout: The persistence_timeout of this SessionPersistence.
        :type persistence_timeout: int
        """
        self._persistence_timeout = persistence_timeout

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
        if not isinstance(other, SessionPersistence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
