# coding: utf-8

import pprint
import re

import six





class MemberJobCard:


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
        'average_score': 'str',
        'score': 'int',
        'send_time': 'str',
        'last_submit_time': 'str'
    }

    attribute_map = {
        'name': 'name',
        'average_score': 'average_score',
        'score': 'score',
        'send_time': 'send_time',
        'last_submit_time': 'last_submit_time'
    }

    def __init__(self, name=None, average_score=None, score=None, send_time=None, last_submit_time=None):
        """MemberJobCard - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._average_score = None
        self._score = None
        self._send_time = None
        self._last_submit_time = None
        self.discriminator = None

        self.name = name
        self.average_score = average_score
        self.score = score
        self.send_time = send_time
        self.last_submit_time = last_submit_time

    @property
    def name(self):
        """Gets the name of this MemberJobCard.

        作业名称

        :return: The name of this MemberJobCard.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MemberJobCard.

        作业名称

        :param name: The name of this MemberJobCard.
        :type: str
        """
        self._name = name

    @property
    def average_score(self):
        """Gets the average_score of this MemberJobCard.

        作业均分(作业有均分该字段才返回)

        :return: The average_score of this MemberJobCard.
        :rtype: str
        """
        return self._average_score

    @average_score.setter
    def average_score(self, average_score):
        """Sets the average_score of this MemberJobCard.

        作业均分(作业有均分该字段才返回)

        :param average_score: The average_score of this MemberJobCard.
        :type: str
        """
        self._average_score = average_score

    @property
    def score(self):
        """Gets the score of this MemberJobCard.

        作业得分(作业有分数该字段才返回)

        :return: The score of this MemberJobCard.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this MemberJobCard.

        作业得分(作业有分数该字段才返回)

        :param score: The score of this MemberJobCard.
        :type: int
        """
        self._score = score

    @property
    def send_time(self):
        """Gets the send_time of this MemberJobCard.

        作业下发时间, 日期格式：yyyy-MM-dd HH:mm:ss

        :return: The send_time of this MemberJobCard.
        :rtype: str
        """
        return self._send_time

    @send_time.setter
    def send_time(self, send_time):
        """Sets the send_time of this MemberJobCard.

        作业下发时间, 日期格式：yyyy-MM-dd HH:mm:ss

        :param send_time: The send_time of this MemberJobCard.
        :type: str
        """
        self._send_time = send_time

    @property
    def last_submit_time(self):
        """Gets the last_submit_time of this MemberJobCard.

        作业最后一次提交时间, 日期格式：yyyy-MM-dd HH:mm:ss

        :return: The last_submit_time of this MemberJobCard.
        :rtype: str
        """
        return self._last_submit_time

    @last_submit_time.setter
    def last_submit_time(self, last_submit_time):
        """Sets the last_submit_time of this MemberJobCard.

        作业最后一次提交时间, 日期格式：yyyy-MM-dd HH:mm:ss

        :param last_submit_time: The last_submit_time of this MemberJobCard.
        :type: str
        """
        self._last_submit_time = last_submit_time

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
        if not isinstance(other, MemberJobCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
