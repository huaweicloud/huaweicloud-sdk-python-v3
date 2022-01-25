# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Nearline:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'item_topic': 'Topic',
        'user_topic': 'Topic',
        'behavior_topic': 'Topic'
    }

    attribute_map = {
        'item_topic': 'item_topic',
        'user_topic': 'user_topic',
        'behavior_topic': 'behavior_topic'
    }

    def __init__(self, item_topic=None, user_topic=None, behavior_topic=None):
        """Nearline - a model defined in huaweicloud sdk"""
        
        

        self._item_topic = None
        self._user_topic = None
        self._behavior_topic = None
        self.discriminator = None

        if item_topic is not None:
            self.item_topic = item_topic
        if user_topic is not None:
            self.user_topic = user_topic
        if behavior_topic is not None:
            self.behavior_topic = behavior_topic

    @property
    def item_topic(self):
        """Gets the item_topic of this Nearline.


        :return: The item_topic of this Nearline.
        :rtype: Topic
        """
        return self._item_topic

    @item_topic.setter
    def item_topic(self, item_topic):
        """Sets the item_topic of this Nearline.


        :param item_topic: The item_topic of this Nearline.
        :type: Topic
        """
        self._item_topic = item_topic

    @property
    def user_topic(self):
        """Gets the user_topic of this Nearline.


        :return: The user_topic of this Nearline.
        :rtype: Topic
        """
        return self._user_topic

    @user_topic.setter
    def user_topic(self, user_topic):
        """Sets the user_topic of this Nearline.


        :param user_topic: The user_topic of this Nearline.
        :type: Topic
        """
        self._user_topic = user_topic

    @property
    def behavior_topic(self):
        """Gets the behavior_topic of this Nearline.


        :return: The behavior_topic of this Nearline.
        :rtype: Topic
        """
        return self._behavior_topic

    @behavior_topic.setter
    def behavior_topic(self, behavior_topic):
        """Sets the behavior_topic of this Nearline.


        :param behavior_topic: The behavior_topic of this Nearline.
        :type: Topic
        """
        self._behavior_topic = behavior_topic

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
        if not isinstance(other, Nearline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other