# coding: utf-8

import pprint
import re

import six





class ActionKafkaForwarding:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'region_name': 'str',
        'project_id': 'str',
        'kafka_addresses': 'list[NetAddress]',
        'kafka_topic': 'str',
        'kafka_username': 'str',
        'kafka_password': 'str',
        'kafka_mechanism': 'str'
    }

    attribute_map = {
        'region_name': 'region_name',
        'project_id': 'project_id',
        'kafka_addresses': 'kafka_addresses',
        'kafka_topic': 'kafka_topic',
        'kafka_username': 'kafka_username',
        'kafka_password': 'kafka_password',
        'kafka_mechanism': 'kafka_mechanism'
    }

    def __init__(self, region_name=None, project_id=None, kafka_addresses=None, kafka_topic=None, kafka_username=None, kafka_password=None, kafka_mechanism=None):
        """ActionKafkaForwarding - a model defined in huaweicloud sdk"""
        
        

        self._region_name = None
        self._project_id = None
        self._kafka_addresses = None
        self._kafka_topic = None
        self._kafka_username = None
        self._kafka_password = None
        self._kafka_mechanism = None
        self.discriminator = None

        if region_name is not None:
            self.region_name = region_name
        if project_id is not None:
            self.project_id = project_id
        if kafka_addresses is not None:
            self.kafka_addresses = kafka_addresses
        if kafka_topic is not None:
            self.kafka_topic = kafka_topic
        if kafka_username is not None:
            self.kafka_username = kafka_username
        if kafka_password is not None:
            self.kafka_password = kafka_password
        if kafka_mechanism is not None:
            self.kafka_mechanism = kafka_mechanism

    @property
    def region_name(self):
        """Gets the region_name of this ActionKafkaForwarding.

        转发kafka消息对应的region区域

        :return: The region_name of this ActionKafkaForwarding.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this ActionKafkaForwarding.

        转发kafka消息对应的region区域

        :param region_name: The region_name of this ActionKafkaForwarding.
        :type: str
        """
        self._region_name = region_name

    @property
    def project_id(self):
        """Gets the project_id of this ActionKafkaForwarding.

        转发kafka消息对应的projectId信息

        :return: The project_id of this ActionKafkaForwarding.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ActionKafkaForwarding.

        转发kafka消息对应的projectId信息

        :param project_id: The project_id of this ActionKafkaForwarding.
        :type: str
        """
        self._project_id = project_id

    @property
    def kafka_addresses(self):
        """Gets the kafka_addresses of this ActionKafkaForwarding.

        转发kafka消息对应的地址列表

        :return: The kafka_addresses of this ActionKafkaForwarding.
        :rtype: list[NetAddress]
        """
        return self._kafka_addresses

    @kafka_addresses.setter
    def kafka_addresses(self, kafka_addresses):
        """Sets the kafka_addresses of this ActionKafkaForwarding.

        转发kafka消息对应的地址列表

        :param kafka_addresses: The kafka_addresses of this ActionKafkaForwarding.
        :type: list[NetAddress]
        """
        self._kafka_addresses = kafka_addresses

    @property
    def kafka_topic(self):
        """Gets the kafka_topic of this ActionKafkaForwarding.

        转发kafka消息关联的topic信息。

        :return: The kafka_topic of this ActionKafkaForwarding.
        :rtype: str
        """
        return self._kafka_topic

    @kafka_topic.setter
    def kafka_topic(self, kafka_topic):
        """Sets the kafka_topic of this ActionKafkaForwarding.

        转发kafka消息关联的topic信息。

        :param kafka_topic: The kafka_topic of this ActionKafkaForwarding.
        :type: str
        """
        self._kafka_topic = kafka_topic

    @property
    def kafka_username(self):
        """Gets the kafka_username of this ActionKafkaForwarding.

        转发kafka关联的用户名信息。

        :return: The kafka_username of this ActionKafkaForwarding.
        :rtype: str
        """
        return self._kafka_username

    @kafka_username.setter
    def kafka_username(self, kafka_username):
        """Sets the kafka_username of this ActionKafkaForwarding.

        转发kafka关联的用户名信息。

        :param kafka_username: The kafka_username of this ActionKafkaForwarding.
        :type: str
        """
        self._kafka_username = kafka_username

    @property
    def kafka_password(self):
        """Gets the kafka_password of this ActionKafkaForwarding.

        转发kafka关联的密码信息。

        :return: The kafka_password of this ActionKafkaForwarding.
        :rtype: str
        """
        return self._kafka_password

    @kafka_password.setter
    def kafka_password(self, kafka_password):
        """Sets the kafka_password of this ActionKafkaForwarding.

        转发kafka关联的密码信息。

        :param kafka_password: The kafka_password of this ActionKafkaForwarding.
        :type: str
        """
        self._kafka_password = kafka_password

    @property
    def kafka_mechanism(self):
        """Gets the kafka_mechanism of this ActionKafkaForwarding.

        转发kafka关联的鉴权机制。 类型说明： PAAS：非SASL鉴权。 PLAIN：SASL/PLAIN模式。需要填写对应的用户名密码信息。 

        :return: The kafka_mechanism of this ActionKafkaForwarding.
        :rtype: str
        """
        return self._kafka_mechanism

    @kafka_mechanism.setter
    def kafka_mechanism(self, kafka_mechanism):
        """Sets the kafka_mechanism of this ActionKafkaForwarding.

        转发kafka关联的鉴权机制。 类型说明： PAAS：非SASL鉴权。 PLAIN：SASL/PLAIN模式。需要填写对应的用户名密码信息。 

        :param kafka_mechanism: The kafka_mechanism of this ActionKafkaForwarding.
        :type: str
        """
        self._kafka_mechanism = kafka_mechanism

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ActionKafkaForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
