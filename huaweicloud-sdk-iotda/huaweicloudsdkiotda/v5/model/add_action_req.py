# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddActionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'channel': 'str',
        'channel_detail': 'ChannelDetail'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'channel': 'channel',
        'channel_detail': 'channel_detail'
    }

    def __init__(self, rule_id=None, channel=None, channel_detail=None):
        """AddActionReq

        The model defined in huaweicloud sdk

        :param rule_id: **参数说明**：规则触发条件ID，用于唯一标识一条规则触发条件，在创建规则时由物联网平台分配获得。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type rule_id: str
        :param channel: **参数说明**：规则动作的类型。 **取值范围**： - HTTP_FORWARDING：HTTP服务消息类型。 - DIS_FORWARDING：转发DIS服务消息类型。 - OBS_FORWARDING：转发OBS服务消息类型。 - AMQP_FORWARDING：转发AMQP服务消息类型。 - DMS_KAFKA_FORWARDING：转发kafka消息类型。
        :type channel: str
        :param channel_detail: 
        :type channel_detail: :class:`huaweicloudsdkiotda.v5.ChannelDetail`
        """
        
        

        self._rule_id = None
        self._channel = None
        self._channel_detail = None
        self.discriminator = None

        self.rule_id = rule_id
        self.channel = channel
        self.channel_detail = channel_detail

    @property
    def rule_id(self):
        """Gets the rule_id of this AddActionReq.

        **参数说明**：规则触发条件ID，用于唯一标识一条规则触发条件，在创建规则时由物联网平台分配获得。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The rule_id of this AddActionReq.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this AddActionReq.

        **参数说明**：规则触发条件ID，用于唯一标识一条规则触发条件，在创建规则时由物联网平台分配获得。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param rule_id: The rule_id of this AddActionReq.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def channel(self):
        """Gets the channel of this AddActionReq.

        **参数说明**：规则动作的类型。 **取值范围**： - HTTP_FORWARDING：HTTP服务消息类型。 - DIS_FORWARDING：转发DIS服务消息类型。 - OBS_FORWARDING：转发OBS服务消息类型。 - AMQP_FORWARDING：转发AMQP服务消息类型。 - DMS_KAFKA_FORWARDING：转发kafka消息类型。

        :return: The channel of this AddActionReq.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this AddActionReq.

        **参数说明**：规则动作的类型。 **取值范围**： - HTTP_FORWARDING：HTTP服务消息类型。 - DIS_FORWARDING：转发DIS服务消息类型。 - OBS_FORWARDING：转发OBS服务消息类型。 - AMQP_FORWARDING：转发AMQP服务消息类型。 - DMS_KAFKA_FORWARDING：转发kafka消息类型。

        :param channel: The channel of this AddActionReq.
        :type channel: str
        """
        self._channel = channel

    @property
    def channel_detail(self):
        """Gets the channel_detail of this AddActionReq.

        :return: The channel_detail of this AddActionReq.
        :rtype: :class:`huaweicloudsdkiotda.v5.ChannelDetail`
        """
        return self._channel_detail

    @channel_detail.setter
    def channel_detail(self, channel_detail):
        """Sets the channel_detail of this AddActionReq.

        :param channel_detail: The channel_detail of this AddActionReq.
        :type channel_detail: :class:`huaweicloudsdkiotda.v5.ChannelDetail`
        """
        self._channel_detail = channel_detail

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
        if not isinstance(other, AddActionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
