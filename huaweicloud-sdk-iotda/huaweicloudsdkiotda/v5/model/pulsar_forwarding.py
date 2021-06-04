# coding: utf-8

import pprint
import re

import six





class PulsarForwarding:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'topic': 'str',
        'cert_id': 'str'
    }

    attribute_map = {
        'url': 'url',
        'topic': 'topic',
        'cert_id': 'cert_id'
    }

    def __init__(self, url=None, topic=None, cert_id=None):
        """PulsarForwarding - a model defined in huaweicloud sdk"""
        
        

        self._url = None
        self._topic = None
        self._cert_id = None
        self.discriminator = None

        self.url = url
        self.topic = topic
        if cert_id is not None:
            self.cert_id = cert_id

    @property
    def url(self):
        """Gets the url of this PulsarForwarding.

        **参数说明**：pulsar的访问url。

        :return: The url of this PulsarForwarding.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PulsarForwarding.

        **参数说明**：pulsar的访问url。

        :param url: The url of this PulsarForwarding.
        :type: str
        """
        self._url = url

    @property
    def topic(self):
        """Gets the topic of this PulsarForwarding.

        **参数说明**：用于接收满足规则条件数据的topic。

        :return: The topic of this PulsarForwarding.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this PulsarForwarding.

        **参数说明**：用于接收满足规则条件数据的topic。

        :param topic: The topic of this PulsarForwarding.
        :type: str
        """
        self._topic = topic

    @property
    def cert_id(self):
        """Gets the cert_id of this PulsarForwarding.

        **参数说明**：证书id

        :return: The cert_id of this PulsarForwarding.
        :rtype: str
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        """Sets the cert_id of this PulsarForwarding.

        **参数说明**：证书id

        :param cert_id: The cert_id of this PulsarForwarding.
        :type: str
        """
        self._cert_id = cert_id

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
        if not isinstance(other, PulsarForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
