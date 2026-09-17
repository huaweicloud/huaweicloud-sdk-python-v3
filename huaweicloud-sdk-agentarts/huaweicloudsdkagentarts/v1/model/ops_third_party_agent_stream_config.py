# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsThirdPartyAgentStreamConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_type': 'str',
        'match_condition': 'OpsThirdPartyAgentDataMatchCondition',
        'output_key': 'str',
        'end_condition': 'OpsThirdPartyAgentDataMatchCondition',
        'end_event_type': 'str'
    }

    attribute_map = {
        'event_type': 'event_type',
        'match_condition': 'match_condition',
        'output_key': 'output_key',
        'end_condition': 'end_condition',
        'end_event_type': 'end_event_type'
    }

    def __init__(self, event_type=None, match_condition=None, output_key=None, end_condition=None, end_event_type=None):
        r"""OpsThirdPartyAgentStreamConfig

        The model defined in huaweicloud sdk

        :param event_type: **参数解释：** 需要匹配的SSE事件类型，用于识别Agent输出事件。不填则匹配所有事件类型。 **约束限制：** 最大长度100字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type event_type: str
        :param match_condition: 
        :type match_condition: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentDataMatchCondition`
        :param output_key: **参数解释：** 目标数据中Agent输出内容的字段路径，支持多级路径（如aa.bb.cc）。仅当match_condition匹配成功时，从该条数据中提取output_key对应的值作为Agent输出。 **约束限制：** 最大长度200字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type output_key: str
        :param end_condition: 
        :type end_condition: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentDataMatchCondition`
        :param end_event_type: **参数解释：** 标识流式输出结束的SSE事件类型。不填则仅通过end_condition判断流结束。 **约束限制：** 最大长度100字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type end_event_type: str
        """
        
        

        self._event_type = None
        self._match_condition = None
        self._output_key = None
        self._end_condition = None
        self._end_event_type = None
        self.discriminator = None

        if event_type is not None:
            self.event_type = event_type
        self.match_condition = match_condition
        self.output_key = output_key
        if end_condition is not None:
            self.end_condition = end_condition
        if end_event_type is not None:
            self.end_event_type = end_event_type

    @property
    def event_type(self):
        r"""Gets the event_type of this OpsThirdPartyAgentStreamConfig.

        **参数解释：** 需要匹配的SSE事件类型，用于识别Agent输出事件。不填则匹配所有事件类型。 **约束限制：** 最大长度100字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The event_type of this OpsThirdPartyAgentStreamConfig.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this OpsThirdPartyAgentStreamConfig.

        **参数解释：** 需要匹配的SSE事件类型，用于识别Agent输出事件。不填则匹配所有事件类型。 **约束限制：** 最大长度100字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param event_type: The event_type of this OpsThirdPartyAgentStreamConfig.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def match_condition(self):
        r"""Gets the match_condition of this OpsThirdPartyAgentStreamConfig.

        :return: The match_condition of this OpsThirdPartyAgentStreamConfig.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentDataMatchCondition`
        """
        return self._match_condition

    @match_condition.setter
    def match_condition(self, match_condition):
        r"""Sets the match_condition of this OpsThirdPartyAgentStreamConfig.

        :param match_condition: The match_condition of this OpsThirdPartyAgentStreamConfig.
        :type match_condition: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentDataMatchCondition`
        """
        self._match_condition = match_condition

    @property
    def output_key(self):
        r"""Gets the output_key of this OpsThirdPartyAgentStreamConfig.

        **参数解释：** 目标数据中Agent输出内容的字段路径，支持多级路径（如aa.bb.cc）。仅当match_condition匹配成功时，从该条数据中提取output_key对应的值作为Agent输出。 **约束限制：** 最大长度200字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The output_key of this OpsThirdPartyAgentStreamConfig.
        :rtype: str
        """
        return self._output_key

    @output_key.setter
    def output_key(self, output_key):
        r"""Sets the output_key of this OpsThirdPartyAgentStreamConfig.

        **参数解释：** 目标数据中Agent输出内容的字段路径，支持多级路径（如aa.bb.cc）。仅当match_condition匹配成功时，从该条数据中提取output_key对应的值作为Agent输出。 **约束限制：** 最大长度200字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param output_key: The output_key of this OpsThirdPartyAgentStreamConfig.
        :type output_key: str
        """
        self._output_key = output_key

    @property
    def end_condition(self):
        r"""Gets the end_condition of this OpsThirdPartyAgentStreamConfig.

        :return: The end_condition of this OpsThirdPartyAgentStreamConfig.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentDataMatchCondition`
        """
        return self._end_condition

    @end_condition.setter
    def end_condition(self, end_condition):
        r"""Sets the end_condition of this OpsThirdPartyAgentStreamConfig.

        :param end_condition: The end_condition of this OpsThirdPartyAgentStreamConfig.
        :type end_condition: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentDataMatchCondition`
        """
        self._end_condition = end_condition

    @property
    def end_event_type(self):
        r"""Gets the end_event_type of this OpsThirdPartyAgentStreamConfig.

        **参数解释：** 标识流式输出结束的SSE事件类型。不填则仅通过end_condition判断流结束。 **约束限制：** 最大长度100字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The end_event_type of this OpsThirdPartyAgentStreamConfig.
        :rtype: str
        """
        return self._end_event_type

    @end_event_type.setter
    def end_event_type(self, end_event_type):
        r"""Sets the end_event_type of this OpsThirdPartyAgentStreamConfig.

        **参数解释：** 标识流式输出结束的SSE事件类型。不填则仅通过end_condition判断流结束。 **约束限制：** 最大长度100字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param end_event_type: The end_event_type of this OpsThirdPartyAgentStreamConfig.
        :type end_event_type: str
        """
        self._end_event_type = end_event_type

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
        if not isinstance(other, OpsThirdPartyAgentStreamConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
