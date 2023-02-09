# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RomaForwarding:

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
        'password': 'str'
    }

    attribute_map = {
        'addresses': 'addresses',
        'topic': 'topic',
        'username': 'username',
        'password': 'password'
    }

    def __init__(self, addresses=None, topic=None, username=None, password=None):
        """RomaForwarding

        The model defined in huaweicloud sdk

        :param addresses: **参数说明**：转发roma消息对应的地址列表
        :type addresses: list[:class:`huaweicloudsdkiotda.v5.NetAddress`]
        :param topic: **参数说明**：转发roma消息关联的topic信息。
        :type topic: str
        :param username: **参数说明**：转发roma关联的用户名信息。
        :type username: str
        :param password: **参数说明**：转发roma关联的密码信息。
        :type password: str
        """
        
        

        self._addresses = None
        self._topic = None
        self._username = None
        self._password = None
        self.discriminator = None

        self.addresses = addresses
        self.topic = topic
        self.username = username
        self.password = password

    @property
    def addresses(self):
        """Gets the addresses of this RomaForwarding.

        **参数说明**：转发roma消息对应的地址列表

        :return: The addresses of this RomaForwarding.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.NetAddress`]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this RomaForwarding.

        **参数说明**：转发roma消息对应的地址列表

        :param addresses: The addresses of this RomaForwarding.
        :type addresses: list[:class:`huaweicloudsdkiotda.v5.NetAddress`]
        """
        self._addresses = addresses

    @property
    def topic(self):
        """Gets the topic of this RomaForwarding.

        **参数说明**：转发roma消息关联的topic信息。

        :return: The topic of this RomaForwarding.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this RomaForwarding.

        **参数说明**：转发roma消息关联的topic信息。

        :param topic: The topic of this RomaForwarding.
        :type topic: str
        """
        self._topic = topic

    @property
    def username(self):
        """Gets the username of this RomaForwarding.

        **参数说明**：转发roma关联的用户名信息。

        :return: The username of this RomaForwarding.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this RomaForwarding.

        **参数说明**：转发roma关联的用户名信息。

        :param username: The username of this RomaForwarding.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        """Gets the password of this RomaForwarding.

        **参数说明**：转发roma关联的密码信息。

        :return: The password of this RomaForwarding.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RomaForwarding.

        **参数说明**：转发roma关联的密码信息。

        :param password: The password of this RomaForwarding.
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
        if not isinstance(other, RomaForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
