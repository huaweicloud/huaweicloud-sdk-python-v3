# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Topics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'topic_urn': 'str',
        'display_name': 'str',
        'push_policy': 'int'
    }

    attribute_map = {
        'name': 'name',
        'topic_urn': 'topic_urn',
        'display_name': 'display_name',
        'push_policy': 'push_policy'
    }

    def __init__(self, name=None, topic_urn=None, display_name=None, push_policy=None):
        """Topics

        The model defined in huaweicloud sdk

        :param name: 主题名称
        :type name: str
        :param topic_urn: Topic的唯一的资源标识。
        :type topic_urn: str
        :param display_name: Topic的显示名，推送邮件消息时，作为邮件发件人显示
        :type display_name: str
        :param push_policy: 消息推送的策略
        :type push_policy: int
        """
        
        

        self._name = None
        self._topic_urn = None
        self._display_name = None
        self._push_policy = None
        self.discriminator = None

        self.name = name
        self.topic_urn = topic_urn
        if display_name is not None:
            self.display_name = display_name
        if push_policy is not None:
            self.push_policy = push_policy

    @property
    def name(self):
        """Gets the name of this Topics.

        主题名称

        :return: The name of this Topics.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Topics.

        主题名称

        :param name: The name of this Topics.
        :type name: str
        """
        self._name = name

    @property
    def topic_urn(self):
        """Gets the topic_urn of this Topics.

        Topic的唯一的资源标识。

        :return: The topic_urn of this Topics.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this Topics.

        Topic的唯一的资源标识。

        :param topic_urn: The topic_urn of this Topics.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def display_name(self):
        """Gets the display_name of this Topics.

        Topic的显示名，推送邮件消息时，作为邮件发件人显示

        :return: The display_name of this Topics.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Topics.

        Topic的显示名，推送邮件消息时，作为邮件发件人显示

        :param display_name: The display_name of this Topics.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def push_policy(self):
        """Gets the push_policy of this Topics.

        消息推送的策略

        :return: The push_policy of this Topics.
        :rtype: int
        """
        return self._push_policy

    @push_policy.setter
    def push_policy(self, push_policy):
        """Sets the push_policy of this Topics.

        消息推送的策略

        :param push_policy: The push_policy of this Topics.
        :type push_policy: int
        """
        self._push_policy = push_policy

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
        if not isinstance(other, Topics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
