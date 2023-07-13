# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRuleActionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_id': 'str',
        'rule_id': 'str',
        'app_id': 'str',
        'channel': 'str',
        'channel_detail': 'ChannelDetail'
    }

    attribute_map = {
        'action_id': 'action_id',
        'rule_id': 'rule_id',
        'app_id': 'app_id',
        'channel': 'channel',
        'channel_detail': 'channel_detail'
    }

    def __init__(self, action_id=None, rule_id=None, app_id=None, channel=None, channel_detail=None):
        """ShowRuleActionResponse

        The model defined in huaweicloud sdk

        :param action_id: 规则动作ID，用于唯一标识一条规则动作，在创建规则动作时由物联网平台分配获得，创建时无需携带，由平台统一分配唯一的action_id。
        :type action_id: str
        :param rule_id: 规则动作对应的的规则触发条件ID。
        :type rule_id: str
        :param app_id: 资源空间ID。
        :type app_id: str
        :param channel: 规则动作的类型，取值范围： - HTTP_FORWARDING：HTTP服务消息类型。 - DIS_FORWARDING：转发DIS服务消息类型。 - OBS_FORWARDING：转发OBS服务消息类型。 - AMQP_FORWARDING：转发AMQP服务消息类型。 - DMS_KAFKA_FORWARDING：转发kafka消息类型。 [- ROMA_FORWARDING: 转发Roma消息类型。（仅企业版支持）](tag:hws) - INFLUXDB_FORWARDING：转发InfluxDB消息类型。[（仅标准版和企业版支持）](tag:hws) - MYSQL_FORWARDING：转发MySQL消息类型。[（仅标准版和企业版支持）](tag:hws) - FUNCTIONGRAPH_FORWARDING：转发FunctionGraph消息类型。[（仅标准版和企业版支持）](tag:hws) [- MRS_KAFKA_FORWARDING：转发MRS_KAFKA消息类型。（仅企业版支持）](tag:hws) [- DMS_ROCKETMQ_FORWARDING：转发RocketMQ消息类型。（仅标准版和企业版支持）](tag:hws)
        :type channel: str
        :param channel_detail: 
        :type channel_detail: :class:`huaweicloudsdkiotda.v5.ChannelDetail`
        """
        
        super(ShowRuleActionResponse, self).__init__()

        self._action_id = None
        self._rule_id = None
        self._app_id = None
        self._channel = None
        self._channel_detail = None
        self.discriminator = None

        if action_id is not None:
            self.action_id = action_id
        if rule_id is not None:
            self.rule_id = rule_id
        if app_id is not None:
            self.app_id = app_id
        if channel is not None:
            self.channel = channel
        if channel_detail is not None:
            self.channel_detail = channel_detail

    @property
    def action_id(self):
        """Gets the action_id of this ShowRuleActionResponse.

        规则动作ID，用于唯一标识一条规则动作，在创建规则动作时由物联网平台分配获得，创建时无需携带，由平台统一分配唯一的action_id。

        :return: The action_id of this ShowRuleActionResponse.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this ShowRuleActionResponse.

        规则动作ID，用于唯一标识一条规则动作，在创建规则动作时由物联网平台分配获得，创建时无需携带，由平台统一分配唯一的action_id。

        :param action_id: The action_id of this ShowRuleActionResponse.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def rule_id(self):
        """Gets the rule_id of this ShowRuleActionResponse.

        规则动作对应的的规则触发条件ID。

        :return: The rule_id of this ShowRuleActionResponse.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this ShowRuleActionResponse.

        规则动作对应的的规则触发条件ID。

        :param rule_id: The rule_id of this ShowRuleActionResponse.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def app_id(self):
        """Gets the app_id of this ShowRuleActionResponse.

        资源空间ID。

        :return: The app_id of this ShowRuleActionResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowRuleActionResponse.

        资源空间ID。

        :param app_id: The app_id of this ShowRuleActionResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def channel(self):
        """Gets the channel of this ShowRuleActionResponse.

        规则动作的类型，取值范围： - HTTP_FORWARDING：HTTP服务消息类型。 - DIS_FORWARDING：转发DIS服务消息类型。 - OBS_FORWARDING：转发OBS服务消息类型。 - AMQP_FORWARDING：转发AMQP服务消息类型。 - DMS_KAFKA_FORWARDING：转发kafka消息类型。 [- ROMA_FORWARDING: 转发Roma消息类型。（仅企业版支持）](tag:hws) - INFLUXDB_FORWARDING：转发InfluxDB消息类型。[（仅标准版和企业版支持）](tag:hws) - MYSQL_FORWARDING：转发MySQL消息类型。[（仅标准版和企业版支持）](tag:hws) - FUNCTIONGRAPH_FORWARDING：转发FunctionGraph消息类型。[（仅标准版和企业版支持）](tag:hws) [- MRS_KAFKA_FORWARDING：转发MRS_KAFKA消息类型。（仅企业版支持）](tag:hws) [- DMS_ROCKETMQ_FORWARDING：转发RocketMQ消息类型。（仅标准版和企业版支持）](tag:hws)

        :return: The channel of this ShowRuleActionResponse.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ShowRuleActionResponse.

        规则动作的类型，取值范围： - HTTP_FORWARDING：HTTP服务消息类型。 - DIS_FORWARDING：转发DIS服务消息类型。 - OBS_FORWARDING：转发OBS服务消息类型。 - AMQP_FORWARDING：转发AMQP服务消息类型。 - DMS_KAFKA_FORWARDING：转发kafka消息类型。 [- ROMA_FORWARDING: 转发Roma消息类型。（仅企业版支持）](tag:hws) - INFLUXDB_FORWARDING：转发InfluxDB消息类型。[（仅标准版和企业版支持）](tag:hws) - MYSQL_FORWARDING：转发MySQL消息类型。[（仅标准版和企业版支持）](tag:hws) - FUNCTIONGRAPH_FORWARDING：转发FunctionGraph消息类型。[（仅标准版和企业版支持）](tag:hws) [- MRS_KAFKA_FORWARDING：转发MRS_KAFKA消息类型。（仅企业版支持）](tag:hws) [- DMS_ROCKETMQ_FORWARDING：转发RocketMQ消息类型。（仅标准版和企业版支持）](tag:hws)

        :param channel: The channel of this ShowRuleActionResponse.
        :type channel: str
        """
        self._channel = channel

    @property
    def channel_detail(self):
        """Gets the channel_detail of this ShowRuleActionResponse.

        :return: The channel_detail of this ShowRuleActionResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.ChannelDetail`
        """
        return self._channel_detail

    @channel_detail.setter
    def channel_detail(self, channel_detail):
        """Sets the channel_detail of this ShowRuleActionResponse.

        :param channel_detail: The channel_detail of this ShowRuleActionResponse.
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
        if not isinstance(other, ShowRuleActionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
