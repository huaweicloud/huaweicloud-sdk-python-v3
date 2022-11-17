# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopicCategory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic_id': 'str',
        'topic_name': 'str',
        'category_id': 'str',
        'category_name': 'str'
    }

    attribute_map = {
        'topic_id': 'topic_id',
        'topic_name': 'topic_name',
        'category_id': 'category_id',
        'category_name': 'category_name'
    }

    def __init__(self, topic_id=None, topic_name=None, category_id=None, category_name=None):
        """TopicCategory

        The model defined in huaweicloud sdk

        :param topic_id: topic的id。
        :type topic_id: str
        :param topic_name: topic的名称。
        :type topic_name: str
        :param category_id: topic对应的类别的id。
        :type category_id: str
        :param category_name: topic对应的类别的名称。
        :type category_name: str
        """
        
        

        self._topic_id = None
        self._topic_name = None
        self._category_id = None
        self._category_name = None
        self.discriminator = None

        if topic_id is not None:
            self.topic_id = topic_id
        if topic_name is not None:
            self.topic_name = topic_name
        if category_id is not None:
            self.category_id = category_id
        if category_name is not None:
            self.category_name = category_name

    @property
    def topic_id(self):
        """Gets the topic_id of this TopicCategory.

        topic的id。

        :return: The topic_id of this TopicCategory.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        """Sets the topic_id of this TopicCategory.

        topic的id。

        :param topic_id: The topic_id of this TopicCategory.
        :type topic_id: str
        """
        self._topic_id = topic_id

    @property
    def topic_name(self):
        """Gets the topic_name of this TopicCategory.

        topic的名称。

        :return: The topic_name of this TopicCategory.
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """Sets the topic_name of this TopicCategory.

        topic的名称。

        :param topic_name: The topic_name of this TopicCategory.
        :type topic_name: str
        """
        self._topic_name = topic_name

    @property
    def category_id(self):
        """Gets the category_id of this TopicCategory.

        topic对应的类别的id。

        :return: The category_id of this TopicCategory.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this TopicCategory.

        topic对应的类别的id。

        :param category_id: The category_id of this TopicCategory.
        :type category_id: str
        """
        self._category_id = category_id

    @property
    def category_name(self):
        """Gets the category_name of this TopicCategory.

        topic对应的类别的名称。

        :return: The category_name of this TopicCategory.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this TopicCategory.

        topic对应的类别的名称。

        :param category_name: The category_name of this TopicCategory.
        :type category_name: str
        """
        self._category_name = category_name

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
        if not isinstance(other, TopicCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
