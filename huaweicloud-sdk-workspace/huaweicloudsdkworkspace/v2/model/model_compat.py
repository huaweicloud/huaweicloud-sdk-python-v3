# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelCompat:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'supports_usage_streaming': 'bool',
        'supports_developer_role': 'bool'
    }

    attribute_map = {
        'supports_usage_streaming': 'supports_usage_streaming',
        'supports_developer_role': 'supports_developer_role'
    }

    def __init__(self, supports_usage_streaming=None, supports_developer_role=None):
        r"""ModelCompat

        The model defined in huaweicloud sdk

        :param supports_usage_streaming: 是否支持使用量流式传输。
        :type supports_usage_streaming: bool
        :param supports_developer_role: 是否支持开发者角色。
        :type supports_developer_role: bool
        """
        
        

        self._supports_usage_streaming = None
        self._supports_developer_role = None
        self.discriminator = None

        if supports_usage_streaming is not None:
            self.supports_usage_streaming = supports_usage_streaming
        if supports_developer_role is not None:
            self.supports_developer_role = supports_developer_role

    @property
    def supports_usage_streaming(self):
        r"""Gets the supports_usage_streaming of this ModelCompat.

        是否支持使用量流式传输。

        :return: The supports_usage_streaming of this ModelCompat.
        :rtype: bool
        """
        return self._supports_usage_streaming

    @supports_usage_streaming.setter
    def supports_usage_streaming(self, supports_usage_streaming):
        r"""Sets the supports_usage_streaming of this ModelCompat.

        是否支持使用量流式传输。

        :param supports_usage_streaming: The supports_usage_streaming of this ModelCompat.
        :type supports_usage_streaming: bool
        """
        self._supports_usage_streaming = supports_usage_streaming

    @property
    def supports_developer_role(self):
        r"""Gets the supports_developer_role of this ModelCompat.

        是否支持开发者角色。

        :return: The supports_developer_role of this ModelCompat.
        :rtype: bool
        """
        return self._supports_developer_role

    @supports_developer_role.setter
    def supports_developer_role(self, supports_developer_role):
        r"""Sets the supports_developer_role of this ModelCompat.

        是否支持开发者角色。

        :param supports_developer_role: The supports_developer_role of this ModelCompat.
        :type supports_developer_role: bool
        """
        self._supports_developer_role = supports_developer_role

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
        if not isinstance(other, ModelCompat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
