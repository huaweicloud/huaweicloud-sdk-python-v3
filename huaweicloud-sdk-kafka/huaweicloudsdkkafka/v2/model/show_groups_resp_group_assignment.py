# coding: utf-8

import pprint
import re

import six





class ShowGroupsRespGroupAssignment:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'topic': 'str',
        'partitions': 'list[str]'
    }

    attribute_map = {
        'topic': 'topic',
        'partitions': 'partitions'
    }

    def __init__(self, topic=None, partitions=None):
        """ShowGroupsRespGroupAssignment - a model defined in huaweicloud sdk"""
        
        

        self._topic = None
        self._partitions = None
        self.discriminator = None

        if topic is not None:
            self.topic = topic
        if partitions is not None:
            self.partitions = partitions

    @property
    def topic(self):
        """Gets the topic of this ShowGroupsRespGroupAssignment.

        topic名称。

        :return: The topic of this ShowGroupsRespGroupAssignment.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this ShowGroupsRespGroupAssignment.

        topic名称。

        :param topic: The topic of this ShowGroupsRespGroupAssignment.
        :type: str
        """
        self._topic = topic

    @property
    def partitions(self):
        """Gets the partitions of this ShowGroupsRespGroupAssignment.

        分区列表。

        :return: The partitions of this ShowGroupsRespGroupAssignment.
        :rtype: list[str]
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        """Sets the partitions of this ShowGroupsRespGroupAssignment.

        分区列表。

        :param partitions: The partitions of this ShowGroupsRespGroupAssignment.
        :type: list[str]
        """
        self._partitions = partitions

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
        if not isinstance(other, ShowGroupsRespGroupAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
