# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateConsumerGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'broadcast': 'bool',
        'retry_max_time': 'int',
        'enabled': 'bool',
        'consume_orderly': 'bool',
        'group_desc': 'str'
    }

    attribute_map = {
        'name': 'name',
        'broadcast': 'broadcast',
        'retry_max_time': 'retry_max_time',
        'enabled': 'enabled',
        'consume_orderly': 'consume_orderly',
        'group_desc': 'group_desc'
    }

    def __init__(self, name=None, broadcast=None, retry_max_time=None, enabled=None, consume_orderly=None, group_desc=None):
        r"""BatchUpdateConsumerGroup

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 消费组名称。 **约束限制**： 只能由英文字母、数字、百分号、竖线、中划线、下划线组成，长度3~64个字符。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type name: str
        :param broadcast: **参数解释**： 是否设置为广播消费。 **约束限制**： 不涉及。 **取值范围**： - true：使用广播消费。 - false：不使用广播消费。 **默认取值**： 不涉及。
        :type broadcast: bool
        :param retry_max_time: **参数解释**： 最大重试次数。 **约束限制**： 不涉及。 **取值范围**： 1~16。 **默认取值**： 不涉及。
        :type retry_max_time: int
        :param enabled: **参数解释**： 是否可以消费。 **约束限制**： 不涉及。 **取值范围**： - true：可以消费。 - false：不可以消费。 **默认取值**： 不涉及。
        :type enabled: bool
        :param consume_orderly: **参数解释**： 是否按顺序消费（仅RocketMQ实例5.x版本需要填写此参数）。[华为云Stack不支持](tag:hcs,hcs_oemout) **约束限制**： 不涉及。 **取值范围**： - true：顺序消费。 - false：不按顺序消费。 **默认取值**： 不涉及。
        :type consume_orderly: bool
        :param group_desc: **参数解释**： 消费组描述。 **约束限制**： 长度0~200个字符 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type group_desc: str
        """
        
        

        self._name = None
        self._broadcast = None
        self._retry_max_time = None
        self._enabled = None
        self._consume_orderly = None
        self._group_desc = None
        self.discriminator = None

        self.name = name
        if broadcast is not None:
            self.broadcast = broadcast
        if retry_max_time is not None:
            self.retry_max_time = retry_max_time
        if enabled is not None:
            self.enabled = enabled
        if consume_orderly is not None:
            self.consume_orderly = consume_orderly
        if group_desc is not None:
            self.group_desc = group_desc

    @property
    def name(self):
        r"""Gets the name of this BatchUpdateConsumerGroup.

        **参数解释**： 消费组名称。 **约束限制**： 只能由英文字母、数字、百分号、竖线、中划线、下划线组成，长度3~64个字符。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The name of this BatchUpdateConsumerGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchUpdateConsumerGroup.

        **参数解释**： 消费组名称。 **约束限制**： 只能由英文字母、数字、百分号、竖线、中划线、下划线组成，长度3~64个字符。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param name: The name of this BatchUpdateConsumerGroup.
        :type name: str
        """
        self._name = name

    @property
    def broadcast(self):
        r"""Gets the broadcast of this BatchUpdateConsumerGroup.

        **参数解释**： 是否设置为广播消费。 **约束限制**： 不涉及。 **取值范围**： - true：使用广播消费。 - false：不使用广播消费。 **默认取值**： 不涉及。

        :return: The broadcast of this BatchUpdateConsumerGroup.
        :rtype: bool
        """
        return self._broadcast

    @broadcast.setter
    def broadcast(self, broadcast):
        r"""Sets the broadcast of this BatchUpdateConsumerGroup.

        **参数解释**： 是否设置为广播消费。 **约束限制**： 不涉及。 **取值范围**： - true：使用广播消费。 - false：不使用广播消费。 **默认取值**： 不涉及。

        :param broadcast: The broadcast of this BatchUpdateConsumerGroup.
        :type broadcast: bool
        """
        self._broadcast = broadcast

    @property
    def retry_max_time(self):
        r"""Gets the retry_max_time of this BatchUpdateConsumerGroup.

        **参数解释**： 最大重试次数。 **约束限制**： 不涉及。 **取值范围**： 1~16。 **默认取值**： 不涉及。

        :return: The retry_max_time of this BatchUpdateConsumerGroup.
        :rtype: int
        """
        return self._retry_max_time

    @retry_max_time.setter
    def retry_max_time(self, retry_max_time):
        r"""Sets the retry_max_time of this BatchUpdateConsumerGroup.

        **参数解释**： 最大重试次数。 **约束限制**： 不涉及。 **取值范围**： 1~16。 **默认取值**： 不涉及。

        :param retry_max_time: The retry_max_time of this BatchUpdateConsumerGroup.
        :type retry_max_time: int
        """
        self._retry_max_time = retry_max_time

    @property
    def enabled(self):
        r"""Gets the enabled of this BatchUpdateConsumerGroup.

        **参数解释**： 是否可以消费。 **约束限制**： 不涉及。 **取值范围**： - true：可以消费。 - false：不可以消费。 **默认取值**： 不涉及。

        :return: The enabled of this BatchUpdateConsumerGroup.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this BatchUpdateConsumerGroup.

        **参数解释**： 是否可以消费。 **约束限制**： 不涉及。 **取值范围**： - true：可以消费。 - false：不可以消费。 **默认取值**： 不涉及。

        :param enabled: The enabled of this BatchUpdateConsumerGroup.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def consume_orderly(self):
        r"""Gets the consume_orderly of this BatchUpdateConsumerGroup.

        **参数解释**： 是否按顺序消费（仅RocketMQ实例5.x版本需要填写此参数）。[华为云Stack不支持](tag:hcs,hcs_oemout) **约束限制**： 不涉及。 **取值范围**： - true：顺序消费。 - false：不按顺序消费。 **默认取值**： 不涉及。

        :return: The consume_orderly of this BatchUpdateConsumerGroup.
        :rtype: bool
        """
        return self._consume_orderly

    @consume_orderly.setter
    def consume_orderly(self, consume_orderly):
        r"""Sets the consume_orderly of this BatchUpdateConsumerGroup.

        **参数解释**： 是否按顺序消费（仅RocketMQ实例5.x版本需要填写此参数）。[华为云Stack不支持](tag:hcs,hcs_oemout) **约束限制**： 不涉及。 **取值范围**： - true：顺序消费。 - false：不按顺序消费。 **默认取值**： 不涉及。

        :param consume_orderly: The consume_orderly of this BatchUpdateConsumerGroup.
        :type consume_orderly: bool
        """
        self._consume_orderly = consume_orderly

    @property
    def group_desc(self):
        r"""Gets the group_desc of this BatchUpdateConsumerGroup.

        **参数解释**： 消费组描述。 **约束限制**： 长度0~200个字符 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The group_desc of this BatchUpdateConsumerGroup.
        :rtype: str
        """
        return self._group_desc

    @group_desc.setter
    def group_desc(self, group_desc):
        r"""Sets the group_desc of this BatchUpdateConsumerGroup.

        **参数解释**： 消费组描述。 **约束限制**： 长度0~200个字符 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param group_desc: The group_desc of this BatchUpdateConsumerGroup.
        :type group_desc: str
        """
        self._group_desc = group_desc

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
        if not isinstance(other, BatchUpdateConsumerGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
