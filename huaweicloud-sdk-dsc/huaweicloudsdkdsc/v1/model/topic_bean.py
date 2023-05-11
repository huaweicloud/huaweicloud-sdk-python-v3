# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopicBean:

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
        'topic_urn': 'str'
    }

    attribute_map = {
        'name': 'name',
        'topic_urn': 'topic_urn'
    }

    def __init__(self, name=None, topic_urn=None):
        """TopicBean

        The model defined in huaweicloud sdk

        :param name: 消息通知主题名称
        :type name: str
        :param topic_urn: 消息通知主题的唯一资源标识符
        :type topic_urn: str
        """
        
        

        self._name = None
        self._topic_urn = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if topic_urn is not None:
            self.topic_urn = topic_urn

    @property
    def name(self):
        """Gets the name of this TopicBean.

        消息通知主题名称

        :return: The name of this TopicBean.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TopicBean.

        消息通知主题名称

        :param name: The name of this TopicBean.
        :type name: str
        """
        self._name = name

    @property
    def topic_urn(self):
        """Gets the topic_urn of this TopicBean.

        消息通知主题的唯一资源标识符

        :return: The topic_urn of this TopicBean.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this TopicBean.

        消息通知主题的唯一资源标识符

        :param topic_urn: The topic_urn of this TopicBean.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

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
        if not isinstance(other, TopicBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
