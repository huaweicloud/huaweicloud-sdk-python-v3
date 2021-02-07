# coding: utf-8

import pprint
import re

import six





class MqsForwarding:


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
        'url': 'str',
        'user_name': 'str',
        'password': 'str',
        'topic': 'str',
        'encrypt_transport': 'bool'
    }

    attribute_map = {
        'url': 'url',
        'user_name': 'user_name',
        'password': 'password',
        'topic': 'topic',
        'encrypt_transport': 'encrypt_transport'
    }

    def __init__(self, url=None, user_name=None, password=None, topic=None, encrypt_transport=None):
        """MqsForwarding - a model defined in huaweicloud sdk"""
        
        

        self._url = None
        self._user_name = None
        self._password = None
        self._topic = None
        self._encrypt_transport = None
        self.discriminator = None

        self.url = url
        self.user_name = user_name
        self.password = password
        self.topic = topic
        if encrypt_transport is not None:
            self.encrypt_transport = encrypt_transport

    @property
    def url(self):
        """Gets the url of this MqsForwarding.

        MQS服务的URL

        :return: The url of this MqsForwarding.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this MqsForwarding.

        MQS服务的URL

        :param url: The url of this MqsForwarding.
        :type: str
        """
        self._url = url

    @property
    def user_name(self):
        """Gets the user_name of this MqsForwarding.

        用于登录MQS的用户名

        :return: The user_name of this MqsForwarding.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this MqsForwarding.

        用于登录MQS的用户名

        :param user_name: The user_name of this MqsForwarding.
        :type: str
        """
        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this MqsForwarding.

        用于登录MQS的密码

        :return: The password of this MqsForwarding.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this MqsForwarding.

        用于登录MQS的密码

        :param password: The password of this MqsForwarding.
        :type: str
        """
        self._password = password

    @property
    def topic(self):
        """Gets the topic of this MqsForwarding.

        订阅的MQS主题

        :return: The topic of this MqsForwarding.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this MqsForwarding.

        订阅的MQS主题

        :param topic: The topic of this MqsForwarding.
        :type: str
        """
        self._topic = topic

    @property
    def encrypt_transport(self):
        """Gets the encrypt_transport of this MqsForwarding.

        是否加密传输

        :return: The encrypt_transport of this MqsForwarding.
        :rtype: bool
        """
        return self._encrypt_transport

    @encrypt_transport.setter
    def encrypt_transport(self, encrypt_transport):
        """Sets the encrypt_transport of this MqsForwarding.

        是否加密传输

        :param encrypt_transport: The encrypt_transport of this MqsForwarding.
        :type: bool
        """
        self._encrypt_transport = encrypt_transport

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
        if not isinstance(other, MqsForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
