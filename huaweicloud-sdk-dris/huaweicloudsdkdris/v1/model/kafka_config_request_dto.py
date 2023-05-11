# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KafkaConfigRequestDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic_prefix': 'str',
        'user_topics': 'list[str]',
        'brokers': 'list[str]',
        'username': 'str',
        'password': 'str'
    }

    attribute_map = {
        'topic_prefix': 'topic_prefix',
        'user_topics': 'user_topics',
        'brokers': 'brokers',
        'username': 'username',
        'password': 'password'
    }

    def __init__(self, topic_prefix=None, user_topics=None, brokers=None, username=None, password=None):
        """KafkaConfigRequestDTO

        The model defined in huaweicloud sdk

        :param topic_prefix: **参数说明**：Topic前缀，不携带时以user_topics中具体Topic为准，携带时前缀将拼接在user_topics中的topic前方，例如：topic_prefixv2x-v1-tracks，topic_prefixv2x-v1-bsm。
        :type topic_prefix: str
        :param user_topics: **参数说明**：kafka的主题列表，根据需要转发的消息类型填写。  **取值范围**：  - v2x-v1-tracks：edge上报的车辆轨迹数据  - v2x-v1-bsm：车载T-BOX，mqtt协议接入rsu， websocket协议接入rsu上报的BSM消息数据  - v2x-v1-rsi：mqtt协议接入rsu，edge上报的RSI消息数据  - v2x-v1-rsm： mqtt协议接入rsu，edge上报的RSM消息数据  - v2x-v1-spat：mqtt协议接入rsu， websocket协议接入rsu上报的SPAT消息数据  - v2x-v1-edge-flow：edge上报的车流量统计信息数据
        :type user_topics: list[str]
        :param brokers: **参数说明**：Kafka broker列表。
        :type brokers: list[str]
        :param username: **参数说明**：kafka用户名。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type username: str
        :param password: **参数说明**：kafka密码。
        :type password: str
        """
        
        

        self._topic_prefix = None
        self._user_topics = None
        self._brokers = None
        self._username = None
        self._password = None
        self.discriminator = None

        if topic_prefix is not None:
            self.topic_prefix = topic_prefix
        if user_topics is not None:
            self.user_topics = user_topics
        self.brokers = brokers
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password

    @property
    def topic_prefix(self):
        """Gets the topic_prefix of this KafkaConfigRequestDTO.

        **参数说明**：Topic前缀，不携带时以user_topics中具体Topic为准，携带时前缀将拼接在user_topics中的topic前方，例如：topic_prefixv2x-v1-tracks，topic_prefixv2x-v1-bsm。

        :return: The topic_prefix of this KafkaConfigRequestDTO.
        :rtype: str
        """
        return self._topic_prefix

    @topic_prefix.setter
    def topic_prefix(self, topic_prefix):
        """Sets the topic_prefix of this KafkaConfigRequestDTO.

        **参数说明**：Topic前缀，不携带时以user_topics中具体Topic为准，携带时前缀将拼接在user_topics中的topic前方，例如：topic_prefixv2x-v1-tracks，topic_prefixv2x-v1-bsm。

        :param topic_prefix: The topic_prefix of this KafkaConfigRequestDTO.
        :type topic_prefix: str
        """
        self._topic_prefix = topic_prefix

    @property
    def user_topics(self):
        """Gets the user_topics of this KafkaConfigRequestDTO.

        **参数说明**：kafka的主题列表，根据需要转发的消息类型填写。  **取值范围**：  - v2x-v1-tracks：edge上报的车辆轨迹数据  - v2x-v1-bsm：车载T-BOX，mqtt协议接入rsu， websocket协议接入rsu上报的BSM消息数据  - v2x-v1-rsi：mqtt协议接入rsu，edge上报的RSI消息数据  - v2x-v1-rsm： mqtt协议接入rsu，edge上报的RSM消息数据  - v2x-v1-spat：mqtt协议接入rsu， websocket协议接入rsu上报的SPAT消息数据  - v2x-v1-edge-flow：edge上报的车流量统计信息数据

        :return: The user_topics of this KafkaConfigRequestDTO.
        :rtype: list[str]
        """
        return self._user_topics

    @user_topics.setter
    def user_topics(self, user_topics):
        """Sets the user_topics of this KafkaConfigRequestDTO.

        **参数说明**：kafka的主题列表，根据需要转发的消息类型填写。  **取值范围**：  - v2x-v1-tracks：edge上报的车辆轨迹数据  - v2x-v1-bsm：车载T-BOX，mqtt协议接入rsu， websocket协议接入rsu上报的BSM消息数据  - v2x-v1-rsi：mqtt协议接入rsu，edge上报的RSI消息数据  - v2x-v1-rsm： mqtt协议接入rsu，edge上报的RSM消息数据  - v2x-v1-spat：mqtt协议接入rsu， websocket协议接入rsu上报的SPAT消息数据  - v2x-v1-edge-flow：edge上报的车流量统计信息数据

        :param user_topics: The user_topics of this KafkaConfigRequestDTO.
        :type user_topics: list[str]
        """
        self._user_topics = user_topics

    @property
    def brokers(self):
        """Gets the brokers of this KafkaConfigRequestDTO.

        **参数说明**：Kafka broker列表。

        :return: The brokers of this KafkaConfigRequestDTO.
        :rtype: list[str]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        """Sets the brokers of this KafkaConfigRequestDTO.

        **参数说明**：Kafka broker列表。

        :param brokers: The brokers of this KafkaConfigRequestDTO.
        :type brokers: list[str]
        """
        self._brokers = brokers

    @property
    def username(self):
        """Gets the username of this KafkaConfigRequestDTO.

        **参数说明**：kafka用户名。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The username of this KafkaConfigRequestDTO.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this KafkaConfigRequestDTO.

        **参数说明**：kafka用户名。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param username: The username of this KafkaConfigRequestDTO.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        """Gets the password of this KafkaConfigRequestDTO.

        **参数说明**：kafka密码。

        :return: The password of this KafkaConfigRequestDTO.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this KafkaConfigRequestDTO.

        **参数说明**：kafka密码。

        :param password: The password of this KafkaConfigRequestDTO.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, KafkaConfigRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
