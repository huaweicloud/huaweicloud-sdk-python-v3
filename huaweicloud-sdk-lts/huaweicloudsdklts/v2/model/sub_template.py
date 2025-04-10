# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubTemplate:

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
        'topic': 'str'
    }

    attribute_map = {
        'sub_type': 'sub_type',
        'content': 'content',
        'topic': 'topic'
    }

    def __init__(self, sub_type=None, content=None, topic=None):
        r"""SubTemplate

        The model defined in huaweicloud sdk

        :param sub_type: 模板子类型，只支持以下5种类型：sms,dingding,wechat,webhook,email
        :type sub_type: str
        :param content: 子模版正文，$符号后所跟变量仅支持以下变量，根据不同告警类型（关键词告警和sql告警），所支持的变量亦不相同。 目前两种告警类型有共同变量如下：告警级别：${event_severity};发生时间：${starts_at};告警源：$event.metadata.resource_provider;资源类型：$event.metadata.resource_type;资源标识：${resources};统计类型：关键词统计;表达式：$event.annotations.condition_expression;当前值: $event.annotations.current_value;统计周期：$event.annotations.frequency; 关键词告警特有变量：查询时间：$event.annotations.results[0].time;查询日志：$event.annotations.results[0].raw_results; sql告警特有变量：日志组/流名称：$event.annotations.results[0].resource_id;查询语句：$event.annotations.results[0].sql;查询时间：$event.annotations.results[0].time;查询URL：$event.annotations.results[0].url;查询日志：$event.annotations.results[0].raw_results; 变量后面的分号\&quot;;\&quot;为英文符号，必须添加，否则模板会出现替换失败的情况
        :type content: str
        :param topic: 邮件主题,只有sub_type&#x3D;email时生效
        :type topic: str
        """
        
        

        self._sub_type = None
        self._content = None
        self._topic = None
        self.discriminator = None

        self.sub_type = sub_type
        self.content = content
        if topic is not None:
            self.topic = topic

    @property
    def sub_type(self):
        r"""Gets the sub_type of this SubTemplate.

        模板子类型，只支持以下5种类型：sms,dingding,wechat,webhook,email

        :return: The sub_type of this SubTemplate.
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        r"""Sets the sub_type of this SubTemplate.

        模板子类型，只支持以下5种类型：sms,dingding,wechat,webhook,email

        :param sub_type: The sub_type of this SubTemplate.
        :type sub_type: str
        """
        self._sub_type = sub_type

    @property
    def content(self):
        r"""Gets the content of this SubTemplate.

        子模版正文，$符号后所跟变量仅支持以下变量，根据不同告警类型（关键词告警和sql告警），所支持的变量亦不相同。 目前两种告警类型有共同变量如下：告警级别：${event_severity};发生时间：${starts_at};告警源：$event.metadata.resource_provider;资源类型：$event.metadata.resource_type;资源标识：${resources};统计类型：关键词统计;表达式：$event.annotations.condition_expression;当前值: $event.annotations.current_value;统计周期：$event.annotations.frequency; 关键词告警特有变量：查询时间：$event.annotations.results[0].time;查询日志：$event.annotations.results[0].raw_results; sql告警特有变量：日志组/流名称：$event.annotations.results[0].resource_id;查询语句：$event.annotations.results[0].sql;查询时间：$event.annotations.results[0].time;查询URL：$event.annotations.results[0].url;查询日志：$event.annotations.results[0].raw_results; 变量后面的分号\";\"为英文符号，必须添加，否则模板会出现替换失败的情况

        :return: The content of this SubTemplate.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this SubTemplate.

        子模版正文，$符号后所跟变量仅支持以下变量，根据不同告警类型（关键词告警和sql告警），所支持的变量亦不相同。 目前两种告警类型有共同变量如下：告警级别：${event_severity};发生时间：${starts_at};告警源：$event.metadata.resource_provider;资源类型：$event.metadata.resource_type;资源标识：${resources};统计类型：关键词统计;表达式：$event.annotations.condition_expression;当前值: $event.annotations.current_value;统计周期：$event.annotations.frequency; 关键词告警特有变量：查询时间：$event.annotations.results[0].time;查询日志：$event.annotations.results[0].raw_results; sql告警特有变量：日志组/流名称：$event.annotations.results[0].resource_id;查询语句：$event.annotations.results[0].sql;查询时间：$event.annotations.results[0].time;查询URL：$event.annotations.results[0].url;查询日志：$event.annotations.results[0].raw_results; 变量后面的分号\";\"为英文符号，必须添加，否则模板会出现替换失败的情况

        :param content: The content of this SubTemplate.
        :type content: str
        """
        self._content = content

    @property
    def topic(self):
        r"""Gets the topic of this SubTemplate.

        邮件主题,只有sub_type=email时生效

        :return: The topic of this SubTemplate.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this SubTemplate.

        邮件主题,只有sub_type=email时生效

        :param topic: The topic of this SubTemplate.
        :type topic: str
        """
        self._topic = topic

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
        if not isinstance(other, SubTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
