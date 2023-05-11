# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MrsKafkaConfigRequestDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_topics': 'list[str]',
        'brokers': 'list[str]',
        'username': 'str',
        'authentication': 'bool',
        'krb5_content': 'str',
        'keytab_content': 'str'
    }

    attribute_map = {
        'user_topics': 'user_topics',
        'brokers': 'brokers',
        'username': 'username',
        'authentication': 'authentication',
        'krb5_content': 'krb5_content',
        'keytab_content': 'keytab_content'
    }

    def __init__(self, user_topics=None, brokers=None, username=None, authentication=None, krb5_content=None, keytab_content=None):
        """MrsKafkaConfigRequestDTO

        The model defined in huaweicloud sdk

        :param user_topics: **参数说明**：mrskafka的主题列表，根据需要转发的消息类型填写。  **取值范围**：  - v2x-v1-tracks：edge上报的车辆轨迹数据  - v2x-v1-bsm：车载T-BOX，mqtt协议接入rsu， websocket协议接入rsu上报的BSM消息数据  - v2x-v1-rsi：mqtt协议接入rsu，edge上报的RSI消息数据  - v2x-v1-rsm： mqtt协议接入rsu，edge上报的RSM消息数据  - v2x-v1-spat：mqtt协议接入rsu， websocket协议接入rsu上报的SPAT消息数据  - v2x-v1-edge-flow：edge上报的车流量统计信息数据
        :type user_topics: list[str]
        :param brokers: **参数说明**：mrsKafka broker列表。
        :type brokers: list[str]
        :param username: **参数说明**：mrskafka用户名，若开启安全认证该参数必填。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type username: str
        :param authentication: **参数说明**：是否开启kerberos安全认证的开关。若开启安全认证则需要先上传kerberos安全认证的凭证。
        :type authentication: bool
        :param krb5_content: **参数说明**：若开启安全认证则需要先上传kerberos安全认证的krb5_file的凭证内容。
        :type krb5_content: str
        :param keytab_content: **参数说明**：若开启安全认证则需要先上传kerberos安全认证的keytab_file的凭证内容。
        :type keytab_content: str
        """
        
        

        self._user_topics = None
        self._brokers = None
        self._username = None
        self._authentication = None
        self._krb5_content = None
        self._keytab_content = None
        self.discriminator = None

        if user_topics is not None:
            self.user_topics = user_topics
        self.brokers = brokers
        if username is not None:
            self.username = username
        if authentication is not None:
            self.authentication = authentication
        if krb5_content is not None:
            self.krb5_content = krb5_content
        if keytab_content is not None:
            self.keytab_content = keytab_content

    @property
    def user_topics(self):
        """Gets the user_topics of this MrsKafkaConfigRequestDTO.

        **参数说明**：mrskafka的主题列表，根据需要转发的消息类型填写。  **取值范围**：  - v2x-v1-tracks：edge上报的车辆轨迹数据  - v2x-v1-bsm：车载T-BOX，mqtt协议接入rsu， websocket协议接入rsu上报的BSM消息数据  - v2x-v1-rsi：mqtt协议接入rsu，edge上报的RSI消息数据  - v2x-v1-rsm： mqtt协议接入rsu，edge上报的RSM消息数据  - v2x-v1-spat：mqtt协议接入rsu， websocket协议接入rsu上报的SPAT消息数据  - v2x-v1-edge-flow：edge上报的车流量统计信息数据

        :return: The user_topics of this MrsKafkaConfigRequestDTO.
        :rtype: list[str]
        """
        return self._user_topics

    @user_topics.setter
    def user_topics(self, user_topics):
        """Sets the user_topics of this MrsKafkaConfigRequestDTO.

        **参数说明**：mrskafka的主题列表，根据需要转发的消息类型填写。  **取值范围**：  - v2x-v1-tracks：edge上报的车辆轨迹数据  - v2x-v1-bsm：车载T-BOX，mqtt协议接入rsu， websocket协议接入rsu上报的BSM消息数据  - v2x-v1-rsi：mqtt协议接入rsu，edge上报的RSI消息数据  - v2x-v1-rsm： mqtt协议接入rsu，edge上报的RSM消息数据  - v2x-v1-spat：mqtt协议接入rsu， websocket协议接入rsu上报的SPAT消息数据  - v2x-v1-edge-flow：edge上报的车流量统计信息数据

        :param user_topics: The user_topics of this MrsKafkaConfigRequestDTO.
        :type user_topics: list[str]
        """
        self._user_topics = user_topics

    @property
    def brokers(self):
        """Gets the brokers of this MrsKafkaConfigRequestDTO.

        **参数说明**：mrsKafka broker列表。

        :return: The brokers of this MrsKafkaConfigRequestDTO.
        :rtype: list[str]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        """Sets the brokers of this MrsKafkaConfigRequestDTO.

        **参数说明**：mrsKafka broker列表。

        :param brokers: The brokers of this MrsKafkaConfigRequestDTO.
        :type brokers: list[str]
        """
        self._brokers = brokers

    @property
    def username(self):
        """Gets the username of this MrsKafkaConfigRequestDTO.

        **参数说明**：mrskafka用户名，若开启安全认证该参数必填。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The username of this MrsKafkaConfigRequestDTO.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this MrsKafkaConfigRequestDTO.

        **参数说明**：mrskafka用户名，若开启安全认证该参数必填。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param username: The username of this MrsKafkaConfigRequestDTO.
        :type username: str
        """
        self._username = username

    @property
    def authentication(self):
        """Gets the authentication of this MrsKafkaConfigRequestDTO.

        **参数说明**：是否开启kerberos安全认证的开关。若开启安全认证则需要先上传kerberos安全认证的凭证。

        :return: The authentication of this MrsKafkaConfigRequestDTO.
        :rtype: bool
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this MrsKafkaConfigRequestDTO.

        **参数说明**：是否开启kerberos安全认证的开关。若开启安全认证则需要先上传kerberos安全认证的凭证。

        :param authentication: The authentication of this MrsKafkaConfigRequestDTO.
        :type authentication: bool
        """
        self._authentication = authentication

    @property
    def krb5_content(self):
        """Gets the krb5_content of this MrsKafkaConfigRequestDTO.

        **参数说明**：若开启安全认证则需要先上传kerberos安全认证的krb5_file的凭证内容。

        :return: The krb5_content of this MrsKafkaConfigRequestDTO.
        :rtype: str
        """
        return self._krb5_content

    @krb5_content.setter
    def krb5_content(self, krb5_content):
        """Sets the krb5_content of this MrsKafkaConfigRequestDTO.

        **参数说明**：若开启安全认证则需要先上传kerberos安全认证的krb5_file的凭证内容。

        :param krb5_content: The krb5_content of this MrsKafkaConfigRequestDTO.
        :type krb5_content: str
        """
        self._krb5_content = krb5_content

    @property
    def keytab_content(self):
        """Gets the keytab_content of this MrsKafkaConfigRequestDTO.

        **参数说明**：若开启安全认证则需要先上传kerberos安全认证的keytab_file的凭证内容。

        :return: The keytab_content of this MrsKafkaConfigRequestDTO.
        :rtype: str
        """
        return self._keytab_content

    @keytab_content.setter
    def keytab_content(self, keytab_content):
        """Sets the keytab_content of this MrsKafkaConfigRequestDTO.

        **参数说明**：若开启安全认证则需要先上传kerberos安全认证的keytab_file的凭证内容。

        :param keytab_content: The keytab_content of this MrsKafkaConfigRequestDTO.
        :type keytab_content: str
        """
        self._keytab_content = keytab_content

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
        if not isinstance(other, MrsKafkaConfigRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
