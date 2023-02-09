# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DmsRocketMQForwarding:

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
        'addresses': 'list[NetAddress]',
        'topic': 'str',
        'username': 'str',
        'password': 'str',
        'enable_ssl': 'bool'
    }

    attribute_map = {
        'addresses': 'addresses',
        'topic': 'topic',
        'username': 'username',
        'password': 'password',
        'enable_ssl': 'enable_ssl'
    }

    def __init__(self, addresses=None, topic=None, username=None, password=None, enable_ssl=None):
        """DmsRocketMQForwarding

        The model defined in huaweicloud sdk

        :param addresses: **参数说明**：转发rocketMQ消息对应的地址列表
        :type addresses: list[:class:`huaweicloudsdkiotda.v5.NetAddress`]
        :param topic: **参数说明**：转发rocketMQ消息关联的topic信息。
        :type topic: str
        :param username: **参数说明**：转发rocketMQ关联的用户名信息。
        :type username: str
        :param password: **参数说明**：转发rocketMQ关联的密码信息。
        :type password: str
        :param enable_ssl: 是否开启SSL，默认为true。
        :type enable_ssl: bool
        """
        
        

        self._addresses = None
        self._topic = None
        self._username = None
        self._password = None
        self._enable_ssl = None
        self.discriminator = None

        self.addresses = addresses
        self.topic = topic
        self.username = username
        self.password = password
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl

    @property
    def addresses(self):
        """Gets the addresses of this DmsRocketMQForwarding.

        **参数说明**：转发rocketMQ消息对应的地址列表

        :return: The addresses of this DmsRocketMQForwarding.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.NetAddress`]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this DmsRocketMQForwarding.

        **参数说明**：转发rocketMQ消息对应的地址列表

        :param addresses: The addresses of this DmsRocketMQForwarding.
        :type addresses: list[:class:`huaweicloudsdkiotda.v5.NetAddress`]
        """
        self._addresses = addresses

    @property
    def topic(self):
        """Gets the topic of this DmsRocketMQForwarding.

        **参数说明**：转发rocketMQ消息关联的topic信息。

        :return: The topic of this DmsRocketMQForwarding.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this DmsRocketMQForwarding.

        **参数说明**：转发rocketMQ消息关联的topic信息。

        :param topic: The topic of this DmsRocketMQForwarding.
        :type topic: str
        """
        self._topic = topic

    @property
    def username(self):
        """Gets the username of this DmsRocketMQForwarding.

        **参数说明**：转发rocketMQ关联的用户名信息。

        :return: The username of this DmsRocketMQForwarding.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this DmsRocketMQForwarding.

        **参数说明**：转发rocketMQ关联的用户名信息。

        :param username: The username of this DmsRocketMQForwarding.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        """Gets the password of this DmsRocketMQForwarding.

        **参数说明**：转发rocketMQ关联的密码信息。

        :return: The password of this DmsRocketMQForwarding.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this DmsRocketMQForwarding.

        **参数说明**：转发rocketMQ关联的密码信息。

        :param password: The password of this DmsRocketMQForwarding.
        :type password: str
        """
        self._password = password

    @property
    def enable_ssl(self):
        """Gets the enable_ssl of this DmsRocketMQForwarding.

        是否开启SSL，默认为true。

        :return: The enable_ssl of this DmsRocketMQForwarding.
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        """Sets the enable_ssl of this DmsRocketMQForwarding.

        是否开启SSL，默认为true。

        :param enable_ssl: The enable_ssl of this DmsRocketMQForwarding.
        :type enable_ssl: bool
        """
        self._enable_ssl = enable_ssl

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
        if not isinstance(other, DmsRocketMQForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
