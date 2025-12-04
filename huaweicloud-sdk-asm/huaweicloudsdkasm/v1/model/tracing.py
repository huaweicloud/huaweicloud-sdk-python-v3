# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Tracing:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'random_sampling_percentage': 'float',
        'default_providers': 'list[str]',
        'extension_providers': 'list[TracingExtensionProvider]'
    }

    attribute_map = {
        'random_sampling_percentage': 'randomSamplingPercentage',
        'default_providers': 'defaultProviders',
        'extension_providers': 'extensionProviders'
    }

    def __init__(self, random_sampling_percentage=None, default_providers=None, extension_providers=None):
        r"""Tracing

        The model defined in huaweicloud sdk

        :param random_sampling_percentage: tracing采样率
        :type random_sampling_percentage: float
        :param default_providers: tracing默认上报的provider名称，必须与extensionProviders中的name字段匹配，或使用ASM预设的provider \&quot;apm-otel\&quot;。 如果使用\&quot;apm-otel\&quot;，需确认当前region已支持APM2.0且网格版本大于1.18。
        :type default_providers: list[str]
        :param extension_providers: 用户自配置provider，目前支持zipkin协议。 如果用户配置zipkin协议的provider，请保证网格版本大于等于1.15。
        :type extension_providers: list[:class:`huaweicloudsdkasm.v1.TracingExtensionProvider`]
        """
        
        

        self._random_sampling_percentage = None
        self._default_providers = None
        self._extension_providers = None
        self.discriminator = None

        if random_sampling_percentage is not None:
            self.random_sampling_percentage = random_sampling_percentage
        if default_providers is not None:
            self.default_providers = default_providers
        if extension_providers is not None:
            self.extension_providers = extension_providers

    @property
    def random_sampling_percentage(self):
        r"""Gets the random_sampling_percentage of this Tracing.

        tracing采样率

        :return: The random_sampling_percentage of this Tracing.
        :rtype: float
        """
        return self._random_sampling_percentage

    @random_sampling_percentage.setter
    def random_sampling_percentage(self, random_sampling_percentage):
        r"""Sets the random_sampling_percentage of this Tracing.

        tracing采样率

        :param random_sampling_percentage: The random_sampling_percentage of this Tracing.
        :type random_sampling_percentage: float
        """
        self._random_sampling_percentage = random_sampling_percentage

    @property
    def default_providers(self):
        r"""Gets the default_providers of this Tracing.

        tracing默认上报的provider名称，必须与extensionProviders中的name字段匹配，或使用ASM预设的provider \"apm-otel\"。 如果使用\"apm-otel\"，需确认当前region已支持APM2.0且网格版本大于1.18。

        :return: The default_providers of this Tracing.
        :rtype: list[str]
        """
        return self._default_providers

    @default_providers.setter
    def default_providers(self, default_providers):
        r"""Sets the default_providers of this Tracing.

        tracing默认上报的provider名称，必须与extensionProviders中的name字段匹配，或使用ASM预设的provider \"apm-otel\"。 如果使用\"apm-otel\"，需确认当前region已支持APM2.0且网格版本大于1.18。

        :param default_providers: The default_providers of this Tracing.
        :type default_providers: list[str]
        """
        self._default_providers = default_providers

    @property
    def extension_providers(self):
        r"""Gets the extension_providers of this Tracing.

        用户自配置provider，目前支持zipkin协议。 如果用户配置zipkin协议的provider，请保证网格版本大于等于1.15。

        :return: The extension_providers of this Tracing.
        :rtype: list[:class:`huaweicloudsdkasm.v1.TracingExtensionProvider`]
        """
        return self._extension_providers

    @extension_providers.setter
    def extension_providers(self, extension_providers):
        r"""Sets the extension_providers of this Tracing.

        用户自配置provider，目前支持zipkin协议。 如果用户配置zipkin协议的provider，请保证网格版本大于等于1.15。

        :param extension_providers: The extension_providers of this Tracing.
        :type extension_providers: list[:class:`huaweicloudsdkasm.v1.TracingExtensionProvider`]
        """
        self._extension_providers = extension_providers

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
        if not isinstance(other, Tracing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
