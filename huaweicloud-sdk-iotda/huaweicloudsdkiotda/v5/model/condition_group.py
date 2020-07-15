# coding: utf-8

import pprint
import re

import six





class ConditionGroup:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'conditions': 'list[RuleCondition]',
        'logic': 'str',
        'time_range': 'TimeRange'
    }

    attribute_map = {
        'conditions': 'conditions',
        'logic': 'logic',
        'time_range': 'time_range'
    }

    def __init__(self, conditions=None, logic=None, time_range=None):
        """ConditionGroup - a model defined in huaweicloud sdk"""
        
        

        self._conditions = None
        self._logic = None
        self._time_range = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if logic is not None:
            self.logic = logic
        if time_range is not None:
            self.time_range = time_range

    @property
    def conditions(self):
        """Gets the conditions of this ConditionGroup.

        规则的条件列表，单个规则最多支持设置10个条件。

        :return: The conditions of this ConditionGroup.
        :rtype: list[RuleCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this ConditionGroup.

        规则的条件列表，单个规则最多支持设置10个条件。

        :param conditions: The conditions of this ConditionGroup.
        :type: list[RuleCondition]
        """
        self._conditions = conditions

    @property
    def logic(self):
        """Gets the logic of this ConditionGroup.

        规则条件列表中多个条件之间的逻辑关系，默认值：and。 - and：逻辑且。 - or：逻辑或。 

        :return: The logic of this ConditionGroup.
        :rtype: str
        """
        return self._logic

    @logic.setter
    def logic(self, logic):
        """Sets the logic of this ConditionGroup.

        规则条件列表中多个条件之间的逻辑关系，默认值：and。 - and：逻辑且。 - or：逻辑或。 

        :param logic: The logic of this ConditionGroup.
        :type: str
        """
        self._logic = logic

    @property
    def time_range(self):
        """Gets the time_range of this ConditionGroup.


        :return: The time_range of this ConditionGroup.
        :rtype: TimeRange
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this ConditionGroup.


        :param time_range: The time_range of this ConditionGroup.
        :type: TimeRange
        """
        self._time_range = time_range

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
        if not isinstance(other, ConditionGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
