# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsThirdPartyAgentResponseConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'stream_config': 'OpsThirdPartyAgentStreamConfig',
        'non_stream_config': 'OpsThirdPartyAgentNonStreamConfig'
    }

    attribute_map = {
        'type': 'type',
        'stream_config': 'stream_config',
        'non_stream_config': 'non_stream_config'
    }

    def __init__(self, type=None, stream_config=None, non_stream_config=None):
        r"""OpsThirdPartyAgentResponseConfig

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 响应类型。 **约束限制：** 枚举值。 **取值范围：** STREAM（流式输出）、NON_STREAM（非流式输出）。 **默认取值：** NON_STREAM。
        :type type: str
        :param stream_config: 
        :type stream_config: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentStreamConfig`
        :param non_stream_config: 
        :type non_stream_config: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentNonStreamConfig`
        """
        
        

        self._type = None
        self._stream_config = None
        self._non_stream_config = None
        self.discriminator = None

        self.type = type
        if stream_config is not None:
            self.stream_config = stream_config
        if non_stream_config is not None:
            self.non_stream_config = non_stream_config

    @property
    def type(self):
        r"""Gets the type of this OpsThirdPartyAgentResponseConfig.

        **参数解释：** 响应类型。 **约束限制：** 枚举值。 **取值范围：** STREAM（流式输出）、NON_STREAM（非流式输出）。 **默认取值：** NON_STREAM。

        :return: The type of this OpsThirdPartyAgentResponseConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OpsThirdPartyAgentResponseConfig.

        **参数解释：** 响应类型。 **约束限制：** 枚举值。 **取值范围：** STREAM（流式输出）、NON_STREAM（非流式输出）。 **默认取值：** NON_STREAM。

        :param type: The type of this OpsThirdPartyAgentResponseConfig.
        :type type: str
        """
        self._type = type

    @property
    def stream_config(self):
        r"""Gets the stream_config of this OpsThirdPartyAgentResponseConfig.

        :return: The stream_config of this OpsThirdPartyAgentResponseConfig.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentStreamConfig`
        """
        return self._stream_config

    @stream_config.setter
    def stream_config(self, stream_config):
        r"""Sets the stream_config of this OpsThirdPartyAgentResponseConfig.

        :param stream_config: The stream_config of this OpsThirdPartyAgentResponseConfig.
        :type stream_config: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentStreamConfig`
        """
        self._stream_config = stream_config

    @property
    def non_stream_config(self):
        r"""Gets the non_stream_config of this OpsThirdPartyAgentResponseConfig.

        :return: The non_stream_config of this OpsThirdPartyAgentResponseConfig.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentNonStreamConfig`
        """
        return self._non_stream_config

    @non_stream_config.setter
    def non_stream_config(self, non_stream_config):
        r"""Sets the non_stream_config of this OpsThirdPartyAgentResponseConfig.

        :param non_stream_config: The non_stream_config of this OpsThirdPartyAgentResponseConfig.
        :type non_stream_config: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentNonStreamConfig`
        """
        self._non_stream_config = non_stream_config

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
        if not isinstance(other, OpsThirdPartyAgentResponseConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
