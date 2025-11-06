# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubTemplateResBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_type': 'str',
        'content': 'str',
        'topic': 'str',
        'send_type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'sub_type': 'sub_type',
        'content': 'content',
        'topic': 'topic',
        'send_type': 'sendType',
        'version': 'version'
    }

    def __init__(self, sub_type=None, content=None, topic=None, send_type=None, version=None):
        r"""SubTemplateResBody

        The model defined in huaweicloud sdk

        :param sub_type: **参数解释：**  消息模板的通知渠道。 **取值范围：**  - sms - dingding - wechat - webhook - email - voice - feishu - welink
        :type sub_type: str
        :param content: **参数解释：**  对应通知渠道的消息模板正文，$符号后所跟变量仅支持以下变量，根据不同告警类型（关键词告警和sql告警），所支持的变量亦不相同。目前两种告警类型有共同变量如下： 告警级别：${event_severity}; 发生时间：${starts_at}; 告警源：$event.metadata.resource_provider; 资源类型：$event.metadata.resource_type; 资源标识：${resources}; 统计类型：关键词统计; 表达式：$event.annotations.condition_expression; 当前值: $event.annotations.current_value; 统计周期：$event.annotations.frequency; 关键词告警特有变量： 查询时间：$event.annotations.results[0].time; 查询日志：$event.annotations.results[0].raw_results; sql告警特有变量： 日志组/流名称：$event.annotations.results[0].resource_id; 查询语句：$event.annotations.results[0].sql; 查询时间：$event.annotations.results[0].time; 查询URL：$event.annotations.results[0].url; 查询日志：$event.annotations.results[0].raw_results;  告警级别：${event_severity}; 发生时间：${starts_at}; 告警源：$event.metadata.resource_provider; 资源类型：$event.metadata.resource_type; 资源标识：${resources}; 统计类型：关键词统计; 表达式：$event.annotations.condition_expression; 当前值: $event.annotations.current_value; 统计周期：$event.annotations.frequency; 关键词告警特有变量： 查询时间：$event.annotations.results[0].time; 查询日志：$event.annotations.results[0].raw_results; sql告警特有变量： 日志组/流名称：$event.annotations.results[0].resource_id; 查询语句：$event.annotations.results[0].sql; 查询时间：$event.annotations.results[0].time; 查询URL：$event.annotations.results[0].url; 查询日志：$event.annotations.results[0].raw_results;   &gt;变量后面的分号\&quot;;\&quot;为英文符号，必须添加，否则模板会出现替换失败的情况。  **取值范围：**  不涉及。
        :type content: str
        :param topic: **参数解释：**  邮件主题。通知渠道为邮件时生效，即sub_type&#x3D;email。 **取值范围：**  不涉及。
        :type topic: str
        :param send_type: **参数解释：**  当消息模板类型为webhook时生效，决定该消息的渲染方式。 **取值范围：**  - HTML - JSON
        :type send_type: str
        :param version: **参数解释：**  消息模板的适用版本。 **取值范围：**   v1：标识为LTS的消息模板。
        :type version: str
        """
        
        

        self._sub_type = None
        self._content = None
        self._topic = None
        self._send_type = None
        self._version = None
        self.discriminator = None

        if sub_type is not None:
            self.sub_type = sub_type
        if content is not None:
            self.content = content
        if topic is not None:
            self.topic = topic
        if send_type is not None:
            self.send_type = send_type
        if version is not None:
            self.version = version

    @property
    def sub_type(self):
        r"""Gets the sub_type of this SubTemplateResBody.

        **参数解释：**  消息模板的通知渠道。 **取值范围：**  - sms - dingding - wechat - webhook - email - voice - feishu - welink

        :return: The sub_type of this SubTemplateResBody.
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        r"""Sets the sub_type of this SubTemplateResBody.

        **参数解释：**  消息模板的通知渠道。 **取值范围：**  - sms - dingding - wechat - webhook - email - voice - feishu - welink

        :param sub_type: The sub_type of this SubTemplateResBody.
        :type sub_type: str
        """
        self._sub_type = sub_type

    @property
    def content(self):
        r"""Gets the content of this SubTemplateResBody.

        **参数解释：**  对应通知渠道的消息模板正文，$符号后所跟变量仅支持以下变量，根据不同告警类型（关键词告警和sql告警），所支持的变量亦不相同。目前两种告警类型有共同变量如下： 告警级别：${event_severity}; 发生时间：${starts_at}; 告警源：$event.metadata.resource_provider; 资源类型：$event.metadata.resource_type; 资源标识：${resources}; 统计类型：关键词统计; 表达式：$event.annotations.condition_expression; 当前值: $event.annotations.current_value; 统计周期：$event.annotations.frequency; 关键词告警特有变量： 查询时间：$event.annotations.results[0].time; 查询日志：$event.annotations.results[0].raw_results; sql告警特有变量： 日志组/流名称：$event.annotations.results[0].resource_id; 查询语句：$event.annotations.results[0].sql; 查询时间：$event.annotations.results[0].time; 查询URL：$event.annotations.results[0].url; 查询日志：$event.annotations.results[0].raw_results;  告警级别：${event_severity}; 发生时间：${starts_at}; 告警源：$event.metadata.resource_provider; 资源类型：$event.metadata.resource_type; 资源标识：${resources}; 统计类型：关键词统计; 表达式：$event.annotations.condition_expression; 当前值: $event.annotations.current_value; 统计周期：$event.annotations.frequency; 关键词告警特有变量： 查询时间：$event.annotations.results[0].time; 查询日志：$event.annotations.results[0].raw_results; sql告警特有变量： 日志组/流名称：$event.annotations.results[0].resource_id; 查询语句：$event.annotations.results[0].sql; 查询时间：$event.annotations.results[0].time; 查询URL：$event.annotations.results[0].url; 查询日志：$event.annotations.results[0].raw_results;   >变量后面的分号\";\"为英文符号，必须添加，否则模板会出现替换失败的情况。  **取值范围：**  不涉及。

        :return: The content of this SubTemplateResBody.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this SubTemplateResBody.

        **参数解释：**  对应通知渠道的消息模板正文，$符号后所跟变量仅支持以下变量，根据不同告警类型（关键词告警和sql告警），所支持的变量亦不相同。目前两种告警类型有共同变量如下： 告警级别：${event_severity}; 发生时间：${starts_at}; 告警源：$event.metadata.resource_provider; 资源类型：$event.metadata.resource_type; 资源标识：${resources}; 统计类型：关键词统计; 表达式：$event.annotations.condition_expression; 当前值: $event.annotations.current_value; 统计周期：$event.annotations.frequency; 关键词告警特有变量： 查询时间：$event.annotations.results[0].time; 查询日志：$event.annotations.results[0].raw_results; sql告警特有变量： 日志组/流名称：$event.annotations.results[0].resource_id; 查询语句：$event.annotations.results[0].sql; 查询时间：$event.annotations.results[0].time; 查询URL：$event.annotations.results[0].url; 查询日志：$event.annotations.results[0].raw_results;  告警级别：${event_severity}; 发生时间：${starts_at}; 告警源：$event.metadata.resource_provider; 资源类型：$event.metadata.resource_type; 资源标识：${resources}; 统计类型：关键词统计; 表达式：$event.annotations.condition_expression; 当前值: $event.annotations.current_value; 统计周期：$event.annotations.frequency; 关键词告警特有变量： 查询时间：$event.annotations.results[0].time; 查询日志：$event.annotations.results[0].raw_results; sql告警特有变量： 日志组/流名称：$event.annotations.results[0].resource_id; 查询语句：$event.annotations.results[0].sql; 查询时间：$event.annotations.results[0].time; 查询URL：$event.annotations.results[0].url; 查询日志：$event.annotations.results[0].raw_results;   >变量后面的分号\";\"为英文符号，必须添加，否则模板会出现替换失败的情况。  **取值范围：**  不涉及。

        :param content: The content of this SubTemplateResBody.
        :type content: str
        """
        self._content = content

    @property
    def topic(self):
        r"""Gets the topic of this SubTemplateResBody.

        **参数解释：**  邮件主题。通知渠道为邮件时生效，即sub_type=email。 **取值范围：**  不涉及。

        :return: The topic of this SubTemplateResBody.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this SubTemplateResBody.

        **参数解释：**  邮件主题。通知渠道为邮件时生效，即sub_type=email。 **取值范围：**  不涉及。

        :param topic: The topic of this SubTemplateResBody.
        :type topic: str
        """
        self._topic = topic

    @property
    def send_type(self):
        r"""Gets the send_type of this SubTemplateResBody.

        **参数解释：**  当消息模板类型为webhook时生效，决定该消息的渲染方式。 **取值范围：**  - HTML - JSON

        :return: The send_type of this SubTemplateResBody.
        :rtype: str
        """
        return self._send_type

    @send_type.setter
    def send_type(self, send_type):
        r"""Sets the send_type of this SubTemplateResBody.

        **参数解释：**  当消息模板类型为webhook时生效，决定该消息的渲染方式。 **取值范围：**  - HTML - JSON

        :param send_type: The send_type of this SubTemplateResBody.
        :type send_type: str
        """
        self._send_type = send_type

    @property
    def version(self):
        r"""Gets the version of this SubTemplateResBody.

        **参数解释：**  消息模板的适用版本。 **取值范围：**   v1：标识为LTS的消息模板。

        :return: The version of this SubTemplateResBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this SubTemplateResBody.

        **参数解释：**  消息模板的适用版本。 **取值范围：**   v1：标识为LTS的消息模板。

        :param version: The version of this SubTemplateResBody.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, SubTemplateResBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
