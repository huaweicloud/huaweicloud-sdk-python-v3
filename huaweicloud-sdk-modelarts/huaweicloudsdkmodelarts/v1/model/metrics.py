# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Metrics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint': 'str',
        'path': 'str',
        'port': 'str',
        'scheme': 'str',
        'metrics_source': 'str'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'path': 'path',
        'port': 'port',
        'scheme': 'scheme',
        'metrics_source': 'metrics_source'
    }

    def __init__(self, endpoint=None, path=None, port=None, scheme=None, metrics_source=None):
        r"""Metrics

        The model defined in huaweicloud sdk

        :param endpoint: **参数解释：** 指标采集地址，支持IP地址、域名或localhost。 **取值范围：** 不涉及。
        :type endpoint: str
        :param path: **参数解释：** 指标采集路径。 **取值范围：** 不涉及
        :type path: str
        :param port: **参数解释：** 指标采集端口。 **取值范围：** 1~65535。
        :type port: str
        :param scheme: **参数解释：** 指标采集协议。 **取值范围：** - HTTP。 - HTTPS。
        :type scheme: str
        :param metrics_source: **参数解释：** 指标来源类型。 **取值范围：** - CONTAINER表示容器内。 - OTHERS表示外部其他地址。 **约束限制：** 不涉及。 **默认取值：** CONTAINER。
        :type metrics_source: str
        """
        
        

        self._endpoint = None
        self._path = None
        self._port = None
        self._scheme = None
        self._metrics_source = None
        self.discriminator = None

        self.endpoint = endpoint
        if path is not None:
            self.path = path
        self.port = port
        self.scheme = scheme
        if metrics_source is not None:
            self.metrics_source = metrics_source

    @property
    def endpoint(self):
        r"""Gets the endpoint of this Metrics.

        **参数解释：** 指标采集地址，支持IP地址、域名或localhost。 **取值范围：** 不涉及。

        :return: The endpoint of this Metrics.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this Metrics.

        **参数解释：** 指标采集地址，支持IP地址、域名或localhost。 **取值范围：** 不涉及。

        :param endpoint: The endpoint of this Metrics.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def path(self):
        r"""Gets the path of this Metrics.

        **参数解释：** 指标采集路径。 **取值范围：** 不涉及

        :return: The path of this Metrics.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this Metrics.

        **参数解释：** 指标采集路径。 **取值范围：** 不涉及

        :param path: The path of this Metrics.
        :type path: str
        """
        self._path = path

    @property
    def port(self):
        r"""Gets the port of this Metrics.

        **参数解释：** 指标采集端口。 **取值范围：** 1~65535。

        :return: The port of this Metrics.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this Metrics.

        **参数解释：** 指标采集端口。 **取值范围：** 1~65535。

        :param port: The port of this Metrics.
        :type port: str
        """
        self._port = port

    @property
    def scheme(self):
        r"""Gets the scheme of this Metrics.

        **参数解释：** 指标采集协议。 **取值范围：** - HTTP。 - HTTPS。

        :return: The scheme of this Metrics.
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        r"""Sets the scheme of this Metrics.

        **参数解释：** 指标采集协议。 **取值范围：** - HTTP。 - HTTPS。

        :param scheme: The scheme of this Metrics.
        :type scheme: str
        """
        self._scheme = scheme

    @property
    def metrics_source(self):
        r"""Gets the metrics_source of this Metrics.

        **参数解释：** 指标来源类型。 **取值范围：** - CONTAINER表示容器内。 - OTHERS表示外部其他地址。 **约束限制：** 不涉及。 **默认取值：** CONTAINER。

        :return: The metrics_source of this Metrics.
        :rtype: str
        """
        return self._metrics_source

    @metrics_source.setter
    def metrics_source(self, metrics_source):
        r"""Sets the metrics_source of this Metrics.

        **参数解释：** 指标来源类型。 **取值范围：** - CONTAINER表示容器内。 - OTHERS表示外部其他地址。 **约束限制：** 不涉及。 **默认取值：** CONTAINER。

        :param metrics_source: The metrics_source of this Metrics.
        :type metrics_source: str
        """
        self._metrics_source = metrics_source

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
        if not isinstance(other, Metrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
