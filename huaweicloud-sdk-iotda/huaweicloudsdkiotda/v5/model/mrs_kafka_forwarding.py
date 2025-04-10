# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MrsKafkaForwarding:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'addresses': 'list[NetAddress]',
        'topic': 'str',
        'kerberos_authentication': 'bool'
    }

    attribute_map = {
        'addresses': 'addresses',
        'topic': 'topic',
        'kerberos_authentication': 'kerberos_authentication'
    }

    def __init__(self, addresses=None, topic=None, kerberos_authentication=None):
        r"""MrsKafkaForwarding

        The model defined in huaweicloud sdk

        :param addresses: **参数说明**：转发kafka消息对应的地址列表
        :type addresses: list[:class:`huaweicloudsdkiotda.v5.NetAddress`]
        :param topic: **参数说明**：转发kafka消息关联的topic信息。
        :type topic: str
        :param kerberos_authentication: 是否Kerberos认证，默认为false。
        :type kerberos_authentication: bool
        """
        
        

        self._addresses = None
        self._topic = None
        self._kerberos_authentication = None
        self.discriminator = None

        self.addresses = addresses
        self.topic = topic
        if kerberos_authentication is not None:
            self.kerberos_authentication = kerberos_authentication

    @property
    def addresses(self):
        r"""Gets the addresses of this MrsKafkaForwarding.

        **参数说明**：转发kafka消息对应的地址列表

        :return: The addresses of this MrsKafkaForwarding.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.NetAddress`]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        r"""Sets the addresses of this MrsKafkaForwarding.

        **参数说明**：转发kafka消息对应的地址列表

        :param addresses: The addresses of this MrsKafkaForwarding.
        :type addresses: list[:class:`huaweicloudsdkiotda.v5.NetAddress`]
        """
        self._addresses = addresses

    @property
    def topic(self):
        r"""Gets the topic of this MrsKafkaForwarding.

        **参数说明**：转发kafka消息关联的topic信息。

        :return: The topic of this MrsKafkaForwarding.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this MrsKafkaForwarding.

        **参数说明**：转发kafka消息关联的topic信息。

        :param topic: The topic of this MrsKafkaForwarding.
        :type topic: str
        """
        self._topic = topic

    @property
    def kerberos_authentication(self):
        r"""Gets the kerberos_authentication of this MrsKafkaForwarding.

        是否Kerberos认证，默认为false。

        :return: The kerberos_authentication of this MrsKafkaForwarding.
        :rtype: bool
        """
        return self._kerberos_authentication

    @kerberos_authentication.setter
    def kerberos_authentication(self, kerberos_authentication):
        r"""Sets the kerberos_authentication of this MrsKafkaForwarding.

        是否Kerberos认证，默认为false。

        :param kerberos_authentication: The kerberos_authentication of this MrsKafkaForwarding.
        :type kerberos_authentication: bool
        """
        self._kerberos_authentication = kerberos_authentication

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
        if not isinstance(other, MrsKafkaForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
