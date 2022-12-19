# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MrsKafkaConfigResponseDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kafka_config_id': 'str',
        'kafka_topics': 'list[str]',
        'brokers': 'list[str]',
        'username': 'str',
        'status': 'str',
        'authentication': 'bool',
        'created_time': 'datetime',
        'last_modified_time': 'datetime'
    }

    attribute_map = {
        'kafka_config_id': 'kafka_config_id',
        'kafka_topics': 'kafka_topics',
        'brokers': 'brokers',
        'username': 'username',
        'status': 'status',
        'authentication': 'authentication',
        'created_time': 'created_time',
        'last_modified_time': 'last_modified_time'
    }

    def __init__(self, kafka_config_id=None, kafka_topics=None, brokers=None, username=None, status=None, authentication=None, created_time=None, last_modified_time=None):
        """MrsKafkaConfigResponseDTO

        The model defined in huaweicloud sdk

        :param kafka_config_id: **参数说明**：每一套Kafka配置的唯一ID。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type kafka_config_id: str
        :param kafka_topics: **参数说明**：kafka的主题列表。  **取值范围**：  - v2x-v1-tracks：edge上报的车辆轨迹数据  - v2x-v1-bsm：车载T-BOX，mqtt协议接入rsu， websocket协议接入rsu上报的BSM消息数据  - v2x-v1-rsi：mqtt协议接入rsu，edge上报的RSI消息数据  - v2x-v1-rsm： mqtt协议接入rsu，edge上报的RSM消息数据  - v2x-v1-spat：mqtt协议接入rsu， websocket协议接入rsu上报的SPAT消息数据  - v2x-v1-edge-flow：edge上报的车流量统计信息数据
        :type kafka_topics: list[str]
        :param brokers: **参数说明**：Kafka broker列表。
        :type brokers: list[str]
        :param username: **参数说明**：mrskafka用户名，若开启安全认证该参数必填。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type username: str
        :param status: **参数说明**：一套kafka的连接状态。  **取值范围**：  - OFFLINE：离线  - ONLINE：在线
        :type status: str
        :param authentication: **参数说明**：是否开启kerberos安全认证的开关。若开启安全认证则需要先上传kerberos安全认证的凭证。
        :type authentication: bool
        :param created_time: **参数说明**：创建时间。 格式为yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; 例如：2015-12-12T12:12:12Z
        :type created_time: datetime
        :param last_modified_time: **参数说明**：修改时间。 格式为yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; 例如：2015-12-12T12:12:12Z
        :type last_modified_time: datetime
        """
        
        

        self._kafka_config_id = None
        self._kafka_topics = None
        self._brokers = None
        self._username = None
        self._status = None
        self._authentication = None
        self._created_time = None
        self._last_modified_time = None
        self.discriminator = None

        if kafka_config_id is not None:
            self.kafka_config_id = kafka_config_id
        if kafka_topics is not None:
            self.kafka_topics = kafka_topics
        if brokers is not None:
            self.brokers = brokers
        if username is not None:
            self.username = username
        if status is not None:
            self.status = status
        if authentication is not None:
            self.authentication = authentication
        if created_time is not None:
            self.created_time = created_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time

    @property
    def kafka_config_id(self):
        """Gets the kafka_config_id of this MrsKafkaConfigResponseDTO.

        **参数说明**：每一套Kafka配置的唯一ID。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The kafka_config_id of this MrsKafkaConfigResponseDTO.
        :rtype: str
        """
        return self._kafka_config_id

    @kafka_config_id.setter
    def kafka_config_id(self, kafka_config_id):
        """Sets the kafka_config_id of this MrsKafkaConfigResponseDTO.

        **参数说明**：每一套Kafka配置的唯一ID。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param kafka_config_id: The kafka_config_id of this MrsKafkaConfigResponseDTO.
        :type kafka_config_id: str
        """
        self._kafka_config_id = kafka_config_id

    @property
    def kafka_topics(self):
        """Gets the kafka_topics of this MrsKafkaConfigResponseDTO.

        **参数说明**：kafka的主题列表。  **取值范围**：  - v2x-v1-tracks：edge上报的车辆轨迹数据  - v2x-v1-bsm：车载T-BOX，mqtt协议接入rsu， websocket协议接入rsu上报的BSM消息数据  - v2x-v1-rsi：mqtt协议接入rsu，edge上报的RSI消息数据  - v2x-v1-rsm： mqtt协议接入rsu，edge上报的RSM消息数据  - v2x-v1-spat：mqtt协议接入rsu， websocket协议接入rsu上报的SPAT消息数据  - v2x-v1-edge-flow：edge上报的车流量统计信息数据

        :return: The kafka_topics of this MrsKafkaConfigResponseDTO.
        :rtype: list[str]
        """
        return self._kafka_topics

    @kafka_topics.setter
    def kafka_topics(self, kafka_topics):
        """Sets the kafka_topics of this MrsKafkaConfigResponseDTO.

        **参数说明**：kafka的主题列表。  **取值范围**：  - v2x-v1-tracks：edge上报的车辆轨迹数据  - v2x-v1-bsm：车载T-BOX，mqtt协议接入rsu， websocket协议接入rsu上报的BSM消息数据  - v2x-v1-rsi：mqtt协议接入rsu，edge上报的RSI消息数据  - v2x-v1-rsm： mqtt协议接入rsu，edge上报的RSM消息数据  - v2x-v1-spat：mqtt协议接入rsu， websocket协议接入rsu上报的SPAT消息数据  - v2x-v1-edge-flow：edge上报的车流量统计信息数据

        :param kafka_topics: The kafka_topics of this MrsKafkaConfigResponseDTO.
        :type kafka_topics: list[str]
        """
        self._kafka_topics = kafka_topics

    @property
    def brokers(self):
        """Gets the brokers of this MrsKafkaConfigResponseDTO.

        **参数说明**：Kafka broker列表。

        :return: The brokers of this MrsKafkaConfigResponseDTO.
        :rtype: list[str]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        """Sets the brokers of this MrsKafkaConfigResponseDTO.

        **参数说明**：Kafka broker列表。

        :param brokers: The brokers of this MrsKafkaConfigResponseDTO.
        :type brokers: list[str]
        """
        self._brokers = brokers

    @property
    def username(self):
        """Gets the username of this MrsKafkaConfigResponseDTO.

        **参数说明**：mrskafka用户名，若开启安全认证该参数必填。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The username of this MrsKafkaConfigResponseDTO.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this MrsKafkaConfigResponseDTO.

        **参数说明**：mrskafka用户名，若开启安全认证该参数必填。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param username: The username of this MrsKafkaConfigResponseDTO.
        :type username: str
        """
        self._username = username

    @property
    def status(self):
        """Gets the status of this MrsKafkaConfigResponseDTO.

        **参数说明**：一套kafka的连接状态。  **取值范围**：  - OFFLINE：离线  - ONLINE：在线

        :return: The status of this MrsKafkaConfigResponseDTO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MrsKafkaConfigResponseDTO.

        **参数说明**：一套kafka的连接状态。  **取值范围**：  - OFFLINE：离线  - ONLINE：在线

        :param status: The status of this MrsKafkaConfigResponseDTO.
        :type status: str
        """
        self._status = status

    @property
    def authentication(self):
        """Gets the authentication of this MrsKafkaConfigResponseDTO.

        **参数说明**：是否开启kerberos安全认证的开关。若开启安全认证则需要先上传kerberos安全认证的凭证。

        :return: The authentication of this MrsKafkaConfigResponseDTO.
        :rtype: bool
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this MrsKafkaConfigResponseDTO.

        **参数说明**：是否开启kerberos安全认证的开关。若开启安全认证则需要先上传kerberos安全认证的凭证。

        :param authentication: The authentication of this MrsKafkaConfigResponseDTO.
        :type authentication: bool
        """
        self._authentication = authentication

    @property
    def created_time(self):
        """Gets the created_time of this MrsKafkaConfigResponseDTO.

        **参数说明**：创建时间。 格式为yyyy-MM-dd'T'HH:mm:ss'Z' 例如：2015-12-12T12:12:12Z

        :return: The created_time of this MrsKafkaConfigResponseDTO.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this MrsKafkaConfigResponseDTO.

        **参数说明**：创建时间。 格式为yyyy-MM-dd'T'HH:mm:ss'Z' 例如：2015-12-12T12:12:12Z

        :param created_time: The created_time of this MrsKafkaConfigResponseDTO.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this MrsKafkaConfigResponseDTO.

        **参数说明**：修改时间。 格式为yyyy-MM-dd'T'HH:mm:ss'Z' 例如：2015-12-12T12:12:12Z

        :return: The last_modified_time of this MrsKafkaConfigResponseDTO.
        :rtype: datetime
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this MrsKafkaConfigResponseDTO.

        **参数说明**：修改时间。 格式为yyyy-MM-dd'T'HH:mm:ss'Z' 例如：2015-12-12T12:12:12Z

        :param last_modified_time: The last_modified_time of this MrsKafkaConfigResponseDTO.
        :type last_modified_time: datetime
        """
        self._last_modified_time = last_modified_time

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
        if not isinstance(other, MrsKafkaConfigResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
