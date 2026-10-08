# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayTargetInferenceConfigurationModelMappingProviderPrefix:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'separator': 'str',
        'strip': 'bool'
    }

    attribute_map = {
        'separator': 'separator',
        'strip': 'strip'
    }

    def __init__(self, separator=None, strip=None):
        r"""CoreGatewayTargetInferenceConfigurationModelMappingProviderPrefix

        The model defined in huaweicloud sdk

        :param separator: 分隔符。
        :type separator: str
        :param strip: 是否去除前缀。
        :type strip: bool
        """
        
        

        self._separator = None
        self._strip = None
        self.discriminator = None

        if separator is not None:
            self.separator = separator
        if strip is not None:
            self.strip = strip

    @property
    def separator(self):
        r"""Gets the separator of this CoreGatewayTargetInferenceConfigurationModelMappingProviderPrefix.

        分隔符。

        :return: The separator of this CoreGatewayTargetInferenceConfigurationModelMappingProviderPrefix.
        :rtype: str
        """
        return self._separator

    @separator.setter
    def separator(self, separator):
        r"""Sets the separator of this CoreGatewayTargetInferenceConfigurationModelMappingProviderPrefix.

        分隔符。

        :param separator: The separator of this CoreGatewayTargetInferenceConfigurationModelMappingProviderPrefix.
        :type separator: str
        """
        self._separator = separator

    @property
    def strip(self):
        r"""Gets the strip of this CoreGatewayTargetInferenceConfigurationModelMappingProviderPrefix.

        是否去除前缀。

        :return: The strip of this CoreGatewayTargetInferenceConfigurationModelMappingProviderPrefix.
        :rtype: bool
        """
        return self._strip

    @strip.setter
    def strip(self, strip):
        r"""Sets the strip of this CoreGatewayTargetInferenceConfigurationModelMappingProviderPrefix.

        是否去除前缀。

        :param strip: The strip of this CoreGatewayTargetInferenceConfigurationModelMappingProviderPrefix.
        :type strip: bool
        """
        self._strip = strip

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
        if not isinstance(other, CoreGatewayTargetInferenceConfigurationModelMappingProviderPrefix):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
