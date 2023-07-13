# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DmsKafkaForwarding:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('password')

    openapi_types = {
        'region_name': 'str',
        'project_id': 'str',
        'addresses': 'list[NetAddress]',
        'topic': 'str',
        'username': 'str',
        'password': 'str',
        'mechanism': 'str'
    }

    attribute_map = {
        'region_name': 'region_name',
        'project_id': 'project_id',
        'addresses': 'addresses',
        'topic': 'topic',
        'username': 'username',
        'password': 'password',
        'mechanism': 'mechanism'
    }

    def __init__(self, region_name=None, project_id=None, addresses=None, topic=None, username=None, password=None, mechanism=None):
        """DmsKafkaForwarding

        The model defined in huaweicloud sdk

        :param region_name: **参数说明**：Kafka服务对应的region区域
        :type region_name: str
        :param project_id: **参数说明**：Kafka服务对应的projectId信息
        :type project_id: str
        :param addresses: **参数说明**：转发kafka消息对应的地址列表
        :type addresses: list[:class:`huaweicloudsdkiotda.v5.NetAddress`]
        :param topic: **参数说明**：转发kafka消息关联的topic信息。
        :type topic: str
        :param username: **参数说明**：转发kafka关联的用户名信息。
        :type username: str
        :param password: **参数说明**：转发kafka关联的密码信息。
        :type password: str
        :param mechanism: **参数说明**：转发kafka关联的鉴权机制。 **取值范围**： - PAAS：非SASL鉴权。 - PLAIN：SASL/PLAIN模式。需要填写对应的用户名密码信息。
        :type mechanism: str
        """
        
        

        self._region_name = None
        self._project_id = None
        self._addresses = None
        self._topic = None
        self._username = None
        self._password = None
        self._mechanism = None
        self.discriminator = None

        self.region_name = region_name
        self.project_id = project_id
        self.addresses = addresses
        self.topic = topic
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if mechanism is not None:
            self.mechanism = mechanism

    @property
    def region_name(self):
        """Gets the region_name of this DmsKafkaForwarding.

        **参数说明**：Kafka服务对应的region区域

        :return: The region_name of this DmsKafkaForwarding.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this DmsKafkaForwarding.

        **参数说明**：Kafka服务对应的region区域

        :param region_name: The region_name of this DmsKafkaForwarding.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def project_id(self):
        """Gets the project_id of this DmsKafkaForwarding.

        **参数说明**：Kafka服务对应的projectId信息

        :return: The project_id of this DmsKafkaForwarding.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DmsKafkaForwarding.

        **参数说明**：Kafka服务对应的projectId信息

        :param project_id: The project_id of this DmsKafkaForwarding.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def addresses(self):
        """Gets the addresses of this DmsKafkaForwarding.

        **参数说明**：转发kafka消息对应的地址列表

        :return: The addresses of this DmsKafkaForwarding.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.NetAddress`]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this DmsKafkaForwarding.

        **参数说明**：转发kafka消息对应的地址列表

        :param addresses: The addresses of this DmsKafkaForwarding.
        :type addresses: list[:class:`huaweicloudsdkiotda.v5.NetAddress`]
        """
        self._addresses = addresses

    @property
    def topic(self):
        """Gets the topic of this DmsKafkaForwarding.

        **参数说明**：转发kafka消息关联的topic信息。

        :return: The topic of this DmsKafkaForwarding.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this DmsKafkaForwarding.

        **参数说明**：转发kafka消息关联的topic信息。

        :param topic: The topic of this DmsKafkaForwarding.
        :type topic: str
        """
        self._topic = topic

    @property
    def username(self):
        """Gets the username of this DmsKafkaForwarding.

        **参数说明**：转发kafka关联的用户名信息。

        :return: The username of this DmsKafkaForwarding.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this DmsKafkaForwarding.

        **参数说明**：转发kafka关联的用户名信息。

        :param username: The username of this DmsKafkaForwarding.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        """Gets the password of this DmsKafkaForwarding.

        **参数说明**：转发kafka关联的密码信息。

        :return: The password of this DmsKafkaForwarding.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this DmsKafkaForwarding.

        **参数说明**：转发kafka关联的密码信息。

        :param password: The password of this DmsKafkaForwarding.
        :type password: str
        """
        self._password = password

    @property
    def mechanism(self):
        """Gets the mechanism of this DmsKafkaForwarding.

        **参数说明**：转发kafka关联的鉴权机制。 **取值范围**： - PAAS：非SASL鉴权。 - PLAIN：SASL/PLAIN模式。需要填写对应的用户名密码信息。

        :return: The mechanism of this DmsKafkaForwarding.
        :rtype: str
        """
        return self._mechanism

    @mechanism.setter
    def mechanism(self, mechanism):
        """Sets the mechanism of this DmsKafkaForwarding.

        **参数说明**：转发kafka关联的鉴权机制。 **取值范围**： - PAAS：非SASL鉴权。 - PLAIN：SASL/PLAIN模式。需要填写对应的用户名密码信息。

        :param mechanism: The mechanism of this DmsKafkaForwarding.
        :type mechanism: str
        """
        self._mechanism = mechanism

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
        if not isinstance(other, DmsKafkaForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
